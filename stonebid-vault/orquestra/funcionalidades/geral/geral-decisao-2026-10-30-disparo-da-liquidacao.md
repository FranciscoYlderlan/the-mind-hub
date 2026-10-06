---
tipo: decisao
funcionalidade: sala-ao-vivo
status: aprovada
criado: 2026-10-30
substitui: 
aliases: [AD-08, Disparo da liquidação]
---
# ✅ Liquidação disparada por agendador no processo e na leitura

- **Proposta (plano):** [[sala-ao-vivo-plano#Pontos para o aval do humano]], ponto 2.
- **Decisão:** A liquidação (AD-08) dispara por dois caminhos: um `setInterval` de 5 s no `server.ts` (desligado nos testes) que liquida até 20 lotes vencidos, e a liquidação na leitura em `GET /lots/:id`, `GET /lots`, `GET /auctioneer/lots`, `GET /me/bids` e `GET /receipts/:publicId`. Sem Cloud Scheduler. Aprovada pelo humano em 2026-10-30 11:2x.
- **Alteração:** nenhuma.
- **Motivo:** Staging dorme (`min=0`) e o agendador para junto; a leitura garante a liquidação quando alguém olha o lote (R-06 de [[contrato-riscos]]).
- **Consequências:** O `SettleLotUseCase` precisa ser idempotente: trava do lote, checagem de `settledAt` e `lotId` único no comprovante (T-05, disparo duplo).

### 🔗 Conexões
- Funcionalidade: [[sala-ao-vivo-contexto]]
- Plano: [[sala-ao-vivo-plano]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
