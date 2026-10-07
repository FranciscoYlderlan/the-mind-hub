---
tipo: plano
funcionalidade: revisao-e-entrega
status: proposta
criado: 2026-10-30
aliases: [Plano da entrega, Plano da etapa 8]
---
# 📋 Revisão e entrega: plano

> [!warning] Proposta da IA
> Nada aqui é decisão. Decisões ficam nas notas `-decisao-` linkadas abaixo.

## Objetivo desta rodada
READMEs e correções do checklist no ar; depois os refinamentos R1, R2 e R3. Base: [[revisao-e-entrega-contexto]].

## Decisões que este plano respeita
- [[geral-decisao-2026-10-30-datas-dos-commits]], [[geral-decisao-2026-10-30-relato-de-uso-de-ia]], [[geral-decisao-2026-10-29-modo-de-implementacao]].

## Tarefas

### E1: READMEs de entrega
- **Faz:** README da API (PR #17) e do web com as telas (PR #22).
- **Verificação:** 2026-10-30 17:1x a 17:3x. API `a4fce52`, CI verde; seção CI/CD corrigida para merge na `main` antes da `staging`. Web `dc91c32`, CI verde, 13 telas em `docs/telas/` pela API simulada; endereços de staging do [[acesso-de-teste]].
- **Estado:** concluída; merges #17 da API e #22 do web. Seção "Características de funcionamento e limites" nos PRs #18 da API e #24 do web (2026-10-30 19:04).

### E2: checklist 11.6 no ar
- **Verificação:** 2026-10-30 17:3x, Chrome, staging e produção sem login: sem bloqueante. Deve corrigir: "Cancelar" em lote com lances. Opcionais: "Fim" da sala parado após prorrogação; campo de lance pré-preenchido. Faltam busca na vitrine e estorno ([[opcionais-plano]]). Criado em staging: lote `7adc44bd-b882-4a07-ac82-44595b3cea4f`, comprovante `qEo88Ve3HxV0tawDC_Sr9A`, depósito de R$ 5.

### T11: correções do checklist (web)
- **Faz:** botão "Cancelar" só em lote cancelável; "Fim" da sala segue a prorrogação; campo de lance sem valor que estrague a digitação.
- **Toca em:** `stonebid-web`, branch `fix/RF-24-ajustes-do-checklist`.
- **Verificação:** 2026-10-30 18:0x. PR #23 do `stonebid-web` (`6bafcc6`), CI verde, 130 testes Playwright (3 novos, cada um falhava sem a correção). "Cancelar" em lote agendado ou ao vivo, antes do fim, com ou sem lances (com lances, o líder recebe estorno: [[geral-decisao-2026-10-30-estorno-no-cancelamento]]). "Fim" já tinha fonte única; faltavam os segundos, e prorrogação no mesmo minuto não aparecia: agora `formatDateTimeWithSeconds`. Campo de lance seleciona o conteúdo no foco (o mínimo continua preenchido). Merge feito. Conferido no Chrome em staging depois da reescrita (2026-10-30 19:2x): link "Ver auditoria" na sala, "Fim" com a prorrogação sem recarregar, campo de lance substitui o mínimo.

### R1: padrão de commit em todo cofre de projeto (`Vault`)
- **Faz:** Criar um novo cofre e Modelo de CLAUDE do cofre passam a levar as regras de Padrão de commit e Commitar no the-mind-hub; `cofre.py verificar` dá ERRO sem essa seção; `cofre.py sincronizar` no `stonebid-vault`.
- **Verificação:** 2026-10-30 18:3x. Seção Commits obrigatória no modelo; `cofre.py verificar` dá ERRO sem ela (provado em cópia temporária); `sincronizar` no `stonebid-vault`, 0 ERRO.

### R2: mensagens e autor dos commits
- **Faz:** [[geral-decisao-2026-10-30-datas-dos-commits]]; `--force` só com confirmação.
- **Verificação:** 2026-10-30 19:1x. `--force-with-lease` em `main` e `staging`: API `f6f07e9` (33 commits), web `955d2f0` (47). Escopo = ID do requisito (humano, 19:04); árvore idêntica, datas preservadas, 0 Co-Authored-By.

### R3: relato do uso de IA
- **Faz:** `.md` próprio com o conteúdo de [[geral-decisao-2026-10-30-relato-de-uso-de-ia]], diagrama do grafo em Mermaid e a tabela; link nos dois READMEs.
- **Verificação:** 2026-10-30 18:4x. `docs/uso-de-ia.md` no web (PR #25), link na API (PR #19); Mermaid renderiza; CI verde; merge feito.

### TF: teste final de aceitação (2026-10-31)
- **Faz:** pedido do humano (2026-10-31 17:09): conferir no Chrome, seguindo o enunciado ([[enunciado-teste-tecnico]], E1 a E6), se todos os requisitos foram aceitos e se a regra de negócio está condizente, sem alterar o projeto. Login só em staging (aval do humano, 17:1x); produção só sem login.
- **Verificação:** 2026-10-31 17:1x a 17:5x, quatro verificadores e um avaliador independente. Produção em `main` = `staging` (API `f6f07e9`, web `955d2f0`).
  - **TF-A (público, produção e staging):** deploy e `/health` ✔; vitrine com Ao vivo, Agendados e Encerrados ✔; seed com lote ao vivo e 3 lances ✔; auditoria sem login ÍNTEGRO com hash encadeado ✔; comprovante por link sem login ✔; privacidade por pseudônimo ✔; sala sem login com SSE ✔; tema escuro ✔; nenhuma chamada à AIC fora da busca ✔; busca na vitrine ✘ (fora, como decidido).
  - **TF-B (leiloeiro, carteira e lances, staging):** 7 de 7 ✔: criação de lote pela busca na AIC; leiloeiro recusado (403); cancelamento sem lances some da vitrine; resultados e total recebido; carteira e depósito com limites; as cinco recusas com mensagem (`BID_BELOW_MINIMUM`, `INSUFFICIENT_FUNDS`, líder, `LOT_NOT_STARTED`, `LOT_ENDED`); comprometido volta na hora ao ser coberto.
  - **TF-C (sala, anti-sniping, liquidação, estorno, staging):** sala atualiza sem recarregar ✔; anti-sniping ✔ (fim = lance + 2 min, duas prorrogações seguidas); liquidação e lote sem lances sem vencedor ✔; Meus arremates e comprovante ✔; auditoria com hash final igual ao do comprovante ✔; cancelamento com estorno ✔. E2.3 parcial: a sala não mostra a posição do usuário nem destaca o próprio lance.
  - **TF-D (repositórios, leitura):** stack, READMEs, seed, regras com transação e `FOR UPDATE`, hash SHA-256 encadeado com selo HMAC e teste que adultera por SQL, Docker Compose, cerca de 220 testes na API e 115 Playwright ✔. CI não lido (403) e testes não rodados (proxy do Prisma).
  - **Avaliador (TF-F):** **nota 8,9 de 10** (funcionais 57,5 de 60; stack, seed e README 12 de 15; qualidade e testes 12 de 15; opcionais 7,5 de 10). Obrigatórios: todos aceitos, menos a posição do usuário na sala (E2.3, parcial). Regra de negócio: condizente.
  - **Pontos a corrigir, do mais grave ao menos grave:** posição do usuário na sala (E2.3); lote ao vivo do seed encerra por volta de 2026-11-13, e depois disso o ambiente fica sem lote ao vivo com lances (E4.2); commits de 2026-10-30 19:0x, depois das 16:00; valores com ponto nas mensagens de lance do web ("R$ 20.00"); rótulo "Lance atual" em lote encerrado; carteira sem atualização em tempo real; README não diz que a busca (E5.1) ficou fora.
  - **Dados de teste em staging:** lotes `19658df2` (cancelado), `676dfe35` (vendido, R$ 35), `e74f4d1a` (vendido, R$ 140, com anti-sniping), `67ad6502` (sem vencedor), `62a231d0` (cancelado com estorno de R$ 150); depósito de R$ 3,21 do Licitante 1.

### TF-E: workflow e andamento no relato de uso de IA
- **Faz:** "O que a memória guarda" em `docs/uso-de-ia.md` do web passa a citar o workflow e o andamento do desenvolvimento, e o rótulo do diagrama acompanha ([[geral-decisao-2026-10-30-relato-de-uso-de-ia]]).
- **Verificação:** 2026-10-31 17:3x. PR #27 do web (`9d7c93e`), CI verde, merge do humano (`b8c8b49`); `staging` do web avançada `955d2f0..b8c8b49`.

## Próxima tarefa e a seguinte
Nenhuma: projeto entregue. Os pontos a corrigir da TF ficam com o humano.

### 🔗 Conexões
- Funcionalidade: [[revisao-e-entrega-contexto]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
