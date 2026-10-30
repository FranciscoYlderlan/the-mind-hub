---
tipo: plano
funcionalidade: carteira-e-lotes
status: proposta
criado: 2026-10-29
---
# 📋 Carteira e lotes (I1)

> [!warning] Proposta da IA
> Nada aqui é decisão. Decisões ficam nas notas `-decisao-` linkadas abaixo.

## Objetivo desta rodada
Etapa 3 do [[geral-plano]] (I1 de [[contrato-processo-e-plano]]): RF-40 a RF-42, RF-20 a RF-22, RF-25, RF-10, RN-13, RN-16 a RN-18, e o 403 do `requireRole` provado no ar (RF-02). Pronto quando o leiloeiro cria um lote a partir da API e ele aparece na vitrine, e o licitante deposita.

## Decisões que este plano respeita
- [[geral-decisao-2026-10-28-stack-backend]], [[geral-decisao-2026-10-28-estrutura-backend]], [[geral-decisao-2026-10-29-camada-mcp]]
- [[geral-decisao-2026-10-28-stack-frontend]], [[geral-decisao-2026-10-28-estrutura-frontend]], [[geral-decisao-2026-10-28-criacao-de-componentes]]
- [[geral-decisao-2026-10-29-modo-de-implementacao]], [[geral-decisao-2026-10-29-padrao-de-branches]], [[geral-decisao-2026-10-29-testes-no-escopo]], [[geral-decisao-2026-10-29-cancelamento-ao-vivo]]

(Dial: médio, de [[geral-contexto]].)

- Desta etapa: [[geral-decisao-2026-10-29-api-de-itens]], [[geral-decisao-2026-10-29-imagem-do-lote-no-banco]], [[geral-decisao-2026-10-29-lance-inicial-e-valor-minimo]], [[geral-decisao-2026-10-29-inicio-e-duracao-do-lote]], [[geral-decisao-2026-10-29-limites-do-deposito]], [[geral-decisao-2026-10-29-edicao-de-lote-fora]], [[geral-decisao-2026-10-29-seed-com-imagem-fixa]], [[geral-decisao-2026-10-29-seed-tambem-em-producao]], [[geral-decisao-2026-10-29-busca-so-em-dominio-publico]], [[geral-decisao-2026-10-29-codigo-do-teto-do-deposito]], [[geral-decisao-2026-10-29-sequencia-no-extrato]]

### Pendente de aval antes da T1 (proposta da IA)
- Respondido em 2026-10-29 22:23: API de itens, imagem no banco, Q-06, Q-07, Q-10 e Q-14 (decisões acima).
- Respondido em 2026-10-29 23:01: seed com imagem fixa, seed também em produção, busca só em domínio público, `DEPOSIT_LIMIT_EXCEEDED` e sequência no extrato no I2 (decisões acima).

## Tarefas

### T1: carteira e lotes no `stonebid-api`
Construída por dois implementadores em paralelo, cada um no seu PR (pedido do humano, 2026-10-29 22:24): **T1a carteira** (`WalletMovement`, rotas `/wallet`, T-11) e **T1b lotes** (`Lot`, busca, imagem, vitrine, painel, cancelamento, T-07). Os dois tocam `schema.prisma`, seed e o registro de tools da MCP: cada um acrescenta só o seu bloco, e o segundo PR a entrar faz rebase sobre o primeiro.
- **Faz:** models `WalletMovement` (tipo, valor em centavos, lote opcional, chave de idempotência única) e `Lot` (cópia do item com imagem, lance inicial, incremento, início, fim original, fim atual, cancelamento; campos do I2 e I3 só quando chegarem) pelo [[contrato-modelo-de-dados]]. Saldo derivado dos movimentos (comprometido = 0 até o I2). Rotas: `GET /wallet`, `POST /wallet/deposits` com cabeçalho `Idempotency-Key` (só LICITANTE), `GET /wallet/movements`; `GET /items/search` por adaptador da API externa (AD-06), com timeout e erro claro; `POST /lots` (só LEILOEIRO, copia item e imagem), `GET /lots` (vitrine: ao vivo, agendados e encerrados pelo relógio do servidor, sem cancelados), `GET /lots/:id`, `GET /lots/:id/image`, `GET /auctioneer/lots` (só os próprios, por estado), `POST /lots/:id/cancel` (dono, sem lances); hora do servidor na resposta da vitrine. Uma tool da MCP por rota. Seed com lotes agendado, ao vivo e encerrado. Testes T-07 (parte da busca), T-08 (papéis) e T-11 (depósito idempotente).
- **Toca em:** `stonebid-api`: `prisma/`, `src/domain/`, `src/application/use-cases/`, `src/infra/http/`, `src/infra/mcp/`, `src/infra/external/`, seed, `test/`.
- **Depende de:** nenhuma (aval dado em 2026-10-29 22:23)
- **Paralelo:** sim, com T2 (contrato das rotas no briefing)
- **Pronto quando:**
  - [ ] lint, Prettier, tipos, Vitest e build passam; CI verde
  - [ ] depósito aumenta o total; a mesma `Idempotency-Key` duas vezes deposita uma vez só (T-11); disponível = total − comprometido
  - [ ] toda mudança de saldo tem linha no extrato; valores só em centavos inteiros
  - [ ] lote criado aparece como agendado ou ao vivo; cancelado some da vitrine; com a API externa fora, busca dá erro claro e vitrine e lote seguem abrindo (T-07)
  - [ ] papel errado dá 403 em depósito, criação e cancelamento; leiloeiro A não vê nem cancela lote do B (T-08)
  - [ ] tools da MCP para as rotas novas
- **Prova:** `npm run lint && npm run typecheck && npm test && npm run build`; E2E das rotas e da MCP
- **Verificação** (relatórios dos implementadores; verificador independente na T4):
  - Data: 2026-10-29
  - Critérios ✔/✘ com a prova de cada um:
    - **T1a, PR #1 do `stonebid-api`:** ✔ lint, Prettier, tipos, 36 testes Vitest e build; CI verde, com `migrate deploy` real. ✔ Mesma `Idempotency-Key` deposita uma vez, inclusive em requisições simultâneas (T-11). ✔ Disponível = total − comprometido. ✔ Extrato com uma linha por depósito. ✔ 403 para LEILOEIRO e 401 sem login. ✔ Tools `wallet_get`, `wallet_deposit` e `wallet_movements`. ✔ Seed com R$ 5.000,00 por licitante, rodado 2x sem duplicar.
    - **T1b, PR #2 do `stonebid-api`:** ✔ lint, Prettier, tipos, 43 testes Vitest e build; CI verde. ✔ Lote nasce agendado ou ao vivo, e o cancelado some da vitrine. ✔ Q-06 e Q-07 validadas. ✔ Leiloeiro A não vê nem cancela lote do B (T-08). ✔ Com a API fora, a busca dá 502 claro e vitrine, lote e imagem seguem respondendo (T-07). ✔ Imagem servida do banco. ✔ 6 tools da MCP. ✔ Seed com 3 lotes e imagens fixas.
    - ✘ **Não provado:** a busca real na AIC, porque o proxy do container recusa `api.artic.edu` (testado contra um servidor que imita a API); fica para a T4, no Chrome. A migração foi escrita à mão, porque o proxy bloqueia `binaries.prisma.sh`, e o CI aplicou sem erro.
    - O CD já roda `prisma migrate deploy` e `db:seed` antes de publicar, em staging e em produção. PR #1 na `main` (2026-10-29). PR #2 com rebase sobre ela (HEAD `61044aa`): os dois lados mantidos nos 9 arquivos em conflito, migrações em ordem (`init` < `wallet_movements` < `lots`), 59 testes, lint, Prettier, tipos e build; CI verde com `migrate deploy` real; `mergeable` limpo. Fica para o I2: relação de `WalletMovement.lotId` com `Lot`. O `.env.example` não lista as variáveis dos lotes (todas têm padrão).
  - Devolvido para correção: não

### T2: carteira, painel do leiloeiro e vitrine no `stonebid-web`
- **Faz:** `/wallet` (total, comprometido, disponível, depósito com chave de idempotência por envio, extrato); painel do leiloeiro (busca na API com mensagem clara na falha, formulário de lote com validação zod, meus lotes por estado, cancelar); vitrine em `/` com três seções e cards (imagem, título, lance inicial, contagem pela hora do servidor); componentes reaproveitados pelo [[registro-de-componentes]].
- **Toca em:** `stonebid-web`: `src/features/wallet/`, `src/features/lots/`, `src/routes/`.
- **Depende de:** contrato das rotas de T1 (no briefing)
- **Paralelo:** sim, com T1
- **Pronto quando:**
  - [ ] lint, Prettier, tipos e build passam; CI verde
  - [ ] duplo clique no depósito gera uma requisição só (ou a mesma chave)
  - [ ] Playwright cobre vitrine, criação de lote e depósito contra API simulada
- **Prova:** `npm run lint && npm run typecheck && npm run build`; Playwright
- **Verificação** (relatório do implementador; Playwright no ar na T4):
  - Data: 2026-10-29
  - Critérios ✔/✘ com a prova de cada um: ✔ PR #3 do `stonebid-web`, com lint, formatação, tipos e build; CI verde. ✔ Duplo clique no depósito gera um `POST` só; com a trava removida, o teste falha. ✔ Playwright 15/15 contra API simulada: vitrine, criação e validação de lote, erro da busca, cancelamento com 409, depósito, extrato e guarda de papel. O Playwright não existia: configuração e job `e2e` no CI criados nesta tarefa. ✔ Arrumação aprovada (23:01), PR #4 do `stonebid-web` (commits `b4b2b7b` e `4887a2b`): `useDebounce` e `useServerNow` em `src/hooks/`, login com o `SubmitButton` comum; lint, Prettier, tipos, build e Playwright 15/15; CI verde. O `SubmitButton` do `auth` segue no cadastro (`register-form.tsx`).
  - Devolvido para correção: não

### T3: staging e produção
- **Faz:** PRs `feat/RF-40-carteira` e `feat/RF-21-lotes` (ou os nomes do padrão de branches), CI verde, merge do humano, `staging` atualizada; migração e seed com lotes em staging e produção.
- **Toca em:** branches dos dois repositórios; banco de staging e produção.
- **Depende de:** T1, T2
- **Paralelo:** não
- **Pronto quando:**
  - [ ] CD verde em staging e produção; lotes do seed na vitrine no ar
- **Prova:** Actions verdes; vitrine de staging no Chrome
- **Verificação:**
  - Data: 
  - Critérios ✔/✘ com a prova de cada um:
  - Devolvido para correção:

### T4: verificação no ar
- **Faz:** orquestrador no Chrome, em staging: leiloeiro busca, cria lote e o vê na vitrine; licitante deposita (duplo clique), confere extrato; 403 com papel errado pela API; verificador independente lê o diff e os testes de T1 e T2.
- **Toca em:** nada (só testa e reporta)
- **Depende de:** T3
- **Paralelo:** não
- **Pronto quando:**
  - [ ] relatórios sem bloqueante
- **Prova:** relatórios
- **Verificação:**
  - Data: 
  - Critérios ✔/✘ com a prova de cada um:
  - Devolvido para correção:

## Próxima tarefa e a seguinte
T1a, T1b e T2 concluídas, com PRs abertos e CI verde. PRs #1 e #2 do `stonebid-api` e PR #3 do `stonebid-web` na `main`. O PR #3 entrou em `7e158db`, antes da arrumação: ela foi reaplicada no PR #4 do `stonebid-web` (CI verde). Próximo: merge do humano do PR #4; em seguida T3 e T4 e, em paralelo com a T4, os PRs `chore` (Node 26, job do `docker compose up`, botão do cadastro).

## Prioridades
Backend primeiro (T1): o I2 grava em cima da carteira e do lote. Se apertar, o painel do leiloeiro sai antes do polimento da vitrine.

## Candidatos a registro
- Node 26: PR `chore` em cada repositório depois do merge dos PRs da etapa 3 ([[geral-decisao-2026-10-29-node-26]]). No da API, job de CI que roda `docker compose up` e espera o `/health` (prova do RNF-11, aprovado pelo humano em 2026-10-29 23:09). No do web, o cadastro passa a usar o `SubmitButton` comum e o do `auth` é apagado (aprovado em 2026-10-29 23:10).
- Sequência no extrato: vai para o plano do I2 ([[geral-decisao-2026-10-29-sequencia-no-extrato]]).
- Referências: AIC com 60 requisições por minuto por IP, dados CC0 e IIIF de 843 px; o proxy bloqueia `binaries.prisma.sh` (contorno com `PRISMA_SCHEMA_ENGINE_BINARY` e migração escrita à mão); `gh pr create` falha porque o GraphQL é bloqueado (abrir PR por `gh api .../pulls`); `ui.shadcn.com` bloqueado (registro local gerado a partir do código-fonte do shadcn).
- Componentes da T2 para o [[registro-de-componentes]]: shadcn `badge`, `table`, `dialog`, `alert-dialog`, `alert`; comuns `CoverImage`, `ErrorState`, `StatCard`, `SubmitButton`; feature `lots` (`LotCard`, `LotsShowcase`, `CreateLotDialog`, `CancelLotButton` e outros, com os hooks `useShowcase`, `useCreateLot`, `useServerNow`, `useDebounce`); feature `wallet` (`WalletBalance`, `DepositForm`, `MovementsTable`, com `useWallet`, `useDeposit`). Feito no PR #3 (aprovado em 2026-10-29 23:01): `useDebounce` e `useServerNow` em `src/hooks/`, login com o `SubmitButton` comum; o cadastro ainda usa o `SubmitButton` do `auth`. Sem `CLAUDE.md` no `stonebid-web`. Erro antigo no console (`Encountered a script tag`, provável `next-themes`), não investigado.

### 🔗 Conexões
- Funcionalidade: [[carteira-e-lotes-contexto]]
- Roteiro: [[geral-plano]] (etapa 3)
- Acesso: [[acesso-de-teste]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
