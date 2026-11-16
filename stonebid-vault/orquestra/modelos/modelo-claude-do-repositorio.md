# Trecho para o CLAUDE.md do repositório de código

Colar o bloco abaixo no `CLAUDE.md` ou `AGENTS.md` do repositório do projeto, trocando os campos. Só o bloco: as Conexões ficam aqui.

```markdown
## Memória do projeto

A memória deste projeto é o cofre Obsidian `{{nome-do-cofre}}`, em `{{caminho-do-cofre}}`.

- Antes de qualquer tarefa, leia `{{caminho-do-cofre}}/CLAUDE.md` e siga a ordem de leitura dele.
- Leia e busque o cofre **pela Obsidian CLI antes de qualquer outra ferramenta** (ferramentas `obsidian_*` do servidor MCP `obsidian-cli`, com `vault="{{nome-do-cofre}}"`). Falhou: siga o plano B da seção "Como buscar" do `CLAUDE.md` do cofre e avise.
- A sessão principal é o orquestrador: só ela escreve no cofre, e registra cada relatório e decisão aprovada assim que chega.
- Subagentes leem o cofre, trabalham em worktree própria e devolvem relatório no formato de `orquestra/modelos/modelo-relatorio-subagente.md`.
- Comandos de prova deste repositório: teste `{{comando}}` · lint `{{comando}}` · tipos `{{comando}}`

## Commits

- Padrão de commit do humano (nota `Padrão de commit` do cofre `Vault`, lida pela CLI): `{emoji} {tipo}(escopo): Description`, em inglês, imperativo, escopo só da lista abaixo; só no nome do humano, sem `Co-Authored-By` nem link de sessão.
- Quando: um commit por unidade lógica; PR ao fim da tarefa.

<!-- projeto:escopos -->
- Escopos deste repositório (lista fechada, escolhida na criação): {{escopos}}
<!-- /projeto:escopos -->
```

### 🔗 Conexões
- Lado do cofre: o `CLAUDE.md` do cofre, gerado de `Modelo de CLAUDE do cofre`
- Formato dos subagentes: [[modelo-briefing-subagente]], [[modelo-relatorio-subagente]]
- Regras: [[manual-da-orquestra]] e Manual da Orquestra - Perfil projeto prático (no Vault)
- Commits: Padrão de commit (no Vault)
