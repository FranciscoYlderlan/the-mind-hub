---
tipo: contexto
funcionalidade: esqueleto
status: concluida
etapa: 2
criado: 2026-10-29
aliases: [Esqueleto no ar, I0, Boilerplate dos repositórios, Project skeleton]
---
# 🧭 Esqueleto no ar (I0)

> [!tldr] Em uma linha
> Os dois repositórios montados, com login por papel, seed e CI, publicados com HTTPS no GCP e na Vercel: a aplicação "vazia" no ar com os 3 usuários de teste.

## Objetivo e motivação
Etapa 2 do [[geral-plano]] (I0 de [[contrato-processo-e-plano]]): RF-01 a RF-03, RNF-01, RNF-02, RNF-11, base de RNF-12 e RNF-13. Deploy cedo, para testar o host real (R-05).

## Fatos que eu informei
- 2026-10-29: "dar inicio a implementação roadmap foi aprovado e agora vamos fazer a etapa 1" (a etapa 1 do roteiro já estava concluída; a primeira de implementação é a 2).
- 2026-10-29: GitHub ligado ao Claude; projeto GCP `project-3eb3570f-ed8a-44be-848` e time na Vercel `franciscoylderlans-projects` já existiam.
- 2026-10-29: pré-pagamento de R$ 200 feito no GCP, ainda não creditado.
- 2026-10-29 15:43: o GCP aprovou o faturamento; seguimos com o GCP ([[geral-decisao-2026-10-29-hospedagem]]).
- 2026-10-29 15:51: o humano mostrou a página de pagamento do faturamento como prova de que o pagamento foi efetuado.
- 2026-10-29 22:06: "Sempre no staging e em prod quem irá testar é o agente para agilizar os processos".
- 2026-10-29 22:08: "esse é um teste técnico todos os dados são fictícios mesmo em produção".
- 2026-10-29: o humano fez a reautenticação da Vercel por código de e-mail e cadastrou o secret `VERCEL_TOKEN` no `stonebid-web`.

## O que já foi feito
- 2026-10-29: T1 e T2 de [[esqueleto-plano]] entregues e publicados na `main` de `stonebid-api` e `stonebid-web`, com CI verde nos dois.
- 2026-10-29: T3 esperou o faturamento do GCP abrir; a troca para o Railway foi feita e desfeita no cofre quando o GCP aprovou ([[diario-2026-10-29-esqueleto]]).
- 2026-10-29 (tarde): T3 quase concluída. GCP montado pelo `gcp-setup.sh` (Cloud SQL `stonebid-db` com os bancos `stonebid` e `stonebid_staging`, Artifact Registry, Secret Manager, contas de serviço, Workload Identity Federation) e alerta de orçamento de R$ 250. Vercel com o projeto `stonebid-web` (produção `stonebid-web.vercel.app`, proteção dos previews desligada). Secrets e variables cadastrados nos dois repositórios; branch `staging` criada nos dois. No ar: API `stonebid-api-7idhzkkvpq-rj.a.run.app`, API de staging `stonebid-api-staging-7idhzkkvpq-rj.a.run.app` e web de produção. Pendentes: PR #1 do `stonebid-web` (alias do staging) e o login dos 3 usuários na URL pública.
- 2026-10-29 21:40: humano liberou o acesso à aplicação no ar para os agentes (projeto de teste, acesso livre); endereços e usuários em [[acesso-de-teste]].
- 2026-10-29 22:09: T3 concluída: alias do staging no ar, login dos 3 usuários no staging (agente) e em produção (humano).
- 2026-10-29 22:15: T4 concluída no Chrome, sem bloqueante ([[esqueleto-plano]]).
- 2026-10-29 22:20: etapa 2 do [[geral-plano]] concluída. Ficam para depois, sem bloqueio: `claude mcp add` em staging (precisa da `MCP_API_KEY_STAGING`), `docker compose up` na máquina do humano e o 403 do `requireRole` no ar, que a etapa 3 prova ([[carteira-e-lotes-plano]]).

## Tempo disponível
O do [[geral-contexto]]: entrega em 2026-10-30 16:00.

## Dial e modelo de IA
- Dial: medio (o do [[geral-contexto]])
- Modelo de IA: Claude Opus 5.5 (`claude-opus-5-5`) [a confirmar]

## Áreas sensíveis
- Login e papéis (RF-01, RF-02): [[contrato-requisitos-funcionais]].
- Rotas do backend mexem na camada MCP: [[geral-decisao-2026-10-29-camada-mcp]].
- Componentes: [[registro-de-componentes]] e [[geral-decisao-2026-10-28-criacao-de-componentes]].

## Mapa
- Plano: [[esqueleto-plano]]
- Decisões: [[geral-decisao-2026-10-29-sessao-jwt-no-cabecalho]], [[geral-decisao-2026-10-29-prisma-7]], [[geral-decisao-2026-10-29-typescript-6-no-web]], [[geral-decisao-2026-10-29-next-themes-para-o-tema]], [[geral-decisao-2026-10-29-vercel-sem-deploy-automatico]], [[geral-decisao-2026-10-29-alias-fixo-do-staging]], [[geral-decisao-2026-10-29-node-26]], [[geral-decisao-2026-10-29-modo-de-implementacao]], [[geral-decisao-2026-10-29-hospedagem]], [[geral-decisao-2026-10-29-padrao-de-branches]], [[geral-decisao-2026-10-29-camada-mcp]]
- Diário: [[diario-2026-10-29-esqueleto]]

## Interpretação do agente
- O "etapa 1" do humano foi lido como a primeira etapa de implementação (etapa 2 do roteiro); a sessão seguiu com a etapa 2 sem objeção do humano.

### 🔗 Conexões
- Mapa: [[moc-orquestra]]
- Acesso de teste: [[acesso-de-teste]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
