import sys, runpy
from pathlib import Path
raiz = Path(sys.argv[1]); E = runpy.run_path(sys.argv[2])["E"]
ok = True
for f, a, n in E:
    p = raiz / f; s = p.read_text(encoding="utf-8"); c = s.count(a)
    if c != 1:
        print(f"FALHA {f}: {c} ocorrencias de {a[:70]!r}"); ok = False; continue
    p.write_text(s.replace(a, n), encoding="utf-8")
print("edicoes:", len(E), "ok" if ok else "COM FALHA")
