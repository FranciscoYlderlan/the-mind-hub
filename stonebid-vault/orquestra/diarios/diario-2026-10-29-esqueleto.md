---
tipo: diario
status: consolidada
criado: 2026-10-29
---
# 📓 Diário 2026-10-29: esqueleto no ar (I0)

## O que foi feito
- 14:18: humano pediu para iniciar a implementação. Etapa 2 do [[geral-plano]] começada; plano [[esqueleto-plano]] (T1 a T4) escrito como proposta.
- 14:2x: `add_repo` recusado (GitHub não ligado). Pasta local `C:\Users\Ylderlan\Documents\Projetos\stonebid` acessada (estava vazia); repositórios no GitHub vazios.
- Subagentes despachados no container: T1 (`stonebid-api`), T2 (`stonebid-web`) e preparação da T3 (script do GCP, `cd.yml`, guia de deploy). Script e guia copiados para `stonebid\stonebid-infra` no computador do humano.
- T1 entregue: Fastify 5.12.7, Prisma **7.10.1** (a 8 só existe em rc e é outro produto, sem `migrate`), zod 4.6.7, Vitest 5.0.5; JWT no `Authorization: Bearer` (7 dias), bcryptjs, `requireAuth`/`requireRole`; seed com upsert (`leiloeiro@stonebid.dev`, `licitante-1@stonebid.dev`, `licitante-2@stonebid.dev`, senha `SEED_PASSWORD`); MCP com api_key e tools `entrar`, `health`, `auth_me`, `auth_register`, `auth_login`; Dockerfile, Compose, CI. Prova: 20 testes, lint, tipos e build. Não provado: `docker compose up` (proxy do container bloqueia registries).
- T2 entregue: shadcn (base radix, preset nova) pelo guia para Vite, TanStack Router com `_public`, `_auth` e `_app`, feature `auth`, `/account` protegida, tema claro/escuro com `next-themes` (sem Zustand), TypeScript 6.0.3 (o `typescript-eslint` não suporta o 7). Prova: lint, tipos, build e Playwright 26/26 contra API simulada.
- 14:59: humano ligou o GitHub; projeto GCP e time na Vercel já existiam. Push recusado até o Claude GitHub App; depois o push funcionou.
- Push na `main` dos dois repositórios (boilerplate direto na `main`, [[geral-decisao-2026-10-29-padrao-de-branches]]). CI falhou no Prettier do `cd.yml` (escrito pelo orquestrador), corrigido; **CI verde nos dois**. CD falha por falta de secrets (esperado).
- 15:22–15:33: GCP pelo Claude in Chrome: o banner avisa que o teste gratuito exige pré-pagamento (humano pagou R$ 200, crédito em até 24 h). Cloud Shell sem conta; o humano rodou `gcloud auth login`. O script parou em "Billing account … is not open" (`UREQ_PROJECT_BILLING_NOT_OPEN`); nada criado.
- 15:35: humano escolheu trocar de host agora e aprovou o **Railway** (Render descartado por dormir após 15 min). A IA registrou uma decisão nova (M-14) e marcou [[geral-decisao-2026-10-29-hospedagem]] como `substituida`.
- Varredura de impacto, desfeita às 15:43 (termos: GCP, Cloud Run, Cloud SQL, Google Cloud, Workload Identity, Artifact Registry, Secret Manager, São Paulo, backlinks da decisão antiga). Tocadas: [[contrato-tecnologias]], [[contrato-do-projeto]], [[contrato-do-projeto-mudancas]], [[contrato-arquitetura]], [[enunciado-teste-tecnico]], [[geral-decisao-2026-10-28-stack-backend]], [[geral-decisao-2026-10-29-camada-mcp]], [[geral-decisao-2026-10-29-padrao-de-branches]], [[geral-contexto]], [[geral-plano]], [[moc-orquestra]], [[esqueleto-plano]] e o bloco `padroes` do `CLAUDE.md`.
- Railway aberto no Chrome: sem login; o humano interrompeu a ação seguinte e pediu a passagem de turno.
- 15:43: o GCP aprovou o faturamento e o humano pediu para desfazer a troca: "iremos seguir com a gcp". As mudanças não estavam commitadas: `git restore` das 14 notas da varredura no `the-mind-hub` e a nota da decisão do Railway apagada (com permissão de exclusão); [[geral-decisao-2026-10-29-hospedagem]] voltou a `aprovada`. Este diário, [[esqueleto-plano]] e [[esqueleto-contexto]] foram ajustados para o GCP. Erro de processo: uma conferência das notas do esqueleto foi feita por `grep` no shell, e não pela Obsidian CLI.
- 15:47: chat novo; humano pediu para continuar. Faturamento conferido (`billingEnabled: true`); o humano mandou a página de pagamento como prova (15:51).
- `gcp-setup.sh` baixado do repositório público e rodado no Cloud Shell sem `BILLING_ACCOUNT`; concluiu tudo (APIs, Artifact Registry, Cloud SQL, segredos, contas de serviço, WIF). A `MCP_API_KEY_STAGING` fica só no Secret Manager (não vai para o cofre).
- Alerta de orçamento criado no console: `stonebid-budget`, R$ 250 por mês (a conta é em BRL), avisos em 50, 90 e 100%, sem descontar créditos.
- Vercel: projeto `stonebid-web` importado (o humano fez a reautenticação por e-mail), primeiro deploy ok; Vercel Authentication desligada; `VERCEL_ORG_ID` e `VERCEL_PROJECT_ID` cadastrados; o humano cadastrou o `VERCEL_TOKEN`.
- GitHub: o proxy do container recusa a API de Actions; secrets e variables cadastrados pelo site, no Chrome. API: os 6 secrets do GCP, `CORS_ORIGIN` e `CORS_ORIGIN_STAGING`. Web: `VERCEL_STAGING_ALIAS`, `VITE_API_URL` e `VITE_API_URL_STAGING`.
- Branch `staging` criada nos dois repositórios a partir da `main`; re-run do CI da `main` nos dois. CDs da API verdes em produção e staging; testes no Chrome: `/health` 200 nos dois, `/mcp` 404 em produção e 401 sem api_key em staging. Web de produção republicado com a URL da API; `/login` abre e o CORS aceita a origem da Vercel.
- CD do web na `staging` publicou o preview, mas o `vercel alias set` falhou ("Error: User not found."): faltava `--scope` do time. Correção no PR #1 do `stonebid-web` (branch `fix/RNF-01-vercel-alias-scope`), CI verde, aguardando o humano decidir o merge.
- Erro de processo: no início da sessão o `CLAUDE.md` do cofre foi lido com `cat` no shell, e não pela Obsidian CLI (as demais leituras foram pela CLI).

## Decisões tomadas
- Nenhuma vigente (a do Railway foi desfeita às 15:43).

## Bugs registrados
- Nenhum.

## Candidatos que não viraram nota
(aguardam o aval do humano; ver dúvidas)
- Decisões: token JWT no cabeçalho em vez de cookie; Prisma 7.10.1 no lugar da 8; TypeScript 6 no web; `next-themes` no lugar do Zustand para o tema; `vercel.json` com `git.deploymentEnabled: false`; alias fixo do staging na Vercel.
- Registro de componentes: shadcn `button input label card sonner field radio-group separator sidebar dropdown-menu empty spinner avatar` (+ tooltip, skeleton, sheet, `use-mobile.ts`); próprios `header`, `public-shell`, `auth-shell`, `app-shell`, `app-sidebar`, `empty-state`, `page-header`, `text-field`, `theme-toggle`, `brand-logo`; da feature auth `login-form`, `register-form`, `auth-card`, `role-choice`, `submit-button`, `session-actions`, `account-summary`; hooks `useZodForm`, `useAuthMutation`, `useLogin`, `useRegister`, `useLogout`, `useSession`.
- Referências (bloqueios do container): proxy recusa `ui.shadcn.com` (contorno: registro local com `REGISTRY_URL`), `binaries.prisma.sh`, registries Docker, a API de Actions do GitHub e `*.run.app`; Prisma 7 bloqueia `migrate reset` quando roda por agente; terminal novo do Cloud Shell não herda o `gcloud auth login`.

> [!tip] Onde parei
> - **Próximo passo:** fechar a T3 de [[esqueleto-plano]]: merge do PR #1 do `stonebid-web` (decisão do humano), depois trazer a `staging` do web para a `main` e conferir o alias `stonebid-web-staging.vercel.app`; o humano entra com os 3 usuários em `https://stonebid-web.vercel.app/login`; testar `claude mcp add` na API de staging. Depois a T4 (verificador + Playwright no ar).
> - **Threads abertas:** PR #1 do `stonebid-web` aberto. Nenhum subagente em andamento. Código só no GitHub; a pasta local `stonebid` tem só `stonebid-infra`.
> - **Dúvidas para o humano:** quem faz o merge do PR #1; resultado do login dos 3 usuários; aprovar os candidatos a decisão acima; Node fixo em 24 (LTS) ou 26 na imagem e no CI; validar `docker compose up` na máquina dele.

### 🔗 Conexões
- Mapa: [[moc-orquestra]]
- Funcionalidades tocadas: [[esqueleto-contexto]]
- Diário do dia: [[diario-2026-10-29]]
- Projeto: [[geral-contexto]]
