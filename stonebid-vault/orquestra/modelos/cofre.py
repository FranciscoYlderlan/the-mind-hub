#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cofre.py - kit da orquestra (original: Vault/Modelos/Orquestra/cofre.py)

Cria, sincroniza e verifica cofres Obsidian seguindo o Manual da Orquestra.
So usa a biblioteca padrao do Python. Rode da raiz do the-mind-hub:

  python Vault/Modelos/Orquestra/cofre.py criar <cofre> --projeto "Nome" --para-que "meia frase" [--repo LINK]
  python Vault/Modelos/Orquestra/cofre.py sincronizar <cofre>
  python Vault/Modelos/Orquestra/cofre.py verificar <cofre>      (vale para o Vault e para cofres de projeto)
  python Vault/Modelos/Orquestra/cofre.py status <cofre> [--atualizar]   (roteiro: onde o projeto esta)

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
SO_NO_PROJETO = {"geral-contexto", "geral-plano", "moc-orquestra", "CLAUDE"}
ESTADOS = ["planejada", "em-construcao", "em-verificacao", "concluida", "arquivada"]
CODE = re.compile(r"(````.*?````|```.*?```|`[^`\n]*`)", re.S)
LINK = re.compile(r"!?\[\[([^\]]*)\]\]")
KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*\.md$")
DATA = r"\d{4}-\d{2}-\d{2}"
ESCOPO_CEREBRO = (
    "\n>\n> **Escopo neste cofre:** vale para as notas de `referencias/` e `MOCs/` o perfil, o tom, o esqueleto, "
    "os links e os tipos (seções 1, 2, 5, 6, 7 e 8), e a taxonomia de tags. Pastas, nomes de arquivo e destino das "
    "notas (seção 3, item 3 da seção 10 e \"Salva em Items/\" do checklist) são substituídos pelo [[Manual da Orquestra]]: "
    "aqui não existe `Items/`, e arquivos são kebab-case (`moc-tema.md`). O limite de ~350 palavras (seção 6) também não "
    "vale aqui: vale o `limite-palavras` do bloco `padroes` do `CLAUDE.md`.")
PADROES = re.compile(r"^```padroes\n(.*?)^```", re.S | re.M)


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
                      ("status: planejada\netapa: \n", "status: em-construcao\netapa-atual: 1\n"),
                      ("# 🧭 {{title}}", f"# 🧭 {a.projeto} — contexto geral"),
                      ("> O que esta funcionalidade é e por que existe.", f"> {a.para_que}"),
                      ("- Dial: alto | medio | baixo (padrão: o do [[geral-contexto]])", "- Dial: [a confirmar] alto | medio | baixo"),
                      ("- AAAA-MM-DD: ", f"- {d}: cofre criado com `cofre.py criar` ([[diario-{d}]])."),
                      ("- Plano: [[nome-da-func-plano]]", "- Roteiro: [[geral-plano]]"),
                      ("- Decisões: [[nome-da-func-decisao-AAAA-MM-DD-titulo]]", "- Decisões: (nenhuma ainda; nomes `geral-decisao-AAAA-MM-DD-titulo`)"),
                      ("- Bugs: [[bug-titulo-AAAA-MM-DD]]", "- Bugs: (nenhum ainda)"),
                      ("- Referências: [[nome-da-referencia]]", "- Referências: [[manual-da-orquestra]], [[manual-do-cerebro]]"),
                      ("- Projeto: [[geral-contexto]]\n", "")], "modelo-contexto")
    escrever(dest / "orquestra/funcionalidades/geral/geral-contexto.md", c)
    escrever(dest / "orquestra/funcionalidades/geral/geral-plano.md", roteiro_inicial(vault, d, a.projeto))

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
        ("## O que foi feito\n(só fatos)", f"## O que foi feito\n- Cofre `{nome}` criado com `cofre.py criar`: estrutura `orquestra/`, kit de modelos, manuais, `CLAUDE.md`, [[moc-orquestra]], [[geral-contexto]] e o roteiro [[geral-plano]]."),
        ("- [[nome-da-func-decisao-AAAA-MM-DD-titulo]]", "- (nenhuma)"), ("- [[bug-titulo-AAAA-MM-DD]]", "- (nenhum)"),
        ("## Candidatos que não viraram nota\n(e por quê)", "## Candidatos que não viraram nota\n- (nenhum)"),
        ("> - **Próximo passo:** ", "> - **Próximo passo:** etapa 1 do [[geral-plano]]: preencher o [[geral-contexto]] (objetivo, motivação, tempo, dial), propor as etapas do roteiro e colar o trecho do modelo-claude-do-repositorio no repositório de código."),
        ("(subagentes em andamento ou relatórios ainda não registrados)", "nenhuma"),
        ("> - **Dúvidas para o humano:** ", "> - **Dúvidas para o humano:** as pendências [a confirmar] do geral-contexto."),
        ("- Funcionalidades tocadas: [[nome-da-func-contexto]]", "- Funcionalidades tocadas: [[geral-contexto]]"),
        ("- Projeto: [[geral-contexto]]\n", "")], "modelo-diario")


def roteiro_inicial(vault, d, projeto):
    s = converter(ler(vault / "Modelos/Orquestra/modelo-roteiro.md"))
    s = preencher(s, [("{{date}}", d), ("# 🧭 Roteiro do projeto", f"# 🧭 Roteiro — {projeto}")], "modelo-roteiro")
    return re.sub(r"## 2\. Nome da etapa\n.*?(?=### 🔗 Conexões)", "", s, flags=re.S)


# ---------------------------------------------------------------- roteiro e status
def etapas(s):
    partes = re.split(r"^## (\d+)\. (.+)$", s, flags=re.M)
    out = []
    for i in range(1, len(partes) - 2, 3):
        corpo = re.split(r"^#{2,3} ", partes[i + 2], flags=re.M)[0]

        def campo(k):
            m = re.search(rf"^- \*\*{k}:\*\* ?(.*)$", corpo, re.M)
            return m.group(1).strip() if m else ""
        out.append({"n": int(partes[i]), "titulo": partes[i + 1].strip(), "status": campo("Status"),
                    "data": campo("Concluída em"), "funcs": links(campo("Funcionalidades")),
                    "notas": links(campo("Notas geradas"))})
    return out


def etapa_atual(etps):
    return next((e for e in etps if e["status"] not in ("concluida", "arquivada")), None)


def linha_atual(cur):
    return f"Etapa atual: **{cur['n']}. {cur['titulo']}** ({cur['status']})" if cur else "Todas as etapas concluídas."


def status(a):
    cofre = Path(a.cofre).resolve()
    rot = cofre / "orquestra/funcionalidades/geral/geral-plano.md"
    gc = cofre / "orquestra/funcionalidades/geral/geral-contexto.md"
    if not rot.exists():
        sys.exit("ERRO: falta o roteiro orquestra/funcionalidades/geral/geral-plano.md")
    s = ler(rot)
    etps = etapas(s)
    cur = etapa_atual(etps)
    if a.atualizar:
        novo = re.sub(r"(\[!tldr\][^\n]*\n> ).*", lambda m: m.group(1) + linha_atual(cur), s, count=1)
        if novo != s:
            escrever(rot, novo); print("atualizado  tldr do roteiro")
        if gc.exists() and cur:
            g = ler(gc)
            g2 = re.sub(r"^etapa-atual:.*$", f"etapa-atual: {cur['n']}", g, count=1, flags=re.M)
            if g2 != g:
                escrever(gc, g2); print("atualizado  etapa-atual do geral-contexto")
    ctxs = {p.stem.lower(): frontmatter(ler(p)) or {} for p in (cofre / "orquestra").rglob("*-contexto.md") if "modelos" not in p.parts}
    feitas = sum(e["status"] in ("concluida", "arquivada") for e in etps)
    print(f"\n== status {cofre.name}: {linha_atual(cur).replace('**', '')}")
    for e in etps:
        marca = {"concluida": "✔", "arquivada": "✔"}.get(e["status"], "▶" if e is cur else "·")
        extra = f" em {e['data']}" if e["data"] else ""
        print(f"  {marca} {e['n']}. {e['titulo']}  [{e['status']}{extra}]")
        for f in e["funcs"]:
            print(f"       funcionalidade {f}: {ctxs.get(f.lower(), {}).get('status', '?')}")
        if e["notas"]:
            print(f"       notas geradas: {', '.join(e['notas'])}")
    print(f"\nConcluídas: {feitas}/{len(etps)}.")
    return 0


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


def padroes(claude_txt):
    """Bloco ```padroes do CLAUDE.md -> (regras [(regex, forma certa, como aparece)], limite de palavras ou None)."""
    m = PADROES.search(claude_txt or "")
    regras, limite = [], None
    if not m:
        return regras, limite, False
    for linha in m.group(1).splitlines():
        linha = linha.strip()
        if not linha or linha.startswith("#"):
            continue
        lm = re.fullmatch(r"limite-palavras:\s*(\d+)", linha)
        if lm:
            limite = int(lm.group(1)); continue
        if "=>" not in linha:
            continue
        errado, certo = (x.strip() for x in linha.split("=>", 1))
        if errado.startswith("re:"):
            regras.append((re.compile(errado[3:]), certo, errado[3:]))
        else:
            regras.append((re.compile(re.escape(errado)), certo, errado))
    return regras, limite, True


def palavras(s):
    return len(s.split())


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
    claude_txt = ler(claude) if claude.exists() else ""
    regras, limite, tem_bloco = padroes(claude_txt)
    eh_kit = lambda p: rel(p).startswith(("orquestra/modelos/", "Modelos/", "orquestra/referencias/manual-"))
    for p in mds:
        if eh_kit(p):
            continue
        r = rel(p)
        alvo_txt = PADROES.sub("", texto[p]) if p == claude else texto[p]
        for rx, certo, como in regras:
            achados = rx.findall(alvo_txt)
            if achados:
                E(r, f"{len(achados)}x fora do padrão '{como}': use {certo} (bloco padroes do CLAUDE.md)")
        if projeto and limite and p != claude and palavras(texto[p]) > limite:
            E(r, f"{palavras(texto[p])} palavras (limite {limite}): divida em nota nova ligada por link (Padronização do CLAUDE.md)")
    if projeto:
        if "## Padronização" not in claude_txt:
            E("CLAUDE.md", "sem a seção 'Padronização' (copie do Modelo de CLAUDE do cofre)")
        if not tem_bloco or not limite:
            E("CLAUDE.md", "sem bloco ```padroes com 'limite-palavras: N'")
    if projeto:
        o = cofre / "orquestra"
        moc0 = cofre / "MOCs/moc-orquestra.md"
        if moc0.exists() and "Etapas vitais" not in ler(moc0):
            E("MOCs/moc-orquestra.md", "mapa sem a seção 'Etapas vitais' (etapa B5 do mapa)")
        diarios = sorted(d for d in (o / "diarios").glob("diario-*.md") if re.fullmatch(rf"diario-{DATA}\.md", d.name)) if (o / "diarios").is_dir() else []
        if not diarios:
            E("orquestra/diarios", "nenhum diário: falta ao menos o diário de criação (etapa A3)")
        elif not re.search(r"\*\*Próximo passo:\*\* *\S", ler(diarios[-1])):
            E(rel(diarios[-1]), "último diário sem 'Próximo passo' no Onde parei (passagem de turno, etapa C3)")
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
            if not re.fullmatch(rf"bug-[a-z0-9-]+-{DATA}(-[a-z0-9-]+)?\.md", n.name):
                E(rel(n), "nome fora do padrão bug-titulo-AAAA-MM-DD.md (parte dividida: bug-titulo-AAAA-MM-DD-assunto.md)")
        for n in (o / "diarios").glob("*.md"):
            if not re.fullmatch(rf"diario-{DATA}(-[a-z0-9-]+)?\.md", n.name):
                E(rel(n), "nome fora do padrão diario-AAAA-MM-DD.md (parte dividida: diario-AAAA-MM-DD-assunto.md)")
        rot = o / "funcionalidades/geral/geral-plano.md"
        gctx = o / "funcionalidades/geral/geral-contexto.md"
        fm_ctx = {p.stem.lower(): (p, frontmatter(texto.get(p, "")) or {}) for p in mds if p.name.endswith("-contexto.md") and not eh_modelo(p)}
        for st, (pc, fmc) in fm_ctx.items():
            if fmc.get("status") not in ESTADOS:
                E(rel(pc), f"status '{fmc.get('status')}' inválido para contexto ({' → '.join(ESTADOS)})")
        if not rot.exists():
            E("orquestra/funcionalidades/geral/geral-plano.md", "falta o roteiro do projeto (etapa A3)")
        else:
            rs = texto[rot]
            etps = etapas(rs)
            nums = [e["n"] for e in etps]
            if not etps:
                E(rel(rot), "roteiro sem etapas (seções '## 1. Nome')")
            elif nums != list(range(1, len(nums) + 1)):
                E(rel(rot), f"etapas fora da sequência 1..N: {nums}")
            for e in etps:
                tag = f"etapa {e['n']}"
                if e["status"] not in ESTADOS:
                    E(rel(rot), f"{tag}: status '{e['status']}' inválido")
                if e["status"] == "concluida":
                    if not re.fullmatch(DATA, e["data"]):
                        E(rel(rot), f"{tag} concluída sem 'Concluída em' AAAA-MM-DD")
                    if not [t for t in e["notas"] if t.lower() in todos]:
                        E(rel(rot), f"{tag} concluída sem link para as notas geradas")
                    for f in e["funcs"]:
                        stf = fm_ctx.get(f.lower(), (None, {}))[1].get("status")
                        if stf not in ("concluida", "arquivada"):
                            E(rel(rot), f"{tag} concluída, mas a funcionalidade {f} está '{stf}'")
            cur = etapa_atual(etps)
            m = re.search(r"\[!tldr\][^\n]*\n> (.*)", rs)
            if not m or m.group(1).strip() != linha_atual(cur):
                E(rel(rot), "linha 'Etapa atual' desatualizada: rode cofre.py status --atualizar")
            if gctx.exists() and cur and fm_ctx.get("geral-contexto", (None, {}))[1].get("etapa-atual") != str(cur["n"]):
                E(rel(gctx), f"etapa-atual difere do roteiro (etapa {cur['n']}): rode cofre.py status --atualizar")
            por_etapa = {e["n"]: {t.lower() for t in e["funcs"]} for e in etps}
            for st, (pc, fmc) in fm_ctx.items():
                if st == "geral-contexto":
                    continue
                et = fmc.get("etapa", "")
                if not et.isdigit() or int(et) not in por_etapa:
                    E(rel(pc), f"frontmatter 'etapa: {et}' não aponta para uma etapa do roteiro")
                elif st not in por_etapa[int(et)]:
                    E(rel(pc), f"funcionalidade fora da lista 'Funcionalidades' da etapa {et} no roteiro")
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
    st = sub.add_parser("status"); st.add_argument("cofre"); st.add_argument("--atualizar", action="store_true")
    a = ap.parse_args()
    if a.cmd == "criar":
        sys.exit(criar(a))
    if a.cmd == "sincronizar":
        sys.exit(sincronizar(a))
    if a.cmd == "status":
        sys.exit(status(a))
    sys.exit(verificar(a.cofre, achar_vault(a.vault, a.cofre)))


if __name__ == "__main__":
    main()
