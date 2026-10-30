---
tipo: decisao
funcionalidade: sala-ao-vivo
status: aprovada
criado: 2026-10-30
substitui: 
aliases: [Rotas do I3]
---
# ✅ Rotas públicas e tools novas do I3

- **Proposta (plano):** [[sala-ao-vivo-plano#Pontos para o aval do humano]], ponto 7.
- **Decisão:** Rotas públicas novas: `GET /lots/:id/events` e `GET /receipts/:publicId`. Rotas com login: `GET /me/bids` (licitante) e o total recebido em `GET /auctioneer/lots`. Tools novas na MCP: `receipts_get` e `bids_mine`; `auctioneer_lots` traz o total e `lots_cancel` exige o motivo. Contrato completo na T1 de [[sala-ao-vivo-plano]]. Aprovada pelo humano em 2026-10-30 11:2x.
- **Alteração:** nenhuma.
- **Motivo:** Cada rota nova sai com a sua tool ([[geral-decisao-2026-10-29-camada-mcp]]); comprovante e stream não têm dado pessoal.
- **Consequências:** Comprovante com link adulterado dá 404 `RECEIPT_NOT_FOUND`; o comprovante não chama a API externa (T-07, T-09).

### 🔗 Conexões
- Funcionalidade: [[sala-ao-vivo-contexto]]
- Plano: [[sala-ao-vivo-plano]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
