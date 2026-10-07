---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-30
aliases: [LOT_ENDED no cancelamento, Cancelamento de lote encerrado, Cancel ended lot]
---
# ✅ Cancelar lote já encerrado dá 409 LOT_ENDED

- **Proposta (plano):** desvio da T2a em [[sala-ao-vivo-plano]].
- **Decisão:** `POST /lots/:id/cancel` em lote já encerrado (liquidado ou ainda não) responde 409 `LOT_ENDED`, o mesmo código do lance fora do prazo. Aprovada pelo humano em 2026-10-30 12:44.
- **Alteração:** nenhuma.
- **Motivo:** diz o motivo real da recusa; o web já mostra a mensagem da API no diálogo.
- **Consequências:** o código `LOT_NOT_CANCELABLE` não aparece para lote encerrado.

### 🔗 Conexões
- Funcionalidade: [[sala-ao-vivo-contexto]]
- Plano: [[sala-ao-vivo-plano]]
- Decisões ligadas: [[geral-decisao-2026-10-29-cancelamento-ao-vivo]], [[geral-decisao-2026-10-30-motivo-do-cancelamento-gravado]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
