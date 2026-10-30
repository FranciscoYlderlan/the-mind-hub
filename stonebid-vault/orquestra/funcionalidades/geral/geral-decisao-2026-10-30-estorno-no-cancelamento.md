---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-30
aliases: [Estorno no cancelamento, Cancelamento com estorno, OPC-2, Refund on cancel]
---
# ✅ Cancelamento de lote com lances e estorno do líder (OPC-2)

- **Proposta (plano):** pesquisador da etapa 7, 2026-10-30 17:4x, em [[opcionais-plano]]. O código recusa cancelar lote com `headSeq > 0`, e o `computeBalance` soma `REFUND` ao total: gravar `REFUND` com a regra de hoje criaria dinheiro, porque o líder só tem `COMMIT`.
- **Decisão:** humano aprovou em 2026-10-30 17:4x:
  1. **Sinalizador** `CANCEL_WITH_BIDS_ENABLED`, ligado em produção e staging; o caso de uso recebe o valor, e o T-10a testa com ele desligado. Com ele ligado, "já tem lances" deixa de ser motivo de recusa.
  2. **Estorno libera o comprometido do líder:** `comprometido = COMMIT − RELEASE − REFUND`; o total não muda e o disponível volta ao de antes do lance. O extrato mostra "Estorno" com o lote. Superados já tinham `RELEASE`; o leiloeiro não recebe nada. Antes do deploy, conferir 0 linhas `REFUND` em produção.
  3. **Mesma transação e trava do cancelamento:** grava `canceledAt` e motivo e, se houver lances, um `REFUND` do `leaderId` no valor de `currentBidCents`. Líder, lance atual e cabeça ficam como estão; cancelar de novo dá "já cancelado".
  4. **Auditoria confere o estorno:** lote cancelado com lances tem exatamente um `REFUND` do líder no valor do lance atual; qualquer outro lote, nenhum. Senão, ADULTERADO com `CANCEL_MISMATCH`.
  5. **Rota sem mudança de contrato:** `POST /lots/:id/cancel {reason}`, 422 do motivo, 403, 404, 409 `LOT_NOT_CANCELABLE` (só "já cancelado") ou `LOT_ENDED`; a tool `lots_cancel` atualiza a descrição.
  6. **Web:** o diálogo avisa "N lances; o líder recebe estorno de R$ X"; o evento SSE `canceled` invalida carteira e meus lances; a auditoria mostra "cancelado em" com o motivo.
  7. **T-10b:** disponível do líder volta e total igual; superados intactos; um `REFUND` só; auditoria ÍNTEGRO, e ADULTERADO com `REFUND` apagado ou duplicado; cancelamento e lance ao mesmo tempo sem comprometido preso; liquidação ignora o lote; meus lances mostra `CANCELED`.
- **Alteração:** nenhuma; o humano aceitou a proposta da IA.
- **Motivo:** o OPC-2 é opcional avaliado no E5; o sentido novo do `REFUND` evita migração e o dinheiro criado; a conferência na auditoria compensa o `canceledAt` sem selo.
- **Consequências:** T-03 e `wallet.test.ts` mudam junto; o sinalizador entra no `cd.yml`. Primeiro corte se apertar: a conferência da auditoria e o aviso do diálogo.

### 🔗 Conexões
- Funcionalidade: [[opcionais-contexto]]
- Plano: [[opcionais-plano]]
- Relacionadas: [[geral-decisao-2026-10-29-cancelamento-ao-vivo]], [[geral-decisao-2026-10-30-motivo-do-cancelamento-gravado]], [[geral-decisao-2026-10-30-posicao-cancelado-inalcancavel]], [[geral-decisao-2026-10-30-achados-da-t5-da-auditoria]], [[geral-decisao-2026-10-29-testes-no-escopo]]
- Regras: [[manual-da-orquestra]]
