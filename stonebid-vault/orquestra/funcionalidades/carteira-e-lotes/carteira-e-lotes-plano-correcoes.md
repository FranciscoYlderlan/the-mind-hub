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

### Aval da T5c
- Miniatura da busca por uma rota da API que entrega a imagem do item: [[geral-decisao-2026-10-29-miniatura-da-busca-pela-api]].

## Tarefas

T5a (resposta do depósito sem o teto) e T5b (erro cru no toast e API simulada) estão verificadas no ar: [[carteira-e-lotes-plano-correcoes-t5a-e-t5b]].

T5c, T5d e T5f a T5h estão verificadas no ar: [[carteira-e-lotes-plano-correcoes-t5c-a-t5h]].

### T5i: feedback ao criar lote
- **Achado:** o toast "Lote criado." some em ~4 s longe do olhar e o lote novo entra 4 a 5 telas abaixo, sem destaque; o título da seção fica atrás do cabeçalho fixo (pesquisa de UX no Chrome, 2026-10-30).
- **Faz:** pacote A + B + C aprovado pelo humano: toast com título, início e ação "Ver lote" (~8 s); rolar até o card novo e realçar; `scroll-margin-top`; botão com "Criando lote…".
- **Toca em:** `stonebid-web`: `src/features/lots/`, painel do leiloeiro, `e2e/`.
- **Verificação:**
  - Data: 2026-10-30 06:4x (merge, PR #9 do `stonebid-web`, `c3811bb`, 39 testes) e 07:0x (Chrome, staging)
  - Critérios ✔/✘ com a prova de cada um:
    - ✔ "Criando lote…" desabilitado durante o envio; duplo clique dá 1 POST.
    - ✔ Toast com título, início e "Ver lote", 8,2 s na tela.
    - ✔ Rola até o card novo, realça e foca. O título "Agendados" fica 4 px sob o cabeçalho, legível.
    - ✔ "Ver lote" rola até o card certo no painel, sem abrir `/lots/:id`; o humano aprovou assim (07:05).
  - Devolvido para correção: não. Acabamentos anotados, sem tarefa por ora (humano, 07:05): os 4 px do título; o foco volta ao elemento anterior depois do "Ver lote" `[a confirmar]`; com lance inicial e incremento vazios o envio não faz nada e não mostra erro.

### T5j: RN-19, obra única por lote
- **Faz:** [[geral-decisao-2026-10-30-obra-unica-por-lote]]. API: regra no domínio, 409 ao criar, um lote só em pedidos simultâneos, situação da obra na busca. Web (depois da T5i e da API): selo "Em leilão"/"Vendido" com link e botão desabilitado.
- **Verificação:**
  - Data: 2026-10-30 06:5x (API, PR #7 do `stonebid-api`, `d4755fd`, 100 testes), 07:00 (web, PR #10 do `stonebid-web`, `492ee4f`, 43 testes) e 07:0x (Chrome, staging)
  - Critérios ✔/✘ com a prova de cada um:
    - ✔ API: busca com `auction` certo (SCHEDULED, LIVE quando começa, `null` sem lote); obra repetida dá 409 `ITEM_ALREADY_AUCTIONED` com `details`; 2 e 4 pedidos simultâneos dão um só 201.
    - ✔ Web: selo "Em leilão" com link para o lote certo; "Criar lote" desabilitado com motivo visível em `aria-describedby`; corrida dá aviso em português no diálogo com "Ver o lote" e a busca recarrega; feedback da T5i intacto.
    - ✘ Selo "Vendido" sem prova no ar: não há lote SOLD em staging antes do I2 (coberto no Playwright).
  - O PR #10 tocou `src/lib/api-client.ts` (fora da lista) para guardar o `details` do erro no `ApiError`.
  - Trava por obra com `pg_advisory_xact_lock` (o estado do lote é calculado pelo relógio, então índice único parcial não serve); provada no repositório com janela forçada (sem a trava, o teste falha).
  - Contrato para o web: busca `items[].auction: null | { status: 'SCHEDULED' | 'LIVE' | 'SOLD', lotId }` (SCHEDULED/LIVE = "Em leilão", SOLD = "Vendido"); 409 `ITEM_ALREADY_AUCTIONED` com `details: { status, lotId }`. Banco fora: busca segue com `auction: null`.
  - Fora do escopo: `README.md` da API sem o 409 e o campo `auction`; no I2, o leitor real de lances precisa de `listLotIdsWithBids` (até lá todo lote encerrado libera a obra).

### T5k: acabamentos achados na verificação
- **Achado:** mensagem do 429 mistura idiomas ("Tente de novo em 48 seconds"); `retry-after` fora do `Access-Control-Expose-Headers`; visitante a 320 px sem folga no cabeçalho.
- **Depende de:** nenhuma (aval do humano em 2026-10-30 06:53)
- **Verificação:**
  - Data: 2026-10-30 07:00 (merge: PR #8 do `stonebid-api`, `e4397c9`, 108 testes; PR #11 do `stonebid-web`, `b489008`, 41 testes) e 07:0x (Chrome, staging)
  - Critérios ✔/✘ com a prova de cada um:
    - ✔ Rajada de 140: 120 com 200 e 20 com 429 "Muitas requisições. Tente de novo em 60 segundos."; o JS lê `retry-after` e `x-ratelimit-*`; `/health` 200 depois.
    - ✔ Visitante a 320 e 305 px sem rolagem horizontal; "Entrar" e "Cadastrar" só ícone, 40 × 40 px, com nome acessível; 12 px de folga. Leiloeiro sem rolagem. Licitante sem prova nova (o PR só mudou o visitante; verificado na T5f).
  - Devolvido para correção: não. Achado: botões do leiloeiro e o "Alternar tema" com 32 px de altura, abaixo de 40 px.

### T5e: repetir a T4 e o verificador independente
- **Faz:** depois do merge de T5a, T5b e T5d e do CD de staging, o orquestrador repete no Chrome o depósito com duplo clique (saldo, extrato e campo atualizam sem recarregar) e a busca; o verificador independente lê o diff e os testes de T1, T2 e T5 (parte da T4 ainda não feita).
- **Toca em:** nada (só testa e reporta)
- **Depende de:** T5a, T5b, T5c e T5d (e T5f, se aprovada)
- **Paralelo:** não
- **Pronto quando:**
  - [x] relatórios sem bloqueante (2026-10-30 08:2x)
- **Prova:** relatórios
- **Verificação:**
  - Data: 2026-10-30 07:2x–07:3x (Chrome, staging, API `e4397c9`, web `492ee4f`; código: API 108 testes, web 45 no Playwright, lint, tipos e build verdes)
  - Critérios ✔/✘ com a prova de cada um:
    - ✔ Chrome: duplo clique dá 1 `POST /wallet/deposits` (Resource Timing); saldo, extrato e campo sem recarregar; `amountCents` bate. Limites em português na tela e na API. Busca com miniaturas só pela API, selo "Em leilão" com link certo. Console limpo.
    - ✔ Código: centavos inteiros ponta a ponta; depósito duplo e corrida (5 simultâneos dão 1×201); teto na resposta; extrato e saldo; papéis, T-07, T-08, RN-19; API simulada igual aos controllers (sem teste de contrato automático).
    - ✘ B1 (bloqueante): `ZodError` cru em inglês nas telas que carregam dados (`error-state.tsx:27`, `item-search.tsx:67`, `__root.tsx:64`); a T5b só cobriu formulários.
    - ✘ Deve corrigir: "1,234" deposita R$ 1.234,00 sem aviso ("1,2,3" vira R$ 12,03; "0,001" vira R$ 1,00); API com mensagem em inglês em `POST /lots` sem corpo e em nome/senha longos no cadastro (o web não limita); RN-18: chave nova a cada envio, nova tentativa de rede pode depositar duas vezes (`deposit-form.tsx:46`).
  - Devolvido para correção: sim, T5l. Staging: licitante-1 ganhou depósitos de R$ 12,34 e R$ 1.234,00 do teste.
  - Repetição: 2026-10-30 08:1x–08:2x (Chrome, staging, API `4d0e021`, web `5489733`): ✔ depósito com duplo clique dá 1 POST, saldo, extrato e campo sem recarregar; ✔ busca "Rembrandt" com 12 miniaturas só pela API de staging; ✔ 3 selos "Em leilão" com link certo; ✔ console limpo. Sem bloqueante. Staging: licitante-1 ganhou depósitos de R$ 12,34, R$ 100,00, R$ 1,00 e R$ 2,00.

### T5l: erro cru no carregamento, valor ambíguo, RN-18 e alvo de toque
- **Faz:** web: toda tela de carregamento com mensagem em português, nunca `error.message` de erro que não veio da API; chave do depósito mantida até sucesso ou troca do valor; campo de valor recusa formato ambíguo ("como 100,00"); limite de tamanho em nome e senha; botões do cabeçalho ("Alternar tema", "Carteira", menu do usuário e botões do leiloeiro) com alvo de toque de 40 × 40 px, sem rolagem horizontal a 305 e 320 px. API: mensagens em português no `POST /lots` sem corpo e nos `.max()` do cadastro.
- **Toca em:** `stonebid-web` (`error-state.tsx`, `item-search.tsx`, `__root.tsx`, carteira, auth, `e2e/`); `stonebid-api` (`lot-schemas.ts`, `auth-schemas.ts`, testes). Um implementador e um PR por repositório.
- **Fora:** opcionais O1 a O4 (teto em `details`, mensagem do `externalId`, teto do `DEPOSIT_LIMIT_CENTS`).
- **Depende de:** nenhuma (aval do humano em 2026-10-30 07:5x, com o alvo de toque de 40 px dentro)
- **Fluxo:** cada implementador abre o próprio PR assim que a sua tarefa termina, sem esperar o outro (humano, 2026-10-30 08:0x).
- **Verificação no ar:** ao fim da implementação, depois do merge e do CD de staging, um subagente verificador no Chrome, diferente dos implementadores, testa as alterações em staging e repete a T5e; então fechar a etapa 3 (humano, 2026-10-30 08:0x).
- **Verificação:**
  - Data: 2026-10-30 08:11 (merge: PR #12 do `stonebid-web`, `5489733`, 67 testes no Playwright; PR #9 do `stonebid-api`, `4d0e021`, 111 testes) e 08:1x–08:2x (Chrome, staging)
  - Critérios ✔/✘ com a prova de cada um:
    - ✔ B1: lote inexistente, JSON fora do formato, falha de rede e 502 com HTML dão mensagem em português na vitrine, no lote e na busca de itens; nenhum `ZodError` nem inglês.
    - ✘ Tela de erro da raiz (`__root.tsx`) sem prova no ar: falha do `/auth/me` vira visitante, não erro; o código usa o mesmo `getLoadErrorMessage`.
    - ✔ "1,234", "1,2,3" e "0,001" recusados com "Valor inválido. Use o formato 100,00." e sem POST; "12,34" e "100,00" com `amountCents` certo.
    - ✔ RN-18: resposta perdida + nova tentativa reusa a chave (201, depois 200) e o saldo sobe uma vez; valor novo gera chave nova; duplo clique dá 1 POST.
    - ✔ Nome (120) e senha (128) limitados no web e na API; `POST /lots` sem corpo e com `{}` em português.
    - ✔ Cabeçalho de visitante, licitante e leiloeiro com 40 × 40 px (menu 42 × 40), sem rolagem a 305 e 320 px.
  - Devolvido para correção: não. Opcionais: `/auth/me` com falha mostra visitante sem aviso; nome e senha sem `maxLength` (o erro só aparece ao enviar). Sem prova: limite no formulário de login.

## Próxima tarefa e a seguinte
T5a a T5l verificadas no ar, sem bloqueante; etapa 3 concluída em 2026-10-30. Agora: depois a etapa 4 (Lances). Cada verificação no ar é feita por um subagente no Chrome, diferente do implementador (humano, 2026-10-29 23:58).

## Prioridades
T5a primeiro: é o bloqueante e o I2 grava saldo em cima da carteira. T5c pode ficar para depois se apertar.

## Candidatos a registro
- Referência: o IIIF da AIC pede desafio da Cloudflare ao navegador, mas responde ao servidor (Cloud Run); ver T5c.
- Regra para briefings de implementador: API simulada do Playwright copia o formato real de cada rota, com teste de contrato.

### 🔗 Conexões
- Plano de origem: [[carteira-e-lotes-plano]] (T4)
- T5a e T5b: [[carteira-e-lotes-plano-correcoes-t5a-e-t5b]]
- T5c a T5h: [[carteira-e-lotes-plano-correcoes-t5c-a-t5h]]
- Funcionalidade: [[carteira-e-lotes-contexto]]
- Acesso: [[acesso-de-teste]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
