---
tipo: plano
funcionalidade: esqueleto
status: proposta
criado: 2026-10-29
---
# 📋 Esqueleto no ar (I0)

> [!warning] Proposta da IA
> Nada aqui é decisão. Decisões ficam nas notas `-decisao-` linkadas abaixo.

## Objetivo desta rodada
Etapa 2 do [[geral-plano]]: aplicação "vazia" no ar com os 3 usuários de teste (I0 de [[contrato-processo-e-plano]]): RF-01 a RF-03, RNF-01, RNF-02, RNF-11, base de RNF-12 e RNF-13.

## Decisões que este plano respeita
- [[geral-decisao-2026-10-28-stack-backend]], [[geral-decisao-2026-10-28-estrutura-backend]]
- [[geral-decisao-2026-10-28-stack-frontend]], [[geral-decisao-2026-10-28-estrutura-frontend]], [[geral-decisao-2026-10-28-criacao-de-componentes]]
- [[geral-decisao-2026-10-29-camada-mcp]], [[geral-decisao-2026-10-29-hospedagem]], [[geral-decisao-2026-10-29-padrao-de-branches]]
- [[geral-decisao-2026-10-28-testes-frontend-playwright]], [[geral-decisao-2026-10-29-testes-no-escopo]]

(Dial: médio, de [[geral-contexto]].)

## Tarefas

### T1: boilerplate e login do `stonebid-api`
- **Faz:** Fastify + Prisma (PostgreSQL) em Clean Architecture; `env/` com zod; erro centralizado; `GET /health`; model `User` com papel LEILOEIRO ou LICITANTE e senha com hash; rotas de cadastro, login e "quem sou eu" (RF-01, RF-02); seed reexecutável com `leiloeiro`, `licitante-1` e `licitante-2` (RNF-02; lotes ficam para o I1); camada MCP com api_key, tool `entrar` e uma tool por rota; Dockerfile, `docker-compose.yml` (RNF-11), `.env.example`, ESLint, Prettier, Vitest com E2E em `test/e2e/`, `ci.yml`, README inicial.
- **Toca em:** repositório `stonebid-api` inteiro (boilerplate direto na `main`).
- **Depende de:** nenhuma
- **Paralelo:** sim, com T2
- **Pronto quando:**
  - [ ] lint, Prettier, tipos, Vitest e build passam
  - [ ] cadastro, login e "quem sou eu" funcionam; senha nunca em texto puro; rota protegida recusa sem login e recusa papel errado
  - [ ] seed roda duas vezes seguidas sem erro
  - [ ] `/mcp` recusa sem api_key; `entrar` + tool de "quem sou eu" funcionam
  - [ ] `docker compose up` sobe API + banco
- **Prova:** `npm run lint && npm run typecheck && npm test && npm run build`; teste E2E de auth e da MCP
- **Verificação** (relatório do implementador; o verificador independente fica para a T4):
  - Data: 2026-10-29
  - Critérios ✔/✘ com a prova de cada um: ✔ lint, Prettier, tipos, 20 testes Vitest e build (exit 0, duas vezes); ✔ senha só com hash bcrypt (teste no banco e na resposta); ✔ 401 sem login e 403 `FORBIDDEN` com papel errado; ✔ seed 2x sem erro; ✔ `/mcp` 401 sem chave, `entrar` + `auth_me` pelo cliente do SDK; ✘ `docker compose up` não provado (proxy do container bloqueia registries; `compose config` valida). CI verde no GitHub.
  - Devolvido para correção: não

### T2: boilerplate e login do `stonebid-web`
- **Faz:** projeto pelo guia do shadcn para Vite; TanStack Router (file-based) com os layouts `_public`, `_auth` e `_app`; TanStack Query; `config/` com env zod; `api-client`; telas de login e cadastro com escolha de papel; vitrine vazia em `/`; guard do `_app` com `?redirect` validado; tokens de tema claro e escuro (base do RNF-13); ESLint, Prettier, `ci.yml`.
- **Toca em:** repositório `stonebid-web` inteiro (boilerplate direto na `main`).
- **Depende de:** contrato das rotas de auth de T1 (combinado no briefing)
- **Paralelo:** sim, com T1
- **Pronto quando:**
  - [ ] lint, Prettier, tipos e build passam
  - [ ] login e cadastro contra a API local funcionam e o login persiste ao recarregar (RF-01)
  - [ ] `/` abre sem login; rota do `_app` sem login vai para `/login?redirect=`
- **Prova:** `npm run lint && npm run typecheck && npm run build`; Playwright (T4)
- **Verificação** (relatório do implementador; o Playwright no ar fica para a T4):
  - Data: 2026-10-29
  - Critérios ✔/✘ com a prova de cada um: ✔ lint, Prettier, tipos e build; ✔ login e cadastro com sessão persistida ao recarregar (Playwright 26/26 contra API simulada, não contra a API real); ✔ `/` sem login; ✔ `/account` sem login vai para `/login?redirect=%2Faccount`. CI verde no GitHub.
  - Devolvido para correção: não

### T3: deploy (GCP, Vercel) e CD
- **Faz:** rodar `infra/gcp-setup.sh` do `stonebid-api` no Cloud Shell do projeto `project-3eb3570f-ed8a-44be-848` (Artifact Registry, Cloud SQL, segredos, Workload Identity Federation; alerta de orçamento à parte) pela [[geral-decisao-2026-10-29-hospedagem]]; cadastrar os secrets e variables no GitHub; projeto na Vercel (importar, desligar proteção dos previews, token, `VITE_API_URL`); `cd.yml` dos dois repositórios (já na `main`); branch `staging` nos dois repositórios; seed em produção e staging.
- **Toca em:** `infra/` e `.github/workflows/cd.yml` do `stonebid-api`, `cd.yml` do `stonebid-web`, contas GCP e Vercel do humano.
- **Depende de:** T1, T2 e faturamento do GCP aberto (aberto em 2026-10-29 15:43)
- **Paralelo:** não
- **Pronto quando:**
  - [ ] push na `main` com CI verde publica API e web; push na `staging` publica a API de staging com `MCP_ENABLED=true`
  - [ ] login com os 3 usuários de teste na URL pública (RNF-01, HTTPS)
- **Prova:** abrir a URL da Vercel e entrar com `leiloeiro`; `claude mcp add` na URL de staging
- **Verificação** (parcial, pelo orquestrador no Chrome; o verificador independente fica para a T4):
  - Data: 2026-10-29
  - Critérios ✔/✘ com a prova de cada um: ✔ push na `main` com CI verde publica a API (`stonebid-api-7idhzkkvpq-rj.a.run.app`, `/health` 200, `/mcp` 404) e o web (`stonebid-web.vercel.app`, `/login` abre, bundle aponta para a API, CORS aceito); ✔ push na `staging` publica a API de staging (`stonebid-api-staging-7idhzkkvpq-rj.a.run.app`, `/health` 200, `/mcp` 401 sem api_key); ✘ alias fixo do web de staging (passo `vercel alias set` falhou com "User not found"; correção no PR #1 do `stonebid-web`, CI verde, aguarda merge do humano); ✘ login com os 3 usuários na URL pública (pendente com o humano: senha em produção não é digitada pelo agente); ✘ `claude mcp add` em staging não testado.
  - Devolvido para correção: não

### T4: verificação no ar
- **Faz:** verificador do backend (critérios de T1 e MCP em staging) e subthread de Playwright no frontend (RF-01 a RF-03 na URL pública).
- **Toca em:** nada (só testa e reporta)
- **Depende de:** T3
- **Paralelo:** não
- **Pronto quando:**
  - [ ] relatórios sem bloqueante
- **Prova:** relatórios dos subagentes
- **Verificação:**
  - Data: 
  - Critérios ✔/✘ com a prova de cada um:
  - Devolvido para correção:

## Próxima tarefa e a seguinte
T1 e T2 concluídas; T3 quase: alias do staging no ar desde 2026-10-29 22:00 (PR #2, API REST da Vercel); login dos 3 usuários ✔ no staging (2026-10-29 22:01, agente no Chrome); falta o login em produção, pelo humano, (endereços e usuários em [[acesso-de-teste]]; acesso livre para agentes). Depois, T4.

## Prioridades
Deploy cedo (R-05: testar o host real logo). Se apertar, T3 antes de qualquer polimento de T2.

## Candidatos a registro
- Sessão entre origens (Vercel ↔ Cloud Run): token JWT no cabeçalho `Authorization: Bearer`, no lugar de cookie `SameSite=None`; já implementado na T1 e T2, aguarda aval.
- Prisma 7.10.1 no lugar da 8 (a 8 só existe em rc e é outro produto); TypeScript 6 no web; `next-themes` no lugar do Zustand para o tema; `vercel.json` com `git.deploymentEnabled: false`; alias fixo do staging na Vercel.
- Registro de componentes da T2 (lista em [[diario-2026-10-29-esqueleto]]).
- Referência: bloqueios do proxy do container (`ui.shadcn.com`, `binaries.prisma.sh`, registries Docker) e o Prisma 7 que recusa `migrate reset` vindo de agente.
- Referência (T3): o proxy do container também recusa a API de Actions do GitHub (secrets e variables) e os hosts `*.run.app`; secrets e variables foram cadastrados pelo site do GitHub no Chrome, e os testes da API no ar também pelo Chrome. Um terminal novo do Cloud Shell não herda o `gcloud auth login` do primeiro.
- Alerta de orçamento em R$ 250 (a conta de faturamento é em BRL), sem descontar créditos, para medir o gasto bruto.

### 🔗 Conexões
- Funcionalidade: [[esqueleto-contexto]]
- Roteiro: [[geral-plano]] (etapa 2)
- Acesso: [[acesso-de-teste]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
