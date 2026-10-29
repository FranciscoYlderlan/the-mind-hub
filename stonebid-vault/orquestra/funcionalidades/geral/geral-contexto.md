---
tipo: contexto
funcionalidade: geral
status: em-construcao
etapa-atual: 1
criado: 2026-10-28
aliases: [Contexto do StoneBid, Visão geral do projeto, Project overview]
---
# 🧭 StoneBid — contexto geral

> [!tldr] Em uma linha
> Casa de leilões online com lances ao vivo, saldo simulado, comprovante compartilhável e histórico de lances auditável por qualquer pessoa.

## Objetivo e motivação
O StoneBid é uma casa de leilões online. O leiloeiro monta lotes a partir de itens de uma API pública, e licitantes disputam cada lote com lances ao vivo, usando um saldo simulado. Quem vence recebe um comprovante compartilhável por link. Qualquer pessoa, sem login, pode auditar o histórico de lances de um lote e verificar se ele foi adulterado. A aplicação precisa estar no ar (deploy).

Motivação: [a confirmar]

## Fatos que eu informei
(o agente preserva sem reinterpretar)
- Dois repositórios: `stonebid-web` (frontend) e `stonebid-api` (backend), ainda não criados no GitHub.
- Stack do frontend: React 19.3, Vite 8.3.4, Tailwind CSS v4.3, TanStack Router v1 (só rotas, não o framework), TanStack Query v5, Zustand latest (só UI global), zod 4.6, shadcn/ui (iniciado pelo guia oficial para Vite), Node 26.13.0, npm, ESLint + Prettier, Playwright, CI/CD com GitHub Actions → [[geral-decisao-2026-10-28-stack-frontend]].
- Stack do backend: Fastify v5.12.7, Prisma v8 sobre PostgreSQL, zod 4.6, Node e PostgreSQL latest, Vitest v5.0.5 (sem Jest), ESLint + Prettier (sem Biome), Docker/Compose e CI/CD com GitHub Actions → [[geral-decisao-2026-10-28-stack-backend]].
- Frontend organizado por features (`routes → features → components/hooks/lib`), com nomes genéricos (`feature1`, `feature2`) na estrutura para não induzir o domínio → [[geral-decisao-2026-10-28-estrutura-frontend]].
- Backend em Clean Architecture (`domain/`, `infra/`, `env/`) → [[geral-decisao-2026-10-28-estrutura-backend]].
- Componentes: registro consultado antes de criar, shadcn/ui primeiro, componentes pequenos e sem repetição → [[geral-decisao-2026-10-28-criacao-de-componentes]] e [[registro-de-componentes]].
- Toda funcionalidade criada no frontend é testada com Playwright por uma **subthread de teste** (outro agente), que só testa e reporta bugs; sem testes unitários ou de componente no frontend → [[geral-decisao-2026-10-28-testes-frontend-playwright]].

## O que já foi feito
- 2026-10-28: cofre montado com a estrutura `orquestra/` e alinhado ao processo das etapas vitais ([[diario-2026-10-28]]).
- 2026-10-28: stack, organização do frontend e do backend e regras de componentes registradas como decisões; registro de componentes criado ([[diario-2026-10-28]]).
- 2026-10-28: Obsidian CLI disponível nas sessões pelo servidor MCP `obsidian-cli`; causa da falha registrada em [[bug-obsidian-cli-mcp-nao-carrega-2026-10-28]].

## Tempo disponível

## Dial e modelo de IA
- Dial: [a confirmar] alto | medio | baixo
- Modelo de IA: 

## Áreas sensíveis
(onde ler bugs e referências antes de mexer)
- Componentes do frontend: ler [[registro-de-componentes]] e [[geral-decisao-2026-10-28-criacao-de-componentes]] antes de criar qualquer componente.
- Busca no cofre (Obsidian CLI): se as ferramentas `obsidian_*` faltarem ou a CLI falhar, ler [[bug-obsidian-cli-mcp-nao-carrega-2026-10-28]] antes de buscar nos `.md`.

## Mapa
- Roteiro: [[geral-plano]]
- Decisões: [[geral-decisao-2026-10-28-testes-frontend-playwright]], [[geral-decisao-2026-10-28-stack-frontend]], [[geral-decisao-2026-10-28-stack-backend]], [[geral-decisao-2026-10-28-estrutura-frontend]], [[geral-decisao-2026-10-28-estrutura-backend]], [[geral-decisao-2026-10-28-criacao-de-componentes]]
- Bugs: [[bug-obsidian-cli-mcp-nao-carrega-2026-10-28]]
- Referências: [[registro-de-componentes]], [[manual-da-orquestra]], [[manual-do-cerebro]]

## Interpretação do agente
(separada dos fatos; marcar [a confirmar] quando for suposição)
- As versões foram registradas como informadas, sem checagem contra os registros do npm.
- Áreas candidatas a sensíveis: lances ao vivo (concorrência) e a verificação de adulteração do histórico [a confirmar].

### 🔗 Conexões
- Mapa: [[moc-orquestra]]
- Regras: [[manual-da-orquestra]], [[manual-do-cerebro]]
