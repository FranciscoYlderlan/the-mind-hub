---
tipo: plano
funcionalidade: carteira-e-lotes
status: proposta
criado: 2026-10-29
aliases: [T5a e T5b verificadas, Correções verificadas da T4, Verified staging fixes]
---
# 📋 Carteira e lotes: correções T5a e T5b (verificadas)

> [!warning] Proposta da IA
> Nada aqui é decisão. Decisões ficam nas notas `-decisao-` linkadas abaixo.

Parte de [[carteira-e-lotes-plano-correcoes]], separada pelo limite de palavras: as duas tarefas já verificadas no ar.

### T5a: resposta do depósito sem o teto (bloqueante)
- **Achado:** `POST /wallet/deposits` devolve `wallet` sem `depositLimitCents`, que o `GET /wallet` traz (`get-wallet-controller.ts`, linha 7). O `depositResponseSchema` do web exige o campo, o `parse` falha e o `onSuccess` do `useDeposit` não roda: o depósito entra no servidor (201, uma linha no extrato), mas a tela segue com o saldo velho, sem a linha nova e com o valor no campo, até recarregar.
- **Faz:** no `stonebid-api`, `deposit-controller.ts` devolve `wallet` no mesmo formato do `GET /wallet` (com `depositLimitCents`), de preferência por uma função só usada pelos dois; conferir a tool `wallet_deposit` da MCP; teste E2E do formato da resposta (201 e replay 200).
- **Toca em:** `stonebid-api`: `src/infra/http/controllers/wallet/`, `src/infra/mcp/tools/wallet-tools.ts`, `test/`.
- **Depende de:** nenhuma
- **Paralelo:** sim, com T5b e T5d
- **Pronto quando:**
  - [ ] resposta do depósito (201 e 200) traz `totalCents`, `committedCents`, `availableCents` e `depositLimitCents`
  - [ ] teste falha sem o campo; lint, Prettier, tipos, Vitest e build; CI verde
- **Prova:** `npm run lint && npm run typecheck && npm test && npm run build`
- **Verificação:**
  - Data: 2026-10-29 23:55 (código) e 2026-10-30 00:05 (Chrome, staging)
  - Critérios ✔/✘ com a prova de cada um:
    - ✔ PR #3 do `stonebid-api` (merge `c7b06a3`): `toWalletDto` em `src/infra/http/presenters/wallet-presenter.ts`, usado pelo `GET /wallet` e pelo depósito; a `wallet_deposit` da MCP chama a mesma rota. CI e CD verdes.
    - ✔ Verificador de código: lint, Prettier, tipos, build e 60/60 testes; com o `deposit-controller.ts` revertido, 4 testes caem; formato bate com o `walletSchema` e o `depositResponseSchema` do web.
    - ✔ Verificador no Chrome (staging): depósito de R$ 10 com duplo clique gerou um só `POST /wallet/deposits` (201 com `depositLimitCents`), uma linha no extrato, saldo e extrato atualizados sem recarregar, campo limpo; recarregar bate.
    - ✔ Chrome, 2026-10-30 06:2x: depósito de R$ 1,00; `POST /wallet/deposits` e `GET /wallet` logo depois deram os mesmos quatro valores (`totalCents: 526200`), iguais aos cards e à soma do extrato. A diferença anotada antes não se repetiu.
  - Devolvido para correção: não

### T5b: erro cru no toast e API simulada fora do contrato
- **Achado:** quando o `parse` da T5a falha, o `onError` do `deposit-form.tsx` mostra no toast a mensagem do `ZodError` como veio, e ninguém na verificação capturou o erro (visto pelo humano). O mesmo padrão `toast.error(error.message)` está em `login-form.tsx`, `register-form.tsx`, `create-lot-form.tsx` e `cancel-lot-button.tsx`. O Playwright passou porque `e2e/support/mock-api.ts` devolve um depósito com `depositLimitCents`, diferente da API real.
- **Faz:** no `stonebid-web`, um tratamento único de erro de mutação: `ApiError` mostra a mensagem da API; qualquer outro erro mostra a mensagem genérica e vai para o `console.error`. Os cinco formulários usam esse tratamento. A API simulada devolve o formato real de cada rota da etapa (conferir com o `stonebid-api`), e um teste cobre a resposta fora do formato.
- **Toca em:** `stonebid-web`: `src/lib/`, `src/features/*/components/`, `e2e/`.
- **Depende de:** nenhuma
- **Paralelo:** sim, com T5a e T5d
- **Pronto quando:**
  - [ ] resposta fora do formato mostra a mensagem genérica, nunca o texto do zod
  - [ ] API simulada igual à real nas rotas da etapa; lint, Prettier, tipos, build e Playwright; CI verde
- **Prova:** `npm run lint && npm run typecheck && npm run build`; Playwright
- **Verificação:**
  - Data: 2026-10-30 00:05 (Chrome, staging)
  - Critérios ✔/✘ com a prova de cada um:
    - ✔ PR #6 do `stonebid-web` (merge `168ac5d`): `src/lib/mutation-error.ts` (`showMutationError`) nos cinco formulários; `e2e/support/mock-api.ts` conferido rota a rota com os controllers da API; `e2e/mutation-errors.spec.ts`; 28 testes do Playwright e CI verdes.
    - ✔ Chrome: senha errada (401 `INVALID_CREDENTIALS`) e depósito acima do teto (400 `DEPOSIT_LIMIT_EXCEEDED`) mostram no toast o texto da API; resposta fora do formato, forçada no navegador, mostra "Algo deu errado. Tente de novo em instantes." e o `ZodError` fica só no console.
  - Devolvido para correção: não. Achado fora do escopo virou a T5f (`placeOfOrigin`).

### 🔗 Conexões
- Plano de origem: [[carteira-e-lotes-plano-correcoes]]
- Funcionalidade: [[carteira-e-lotes-contexto]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
