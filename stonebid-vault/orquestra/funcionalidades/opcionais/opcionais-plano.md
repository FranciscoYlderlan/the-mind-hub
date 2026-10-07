---
tipo: plano
funcionalidade: opcionais
status: proposta
criado: 2026-10-30
aliases: [Plano do I5, Plano dos opcionais]
---
# 📋 Opcionais (I5): plano

> [!warning] Proposta da IA
> Nada aqui é decisão. Decisões ficam nas notas `-decisao-` linkadas abaixo.

## Objetivo desta rodada
Estorno no cancelamento e busca na vitrine no ar em staging, nessa ordem. Base: [[opcionais-contexto]].

## Decisões que este plano respeita
- [[geral-decisao-2026-10-30-estorno-no-cancelamento]], [[geral-decisao-2026-10-30-busca-na-vitrine]], [[geral-decisao-2026-10-29-cancelamento-ao-vivo]], [[geral-decisao-2026-10-29-camada-mcp]], [[geral-decisao-2026-10-29-modo-de-implementacao]].

## Tarefas

### B1: estorno na API (M)
- **Faz:** itens 1 a 5 e 7 de [[geral-decisao-2026-10-30-estorno-no-cancelamento]]; sinalizador no `cd.yml`.
- **Toca em:** `stonebid-api`: `lot.ts`, `wallet.ts`, `cancel-lot.ts`, `prisma-lots-repository.ts`, `lot-audit.ts`, `prisma-lot-audit-reader.ts`, `env`, `cd.yml`, `lots-tools.ts`, `test/`, README. Branch `feat/RF-23-estorno-no-cancelamento`.
- **Paralelo:** sim, com B2.
- **Pronto quando:** T-10a, T-10b, T-03 e T-06 passando; CI verde.
- **Verificação:** 2026-10-30 18:5x. PR #20 da API, 241 testes, CI verde, merge 19:04. Motivo novo da auditoria: `CANCEL_MISMATCH`.
- **Prova:** `npm run lint && npm run typecheck && npm test && npm run build`

### B2: estorno no web (P)
- **Faz:** item 6 da decisão; API simulada igual à real.
- **Toca em:** `stonebid-web`: `cancel-lot-button.tsx`, `useLotStream.ts`, extrato, auditoria, `e2e/`. Branch `feat/RF-23-estorno-no-cancelamento`.
- **Paralelo:** sim, com B1.
- **Pronto quando:** aviso no diálogo; carteira do líder atualiza sem recarregar; Playwright verde.
- **Verificação:** 2026-10-30 18:5x. PR #26 do web, 137 testes Playwright, CI verde, merge 19:04.

### B3: verificação do estorno no Chrome (P)
- **Faz:** merge do humano, `staging` avançada, cancelamento com lances em staging, posição `CANCELED`, auditoria ÍNTEGRO.
- **Depende de:** B1, B2
- **Verificação:** 2026-10-30 19:2x, no Chrome em staging (API `f6f07e9`, web `955d2f0`). Lote `a785a3b4` com 2 lances cancelado: diálogo com o aviso de estorno, `REFUND` de R$ 15,00 no extrato do líder, comprometido 63000 → 61500, posição `CANCELED`, superado só com `COMMIT` e `RELEASE`, auditoria ÍNTEGRO. Limite: a `/wallet` aberta durante o cancelamento não atualiza; a sala do lote e a navegação seguinte, sim.

### A1: busca na API (M)
- **Faz:** itens 1 a 6, 8 e 9 de [[geral-decisao-2026-10-30-busca-na-vitrine]].
- **Toca em:** `stonebid-api`: caso de uso novo, `LotsRepository`, `lot-schemas.ts`, `lots-routes.ts`, `lots-tools.ts`, `test/e2e`. Branch `feat/RF-11-busca-na-vitrine`.
- **Paralelo:** sim, com A2. **Depende de:** B3.

### A2: busca no web (M)
- **Faz:** item 7 da decisão; API simulada com teste de contrato.
- **Toca em:** `stonebid-web`: `src/features/lots/`, `src/routes/_public/index.tsx`, `e2e/`. Branch `feat/RF-11-busca-na-vitrine`.
- **Paralelo:** sim, com A1.

### A3: verificação da busca no Chrome (P)
- **Depende de:** A1, A2

## Próxima tarefa e a seguinte
Nenhuma nesta rodada: a busca (A1 a A3) ficou fora da etapa 7 (humano, 2026-10-30 18:29).

## Prioridades
Corte: conferência do estorno na auditoria e aviso do diálogo; na busca, faixa de preço e ordenação, depois filtro só no navegador.

### 🔗 Conexões
- Funcionalidade: [[opcionais-contexto]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
