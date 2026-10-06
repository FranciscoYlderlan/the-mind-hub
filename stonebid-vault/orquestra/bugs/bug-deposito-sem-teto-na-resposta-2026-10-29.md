---
tipo: bug
funcionalidade: carteira-e-lotes
status: resolvido
criado: 2026-10-29
aliases: [depósito não atualiza o saldo, saldo só muda ao recarregar, depositLimitCents ausente, deposit response missing field]
---
# 🐞 Depósito sem o teto na resposta: a tela não atualiza o saldo

## Contexto
Verificação no ar da T4 de [[carteira-e-lotes-plano]], em staging, 2026-10-29 23:30–23:40. O licitante deposita pela tela da carteira.

## Sintoma
- **Esperado:** depois do depósito, saldo, extrato e campo de valor atualizam sem recarregar.
- **Observado:** o servidor grava (201, linha nova no extrato), mas a tela segue com o saldo velho, sem a linha nova e com o valor no campo, até recarregar. O humano viu ainda um toast com o texto cru do `ZodError`.

## Impacto
Bloqueante da etapa 3: o licitante não confia no saldo e tende a depositar de novo. O I2 grava saldo comprometido em cima da carteira.

## Hipóteses
- Cache do TanStack Query não invalidado: descartada; a invalidação estava no `onSuccess`, que nem rodava.
- Corrida no duplo clique: descartada; um só POST no Resource Timing.
- **Contrato diferente entre as rotas:** confirmada (abaixo).

## Linha do tempo técnica
- 23:3x: verificador no Chrome acha o saldo parado; o humano vê o toast em inglês.
- 23:5x: T5a (API) e T5b (web) despachadas em paralelo, um PR cada.
- 2026-10-30 00:05: merge e Chrome em staging aprovam as duas.

## Pseudocódigo do problema
```text
GET  /wallet           -> { totalCents, committedCents, availableCents, depositLimitCents }
POST /wallet/deposits  -> { wallet: { totalCents, committedCents, availableCents } }  // sem o teto
web: depositResponseSchema.parse(body)  // exige depositLimitCents -> ZodError
     onSuccess nunca roda; onError mostra error.message cru
```

## Testes feitos
- Chrome: depósito com duplo clique, leitura da resposta no painel de rede.
- Playwright passava: a API simulada (`e2e/support/mock-api.ts`) devolvia o depósito **com** `depositLimitCents`, diferente da API real.

## Evidências encontradas
`get-wallet-controller.ts` montava o DTO completo; `deposit-controller.ts` montava outro, sem o teto. O `parse` do web falhava no campo ausente.

## Correção aplicada
- API, PR #3 do `stonebid-api` (merge `c7b06a3`): `toWalletDto` em `wallet-presenter.ts`, usado pelas duas rotas; com o controller revertido, 4 testes caem.
- Web, PR #6 do `stonebid-web` (merge `168ac5d`): `showMutationError` nos cinco formulários (erro que não veio da API vira mensagem genérica) e API simulada conferida rota a rota com os controllers.
- Detalhes: [[carteira-e-lotes-plano-correcoes-t5a-e-t5b]].

## Solução
Um presenter só por recurso: toda rota que devolve a carteira passa pela mesma função.

## Como validar que não voltou
Teste E2E da API que confere o formato do 201 e do replay 200 do depósito; no Chrome, depósito com duplo clique atualiza saldo, extrato e campo sem recarregar (repetido na T5e, 2026-10-30 08:2x).

## Logs que deveriam existir
`console.error` do `ZodError` no web (hoje existe, desde a T5b); falha de `parse` de resposta da API contada como erro de contrato.

## O que aprendi
- A API simulada escondeu a falha: mock que não é conferido contra os controllers reais prova o mock, não o sistema.
- Erro que não veio da API nunca vai cru para o usuário.
- Lição geral no `Vault`: "API simulada conferida contra a API real".

### 🔗 Conexões
- Funcionalidade: [[carteira-e-lotes-contexto]]
- Correções: [[carteira-e-lotes-plano-correcoes-t5a-e-t5b]]
- Decisões: [[geral-decisao-2026-10-29-limites-do-deposito]]
- Outros bugs: [[bug-placeoforigin-lido-como-origin-2026-10-30]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
