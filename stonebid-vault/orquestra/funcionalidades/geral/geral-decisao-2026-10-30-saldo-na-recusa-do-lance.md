---
tipo: decisao
funcionalidade: lances
status: aprovada
criado: 2026-10-30
substitui: 
aliases: [Saldo na recusa, INSUFFICIENT_FUNDS com disponível, Insufficient funds details]
---
# ✅ Recusa por saldo devolve o disponível

- **Proposta (plano):** [[lances-plano#Pontos para o aval do humano]], ponto 5.
- **Decisão:** a recusa `INSUFFICIENT_FUNDS` (422) devolve `details.availableCents`, e a tela mostra quanto o licitante tem disponível. Aprovada pelo humano em 2026-10-30 08:4x.
- **Alteração:** nenhuma.
- **Motivo:** o RF-70 pede motivo claro; com o disponível, o licitante sabe quanto depositar.
- **Consequências:** o mesmo vale para a tool `bids_place` da MCP, que repassa a resposta da rota.

### 🔗 Conexões
- Funcionalidade: [[lances-contexto]]
- Plano: [[lances-plano]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
