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

## Contrato

- `docs/contrato/` é a fonte de verdade do que o produto faz: requisitos, atores (ATR), entidades (ENT), casos de uso (UC), componentes (CMP), erros (ERR), navegação (NAV) e critérios de aceite (AC). Ordem e regras em `docs/contrato/README.md`.
- Tela não cria regra: cada tela realiza CMP, UC e NAV do contrato. Regra que falta entra primeiro no contrato, com aval do humano e item em `docs/contrato/mudancas.md`.
- Campo de entrada: schema zod tirado do ENT (tipo, tamanho, formato, valores, teto), uma mensagem por violação (a do ERR) e o campo impede o impossível (S26 da nota `Padrão de projeto de software` do cofre `Vault`).
- Comentário curto e pontual: só o porquê que o código não mostra; ID citado só se existir em `docs/contrato/` (S27).
- Toda funcionalidade tem contrato (ENT, UC com FA e FE, ERR, AC); com interface, também CMP e NAV. Ao final de cada uma, o orquestrador roda o verificador de fluxo principal e depois o adversarial: eles executam os AC pela API e, com interface, na tela. Nenhuma suíte de E2E de interface fica no repositório.

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
- Regras: [[Manual da Orquestra]] e [[Manual da Orquestra - Perfil projeto prático]]
- Contrato que o bloco cita: [[Contrato funcional]] (modelos em `Modelos/Orquestra/contrato/`)
- Commits: [[Padrão de commit]]
