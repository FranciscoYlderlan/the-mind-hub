---
tipo: plano
funcionalidade: auditoria-publica
status: proposta
criado: 2026-10-30
aliases: [Plano do I4, Plano da auditoria, Audit plan]
---
# 📋 Auditoria pública (I4): plano

> [!warning] Proposta da IA
> Nada aqui é decisão. Decisões ficam nas notas `-decisao-` linkadas abaixo.

## Objetivo desta rodada
Rota pública da auditoria na API, página `/lots/$id/audit` no web e T-06 com as adulterações, tudo no ar em staging. Base: [[auditoria-publica-contexto]].

## Decisões que este plano respeita
- [[geral-decisao-2026-10-29-comprovante-e-hash]], [[geral-decisao-2026-10-30-caminho-da-auditoria]], [[geral-decisao-2026-10-29-testes-no-escopo]], [[geral-decisao-2026-10-29-camada-mcp]], [[geral-decisao-2026-10-29-modo-de-implementacao]].

(Dial: o do [[geral-contexto]].)

### Pontos para o aval do humano
Aval em 2026-10-30 13:2x, todos como propostos:
1. a 5. Rota, conferência, T-06, tool e página: [[geral-decisao-2026-10-30-auditoria-publica]].
6. ADULTERADO no ar: [[geral-decisao-2026-10-30-adulterado-provado-no-ci]].

## Tarefas

### T1: contrato da API (sem PR)
- **Faz:** o orquestrador fixa nos briefings: `GET /lots/:id/audit` público, `no-store`, 404 `LOT_NOT_FOUND`; corpo `{ lot, bids: [{ seq, pseudonym, amountCents, createdAt, prevHash, hash }], verdict: INTACT|TAMPERED, firstInconsistency: null|{ seq, reason }, checkedAt }`; motivos `GAP`, `CONTENT_CHANGED`, `BAD_SEAL`, `BROKEN_LINK`, `HEAD_MISMATCH`, `RECEIPT_MISMATCH`, `SETTLEMENT_MISMATCH`; tool `lots_audit`.
- **Pronto quando:**
  - [x] contrato nos briefings de T2 e T3 (2026-10-30 13:2x)

### T2: auditoria na API
- **Faz:** caso de uso e rota, conferência ampliada (comprovante e extrato), tool `lots_audit`, T-06 nos 5 casos ao vivo e liquidado, T-09 da resposta, seção "Auditoria" no README.
- **Toca em:** `stonebid-api`: `src/domain/integrity/`, `src/application/use-cases/`, `src/infra/`, `test/`, `README.md`. Branch `feat/RF-60-auditoria-publica`.
- **Paralelo:** sim, com T3
- **Pronto quando:**
  - [x] T-06 e E2E da rota e da tool; CI verde
- **Prova:** `npm run lint && npm run typecheck && npm test && npm run build`

- **Verificação:**
  - Data: 2026-10-30 13:4x. PR #14 do `stonebid-api` (`ec30df3`), CI verde, 216 testes (23 novos), com Postgres local no container.
  - T-06: íntegro `INTACT`; valor editado `{2, CONTENT_CHANGED}`; lance apagado no meio `{2, GAP}`; lance inserido (renumerando) `{2, CONTENT_CHANGED}`; último apagado `{null, HEAD_MISMATCH}`, ao vivo e liquidado. Comprovante adulterado `RECEIPT_MISMATCH`, DEBIT adulterado `SETTLEMENT_MISMATCH`, erro da cadeia antes do comprovante. T-09, `no-store`, JWT ignorado, cancelado e 404 cobertos. Tool `lots_audit` com o mesmo corpo da rota; seção "Auditoria" no README.
  - Desvios aceitos pelo humano em 2026-10-30 13:4x: conferência mais rígida de comprovante e extrato e leitura em `REPEATABLE READ` ([[geral-decisao-2026-10-30-auditoria-publica]]).

### T3: página da auditoria (web)
- **Faz:** `/lots/$id/audit` em `_public` com selo, motivo, tabela, "Verificar de novo", 404 amigável; link "Ver auditoria" na sala; link do comprovante por `Link` tipado.
- **Toca em:** `stonebid-web`: `src/features/audit/`, rotas do lote e do comprovante, `mock-api.ts`, `e2e/`. Branch `feat/RF-60-pagina-da-auditoria`, Playwright na porta 4176.
- **Paralelo:** sim, com T2
- **Pronto quando:**
  - [x] Playwright de íntegro, adulterado, vazio, 404, deslogado e 320 px; CI verde
- **Prova:** `npm run lint && npm run typecheck && npm run build`; Playwright

- **Verificação:**
  - Data: 2026-10-30 13:5x. PR #19 do `stonebid-web` (`d85f39c`), CI verde, 125 testes Playwright (10 novos). Rota em `$id_.audit.tsx` (o `_` tira a página do layout da sala, que não tem `Outlet`; URL `/lots/$id/audit`); consulta com `staleTime: 0`, sem `signal` e sem prefetch, para uma chamada por acesso; `seq: null` aparece como "registro do lote".
  - Corrigido o import entre features (`audit` → `lots`, `receipts`), proibido por [[geral-decisao-2026-10-28-estrutura-frontend]]: commit `59f976a` no PR #19, CI verde, 125 testes. `CopyButton` em `src/components/common/`; `AuditView` recebe `lotSlot`; a rota compõe `LotAuditHeader` (novo, em `features/lots`, lê o lote pela consulta da própria feature, uma requisição a mais); o schema da auditoria valida em `lot` só o `id`. Nenhuma feature importa outra.

### T4: merge e staging
- **Faz:** merge do humano (API, depois web); `staging` avançada nos dois; CD verde.
- **Estado (2026-10-30 14:0x):** API: merge do #14 (`3901df8`), `staging` `f756ac2..3901df8`. Web: merge do #19 (`972b7ae`), `staging` `9e68191..972b7ae`, CD de staging verde (run `41095191371`).
- **Depende de:** T2, T3

### T5: verificação no ar
- **Faz:** verificador no Chrome em staging (auditoria deslogada de lote ao vivo, liquidado e cancelado; link da sala e do comprovante; ÍNTEGRO; console limpo) e verificador de código nos diffs.
- **Depende de:** T4

- **Verificação:**
  - Data: 2026-10-30 14:5x. **Chrome em staging, deslogado:** 5 de 5 ✔. Ao vivo `5eed0000-0000-4000-8000-000000000001`, vendidos `12788892-…` e `3dfae377-…`, cancelado `3bb9f3d1-…` (sem lances): ÍNTEGRO, tabela, `INTACT` com `no-store`, "Verificar de novo" refaz a chamada; links da sala e do comprovante certos; 404 `LOT_NOT_FOUND` amigável; 320 px sem rolagem; console limpo nas 4 páginas de auditoria. Não verificado: cancelado com lances (não há em staging).
  - **Código (#14 e #19):** contrato todo ✔; 1 bloqueante (lote vendido trocado para `NO_WINNER`, sem comprovante e DEBIT, passa `INTACT` sem o `SEAL_SECRET`), `seq` do último lance em `RECEIPT_MISMATCH`/`SETTLEMENT_MISMATCH` contra o `null` do web, cadeia vazia passa `INTACT`, 4 opcionais. Escolhas do humano: [[geral-decisao-2026-10-30-achados-da-t5-da-auditoria]].

### T6: correções da conferência (API)
- **Faz:** os itens 1, 2, 3 e 4 de [[geral-decisao-2026-10-30-achados-da-t5-da-auditoria]]: resultado contra os lances, CREDIT do leiloeiro, lance atual e líder, `seq: null` em `RECEIPT_MISMATCH` e `SETTLEMENT_MISMATCH`, casos novos no T-06 (incluindo `BAD_SEAL` e `BROKEN_LINK` por SQL), "Limite" do README com a cadeia vazia e a tabela de motivos com o `seq` novo.
- **Toca em:** `stonebid-api`: `src/domain/integrity/lot-audit.ts`, `bid-chain.ts`, `src/infra/` (`prisma-lot-audit-reader.ts`), `test/`, `README.md`. Branch `fix/RF-60-conferencia-da-auditoria`.
- **Paralelo:** sim, com T7
- **Pronto quando:**
  - [x] T-06 com os casos novos; CI verde
- **Prova:** `npm run lint && npm run typecheck && npm test && npm run build`

- **Verificação:**
  - Data: 2026-10-30 15:1x. PR #15 do `stonebid-api` (`9f6b500`), CI verde, 229 testes. Ordem: cadeia, comprovante, liquidação, lance atual e líder. Resultado trocado para `NO_WINNER` sem comprovante e DEBIT dá `TAMPERED`; CREDIT do leiloeiro conferido; `RECEIPT_MISMATCH` e `SETTLEMENT_MISMATCH` com `seq: null`; README com a tabela de motivos e a cadeia vazia no "Limite".
  - Lance atual e líder fora do último lance dão `HEAD_MISMATCH` com `seq: null` (gravados junto com a cabeça; valem também no lote ao vivo).
  - Também recusa `SOLD` sem lances (sai `RECEIPT_MISMATCH`, porque o comprovante vem antes) e `settledAt`/`result` com só um preenchido. T-06 por SQL ao vivo e liquidado: `BAD_SEAL`, `BROKEN_LINK` (montado com o `SEAL_SECRET` de teste), lance atual e líder; no liquidado, CREDIT alterado e apagado e resultado trocado. O que os CHECK do banco impedem fica só no teste unitário.

### T7: link da auditoria em sala 404 (web)
- **Faz:** item 5 de [[geral-decisao-2026-10-30-achados-da-t5-da-auditoria]]: "Ver auditoria" só dentro da sala que carregou (hoje fica fora do `LotRoom`, em `routes/_public/lots/$id.tsx:41`); Playwright do caso 404.
- **Toca em:** `stonebid-web`: `src/routes/_public/lots/$id.tsx`, `src/features/lots/`, `e2e/`. Branch `fix/RF-60-link-da-auditoria`.
- **Paralelo:** sim, com T6
- **Pronto quando:**
  - [x] Playwright do 404 sem o link; CI verde
- **Prova:** `npm run lint && npm run typecheck && npm run build`; Playwright

- **Verificação:**
  - Data: 2026-10-30 15:1x. PR #20 do `stonebid-web` (`9365f7e`), CI verde, 127 testes Playwright (2 novos). `LotRoom` ganhou `auditSlot`, mostrado só com o lote carregado; a rota passa o `Link` por ele. Casos novos: sala 404 sem o link e sem chamada à auditoria; leiloeiro vê o link na sala carregada.

### T8: merge, staging e verificação
- **Faz:** merge do humano em T6 e T7; `staging` avançada nos dois; CD de staging verde; verificador no Chrome (auditoria dos lotes da T5 segue ÍNTEGRO; sala 404 sem o link) e verificador de código nos dois diffs.
- **Depende de:** T6, T7

- **Verificação:**
  - Data: 2026-10-30 17:0x. Merges às 15:19: API `bab9347`, web `40db2c4`. `staging` API `3901df8..bab9347`, web `972b7ae..40db2c4`; CD de staging verde.
  - **Código:** 8 de 8 ✔ (resultado trocado, CREDIT, lance atual e líder com `seq: null`, `seq: null` nos dois motivos, T-06 e README, link só com sala carregada, sem import entre features, nada fora do escopo). 3 opcionais viraram T9 e T10.
  - **Chrome, staging, deslogado:** 5 de 5 ✔. Ao vivo `5eed0000-0000-4000-8000-000000000001`, vendidos `12788892-5daf-4826-8f20-49f5b8921217` e `3dfae377-7e01-4adc-94e3-cdba78f674ad`, cancelado `3bb9f3d1-9472-4fc2-8f77-a45799d3182c`: 200, `INTACT`, `no-store`, ÍNTEGRO; sala 404 sem o link e sem chamada à auditoria; 320 px medido em iframe (a janela não redimensionou).

### T9: comentário e ordem da conferência (API)
- **Faz:** comentário de `receiptOk` no estado atual; teste que fixa a ordem (comprovante e lance atual adulterados dão `RECEIPT_MISMATCH`; extrato e líder dão `SETTLEMENT_MISMATCH`). Humano, 2026-10-30 17:04.
- **Verificação:** PR #16 do `stonebid-api` (`f56c7d7`), CI verde, unidade 9 de 9. Números de item dos comentários alinhados ao README. Aguardando merge.

### T10: "Ver auditoria" na sala de lance (web)
- **Faz:** `auditSlot` em `src/routes/_app/bidding/$id.tsx`; Playwright do licitante e do 404.
- **Verificação:** PR #21 do `stonebid-web` (`8b396dc`), CI verde, 129 testes Playwright. Aguardando merge.

## Próxima tarefa e a seguinte
T1 a T10 feitas; T9 e T10 aguardam merge e vão para a `staging` junto com a etapa 8 ([[revisao-e-entrega-plano]]).

## Prioridades
T2 é o caminho crítico. Se apertar: corta a tool `lots_audit`, depois a conferência do extrato.

## Candidatos a registro
- Passo a passo do agente: Postgres local no container precisa de `initdb` numa pasta do usuário `postgres` (o scratchpad dá erro de permissão); o seed exige `CORS_ORIGIN`; o setup local troca `prisma migrate deploy` por `psql` mais `tsx prisma/seed.ts`.

### 🔗 Conexões
- Funcionalidade: [[auditoria-publica-contexto]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
