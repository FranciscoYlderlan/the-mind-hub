---
tipo: plano
funcionalidade: sala-ao-vivo
status: proposta
criado: 2026-10-30
aliases: [Plano do I3, Plano da sala ao vivo, Live room plan]
---
# 📋 Sala ao vivo e liquidação (I3): plano

> [!warning] Proposta da IA
> Nada aqui é decisão. Decisões ficam nas notas `-decisao-` linkadas abaixo.

## Objetivo desta rodada
Sala que atualiza sem recarregar, anti-sniping, liquidação única com movimentos da carteira, comprovante público, Meus arremates e total do leiloeiro, tudo no ar em staging. Base: [[sala-ao-vivo-contexto]].

## Decisões que este plano respeita
- [[geral-decisao-2026-10-29-comprovante-e-hash]], [[geral-decisao-2026-10-29-testes-no-escopo]], [[geral-decisao-2026-10-29-cancelamento-ao-vivo]], [[geral-decisao-2026-10-29-camada-mcp]], [[geral-decisao-2026-10-29-seed-tambem-em-producao]], [[geral-decisao-2026-10-30-lance-atual-no-lote]], [[geral-decisao-2026-10-29-modo-de-implementacao]].

(Dial: o do [[geral-contexto]].)

### Pontos para o aval do humano
Aval em 2026-10-30 11:2x, todos como propostos:
1. Tempo real: [[geral-decisao-2026-10-30-tempo-real-por-sse]].
2. Disparo da liquidação: [[geral-decisao-2026-10-30-disparo-da-liquidacao]].
3. Movimentos da carteira: [[geral-decisao-2026-10-30-movimentos-da-liquidacao]].
4. Resultado no lote: [[geral-decisao-2026-10-30-resultado-no-lote]].
5. Anti-sniping: [[geral-decisao-2026-10-30-limite-do-anti-sniping]].
6. Viewer no lote: [[geral-decisao-2026-10-30-viewer-no-lote]].
7. Rotas e tools: [[geral-decisao-2026-10-30-rotas-publicas-do-i3]].
8. Seed liquidado: [[geral-decisao-2026-10-30-seed-com-lote-liquidado]].
9. Motivo do cancelamento: [[geral-decisao-2026-10-30-motivo-do-cancelamento-gravado]].

Também entram aqui, do I2: [[geral-decisao-2026-10-30-pseudonimo-com-6-digitos]], [[geral-decisao-2026-10-30-dar-lance-so-para-licitante]], [[geral-decisao-2026-10-30-recarga-de-15s-ate-o-i3]].

## Tarefas

### T1: contrato da API (sem PR)
- **Faz:** o orquestrador fixa nos briefings: `LotDto` com `result`, `settledAt`, `receiptPublicId`, `cancelReason` e `viewer` (só em `GET /lots/:id` com JWT de licitante; senão `null`); `GET /lots/:id/events` (SSE público: `snapshot`, `bid`, `canceled`, `settled`, cada um com `{ serverTime, lot }`, `: ping` a cada 15 s); `POST /lots/:id/cancel` com `{ reason }` de 3 a 280 caracteres; `GET /receipts/:publicId` (público, 404 `RECEIPT_NOT_FOUND`); `GET /me/bids` (licitante, posição `LEADING`, `OUTBID`, `WON`, `LOST` ou `CANCELED`); `GET /auctioneer/lots` com `totalReceivedCents`; tools `receipts_get` e `bids_mine`.
- **Pronto quando:**
  - [x] contrato nos briefings de T2a, T2b, T3 e T4 (2026-10-30 11:3x)

### T2a: liquidação, comprovante e anti-sniping (API)
- **Faz:** schema e migração (`settledAt`, `result`, `cancelReason`, `Receipt`); pseudônimo de 6 dígitos com migração que apaga os lances de teste e zera a cabeça dos lotes; anti-sniping no lance; `SettleLotUseCase` idempotente com agendador de 5 s e liquidação na leitura; viewer; `/receipts`, `/me/bids`, total do leiloeiro; motivo do cancelamento; tools; seed com lote liquidado; README.
- **Toca em:** `stonebid-api`: `prisma/`, `src/domain/`, `src/application/`, `src/infra/`, `src/server.ts`, `test/`. Branch `feat/RN-11-liquidacao-e-comprovante`.
- **Paralelo:** sim, com T2b, T3 e T4
- **Pronto quando:**
  - [ ] T-04, T-05 (inclui disparo duplo), T-07, T-09 e E2E das rotas e tools; CI verde
- **Prova:** `npm run lint && npm run typecheck && npm test && npm run build`

### T2b: tempo real por SSE (API)
- **Faz:** port de publicação de eventos, barramento em memória, rota do stream, publicação depois do COMMIT no lance e no cancelamento, `--max-instances=1` no `cd.yml`.
- **Toca em:** `stonebid-api`: `src/application/`, `src/infra/http/`, `src/infra/events/`, `src/app.ts`, `.github/workflows/cd.yml`, `test/`. Branch `feat/RF-31-sala-em-tempo-real`.
- **Paralelo:** sim; merge antes da T2a, que publica `settled` depois do rebase
- **Pronto quando:**
  - [ ] E2E: lance chega pelo stream em < 2 s; cancelamento gera `canceled`; listener removido ao fechar; CI verde
- **Prova:** idem T2a

### T3: sala ao vivo (web)
- **Faz:** `EventSource` com plano B de 3 s; contagem pelo `serverTime` e aviso de prorrogação; "ganhando" ou "superado"; estados vendido, sem vencedor e cancelado com motivo; "Dar lance" escondido do leiloeiro.
- **Toca em:** `stonebid-web`: `src/features/lots/`, `src/features/bids/`, rotas do lote, `e2e/`. Branch `feat/RF-31-sala-ao-vivo`, Playwright na porta 4174.
- **Paralelo:** sim
- **Pronto quando:**
  - [ ] Playwright de cada estado e da queda do stream; CI verde
- **Prova:** `npm run lint && npm run typecheck && npm run build`; Playwright

### T4: Meus arremates, comprovante e total (web)
- **Faz:** página pública `/receipts/$publicId` com cópia do link; Meus arremates; total recebido e resultado no painel do leiloeiro; motivo no cancelamento.
- **Toca em:** `stonebid-web`: `src/features/receipts/`, Meus arremates, painel do leiloeiro, rotas novas, `e2e/`. Branch `feat/RF-50-arremates-e-comprovante`, Playwright na porta 4175.
- **Paralelo:** sim
- **Pronto quando:**
  - [ ] Playwright das telas novas e do cancelamento com motivo; CI verde
- **Prova:** idem T3

### T5: merge e staging
- **Faz:** merge do humano na ordem T2b → T2a → `staging` da API → T3 → T4 → `staging` do web; CD verde; migração do pseudônimo aplicada nos dois ambientes.
- **Depende de:** T2a a T4

### T6: verificação no ar
- **Faz:** verificador no Chrome em staging: leilão completo com dois licitantes (lance que chega à outra aba sem recarregar, anti-sniping num lote curto, liquidação, comprovante por link sem login, Meus arremates, total do leiloeiro, cancelamento com motivo); verificador de código lê os diffs.
- **Depende de:** T5
- **Pronto quando:**
  - [ ] relatórios sem bloqueante

## Próxima tarefa e a seguinte
Agora: T2a, T2b, T3 e T4 em paralelo (despachadas 11:3x). Depois: T5 e T6. A T5 do I2 ([[lances-plano]]) corre junto no Chrome.

## Prioridades
T2a é o caminho crítico. Se apertar: corta o seed liquidado, depois o aviso de prorrogação no web.

## Candidatos a registro
- (nenhum ainda)

### 🔗 Conexões
- Funcionalidade: [[sala-ao-vivo-contexto]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
