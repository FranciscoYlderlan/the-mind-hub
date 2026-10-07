---
tipo: plano
funcionalidade: lances
status: proposta
criado: 2026-10-30
aliases: [Plano do I2, Plano de lances, Bids plan]
---
# 📋 Lances (I2): plano

> [!warning] Proposta da IA
> Nada aqui é decisão. Decisões ficam nas notas `-decisao-` linkadas abaixo.

## Objetivo desta rodada
Lance válido gravado com saldo comprometido, devolução ao antigo líder e hash encadeado, um por vez por lote; cada recusa do RF-70 com mensagem em português; tela de lance no web; tudo no ar em staging. Base: [[lances-contexto]].

## Decisões que este plano respeita
- [[geral-decisao-2026-10-29-comprovante-e-hash]], [[geral-decisao-2026-10-29-sequencia-no-extrato]], [[geral-decisao-2026-10-30-obra-unica-por-lote]], [[geral-decisao-2026-10-29-lance-inicial-e-valor-minimo]], [[geral-decisao-2026-10-29-testes-no-escopo]], [[geral-decisao-2026-10-29-cancelamento-ao-vivo]], [[geral-decisao-2026-10-29-camada-mcp]], [[geral-decisao-2026-10-28-estrutura-frontend]], [[geral-decisao-2026-10-28-estrutura-backend]], [[geral-decisao-2026-10-29-modo-de-implementacao]].

(Dial: o do [[geral-contexto]].)

### Pontos para o aval do humano
Aval em 2026-10-30 08:4x, todos como propostos:
1. Sequência do extrato global: [[geral-decisao-2026-10-29-sequencia-no-extrato]].
2. Pseudônimo: [[geral-decisao-2026-10-30-pseudonimo-por-hmac]].
3. Lance atual e líder no lote: [[geral-decisao-2026-10-30-lance-atual-no-lote]].
4. Anti-sniping no I3, com `endsAt` lido sob a trava: [[geral-decisao-2026-10-30-historico-de-lances-no-i2]] (Consequências).
5. Disponível na recusa por saldo: [[geral-decisao-2026-10-30-saldo-na-recusa-do-lance]].
6. Histórico público no I2: [[geral-decisao-2026-10-30-historico-de-lances-no-i2]].

## Tarefas

### T1: contrato da API (sem PR)
- **Faz:** o orquestrador fixa no briefing de T2 e T3: `POST /lots/:id/bids` (só BIDDER, `Idempotency-Key`, 201 novo e 200 replay) e `GET /lots/:id/bids` (público, pseudônimo); `LotDto` com `currentBidCents` real e `minNextBidCents`; códigos do RF-70: `BID_BELOW_MINIMUM` 422 (`details.minAmountCents`), `INSUFFICIENT_FUNDS` 422, `ALREADY_WINNING` 409, `LOT_NOT_STARTED`, `LOT_ENDED` e `LOT_CANCELED` 409, `FORBIDDEN` 403, `UNAUTHORIZED` 401.
- **Depende de:** aval dos pontos 1 a 6 (dado)
- **Pronto quando:**
  - [x] contrato nos briefings de T2 e T3 (2026-10-30 08:4x)

### T2a: núcleo do lance (API)
- **Faz:** schema e migração (`Bid` com `@@unique([lotId, seq])` e chave de idempotência por licitante, cabeça no `Lot`, sequência e FK `lotId` no `WalletMovement`); segredos no env; domínio `validateBid`, hash, selo e pseudônimo; `PlaceBidUseCase` com trava do lote (`FOR UPDATE`) e da carteira; COMMIT do novo líder e RELEASE do antigo; `PrismaLotBidsReader` no lugar do stub; cancelamento dentro da mesma trava.
- **Toca em:** `stonebid-api`: `prisma/`, `src/domain/`, `src/application/`, `src/infra/repositories/`, `src/env/`, `test/`.
- **Depende de:** T1
- **Paralelo:** sim, com T3
- **Pronto quando:**
  - [ ] T-01, T-02 (N lances paralelos, invariantes do RNF-04, seq 1..n sem buraco), T-03 (exemplo da Ana), T-11 do lance e concorrência do T-10a passando; teste de corrida falha sem a trava
  - [ ] cadeia recalculável; lint, tipos, testes, build; CI verde
- **Prova:** `npm run lint && npm run typecheck && npm test && npm run build`

- **Verificação:**
  - Data: 2026-10-30 09:13 (merge: PR #10 do `stonebid-api`, `21cab57`, 138 testes; `cd.yml` com os segredos em `630d259`)
  - Critérios ✔/✘: CI verde; T-01, T-02 (falha sem as travas, com janela forçada), T-03, T-11 do lance e T-10a no repositório. A carteira trava com `FOR NO KEY UPDATE` para lances cruzados não travarem um ao outro. Sem prova no ar ainda (T5).
  - Desvios: sequência pelo `autoincrement()` do Prisma (global e crescente); pseudônimo recalculado, não gravado; caso de uso também barra o leiloeiro; chave reusada dá 409 `IDEMPOTENCY_KEY_REUSED` com mensagem de lance.

### T2b: rotas e MCP (API)
- **Faz:** controllers e schemas das duas rotas, `LotDto` novo, tools `bids_place` e `bids_list`, seed com lances no lote ao vivo, T-08 (leiloeiro dá 403), T-09 (histórico sem nome nem e-mail), README.
- **Toca em:** `stonebid-api`: `src/infra/http/`, `src/infra/mcp/`, `prisma/seed.ts`, `test/e2e/`.
- **Depende de:** T2a (mesmo implementador, em sequência)
- **Paralelo:** sim, com T3
- **Pronto quando:**
  - [ ] cada motivo do RF-70 com teste E2E; tools com teste; CI verde
- **Prova:** idem T2a

- **Verificação:**
  - Data: 2026-10-30 09:13 (merge: PR #11 do `stonebid-api`, `55b1400`, 154 testes); CD de produção e de staging verdes; `staging` avançada (`4d0e021..55b1400`).
  - Sem prova no ar ainda (T5). Fora do escopo: pseudônimo de 4 dígitos com colisão ~1 em 65 mil no mesmo lote; `REVOKE UPDATE, DELETE` nos lances não feito.

### T3: tela de lance (web)
- **Faz:** `LotRoom` com `bidSlot`; rota `/bidding/$id` (só licitante; leiloeiro vai para `/lots/$id`); `BidPanel` que sugere `minNextBidCents`, mantém a chave até sucesso ou troca do valor, mostra a mensagem do RF-70 e invalida lote e carteira; "Dar lance" leva ao login e volta; API simulada igual ao contrato.
- **Toca em:** `stonebid-web`: `src/features/lots/` (ou `bids/`), `src/routes/_app/bidding/`, `e2e/`.
- **Depende de:** T1
- **Paralelo:** sim, com T2a, T2b e T5m
- **Pronto quando:**
  - [ ] Playwright: lance aceito, cada recusa, duplo clique dá 1 POST, login e volta; CI verde
- **Prova:** `npm run lint && npm run typecheck && npm run build`; Playwright

- **Verificação:**
  - Data: 2026-10-30 09:13 (merge: PR #14 do `stonebid-web`, `c366aef`, 94 testes); CD de produção verde; `staging` avançada (`fc92756..c366aef`).
  - Sem prova no ar ainda (T5). Escolhas do implementador sem aval: recarga de 15 s do lote e do histórico; leiloeiro vê "Dar lance" em `/lots/$id` e volta à mesma página sem aviso; mensagens de recusa da API simulada escritas pelo implementador. Parser de reais em `src/lib/money.ts` e cache da carteira em `src/lib/wallet-cache.ts`.

### T4: segredos e staging
- **Faz:** segredos do selo e do pseudônimo no Secret Manager (staging e produção) e no `cd.yml`, pelo Chrome; merge do humano; `staging` avançada.
- **Depende de:** T2b, T3
- **Paralelo:** não
- **Pronto quando:**
  - [ ] CD verde, migração aplicada nos dois ambientes
- **Prova:** Actions

- **Verificação:**
  - Data: 2026-10-30 09:1x. O humano criou no Cloud Shell `SEAL_SECRET`, `PSEUDONYM_SECRET`, `SEAL_SECRET_STAGING` e `PSEUDONYM_SECRET_STAGING` (o `gcloud` estava sem conta para o agente) e fez o merge dos três PRs. CD verde nos dois ambientes da API; `staging` dos dois repositórios avançada.

### T5: verificação no ar
- **Faz:** verificador no Chrome em staging (dois licitantes, exemplo da Ana, recusas na tela, comprometido e liberado na carteira, MCP); verificador de código lê o diff.
- **Depende de:** T4
- **Pronto quando:**
  - [x] relatórios sem bloqueante (Chrome; o verificador de código vai junto com o do I3)
- **Prova:** relatórios

- **Verificação:**
  - Data: 2026-10-30 11:4x, staging (API `55b1400`, web `c366aef`), verificador no Chrome.
  - Critérios ✔/✘: ✔ dois licitantes (comprometido do superado volta ao disponível na hora); ✔ exemplo da Ana adaptado (sem segundo lote barato; liquidação é do I3); ✔ recusas na tela com o texto da API (mínimo, saldo, já lidera; agendado e encerrado pela API; cancelado sem lote visível); ✔ duplo clique dá 1 POST, seq sem buraco; ✔ histórico público só com pseudônimo, login e volta; ✘ MCP sem caminho (a `MCP_API_KEY_STAGING` só no Secret Manager).
  - Achados: leiloeiro vê "Dar lance" mudo (já na T3 de [[sala-ao-vivo-plano]], [[geral-decisao-2026-10-30-dar-lance-so-para-licitante]]); `/register` sem papel mostra erro do Zod em inglês (fora do I2); lote agendado esconde o botão sem explicar (opcional).

## Próxima tarefa e a seguinte
T1 a T4 feitas (merge e staging em 2026-10-30 09:1x). T5 no Chrome aprovada em 2026-10-30 11:4x, sem bloqueante; o verificador de código do I2 fica junto com o do I3 ([[sala-ao-vivo-plano]]).

## Prioridades
T2a é o caminho crítico (concorrência e hash). T3 pode encolher (sem "login e volta") se apertar.

## Candidatos a registro
- (nenhum ainda)

### 🔗 Conexões
- Funcionalidade: [[lances-contexto]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
