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
  - [x] T-04, T-05 (inclui disparo duplo), T-07, T-09 e E2E das rotas e tools; CI verde
- **Prova:** `npm run lint && npm run typecheck && npm test && npm run build`

- **Verificação:**
  - Data: 2026-10-30 12:1x. PR #13 do `stonebid-api` (`b2bd859`), rebaseado sobre o #12, CI verde, 193 testes; merge do humano às 12:07 (`f756ac2`); `staging` avançada (`8c27da3..f756ac2`).
  - Disparo duplo: 5 disparos simultâneos dão 1 comprovante e 1 DEBIT/CREDIT; índice parcial único de DEBIT/CREDIT por lote como segunda barreira. `settled` publicado no SSE depois do COMMIT. Migration `20261030110000_reset_bids_pseudonym_6` apaga os lances de teste no próximo CD. Seed: `seed-3` liquidado, `licitante-2` vence por R$ 350,00.
  - Desvios (aprovados em 2026-10-30 12:44, [[geral-decisao-2026-10-30-lot-ended-no-cancelamento]] e [[geral-decisao-2026-10-30-422-no-cancelamento]]): cancelar lote encerrado ainda não liquidado dá 409 `LOT_ENDED` (antes `LOT_NOT_CANCELABLE`); `GET /receipts/:publicId` não liquida na leitura (o comprovante só existe depois); 422 só no cancelamento (o resto segue 400 `VALIDATION_ERROR`); `lots_get` da MCP manda o token para o `viewer`.

### T2b: tempo real por SSE (API)
- **Faz:** port de publicação de eventos, barramento em memória, rota do stream, publicação depois do COMMIT no lance e no cancelamento, `--max-instances=1` no `cd.yml`.
- **Toca em:** `stonebid-api`: `src/application/`, `src/infra/http/`, `src/infra/events/`, `src/app.ts`, `.github/workflows/cd.yml`, `test/`. Branch `feat/RF-31-sala-em-tempo-real`.
- **Paralelo:** sim; merge antes da T2a, que publica `settled` depois do rebase
- **Pronto quando:**
  - [x] E2E: lance chega pelo stream em < 2 s; cancelamento gera `canceled`; listener removido ao fechar; CI verde
- **Prova:** idem T2a

- **Verificação:**
  - Data: 2026-10-30 11:49. PR #12 do `stonebid-api` (`e935308`), CI verde, 160 testes; merge do humano (`8c27da3`); `staging` avançada (`55b1400..8c27da3`).
  - Port `LotEventsPublisher.publish(lotId, 'bid'|'canceled'|'settled')` (`src/application/lot-events-publisher.ts`), factory `makeLotEventsPublisher()`; barramento relê o lote uma vez por evento, em fila por lote; rota inscreve antes do snapshot; replay da mesma chave não gera evento.
  - Desvios (aprovados em 2026-10-30 12:44, [[geral-decisao-2026-10-30-concorrencia-do-cloud-run]]): `--concurrency=1000` além do `--max-instances=1` no `cd.yml` (cada stream ocupa uma vaga; o padrão de 80 enfileiraria o 81º); sem tool MCP para o stream (MCP é pedido e resposta). Falta: `settled` publicado pela T2a; medir buffer do Cloud Run e os 2 s do RNF-06 no Chrome.

### T3: sala ao vivo (web)
- **Faz:** `EventSource` com plano B de 3 s; contagem pelo `serverTime` e aviso de prorrogação; "ganhando" ou "superado"; estados vendido, sem vencedor e cancelado com motivo; "Dar lance" escondido do leiloeiro.
- **Toca em:** `stonebid-web`: `src/features/lots/`, `src/features/bids/`, rotas do lote, `e2e/`. Branch `feat/RF-31-sala-ao-vivo`, Playwright na porta 4174.
- **Paralelo:** sim
- **Pronto quando:**
  - [x] Playwright de cada estado e da queda do stream; CI verde
- **Prova:** `npm run lint && npm run typecheck && npm run build`; Playwright

- **Verificação:**
  - Data: 2026-10-30 12:2x. PR #15 do `stonebid-web` (`3000135`), CI verde, 104 testes Playwright; merge do humano às 12:17 (`ab1c809` na `main`).
  - `useLotStream` com `snapshot`, `bid`, `canceled` e `settled`, mantendo o `viewer` do `GET /lots/:id`; reabre o stream 5 s depois de erro HTTP; plano B de 3 s, recarga de 15 s removida; "Prorrogado +2 min" por 6 s; estados de fim com link do comprovante; "Dar lance" escondido do leiloeiro.
  - Desvios (aprovados em 2026-10-30 12:44): `routes/_public/lots/$id.tsx` lê o `user` da sessão já resolvida no layout raiz, sem consulta e sem redirecionar ([[geral-decisao-2026-10-30-sala-publica-le-a-sessao]]); link do comprovante por `<a href>`; `BidHistory` recebe a consulta da sala em vez do `id`.

### T4: Meus arremates, comprovante e total (web)
- **Faz:** página pública `/receipts/$publicId` com cópia do link; Meus arremates; total recebido e resultado no painel do leiloeiro; motivo no cancelamento.
- **Toca em:** `stonebid-web`: `src/features/receipts/`, Meus arremates, painel do leiloeiro, rotas novas, `e2e/`. Branch `feat/RF-50-arremates-e-comprovante`, Playwright na porta 4175.
- **Paralelo:** sim
- **Pronto quando:**
  - [x] Playwright das telas novas e do cancelamento com motivo; CI verde
- **Prova:** idem T3

- **Verificação:**
  - Data: 2026-10-30 12:2x. PR #16 do `stonebid-web` (`ad3231d`), CI verde nos dois checks, 101 testes Playwright. 12:3x: conflitos com o #15 resolvidos por merge da `main` na branch, sem push forçado (`10e59fd`), CI verde, 111 testes, PR `clean`; merge do humano às 12:30 (`728210a`). Na resolução: o `LotDto` ficou o do #15; o `lot-outcome.tsx` da T4 virou `auctioneer-lot-outcome.tsx`; o link do comprovante na sala virou `Link` tipado.
  - Comprovante em `/receipts/$id` (público, copiar link e hash, 404 amigável); `/my-bids` só para licitante, no menu; painel com "Total recebido" e resultado de cada lote; cancelamento com motivo (3 a 280, contador, erro da API no diálogo).
  - Desvios (sem aval): parâmetro `$id` em vez de `$publicId` (regra de [[geral-decisao-2026-10-28-estrutura-frontend]]); link da auditoria por `<a href>` para `/lots/:id/audit`, rota que ainda não existe no web; uma linha em `session-actions.tsx` (só o item com `roleArea` vira atalho do cabeçalho, para não rolar a 305 px); campo do motivo com `Input` (sem `textarea` do shadcn); textos de erro da API simulada escritos pelo implementador, a conferir contra a API real.
  - Componentes novos para o [[registro-de-componentes]]: `lot-outcome`, `copy-button`, `receipt-view`, `my-bids-list`, `my-bid-card`, `bid-position-badge`.

### T5: merge e staging
- **Estado (2026-10-30 12:3x):** API: #12 e #13 com merge, `staging` em `f756ac2`, CD verde. Web: #15 e #16 com merge; `staging` avançada (`c366aef..728210a`); falta conferir o CD de staging do web.
- **Faz:** merge do humano na ordem T2b → T2a → `staging` da API → T3 → T4 → `staging` do web; CD verde; migração do pseudônimo aplicada nos dois ambientes.
- **Depende de:** T2a a T4

### T6: verificação no ar
- **Faz:** verificador no Chrome em staging: leilão completo com dois licitantes (lance que chega à outra aba sem recarregar, anti-sniping num lote curto, liquidação, comprovante por link sem login, Meus arremates, total do leiloeiro, cancelamento com motivo); verificador de código lê os diffs.
- **Depende de:** T5
- **Pronto quando:**
  - [x] relatórios sem bloqueante (2026-10-30 12:4x–13:0x)

- **Verificação:**
  - Código (API `f756ac2`, web `728210a`, sobre o estado final da `main`; PRs empilhados): sem bloqueante. ✔ liquidação idempotente (`FOR UPDATE`, índices únicos, prova sem a trava), ✔ SSE depois do COMMIT e limpeza ao fechar, ✔ anti-sniping, ✔ trava e ordem do lance, ✔ comprovante sem dado pessoal, ✔ `viewer` só com JWT de licitante. Deve corrigir: `viewer` sobrevivendo à troca de sessão (PR #17 do `/register` e PR #18 do `viewer`, abaixo) e link da auditoria em 404 até o I4 ([[geral-decisao-2026-10-30-caminho-da-auditoria]]). Opcionais: separador no selo do comprovante (v2), SSE sem contrapressão, posição `WON` antes da liquidação por um instante, agendador parado em staging pelo `--cpu-throttling` (a leitura cobre).
  - Chrome em staging: sem bloqueante, 10 de 12 ✔. Lance chega na outra aba em 194 ms pelo `EventSource`, sem buffer no Cloud Run (RNF-06); anti-sniping leva o fim a lance + 2 min nas duas abas; `settled` 1,2 s depois do fim; COMMIT, RELEASE e DEBIT sem duplicar; comprovante abre deslogado e id inválido dá 404 amigável; Meus arremates, "Total recebido" (R$ 350,00 → R$ 480,00), cancelamento com motivo pelo SSE, `seed-3` e "Dar lance" escondido do leiloeiro ✔; console limpo. Sem prova: MCP (sem chave; humano aceitou seguir sem, 12:44) e posição `CANCELED` (inalcançável: só se cancela lote sem lances; fica como está, [[geral-decisao-2026-10-30-posicao-cancelado-inalcancavel]]). Opcionais: aviso "Prorrogado +32 s" mostra o quanto o fim andou, não "+2 min"; botão "Cancelar" visível em lote com lances; rótulo "Lance atual" em lote encerrado.
  - Dados de teste em staging: lotes "Arrival of the Normandy Train" (vendido, R$ 130,00), "Stacks of Wheat" (lance de R$ 100,00 até 13:30) e "Water Lilies" (cancelado).

### T7: correções da T6 (web)
- **Faz:** mensagem em português do papel no `/register` (PR #17, merge do humano às 12:54); cache descartado no login e no logout, para o `viewer` não sobreviver à troca de sessão (PR #18, CI verde, 112 testes Playwright, merge do humano às 13:06). `staging` do web avançada (`728210a..9e68191`).
- **Pronto quando:**
  - [x] PR #17 com merge
  - [x] PR #18 com merge e `staging` do web avançada (`9e68191`)
  - [x] verificador no Chrome em staging: `/register` sem papel e troca de sessão na sala (logout some o estado pessoal; login pelo "Dar lance" mostra o próprio estado)

- **Verificação:**
  - Data: 2026-10-30 13:3x, Chrome em staging (web `9e68191`): 4 de 4 ✔, sem bloqueante. `/register` sem papel mostra "Escolha se você vai ser leiloeiro ou licitante."; logout e volta à sala sem recarregar tira "Você está ganhando"; "Dar lance" deslogado leva a `/login?redirect=/bidding/:id` e o Licitante 2 vê "Você foi superado"; a troca ao contrário também não guarda o estado do outro; console limpo. Nenhum dado de teste criado.

## Próxima tarefa e a seguinte
T1 a T7 feitas. Próxima etapa: [[auditoria-publica-plano]].

## Prioridades
T2a é o caminho crítico. Se apertar: corta o seed liquidado, depois o aviso de prorrogação no web.

## Candidatos a registro
- Bug de ambiente: o `global-setup` dos testes precisa apagar comprovantes antes dos lotes (FK RESTRICT); sem isso a 2ª execução local falha com "No test files found" e `code.charCodeAt`.
- Receita do binário falso do schema engine que funciona com `prisma migrate deploy` (sai 0 em `cli ...` e responde JSON-RPC): seção 3 de [[passo-a-passo-do-agente]].
- Registro de componentes: os 6 novos da T4 e os 3 da T3 (`lot-outcome`, `lot-room-countdown`, `viewer-position`).

### 🔗 Conexões
- Funcionalidade: [[sala-ao-vivo-contexto]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
