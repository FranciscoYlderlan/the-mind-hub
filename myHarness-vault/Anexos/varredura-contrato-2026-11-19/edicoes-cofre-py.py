E = []
def e(a, n): E.append(("Modelos/Orquestra/cofre.py", a, n))
e("""Modelos do repositorio: Vault/Modelos/Orquestra/contrato/ (contrato funcional, copiado para docs/contrato/ do repositorio de
codigo) vai no kit para orquestra/modelos/contrato/ so no perfil pratico (o perfil vem da linha '- Perfil:' do geral-contexto,
tambem no 'sincronizar' e no 'verificar'), como a secao "Validar cada funcionalidade" do CLAUDE.md; e Markdown puro, sem frontmatter nem Conexoes, e o 'verificar' nao o le.""",
"""Contrato funcional: Vault/Modelos/Orquestra/contrato/ e copiado pelo 'criar' para Anexos/contrato/ do cofre novo, so no perfil
pratico (o perfil vem da linha '- Perfil:' do geral-contexto, tambem no 'verificar'). Ali ele e editado durante o projeto, so pelo
orquestrador; o 'sincronizar' nunca o sobrescreve. E Markdown puro, sem frontmatter nem Conexoes, e o 'verificar' nao o le como
nota, mas da ERRO se um cofre pratico nao tiver Anexos/contrato/00-requisitos.md.""")
e("""# Modelos de arquivos do repositorio de codigo (nao sao notas): copiados no kit, ignorados pelo verificar.
MODELOS_DO_REPO = ("Modelos/Orquestra/contrato/", "orquestra/modelos/contrato/")""",
"""# Contrato funcional (Markdown puro, nao sao notas): modelo no Vault, contrato do projeto em Anexos/contrato/.
# orquestra/modelos/contrato/ e o lugar antigo (cofre de antes de 2026-11-19): ignorado como nota, com AVISO para migrar.
CONTRATO = "Anexos/contrato/"
CONTRATO_ANTIGO = "orquestra/modelos/contrato/"
NAO_NOTAS = ("Modelos/Orquestra/contrato/", CONTRATO, CONTRATO_ANTIGO)""")
e("""    for f in sorted((vault / "Modelos" / "Orquestra" / "contrato").glob("*.md")) if pratico else []:
        k["modelos/contrato/" + f.name] = ler(f)  # Markdown puro do repositorio (so no pratico): copia sem converter
""", "")
e("""def kit(vault, pratico=True):""", """def contrato_modelo(vault):
    \"\"\"Arquivos do contrato funcional (nome -> texto), copiados sem converter para Anexos/contrato/ pelo criar.\"\"\"
    return {f.name: ler(f) for f in sorted((vault / "Modelos" / "Orquestra" / "contrato").glob("*.md"))}


def kit(vault, pratico=True):""")
e("""    escrever(dest / PADROES_NOTA, padroes_inicial(d, a.projeto))
""", """    escrever(dest / PADROES_NOTA, padroes_inicial(d, a.projeto))
    if pratico:  # contrato do projeto: nasce aqui e so o orquestrador o altera (Q01); o sincronizar nao o toca
        for nome, txt in contrato_modelo(vault).items():
            escrever(dest / CONTRATO / nome, txt)
""")
e("""         + (("; colar o trecho do modelo-claude-do-repositorio no repositório de código, copiar `orquestra/modelos/contrato/` para "
             "`docs/contrato/` do repositório e preencher o `00-requisitos.md` a partir do documento-fonte e, se for software, propor \"""",
"""         + (("; colar o trecho do modelo-claude-do-repositorio no repositório de código, preencher o "
             "`Anexos/contrato/00-requisitos.md` a partir do documento-fonte e, se for software, propor \"""")
e("""    mds = [p for p in cofre.rglob("*.md") if not oculto(p) and not rel(p).startswith(MODELOS_DO_REPO)]""",
"""    mds = [p for p in cofre.rglob("*.md") if not oculto(p) and not rel(p).startswith(NAO_NOTAS)]""")
e("""        vault = vault or achar_vault(None, cofre)
        if vault:
            for relk, txt in kit(vault, not perfil_estudo(cofre)).items():""",
"""        vault = vault or achar_vault(None, cofre)
        if not perfil_estudo(cofre):
            exigidos = list(contrato_modelo(vault)) if vault else ["00-requisitos.md"]
            faltam = [n for n in exigidos if not (cofre / CONTRATO / n).exists()]
            if faltam:
                E(CONTRATO.rstrip("/"), f"perfil prático sem o contrato funcional completo (faltam {', '.join(faltam)}): "
                  "copie Vault/Modelos/Orquestra/contrato/ para Anexos/contrato/ (cofre novo: o criar já copia; "
                  "contrato em uso em outro lugar: mova para cá, com confirmação)")
            if (cofre / CONTRATO_ANTIGO).is_dir():
                A(CONTRATO_ANTIGO.rstrip("/"), "lugar antigo do contrato: o contrato do projeto mora em Anexos/contrato/; "
                  "mova ou arquive esta pasta, com confirmação do humano")
        if vault:
            for relk, txt in kit(vault, not perfil_estudo(cofre)).items():""")
