---
tipo: decisao
funcionalidade: sala-ao-vivo
status: aprovada
criado: 2026-10-30
substitui: 
aliases: [cancelReason]
---
# ✅ Motivo do cancelamento gravado no lote

- **Proposta (plano):** [[sala-ao-vivo-plano#Pontos para o aval do humano]], ponto 9.
- **Decisão:** O `Lot` ganha `cancelReason`; `POST /lots/:id/cancel` exige `{ reason }` com 3 a 280 caracteres (sem ele, 422 `VALIDATION_ERROR`); a tela do leiloeiro pede o motivo e o `LotDto` o mostra. Entra no I3. Aprovada pelo humano em 2026-10-30 11:2x.
- **Alteração:** nenhuma.
- **Motivo:** [[geral-decisao-2026-10-29-cancelamento-ao-vivo]] já exige o motivo, obrigatório também sem lances, e o schema não tinha coluna para ele.
- **Consequências:** A tool `lots_cancel` passa a exigir `reason`; a sala recebe o evento `canceled` com o motivo.

### 🔗 Conexões
- Funcionalidade: [[sala-ao-vivo-contexto]]
- Plano: [[sala-ao-vivo-plano]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
