---
tipo: decisao
funcionalidade: lances
status: aprovada
criado: 2026-10-30
substitui: 
aliases: [Histórico de lances no I2, GET bids público, Public bid history]
---
# ✅ Histórico público de lances já no I2

- **Proposta (plano):** [[lances-plano#Pontos para o aval do humano]], ponto 6.
- **Decisão:** `GET /lots/:id/bids` público entra no I2: ordem, pseudônimo, valor e hora, sem `bidderId`, nome, e-mail, `hash` ou `seal`. Aprovada pelo humano em 2026-10-30 08:4x.
- **Alteração:** nenhuma.
- **Motivo:** a MCP acompanha lances pelo histórico ([[geral-decisao-2026-10-29-camada-mcp]]), e o T-09 já se aplica.
- **Consequências:** a auditoria do I4 (RF-60, RF-61) amplia a leitura com hash, selo e veredito; até lá, o histórico não promete integridade. Anti-sniping (RN-10, T-04) segue no I3, com `endsAt` lido sob a trava do lote desde o I2 (ponto 4 do plano).

### 🔗 Conexões
- Funcionalidade: [[lances-contexto]]
- Plano: [[lances-plano]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
