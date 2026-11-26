---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-26
substitui: 
---
# ✅ Rebase com force na branch da PR

- **Proposta (plano):** pedido do humano em 2026-11-26, 17h22, sobre a PR #17 (T8): a branch trazia os commits da T7 com hashes que não estão na `main` e um merge da `main`, e o GitHub não liberou o "Rebase and merge".
- **Decisão:** quando a branch de uma PR tem commits com hashes diferentes dos da `main` (o mesmo conteúdo com outro hash, ou um merge da `main`), o implementador refaz a branch sobre a `main` por rebase, só com os commits da tarefa, e dá `git push --force-with-lease` nessa branch. Antes, guarda o hash antigo numa branch local de backup e confere que o conteúdo final é igual ao de antes.
- **Alteração:** nenhuma
- **Motivo:** aval do humano em 2026-11-26, 17h22 ("sempre quando uma branch estiver com os indexes trocados eu gosto de usar o rebase [...] vamos fazer --force").
- **Consequências:** o `--force-with-lease` vale só na branch da tarefa, nunca na `main`; o briefing diz a branch e o hash esperado. O merge da `main` numa branch de tarefa deixa de ser o caminho para atualizar uma PR.

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[integracoes-plano]]
- Junto: [[geral-decisao-2026-11-23-uma-pr-por-tarefa]], [[geral-decisao-2026-11-23-push-e-pr-no-github]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
