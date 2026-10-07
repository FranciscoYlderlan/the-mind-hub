---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-30
aliases: [Posição Cancelado, CANCELED em Meus arremates, Canceled bid position]
---
# ✅ Posição "Cancelado" em Meus arremates fica como está

- **Proposta (plano):** achado do verificador no Chrome da T6 em [[sala-ao-vivo-plano]].
- **Decisão:** a posição `CANCELED` de `GET /me/bids` e o selo dela no web ficam no código, sem mudança, mesmo sem caso real hoje. Aprovada pelo humano em 2026-10-30 13:06.
- **Alteração:** nenhuma.
- **Motivo:** só se cancela lote sem lances ([[geral-decisao-2026-10-29-cancelamento-ao-vivo]]), e lote sem lances não aparece em Meus arremates; a posição só passa a existir se o cancelamento com estorno dos opcionais (I5) entrar.
- **Consequências:** a posição `CANCELED` fica sem prova no ar; se o I5 permitir cancelar lote com lances, ela entra no teste do Chrome.

### 🔗 Conexões
- Funcionalidade: [[sala-ao-vivo-contexto]]
- Plano: [[sala-ao-vivo-plano]]
- Decisões ligadas: [[geral-decisao-2026-10-29-cancelamento-ao-vivo]], [[geral-decisao-2026-10-30-motivo-do-cancelamento-gravado]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
