#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cofre.py - kit da orquestra (original: Vault/Modelos/Orquestra/cofre.py)

Cria, sincroniza e verifica cofres Obsidian seguindo o Manual da Orquestra.
So usa a biblioteca padrao do Python. Rode da raiz do the-mind-hub:

  python Vault/Modelos/Orquestra/cofre.py criar <cofre> --projeto "Nome" --para-que "meia frase" [--repo LINK]
  python Vault/Modelos/Orquestra/cofre.py sincronizar <cofre>
  python Vault/Modelos/Orquestra/cofre.py verificar <cofre>      (vale para o Vault e para cofres de projeto)

Dentro de um cofre de projeto: python orquestra/modelos/cofre.py verificar .
'verificar' sai com codigo 1 se houver ERRO. Ninguem diz "pronto" com ERRO.
"""
import argparse, datetime, re, sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

PASTAS = ["entradas", "funcionalidades/geral", "referencias", "diarios", "modelos", "arquivos", "bugs"]
MAP = {"Manual do Meu Cérebro no Obsidian": "manual-do-cerebro", "Manual da Orquestra": "manual-da-orquestra",
       "Modelo de nota": "modelo-nota", "MOC Programação": "moc-orquestra", "Home": "moc-orquestra",
       "MOC Tema": "moc-orquestra"}
PH_PREFIX = ("nome-da-", "bug-titulo", "Nota ", "nome-da-imagem", "nota-antiga")
PH = {"Link", "Links", "MOC Tema"}
SO_NO_PROJETO = {"geral-contexto", "moc-orquestra", "CLAUDE"}
CODE = re.compile(r"(````.*?````|```.*?```|`[^`\n]*`)", re.S)
LINK = re.compile(r"!?\[\[([^\]]*)\]\]")
KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*\.md$")
DATA = r"\d{4}-\d{2}-\d{2}"
ESCOPO_CEREBRO = (
    "\n>\n> **Escopo neste cofre:** vale para as notas de `referencias/` e `MOCs/` o perfil, o tom, o esqueleto, "
    "os links e os tipos (seções 1, 2, 5, 6, 7 e 8), e a taxonomia de tags. Pastas, nomes de arquivo e destino das "
    "notas (seção 3, item 3 da seção 10 e \"Salva em Items/\" do checklist) são substituídos pelo [[Manual da Orquestra]]: "
    "aqui não existe `Items/`, e arquivos são kebab-case (`moc-tema.md`).")


def hoje():
    return datetime.date.today().isoformat()


def ler(p):
    return Path(p).read_text(encoding="utf-8")


def escrever(p, s):
    p = Path(p)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s, encoding="utf-8")


def sem_codigo(s):
    return "".join(CODE.split(s)[0::2])


def alvo(inner):
    return inner.split("|")[0].split("#")[0].strip().split("/")[-1]


def links(s):
    return [alvo(m) for m in LINK.findall(sem_codigo(s))]


def eh_ph(t):
    return t.startswith(PH_PREFIX) or t in PH


def converter(s):
    """Links do Vault -> nomes do cofre de projeto; outras notas do Vault viram texto."""
    parts = CODE.split(s)

    def sub(m):
        inner = m.group(1)
        t = alvo(inner)
        alias = inner.split("|")[1] if "|" in inner else None
        if t in MAP:
            return m.group(0).replace(t, MAP[t], 1)
        if (not t or m.group(0).startswith("!") or t.startswith(("modelo-", "manual-")) or eh_ph(t)
                or t in SO_NO_PROJETO or re.match(r"^(bug-|diario-)", t)):
            return m.group(0)
        return f"{alias or t} (no Vault)"

    for i in range(0, len(parts), 2):
        parts[i] = LINK.sub(sub, parts[i])
    return "".join(parts)


def preencher(s, pares, origem):
    for velho, novo in pares:
        if velho not in s:
            sys.exit(f"ERRO: o modelo {origem} mudou e nao contem mais: {velho!r}. Atualize o cofre.py.")
        s = s.replace(velho, novo)
    return s


def achar_vault(arg=None, cofre=None):
    cands = [Path(arg)] if arg else []
    try:
        cands.append(Path(__file__).resolve().parents[2])
    except IndexError:
        pass
    if cofre:
        c = Path(cofre).resolve()
        cands += [c.parent / "Vault", c / "Vault"]
    for c in cands:
        if (c / "Items" / "Manual da Orquestra.md").exists():
            return c
    return None


def versao(s):
    vs = [int(x) for x in re.findall(r"^- v(\d+) ", s, re.M)]
    return max(vs) if vs else 0


def copia_manual(vault, nome, extra=""):
    s = ler(vault / "Items" / nome)
    h = (f"> [!info] Cópia do Vault\n> Cópia de `Vault/Items/{nome}`, versão v{versao(s)}. "
         f"O original manda: ao mudar lá, rode `cofre.py sincronizar`." + extra)
    fim = s.index("\n---\n", 4) + 5
    return converter(s[:fim] + "\n" + h + "\n\n" + s[fim:])


def kit(vault):
    k = {}
    for f in sorted((vault / "Modelos" / "Orquestra").iterdir()):
        if f.suffix == ".md":
            k["modelos/" + f.name] = converter(ler(f))
        elif f.name == "cofre.py":
            k["modelos/cofre.py"] = ler(f)
    k["modelos/modelo-nota.md"] = converter(ler(vault / "Modelos" / "Modelo de nota.md"))
    k["referencias/manual-da-orquestra.md"] = copia_manual(vault, "Manual da Orquestra.md")
    k["referencias/manual-do-cerebro.md"] = copia_manual(vault, "Manual do Meu Cérebro no Obsidian.md", ESCOPO_CEREBRO)
    return k


def claude_md(vault, pasta, projeto, para, repo):
    t = ler(vault / "Modelos" / "Modelo de CLAUDE do cofre.md")
    t = preencher(t, [("{{nome-da-pasta}}", pasta), ("{{projeto}}", projeto),
                      ("{{para quê, em meia frase}}", para), ("{{link ou caminho}}", repo)], "Modelo de CLAUDE do cofre")
    return converter(t)


# ---------------------------------------------------------------- criar
def criar(a):
    dest = Path(a.cofre)
    vault = achar_vault(a.vault, dest)
    if not vault:
        sys.exit("ERRO: Vault nao encontrado. Use --vault CAMINHO.")
    if dest.exists():
        extras = [p.name for p in dest.iterdir() if p.name not in {".obsidian", "Bem-vindo.md", ".git", ".gitkeep"}]
        if extras:
            sys.exit(f"ERRO: {dest} ja tem conteudo {extras}. Para atualizar um cofre existente use: sincronizar")
    d = hoje()
    for p in PASTAS:
        (dest / "orquestra" / p).mkdir(parents=True, exist_ok=True)
    for p in ("MOCs", "Anexos"):
        (dest / p).mkdir(parents=True, exist_ok=True)
    for rel, txt in kit(vault).items():
        escrever(dest / "orquestra" / rel, txt)
    escrever(dest / "CLAUDE.md", claude_md(vault, dest.name, a.projeto, a.para_que, a.repo))

    m = converter(ler(vault / "Modelos/Orquestra/modelo-moc-orquestra.md"))
    m = preencher(m, [("{{date}}", d), ("# 🗺️ Mapa da Orquestra", f"# 🗺️ Mapa da Orquestra — {a.projeto}"),
                      ("- (uma linha por funcionalidade: `[[nome-da-func-contexto]]` + meia frase)",
                       "- (nenhuma ainda; uma linha por funcionalidade: `[[nome-da-func-contexto]]` + meia frase)"),
                      ("- (funcionalidades movidas para `orquestra/arquivos/`)", "- (nenhuma ainda)")], "modelo-moc-orquestra")
    escrever(dest / "MOCs/moc-orquestra.md", m)

    c = converter(ler(vault / "Modelos/Orquestra/modelo-contexto.md"))
    c = preencher(c, [("funcionalidade: \n", "funcionalidade: geral\n"), ("{{date}}", d),
                      ("# 🧭 {{title}}", f"# 🧭 {a.projeto} — contexto geral"),
                      ("> O que esta funcionalidade é e por que existe.", f"> {a.para_que}"),
                      ("- Dial: alto | medio | baixo (padrão: o do [[geral-contexto]])", "- Dial: [a confirmar] alto | medio | baixo"),
                      ("- AAAA-MM-DD: ", f"- {d}: cofre criado com `cofre.py criar` ([[diario-{d}]])."),
                      ("- Plano: [[nome-da-func-plano]]", "- Plano: (nenhum ainda)"),
                      ("- Decisões: [[nome-da-func-decisao-AAAA-MM-DD-titulo]]", "- Decisões: (nenhuma ainda; nomes `geral-decisao-AAAA-MM-DD-titulo`)"),
                      ("- Bugs: [[bug-titulo-AAAA-MM-DD]]", "- Bugs: (nenhum ainda)"),
                      ("- Referências: [[nome-da-referencia]]", "- Referências: [[manual-da-orquestra]], [[manual-do-cerebro]]"),
                      ("- Projeto: [[geral-contexto]]\n", "")], "modelo-contexto")
    escrever(dest / "orquestra/funcionalidades/geral/geral-contexto.md", c)

    escrever(dest / f"orquestra/diarios/diario-{d}.md", diario_criacao(vault, d, dest.name))
    for p in ("orquestra/entradas", "orquestra/arquivos", "orquestra/bugs", "Anexos"):
        if not any((dest / p).iterdir()):
            (dest / p / ".gitkeep").touch()
    print(f"Cofre {dest} criado. Proximo passo: preencher o geral-contexto e rodar verificar.")
    return verificar(dest, vault)


def diario_criacao(vault, d, nome):
    s = converter(ler(vault / "Modelos/Orquestra/modelo-diario.md"))
    return preencher(s, [
        ("{{date}}", d), ("# 📓 {{title}}", f"# 📓 Diário {d}"),
        ("## O que foi feito\n(só fatos)", f"## O que foi feito\n- Cofre `{nome}` criado com `cofre.py criar`: estrutura `orquestra/`, kit de modelos, manuais, `CLAUDE.md`, [[moc-orquestra]] e [[geral-contexto]]."),
        ("- [[nome-da-func-decisao-AAAA-MM-DD-titulo]]", "- (nenhuma)"), ("- [[bug-titulo-AAAA-MM-DD]]", "- (nenhum)"),
        ("## Candidatos que não viraram nota\n(e por quê)", "## Candidatos que não viraram nota\n- (nenhum)"),
        ("> O próximo passo concreto para a próxima sessão.", "> Preencher o [[geral-contexto]] (objetivo, motivação, tempo, dial) e colar o trecho do modelo-claude-do-repositorio no repositório de código."),
        ("- Funcionalidades tocadas: [[nome-da-func-contexto]]", "- Funcionalidades tocadas: [[geral-contexto]]"),
        ("- Projeto: [[geral-contexto]]\n", "")], "modelo-diario")


# ---------------------------------------------------------------- sincronizar
def sincronizar(a):
    cofre = Path(a.cofre)
    vault = achar_vault(a.vault, cofre)
    if not vault:
        sys.exit("ERRO: Vault nao encontrado. Use --vault CAMINHO.")
    for rel, txt in kit(vault).items():
        dst = cofre / "orquestra" / rel
        if not dst.exists() or ler(dst) != txt:
            escrever(dst, txt)
            print("atualizado  orquestra/" + rel)
    atual = ler(cofre / "CLAUDE.md") if (cofre / "CLAUDE.md").exists() else ""
    m1 = re.search(r'^# Cofre "[^"]+" — (.+?) \(guia para agentes\)', atual, re.M)
    m2 = re.search(r"\*\*memória do projeto .+?\*\*: (.+?)\. Este arquivo", atual)
    m3 = re.search(r"Repositório de código: (.+?)\.\s*$", atual, re.M)
    if m1 and m2 and m3:
        novo = claude_md(vault, cofre.resolve().name, m1.group(1), m2.group(1), m3.group(1))
        if novo != atual:
            escrever(cofre / "CLAUDE.md", novo)
            print("atualizado  CLAUDE.md (regenerado do Modelo de CLAUDE do cofre)")
    else:
        print("AVISO  CLAUDE.md fora do padrao: nao regenerei; compare com o Modelo de CLAUDE do cofre")
    print("Notas do cofre (contexto, moc, diarios...) nao sao sobrescritas: se o modelo delas mudou, ajuste seguindo 'Atualizar a memoria'.")
    return verificar(cofre, vault)


# ---------------------------------------------------------------- verificar
def frontmatter(s):
    if not s.startswith("---\n"):
        return None
    fim = s.find("\n---", 4)
    if fim < 0:
        return None
    fm = {}
    for linha in s[4:fim].splitlines():
        m = re.match(r"^([A-Za-z_-]+):\s*(.*)$", linha)
        if m:
            fm[m.group(1)] = m.group(2).strip()
    return fm


def lista(v):
    v = (v or "").strip()
    if v.startswith("[") and v.endswith("]"):
        return [x.strip() for x in v[1:-1].split(",") if x.strip()]
    return []


def verificar(cofre, vault=None):
    cofre = Path(cofre).resolve()
    erros, avisos = [], []
    E = lambda f, m: erros.append(f"{f}: {m}")
    A = lambda f, m: avisos.append(f"{f}: {m}")
    projeto = (cofre / "orquestra").is_dir()
    rel = lambda p: p.relative_to(cofre).as_posix()
    oculto = lambda p: any(x.startswith(".") for x in p.relative_to(cofre).parts)
    mds = [p for p in cofre.rglob("*.md") if not oculto(p)]
    todos = {p.stem.lower() for p in mds} | {p.name.lower() for p in cofre.rglob("*") if p.is_file() and not oculto(p)}
    texto = {p: ler(p) for p in mds}
    saida = {p: links(texto[p]) for p in mds}
    entrada = {}
    for p, ls in saida.items():
        for t in ls:
            entrada.setdefault(t.lower(), set()).add(p.stem.lower())
    eh_modelo = lambda p: rel(p).startswith(("orquestra/modelos/", "Modelos/"))
    eh_captura = lambda p: rel(p).startswith(("orquestra/entradas/", "00 Inbox/"))

    for p in mds:
        r, s, modelo = rel(p), texto[p], eh_modelo(p)
        if p.name == "Bem-vindo.md":
            A(r, "nota padrão do Obsidian; apagar só com confirmação do humano")
            continue
        for t in sorted(set(links(s))):
            if not t:
                if not modelo:
                    E(r, "link vazio [[]]")
                continue
            if t.lower() in todos:
                continue
            if modelo and (eh_ph(t) or (not projeto and t in SO_NO_PROJETO)):
                continue
            if not projeto and not modelo:
                A(r, f"link para nota que ainda não existe: [[{t}]] (fila de ideias?)")
            else:
                E(r, f"link quebrado: [[{t}]]")
        if not modelo and "{{" in sem_codigo(s):
            E(r, "campo de modelo não preenchido ({{...}})")
        pend = sem_codigo(s).count("[a confirmar]")
        if pend and not modelo:
            A(r, f"{pend} pendência(s) [a confirmar]")
        if p.name == "CLAUDE.md" or eh_captura(p):
            continue
        ent = entrada.get(p.stem.lower(), set()) - {p.stem.lower()}
        if not ent:
            E(r, "órfã: nenhuma nota aponta para ela (ligue no hub ou MOC)")
        if modelo:
            if "Conexões" not in s and "Mapa no Obsidian" not in s:
                E(r, "modelo sem seção de Conexões")
            continue
        reais = {t.lower() for t in saida[p] if t.lower() in todos and t.lower() != p.stem.lower()}
        if len(reais) < 2:
            E(r, f"{len(reais)} link(s) de saída válidos (mínimo 2)")
        fm = frontmatter(s)
        if fm is None:
            E(r, "sem frontmatter")
            continue
        for k in ("tipo", "status", "criado"):
            if not fm.get(k):
                E(r, f"frontmatter sem `{k}`")
        if fm.get("criado") and not re.fullmatch(DATA, fm["criado"]):
            E(r, "`criado` fora do formato AAAA-MM-DD")
        if not projeto and r.startswith("Items/"):
            na, nt = len(lista(fm.get("aliases"))), len(lista(fm.get("tags")))
            if not 2 <= na <= 4:
                E(r, f"aliases: {na} (esperado 2 a 4, em lista)")
            if not 1 <= nt <= 3:
                E(r, f"tags: {nt} (esperado 1 a 3, em lista)")

    claude = cofre / "CLAUDE.md"
    if claude.exists() and "## Etapas vitais" not in ler(claude):
        E("CLAUDE.md", "sem a seção 'Etapas vitais' (regenere com sincronizar)")
    if projeto:
        o = cofre / "orquestra"
        moc0 = cofre / "MOCs/moc-orquestra.md"
        if moc0.exists() and "Etapas vitais" not in ler(moc0):
            E("MOCs/moc-orquestra.md", "mapa sem a seção 'Etapas vitais' (etapa B5 do mapa)")
        if (o / "diarios").is_dir() and not list((o / "diarios").glob("diario-*.md")):
            E("orquestra/diarios", "nenhum diário: falta ao menos o diário de criação (etapa A3)")
        for pz in PASTAS:
            if not (o / pz).is_dir():
                E("orquestra/" + pz, "pasta obrigatória ausente")
        for ob in ("CLAUDE.md", "MOCs/moc-orquestra.md", "orquestra/funcionalidades/geral/geral-contexto.md"):
            if not (cofre / ob).exists():
                E(ob, "arquivo obrigatório ausente")
        for p in mds:
            r = rel(p)
            if r.startswith(("orquestra/", "MOCs/")) and not KEBAB.match(p.name):
                E(r, "nome fora do kebab-case sem acento")
            if re.search(r"\d{2}-\d{2}-\d{4}", p.name):
                E(r, "data no nome fora do formato AAAA-MM-DD")
        moc = cofre / "MOCs/moc-orquestra.md"
        moc_links = {t.lower() for t in saida.get(moc, [])}
        for base in (o / "funcionalidades", o / "arquivos"):
            if not base.is_dir():
                continue
            for fdir in sorted(d for d in base.iterdir() if d.is_dir()):
                f = fdir.name
                ctx = fdir / f"{f}-contexto.md"
                if not ctx.exists():
                    E(rel(fdir), f"falta {f}-contexto.md (hub da funcionalidade)")
                    continue
                ctx_links = {t.lower() for t in saida.get(ctx, [])}
                for n in sorted(fdir.glob("*.md")):
                    if n == ctx:
                        continue
                    if not re.fullmatch(rf"{re.escape(f)}-(plano|decisao-{DATA}-[a-z0-9-]+)\.md", n.name):
                        E(rel(n), f"nome fora do padrão ({f}-plano.md ou {f}-decisao-AAAA-MM-DD-titulo.md)")
                    if n.stem.lower() not in ctx_links:
                        E(rel(n), f"não está no mapa de {f}-contexto")
                if ctx.stem.lower() not in moc_links:
                    E(rel(ctx), "funcionalidade fora do moc-orquestra")
        for n in (o / "bugs").glob("*.md"):
            if not re.fullmatch(rf"bug-[a-z0-9-]+-{DATA}\.md", n.name):
                E(rel(n), "nome fora do padrão bug-titulo-AAAA-MM-DD.md")
        for n in (o / "diarios").glob("*.md"):
            if not re.fullmatch(rf"diario-{DATA}\.md", n.name):
                E(rel(n), "nome fora do padrão diario-AAAA-MM-DD.md")
        vault = vault or achar_vault(None, cofre)
        if vault:
            for relk, txt in kit(vault).items():
                dst = o / relk
                if not dst.exists():
                    E("orquestra/" + relk, "falta no kit: rode sincronizar")
                elif ler(dst) != txt:
                    A("orquestra/" + relk, "diferente do original no Vault: rode sincronizar")
        else:
            A("-", "Vault não encontrado: não comparei o kit com o original")

    print(f"\n== verificar {cofre.name} ({'cofre de projeto' if projeto else 'cofre pessoal'})")
    for x in erros:
        print("ERRO  ", x)
    for x in avisos:
        print("AVISO ", x)
    ok = not erros
    print(f"\nResultado: {len(erros)} ERRO, {len(avisos)} AVISO. "
          + ("OK: pode dizer pronto (resolva os AVISOS quando puder)." if ok else "NÃO está pronto: corrija e rode de novo."))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description="Kit da orquestra: criar, sincronizar e verificar cofres.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("criar")
    c.add_argument("cofre"); c.add_argument("--projeto", required=True); c.add_argument("--para-que", required=True)
    c.add_argument("--repo", default="[a confirmar]"); c.add_argument("--vault")
    s = sub.add_parser("sincronizar"); s.add_argument("cofre"); s.add_argument("--vault")
    v = sub.add_parser("verificar"); v.add_argument("cofre"); v.add_argument("--vault")
    a = ap.parse_args()
    if a.cmd == "criar":
        sys.exit(criar(a))
    if a.cmd == "sincronizar":
        sys.exit(sincronizar(a))
    sys.exit(verificar(a.cofre, achar_vault(a.vault, a.cofre)))


if __name__ == "__main__":
    main()
