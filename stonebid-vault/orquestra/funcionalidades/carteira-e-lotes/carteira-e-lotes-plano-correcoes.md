---
tipo: plano
funcionalidade: carteira-e-lotes
status: proposta
criado: 2026-10-29
aliases: [Correções da T4, T5 carteira e lotes, Fixes from staging check]
---
# 📋 Carteira e lotes: correções da verificação no ar (T5)

> [!warning] Proposta da IA
> Nada aqui é decisão. Decisões ficam nas notas `-decisao-` linkadas abaixo.

## Objetivo desta rodada
Corrigir o que a T4 de [[carteira-e-lotes-plano]] achou em staging (2026-10-29 23:30–23:40) e repetir a T4. Pronto quando o licitante deposita pela tela e vê saldo e extrato novos sem recarregar, e nenhum erro cru chega ao usuário. Cada tarefa é um subagente implementador, no seu PR (pedido do humano, 2026-10-29 23:40).

## Decisões que este plano respeita
- As de [[carteira-e-lotes-plano]], em especial [[geral-decisao-2026-10-29-limites-do-deposito]], [[geral-decisao-2026-10-29-api-de-itens]], [[geral-decisao-2026-10-29-camada-mcp]], [[geral-decisao-2026-10-29-padrao-de-branches]] e [[geral-decisao-2026-10-29-modo-de-implementacao]].

(Dial: médio, de [[geral-contexto]].)

### Pendente de aval antes da T5c (proposta da IA)
- Como mostrar a miniatura na busca: rota da API que entrega a imagem do item (o servidor alcança o IIIF) ou só o título, sem imagem, até criar o lote.

## Tarefas

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
  - Data:
  - Critérios ✔/✘ com a prova de cada um:
  - Devolvido para correção:

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
  - Data:
  - Critérios ✔/✘ com a prova de cada um:
  - Devolvido para correção:

### T5c: miniaturas da busca não carregam
- **Achado:** as imagens IIIF da AIC (`www.artic.edu/iiif/2/...`) abrem no navegador com o desafio anti-robô da Cloudflare ("Um momento…"); o `<img>` falha e o `CoverImage` mostra o marcador em todos os resultados. A cópia feita pelo servidor na criação do lote funciona (JPEG de 272 KB, servido por `/lots/:id/image`).
- **Faz:** o que o humano aprovar no "Pendente de aval" acima.
- **Toca em:** `stonebid-api` (`src/infra/external/`, `src/infra/http/`, MCP) e/ou `stonebid-web` (`catalog-item-card.tsx`, `create-lot-dialog.tsx`).
- **Depende de:** aval do humano
- **Paralelo:** sim, depois do aval
- **Pronto quando:**
  - [ ] a busca em staging mostra imagem (ou o que for aprovado) sem pedir ao navegador o IIIF da AIC
- **Prova:** Chrome em staging
- **Verificação:**
  - Data:
  - Critérios ✔/✘ com a prova de cada um:
  - Devolvido para correção:

### T5d: sem caminho para o painel e a carteira
- **Achado:** na vitrine e no cabeçalho não há link para `/auctioneer` nem para `/wallet`; o menu do usuário tem só "Minha conta" e "Sair". O menu lateral com "Painel do leiloeiro" ou "Carteira" só aparece dentro da área logada, aberta pela URL.
- **Faz:** no `stonebid-web`, o menu do usuário (e o cabeçalho, se couber) leva ao painel quando o papel é LEILOEIRO e à carteira quando é LICITANTE.
- **Toca em:** `stonebid-web`: componente do cabeçalho e menu do usuário, `e2e/`.
- **Depende de:** nenhuma
- **Paralelo:** sim, com T5a e T5b
- **Pronto quando:**
  - [ ] da vitrine, cada papel chega à sua área em um clique; Playwright cobre os dois papéis; CI verde
- **Prova:** Playwright
- **Verificação:**
  - Data:
  - Critérios ✔/✘ com a prova de cada um:
  - Devolvido para correção:

### T5e: repetir a T4 e o verificador independente
- **Faz:** depois do merge de T5a, T5b e T5d e do CD de staging, o orquestrador repete no Chrome o depósito com duplo clique (saldo, extrato e campo atualizam sem recarregar) e a busca; o verificador independente lê o diff e os testes de T1, T2 e T5 (parte da T4 ainda não feita).
- **Toca em:** nada (só testa e reporta)
- **Depende de:** T5a, T5b, T5d (e T5c, se aprovada)
- **Paralelo:** não
- **Pronto quando:**
  - [ ] relatórios sem bloqueante
- **Prova:** relatórios
- **Verificação:**
  - Data:
  - Critérios ✔/✘ com a prova de cada um:
  - Devolvido para correção:

## Próxima tarefa e a seguinte
T5a, T5b e T5d em paralelo, cada uma num subagente; aval da T5c com o humano; então T5e. Os PRs `chore` do Node 26 seguem em [[carteira-e-lotes-plano]] e podem andar em paralelo, sem tocar nos mesmos arquivos.

## Prioridades
T5a primeiro: é o bloqueante e o I2 grava saldo em cima da carteira. T5c pode ficar para depois se apertar.

## Candidatos a registro
- Referência: o IIIF da AIC pede desafio da Cloudflare ao navegador, mas responde ao servidor (Cloud Run); ver T5c.
- Regra para briefings de implementador: API simulada do Playwright copia o formato real de cada rota, com teste de contrato.

### 🔗 Conexões
- Plano de origem: [[carteira-e-lotes-plano]] (T4)
- Funcionalidade: [[carteira-e-lotes-contexto]]
- Acesso: [[acesso-de-teste]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
