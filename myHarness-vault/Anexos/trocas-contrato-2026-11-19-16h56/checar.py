"""Checa trocas.json contra o contrato atual, sem gravar nada.
Uso: python checar.py <pasta_do_contrato> [trocas.json]
Aplica as trocas em memória, na ordem (como o aplicar.py), e confere:
1) cada "atual" aparece exatamente 1 vez no arquivo, no momento em que é aplicado
2) todo ID citado (ERR, ENT, AC, RN, RF, RNF, UC, CMP, TEL, NAV, ATR) existe depois das trocas
3) toda citação "UC-xx FA/FE-yy" existe no UC
4) IDs novos sem colisão: os definidos só depois das trocas são exatamente os esperados, cada um 1 vez;
   M-xx novos não existiam, aparecem 1 vez e ficam no topo (M-30 ... M-23, M-22)
5) nenhum órfão novo (ID definido e nunca citado fora da definição; mudancas.md não conta)
6) os 8 pontos aprovados não deixam o estado antigo no contrato (fora de mudancas.md)"""
import json, os, re, sys
from collections import Counter

ARQS = ["00-requisitos.md","01-atores.md","02-entidades.md","03-casos-de-uso.md","04-componentes.md","05-erros.md","06-navegacao.md","07-rastreabilidade.md","08-criterios-de-aceite.md","README.md","mudancas.md"]
DEF = [("ERR","05-erros.md", r"^\| (ERR-\d+) \|"), ("ENT","02-entidades.md", r"^## (ENT-\d+)"),
 ("AC","08-criterios-de-aceite.md", r"^\| (AC-\d+) \|"), ("RN","00-requisitos.md", r"^\| (RN-\d+) \|"),
 ("RF","00-requisitos.md", r"^\| (RF-\d+) \|"), ("RNF","00-requisitos.md", r"^\| (RNF-\d+) \|"),
 ("UC","03-casos-de-uso.md", r"^## (UC-\d+)"), ("CMP","04-componentes.md", r"^## (CMP-\d+)"),
 ("TEL","04-componentes.md", r"^\| (TEL-\d+) \|"), ("NAV","06-navegacao.md", r"^\| (NAV-\d+) \|"),
 ("ATR","01-atores.md", r"^\| (ATR-\d+) \|")]
ID_RE = re.compile(r"\b(ERR|ENT|AC|RNF|RN|RF|UC|CMP|TEL|NAV|ATR)-(\d+)\b")
NOVOS_ESPERADOS = {"ERR-52", "AC-149", "AC-150", "AC-151", "AC-152"}
M_NOVOS = [f"M-{n}" for n in range(23, 31)]
ESTADO_ANTIGO = [
 (1, '[a confirmar: "Aprovar" fica bloqueado'), (2, "[a confirmar: a decisão não dá o tratamento]"),
 (3, "[a confirmar: o aviso volta a cada resposta"), (4, "[a confirmar: o que a linha traz]"),
 (5, "[a confirmar: rótulos]"), (6, "| erro | não se aplica | — |\n| sucesso | passagem concluída"),
 (7, 'sobe a cada "Pedir alteração" |'), (8, "a conferir no resultado do P2")]

def definicoes(tx):
    d = {}
    for pre, arq, rx in DEF:
        for i, l in enumerate(tx[arq].splitlines()):
            m = re.match(rx, l)
            if m: d.setdefault(m.group(1), []).append((arq, i))
    return d

def norm(p, n): return f"{p}-{int(n):02d}"

def citacoes(tx, defs):
    out = []
    for arq, t in tx.items():
        for i, l in enumerate(t.splitlines()):
            for m in ID_RE.finditer(l):
                id_ = norm(m.group(1), m.group(2))
                if (arq, i) in defs.get(id_, []) and l.lstrip("|# ").startswith(m.group(0)): continue
                out.append((id_, arq, i + 1))
    return out

def fluxos_uc(tx):
    f, uc = {}, None
    for l in tx["03-casos-de-uso.md"].splitlines():
        m = re.match(r"^## (UC-\d+)", l)
        if m: uc = m.group(1); f[uc] = set(); continue
        m = re.match(r"^\| (F[AE]-\d+) \|", l)
        if m and uc: f[uc].add(m.group(1))
    return f

def orfaos(tx, defs):
    cit = {c[0] for c in citacoes(tx, defs) if c[1] != "mudancas.md"}
    return sorted(i for i in defs if i not in cit and i.split("-")[0] in ("ERR","ENT","AC","RN","RF","UC","CMP"))

def main():
    pasta = sys.argv[1]
    cam = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "trocas.json")
    trocas = json.load(open(cam, encoding="utf-8"))
    antes = {a: open(os.path.join(pasta, a), encoding="utf-8").read() for a in ARQS}
    tx = dict(antes); ok = True
    print(f"1) Cada 'atual' único ({len(trocas)} trocas, aplicadas em memória na ordem)")
    ruins = []
    for n, tr in enumerate(trocas, 1):
        q = tx[tr["arquivo"]].count(tr["atual"])
        if q != 1: ruins.append(f"#{n} {tr['arquivo']}: aparece {q} vez(es): {tr['atual'][:70]!r}"); continue
        tx[tr["arquivo"]] = tx[tr["arquivo"]].replace(tr["atual"], tr["novo"], 1)
    for r in ruins: print("   ERRO " + r)
    print(f"   OK: {len(trocas)}/{len(trocas)} únicas" if not ruins else f"   {len(ruins)} com problema"); ok &= not ruins
    por = Counter(tr["motivo"].split(":")[0] for tr in trocas)
    print("   por ponto (M):", ", ".join(f"{k}: {v}" for k, v in sorted(por.items())))
    d0, d1 = definicoes(antes), definicoes(tx)
    print("2) IDs citados que não existem (depois das trocas)")
    falta = [(i, a, n) for i, a, n in citacoes(tx, d1) if i not in d1]
    for i, a, n in falta: print(f"   ERRO {i} citado em {a}:{n}")
    print("   OK: todo ID citado existe" if not falta else ""); ok &= not falta
    print("3) Citações UC-xx FA/FE-yy")
    f = fluxos_uc(tx); r3 = []
    for a, t in tx.items():
        for i, l in enumerate(t.splitlines()):
            for m in re.finditer(r"\b(UC-\d+) ((?:F[AE]-\d+)(?:(?:, | e )F[AE]-\d+)*)", l):
                for fl in re.findall(r"F[AE]-\d+", m.group(2)):
                    if fl not in f.get(m.group(1), set()): r3.append(f"{m.group(1)} {fl} em {a}:{i+1}")
    for r in r3: print("   ERRO " + r)
    print("   OK: todo FA/FE citado existe no UC" if not r3 else ""); ok &= not r3
    print("4) IDs novos sem colisão")
    novos = set(d1) - set(d0)
    colid = sorted(i for i in NOVOS_ESPERADOS if i in d0)
    dup = sorted(i for i, v in d1.items() if len(v) > 1)
    sumiu = sorted(set(d0) - set(d1))
    mm0 = re.findall(r"^\| (M-\d+) \|", antes["mudancas.md"], re.M)
    mm1 = Counter(re.findall(r"^\| (M-\d+) \|", tx["mudancas.md"], re.M))
    mcol = [m for m in M_NOVOS if m in mm0]; mfalta = [m for m in M_NOVOS if mm1[m] != 1]
    topo = re.findall(r"^\| (M-\d+) \|", tx["mudancas.md"], re.M)[:9]
    for c, msg in [(colid, "já existiam antes"), (dup, "definidos mais de 1 vez"), (sumiu, "sumiram"), (mcol, "M já existia"), (mfalta, "M não definido exatamente 1 vez")]:
        if c: print(f"   ERRO {msg}: {c}")
    if novos != NOVOS_ESPERADOS: print(f"   ERRO novos {sorted(novos)} != esperados {sorted(NOVOS_ESPERADOS)}")
    print(f"   novos: {sorted(novos, key=lambda x:(x.split('-')[0], int(x.split('-')[1])))}; M novos: {M_NOVOS[0]} a {M_NOVOS[-1]}; topo: {topo}")
    c4 = not (colid or dup or sumiu or mcol or mfalta) and novos == NOVOS_ESPERADOS and topo == M_NOVOS[::-1] + ["M-22"]
    print("   OK" if c4 else "   ERRO (topo deve ser M-30 ... M-23, M-22)"); ok &= c4
    print("5) Órfãos novos (ERR/ENT/AC/RN/RF/UC/CMP)")
    o0, o1 = set(orfaos(antes, d0)), orfaos(tx, d1)
    on = [o for o in o1 if o not in o0]
    print(f"   antes: {len(o0)}; depois: {len(o1)}; novos: {on if on else 'nenhum'}"); ok &= not on
    ac07 = {norm('AC', n) for n in re.findall(r"AC-(\d+)", tx["07-rastreabilidade.md"])}
    sem = sorted(i for i in NOVOS_ESPERADOS if i.startswith("AC-") and i not in ac07)
    print(f"   AC novos fora de 07-rastreabilidade: {sem if sem else 'nenhum'}"); ok &= not sem
    print("6) Estado antigo dos 8 pontos fora de mudancas.md")
    r6 = [(p, a, termo) for p, termo in ESTADO_ANTIGO for a, t in tx.items() if a != "mudancas.md" and termo in t]
    for p, a, termo in r6: print(f"   ERRO ponto {p}: {termo[:60]!r} em {a}")
    print("   OK: nenhum" if not r6 else ""); ok &= not r6
    print("RESULTADO:", "OK" if ok else "FALHOU"); sys.exit(0 if ok else 1)

main()
