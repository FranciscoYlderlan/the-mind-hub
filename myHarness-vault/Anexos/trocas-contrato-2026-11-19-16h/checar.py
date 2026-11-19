"""Checa a cópia aplicada do contrato.
Uso: python checar.py <pasta> [<pasta_original>]
1) nenhum adiamento/ADIAMENTO_JA_USADO/segundo adiamento fora de mudancas.md
2) todo ID citado (ERR, ENT, AC, RN, RF, RNF, UC, CMP, TEL, NAV, ATR) existe
3) toda citação "UC-xx FA/FE-yy" existe no UC
4) nenhum ID órfão (definido e nunca citado fora da própria definição); com a pasta original, separa órfãos antigos de novos"""
import os, re, sys

ARQS = ["00-requisitos.md","01-atores.md","02-entidades.md","03-casos-de-uso.md","04-componentes.md","05-erros.md","06-navegacao.md","07-rastreabilidade.md","08-criterios-de-aceite.md","README.md","mudancas.md"]
DEF = [  # (prefixo, arquivo, regex da linha que define)
 ("ERR","05-erros.md", r"^\| (ERR-\d+) \|"), ("ENT","02-entidades.md", r"^## (ENT-\d+)"),
 ("AC","08-criterios-de-aceite.md", r"^\| (AC-\d+) \|"), ("RN","00-requisitos.md", r"^\| (RN-\d+) \|"),
 ("RF","00-requisitos.md", r"^\| (RF-\d+) \|"), ("RNF","00-requisitos.md", r"^\| (RNF-\d+) \|"),
 ("UC","03-casos-de-uso.md", r"^## (UC-\d+)"), ("CMP","04-componentes.md", r"^## (CMP-\d+)"),
 ("TEL","04-componentes.md", r"^\| (TEL-\d+) \|"), ("NAV","06-navegacao.md", r"^\| (NAV-\d+) \|"),
 ("ATR","01-atores.md", r"^\| (ATR-\d+) \|"),
]
ID_RE = re.compile(r"\b(ERR|ENT|AC|RNF|RN|RF|UC|CMP|TEL|NAV|ATR)-(\d+)\b")

def ler(pasta):
    return {a: open(os.path.join(pasta, a), encoding="utf-8").read() for a in ARQS}

def definicoes(tx):
    d = {}
    for pre, arq, rx in DEF:
        for i, l in enumerate(tx[arq].splitlines()):
            m = re.match(rx, l)
            if m: d[m.group(1)] = (arq, i)
    return d

def norm(p, n):  # AC-8 e AC-08 são o mesmo
    return f"{p}-{int(n):02d}"

def citacoes(tx, defs):
    """lista de (id, arquivo, linha) excluindo a linha/cabeçalho que define o id"""
    out = []
    for arq, t in tx.items():
        for i, l in enumerate(t.splitlines()):
            for m in ID_RE.finditer(l):
                id_ = norm(m.group(1), m.group(2))
                if defs.get(id_) == (arq, i) and l.lstrip("|# ").startswith(m.group(0)):
                    continue
                out.append((id_, arq, i + 1))
    return out

def fluxos_uc(tx):
    """UC -> conjunto de FA/FE definidos"""
    f, uc = {}, None
    for l in tx["03-casos-de-uso.md"].splitlines():
        m = re.match(r"^## (UC-\d+)", l)
        if m: uc = m.group(1); f[uc] = set(); continue
        m = re.match(r"^\| (F[AE]-\d+) \|", l)
        if m and uc: f[uc].add(m.group(1))
    return f

CHECA_ORFAO = ("ERR", "ENT", "AC", "RN", "RF", "UC", "CMP")  # NAV, TEL, ATR, RNF: só informativo

def orfaos(tx, defs, prefixos=CHECA_ORFAO):
    cit = {c[0] for c in citacoes(tx, defs) if c[1] != "mudancas.md"}
    return sorted(i for i in defs if i not in cit and i.split("-")[0] in prefixos)

def main():
    pasta = sys.argv[1]
    tx = ler(pasta); defs = definicoes(tx); ok = True
    # 1
    print("1) Termos do adiamento fora de mudancas.md")
    achou = [(a, i+1, l.strip()[:90]) for a, t in tx.items() if a != "mudancas.md"
             for i, l in enumerate(t.splitlines()) if re.search(r"adiamento|ADIAMENTO_JA_USADO|segundo adiamento|\badiar\b|\badia\b", l, re.I)]
    for a, n, l in achou: print(f"   ERRO {a}:{n}: {l}")
    print("   OK: nenhum" if not achou else f"   {len(achou)} ocorrência(s)"); ok &= not achou
    # 2
    print("2) IDs citados que não existem")
    falta = [(i, a, n) for i, a, n in citacoes(tx, defs) if i not in defs]
    for i, a, n in falta: print(f"   ERRO {i} citado em {a}:{n}")
    print("   OK: todo ERR/ENT/AC/RN/RF/RNF/UC/CMP/TEL/NAV/ATR citado existe" if not falta else ""); ok &= not falta
    # 3
    print("3) Citações UC-xx FA/FE-yy")
    f = fluxos_uc(tx); ruins = []
    for a, t in tx.items():
        for i, l in enumerate(t.splitlines()):
            for m in re.finditer(r"\b(UC-\d+) ((?:F[AE]-\d+)(?:(?:, | e )F[AE]-\d+)*)", l):
                for fl in re.findall(r"F[AE]-\d+", m.group(2)):
                    if fl not in f.get(m.group(1), set()): ruins.append(f"{m.group(1)} {fl} em {a}:{i+1}")
    # coluna Fluxos da rastreabilidade (linhas com um só UC)
    for i, l in enumerate(tx["07-rastreabilidade.md"].splitlines()):
        c = [x.strip() for x in l.split("|")]
        if len(c) > 4 and re.fullmatch(r"UC-\d+", c[2] or ""):
            for fl in re.findall(r"F[AE]-\d+", c[3]):
                if fl not in f.get(c[2], set()): ruins.append(f"{c[2]} {fl} (coluna Fluxos) em 07:{i+1}")
    for r in ruins: print("   ERRO " + r)
    print("   OK: todo FA/FE citado existe no UC" if not ruins else ""); ok &= not ruins
    # 4
    print("4) IDs órfãos ERR/ENT/AC/RN/RF/UC/CMP (definidos e nunca citados fora da definição; mudancas.md não conta)")
    orf = orfaos(tx, defs)
    if len(sys.argv) > 2:
        to = ler(sys.argv[2]); antes = set(orfaos(to, definicoes(to)))
        novos = [o for o in orf if o not in antes]
        print(f"   antes das trocas: {len(antes)} {sorted(antes) if antes else ''}")
        print(f"   depois: {len(orf)}; órfãos novos: {novos if novos else 'nenhum'}")
        ok &= not novos
    else:
        print(f"   {orf if orf else 'nenhum'}"); ok &= not orf
    # extra: AC definidos que não estão na rastreabilidade
    ac07 = {norm('AC', n) for n in re.findall(r"AC-(\d+)", tx["07-rastreabilidade.md"])}
    sem = sorted(i for i in defs if i.startswith("AC-") and i not in ac07)
    info = orfaos(tx, defs, ("NAV", "TEL", "ATR", "RNF"))
    print(f"   informativo (NAV/TEL/ATR/RNF não citados fora da definição): {info if info else 'nenhum'}")
    print(f"   AC fora de 07-rastreabilidade: {sem if sem else 'nenhum'}")
    print("RESULTADO:", "OK" if ok else "FALHOU"); sys.exit(0 if ok else 1)

main()
