"""Prova das trocas. Uso: python3 checar.py <pasta-original> <pasta-aplicada> [trocas.json]

(a) aplica de novo, do zero, numa pasta temporária e confere cada troca;
(b) nenhuma citação a S1..S6 (nem S10, S13) sobra;
(c) todo ID citado em 07 e 08 (e, de quebra, em todo o contrato) está definido no arquivo dono.
"""
import difflib, json, pathlib, re, shutil, subprocess, sys, tempfile

orig, aplic = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
trocas = json.loads(pathlib.Path(sys.argv[3] if len(sys.argv) > 3 else pathlib.Path(__file__).with_name("trocas.json")).read_text(encoding="utf-8"))
ok = True

# (a)
with tempfile.TemporaryDirectory() as tmp:
    for f in orig.glob("*.md"):
        shutil.copy(f, tmp)
    r = subprocess.run([sys.executable, "-I", str(pathlib.Path(__file__).with_name("aplicar.py")), tmp], capture_output=True, text=True)
    print("(a)", r.stdout.strip())
    ok &= r.returncode == 0
    iguais = all((pathlib.Path(tmp) / f.name).read_text(encoding="utf-8") == f.read_text(encoding="utf-8") for f in aplic.glob("*.md"))
    print("    cópia aplicada igual a uma aplicação do zero:", iguais); ok &= iguais
final = {f.name: f.read_text(encoding="utf-8") for f in aplic.glob("*.md")}
faltam = []
for i, tr in enumerate(trocas):
    if not tr["novo"]:
        if tr["atual"] in final[tr["arquivo"]]:
            faltam.append(tr["id"])
        continue
    if tr["novo"] in final[tr["arquivo"]]:
        continue
    # o "novo" foi retocado depois por outra troca do mesmo arquivo
    def sobrepoe(a, b):
        m = difflib.SequenceMatcher(None, a, b, autojunk=False).find_longest_match(0, len(a), 0, len(b))
        return m.size >= min(25, len(a))
    if not any(t2["arquivo"] == tr["arquivo"] and sobrepoe(t2["atual"], tr["novo"]) for t2 in trocas[i + 1:]):
        faltam.append(tr["id"])
print(f"    {len(trocas) - len(faltam)}/{len(trocas)} trocas presentes no resultado (ou retocadas por troca posterior); faltando: {faltam or 'nenhuma'}")
ok &= not faltam

# (b)
sobras = [(n, i + 1, m.group()) for n, tx in final.items() if n != "mudancas.md" for i, l in enumerate(tx.splitlines())
          for m in re.finditer(r"\bS(?:[1-6]|10|13)\b", l)]
print("(b) citações a S1..S6, S10, S13 que sobraram (fora do histórico mudancas.md):", sobras or "nenhuma"); ok &= not sobras
# S e D citados existem em 00?
defs_sd = set(re.findall(r"^\| ([SD]\d+) \|", final["00-requisitos.md"], re.M))
cit_sd = {m for n, tx in final.items() if n != "mudancas.md" for m in re.findall(r"\b([SD]\d{1,2})\b", tx)}
orf_sd = sorted(cit_sd - defs_sd)
print("    D e S citados sem definição em 00:", orf_sd or "nenhum"); ok &= not orf_sd

# (c)
DONO = {"RF": ("00-requisitos.md", r"^\| (RF-\d+) \|"), "RNF": ("00-requisitos.md", r"^\| (RNF-\d+) \|"),
        "RN": ("00-requisitos.md", r"^\| (RN-\d+) \|"), "ATR": ("01-atores.md", r"^\| (ATR-\d+) \|"),
        "ENT": ("02-entidades.md", r"^## (ENT-\d+) "), "UC": ("03-casos-de-uso.md", r"^## (UC-\d+) "),
        "TEL": ("04-componentes.md", r"^\| (TEL-\d+) \|"), "CMP": ("04-componentes.md", r"^## (CMP-\d+) "),
        "ERR": ("05-erros.md", r"^\| (ERR-\d+) \|"), "NAV": ("06-navegacao.md", r"^\| (NAV-\d+) \|"),
        "AC": ("08-criterios-de-aceite.md", r"^\| (AC-\d+) \|")}
nav = (orig / "06-navegacao.md").read_text(encoding="utf-8")
final.setdefault("06-navegacao.md", nav)
defs = set()
for pre, (arq, rx) in DONO.items():
    defs |= set(re.findall(rx, final[arq], re.M))
padrao = r"\b(?:RNF|RF|RN|ATR|ENT|UC|TEL|CMP|ERR|NAV|AC)-\d+\b"
for alvo in ("07-rastreabilidade.md", "08-criterios-de-aceite.md"):
    cit = set(re.findall(padrao, final[alvo]))
    orf = sorted(cit - defs)
    print(f"(c) {alvo}: {len(cit)} IDs citados, sem definição: {orf or 'nenhum'}"); ok &= not orf
todos = {m for tx in final.values() for m in re.findall(padrao, tx)}
orf = sorted(todos - defs)
print(f"    todo o contrato: {len(todos)} IDs citados, sem definição: {orf or 'nenhum'}"); ok &= not orf
# IDs definidos que nenhum outro arquivo cita (só aviso)
print("    ERR novos citados em 07:", sorted(e for e in ("ERR-45", "ERR-46", "ERR-47", "ERR-48", "ERR-49") if e in final["07-rastreabilidade.md"]))

# extra: grafia
gr = [(n, l.strip()[:70]) for n, tx in final.items() for l in tx.splitlines()
      if re.search(r"(?<![Yy])(?<!-)[Hh]arness", l) and "Harness — especificação funcional" not in l]
print("(extra) grafia \"harness\" fora do título do documento-fonte:", gr or "nenhuma"); ok &= not gr
print("PROVA:", "PASSOU" if ok else "FALHOU")
sys.exit(0 if ok else 1)
