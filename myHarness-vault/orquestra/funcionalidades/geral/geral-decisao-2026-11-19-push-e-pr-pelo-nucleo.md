---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-19
substitui: 
---
# ✅ O núcleo faz o push e abre o PR

- **Proposta (plano):** dúvida 2 da Lista 2 de `Anexos/relatorio-contrato-2026-11-19.txt`: o contrato dizia que o subagente faz push e PR, mas a [[geral-decisao-2026-11-19-agente-por-claude-p]] roda o agente sem token do GitHub.
- **Decisão:** o subagente só commita na própria worktree; o núcleo do MyHarness faz o push e abre o PR (RF-27), com o token do app OAuth próprio ([[geral-decisao-2026-11-19-github-oauth-proprio]]).
- **Alteração:** RN-17, ATR-03, UC-04 passo 3, o prompt de fábrica e o AC-114 do contrato em `Anexos/contrato/`, a reescrever no estado atual (item M-xx do `mudancas.md`).
- **Motivo:** resposta do humano em 2026-11-19 (opção recomendada pelo pesquisador do contrato).
- **Consequências:** nenhum agente recebe token do GitHub; o P1 continua valendo sem mudança.

### 🔗 Conexões
- Projeto: [[geral-contexto]]
- Plano: [[geral-plano]]
- Regras: [[manual-da-orquestra]]
- Origem: [[diario-2026-11-19]]
