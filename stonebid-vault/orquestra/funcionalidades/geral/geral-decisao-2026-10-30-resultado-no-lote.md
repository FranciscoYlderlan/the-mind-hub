---
tipo: decisao
funcionalidade: sala-ao-vivo
status: aprovada
criado: 2026-10-30
substitui: 
aliases: [Resultado do lote]
---
# ✅ Resultado da liquidação guardado no lote

- **Proposta (plano):** [[sala-ao-vivo-plano#Pontos para o aval do humano]], ponto 4.
- **Decisão:** O `Lot` ganha `settledAt` e `result` (`SOLD` ou `NO_WINNER`). Vencedor e valor final são o `leaderId` e o `currentBidCents`, que congelam na liquidação, sem colunas novas. A tabela `Receipt` segue o formato de [[geral-decisao-2026-10-29-comprovante-e-hash]]. Aprovada pelo humano em 2026-10-30 11:2x.
- **Alteração:** nenhuma.
- **Motivo:** O lote já guarda o líder e o lance atual ([[geral-decisao-2026-10-30-lance-atual-no-lote]]); repetir em outra coluna abriria espaço para divergência.
- **Consequências:** Lote liquidado não aceita lance nem cancelamento; o `LotDto` ganha `result`, `settledAt` e `receiptPublicId`.

### 🔗 Conexões
- Funcionalidade: [[sala-ao-vivo-contexto]]
- Plano: [[sala-ao-vivo-plano]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
