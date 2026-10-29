"""Aplica trocas.json numa pasta do contrato.

Uso: python3 aplicar.py <pasta-do-contrato> [trocas.json]

Aplica as trocas em ordem, em memória. Cada "atual" precisa ocorrer exatamente
uma vez no arquivo no momento da troca. Se alguma falhar, nada é gravado.
"""
import json, pathlib, sys


def main():
    if len(sys.argv) < 2:
        sys.exit("uso: python3 aplicar.py <pasta-do-contrato> [trocas.json]")
    pasta = pathlib.Path(sys.argv[1])
    arq_trocas = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else pathlib.Path(__file__).with_name("trocas.json")
    trocas = json.loads(arq_trocas.read_text(encoding="utf-8"))

    textos, erros = {}, []
    for i, tr in enumerate(trocas, 1):
        nome = tr["arquivo"]
        if nome not in textos:
            caminho = pasta / nome
            if not caminho.is_file():
                erros.append(f"[{i}] {tr['id']}: arquivo inexistente {nome}")
                continue
            textos[nome] = caminho.read_text(encoding="utf-8")
        n = textos[nome].count(tr["atual"])
        if n != 1:
            erros.append(f"[{i}] {tr['id']} ({nome}): 'atual' ocorre {n} vez(es)")
            continue
        textos[nome] = textos[nome].replace(tr["atual"], tr["novo"], 1)

    if erros:
        print("FALHOU, nada gravado:")
        print("\n".join(erros))
        sys.exit(1)
    for nome, texto in textos.items():
        (pasta / nome).write_text(texto, encoding="utf-8")
    print(f"OK: {len(trocas)} trocas aplicadas em {len(textos)} arquivos: {', '.join(sorted(textos))}")


if __name__ == "__main__":
    main()
