---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-19
substitui: 
---
# ✅ Data e hora em UTC no SQLite, hora local na tela

- **Proposta (plano):** dúvida 4 da Lista 2 de `Anexos/relatorio-contrato-2026-11-19.txt`.
- **Decisão:** toda data e hora é guardada no SQLite em ISO 8601 UTC e mostrada na tela na hora local do Windows.
- **Alteração:** entidades com data em `02-entidades.md` do contrato em `Anexos/contrato/` (item M-xx do `mudancas.md`).
- **Motivo:** resposta do humano em 2026-11-19 (opção recomendada pelo pesquisador do contrato).
- **Consequências:** o esquema SQLite do G1 usa texto ISO 8601 com `Z`; a conversão para a hora local fica só na tela.

### 🔗 Conexões
- Projeto: [[geral-contexto]]
- Plano: [[geral-plano]]
- Regras: [[manual-da-orquestra]]
- Origem: [[diario-2026-11-19]]
