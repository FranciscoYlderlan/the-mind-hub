"""Aplica trocas.json, em ordem, nos arquivos de uma pasta.
Uso: python aplicar.py <pasta> [trocas.json]
Falha (código 1, sem gravar nada) se algum "atual" não aparecer exatamente 1 vez."""
import json, os, sys

def main():
    if len(sys.argv) < 2:
        sys.exit("uso: python aplicar.py <pasta> [trocas.json]")
    pasta = sys.argv[1]
    caminho_trocas = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "trocas.json")
    trocas = json.load(open(caminho_trocas, encoding="utf-8"))
    textos, por_arquivo, erros = {}, {}, []
    for n, tr in enumerate(trocas, 1):
        arq = tr["arquivo"]
        if arq not in textos:
            p = os.path.join(pasta, arq)
            if not os.path.isfile(p):
                erros.append(f"#{n} {arq}: arquivo não existe"); continue
            textos[arq] = open(p, encoding="utf-8").read()
        qtd = textos[arq].count(tr["atual"])
        if qtd != 1:
            erros.append(f"#{n} {arq}: 'atual' aparece {qtd} vez(es): {tr['atual'][:70]!r}")
            continue
        textos[arq] = textos[arq].replace(tr["atual"], tr["novo"], 1)
        por_arquivo[arq] = por_arquivo.get(arq, 0) + 1
    if erros:
        print("FALHOU; nada foi gravado:"); [print("  " + e) for e in erros]; sys.exit(1)
    for arq, txt in textos.items():
        with open(os.path.join(pasta, arq), "w", encoding="utf-8") as f:
            f.write(txt)
    print(f"OK: {len(trocas)} trocas aplicadas, cada 'atual' único")
    for arq in sorted(por_arquivo):
        print(f"  {arq}: {por_arquivo[arq]}")

main()
