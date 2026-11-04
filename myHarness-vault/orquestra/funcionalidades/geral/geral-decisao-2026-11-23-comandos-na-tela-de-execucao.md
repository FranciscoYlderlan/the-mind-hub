---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-23
substitui: 
---
# ✅ Comandos da execução vão para a tela de execução

- **Proposta (plano):** conferência da T5 do [[fundacao-plano]]: o DTO `Execucao` saiu sem `comandos` (ENT-07, M-41), com a ideia de mostrar os comandos só pelo Log (ENT-12).
- **Decisão:** os comandos executados pelo agente (`comandos` da ENT-07) entram no DTO `Execucao` da IPC e aparecem na tela de execução.
- **Alteração:** recusada a ideia de deixar os comandos só no Log.
- **Motivo:** resposta do humano em 2026-11-23, às 17h26: "na tela de execução".
- **Consequências:** o DTO `Execucao` em Rust, TS e zod ganha `comandos` (lista de texto, mascarada pela RN-04); em que componente da tela os comandos aparecem (CMP-04 ou CMP-05) [a confirmar] no contrato da etapa 7.

### 🔗 Conexões
- Funcionalidade: [[fundacao-contexto]]
- Plano: [[fundacao-plano]]
- Candidatos: [[fundacao-plano-candidatos]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
