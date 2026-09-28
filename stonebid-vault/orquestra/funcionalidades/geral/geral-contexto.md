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

Motivação: teste técnico Elite Dev da Verzel e aprendizado.

## Fatos que eu informei
(o agente preserva sem reinterpretar)
- Dois repositórios: `stonebid-web` (frontend) e `stonebid-api` (backend), ainda não criados no GitHub.
- 2026-10-29: repositórios criados no GitHub: https://github.com/FranciscoYlderlan/stonebid-api e https://github.com/FranciscoYlderlan/stonebid-web. Pasta do projeto no computador: `C:\Users\Ylderlan\Documents\Projetos\stonebid`.
- 2026-10-29: branches `main` (produção), `staging` e de trabalho `tipo/ID-descricao-curta` (ex.: `feat/RN-04-incremento-minimo`); boilerplate inicial direto na `main` → [[geral-decisao-2026-10-29-padrao-de-branches]].
- 2026-10-29: configuração do GCP aprovada (São Paulo, Cloud Run com 1 instância mínima, Cloud SQL `db-f1-micro`, Workload Identity Federation, alerta de US$ 50, staging como segundo serviço) → [[geral-decisao-2026-10-29-hospedagem]].
- 2026-10-29: Prisma com `@@map` em snake_case; testes E2E do backend em `test/e2e/` na raiz → [[geral-decisao-2026-10-28-estrutura-backend]].
- 2026-10-29: camada MCP e Playwright entram no contrato como mudança → [[contrato-do-projeto]].
- 2026-10-29: sempre que for etapa de programação em algum dos repositórios, o acesso é permitido para essa etapa (regra em `CLAUDE.md`, seção "Repositórios e acesso").
- Stack do frontend: React 19.3, Vite 8.3.4, Tailwind CSS v4.3, TanStack Router v1 (só rotas, não o framework), TanStack Query v5, Zustand latest (só UI global), zod 4.6, shadcn/ui (iniciado pelo guia oficial para Vite), Node 26.13.0, npm, ESLint + Prettier, Playwright, CI/CD com GitHub Actions → [[geral-decisao-2026-10-28-stack-frontend]].
- Stack do backend: Fastify v5.12.7, Prisma v8 sobre PostgreSQL, zod 4.6, Node e PostgreSQL latest, Vitest v5.0.5 (sem Jest), ESLint + Prettier (sem Biome), Docker/Compose e CI/CD com GitHub Actions → [[geral-decisao-2026-10-28-stack-backend]].
- Frontend organizado por features (`routes → features → components/hooks/lib`), com nomes genéricos (`feature1`, `feature2`) na estrutura para não induzir o domínio → [[geral-decisao-2026-10-28-estrutura-frontend]].
- Backend em Clean Architecture (`domain/`, `infra/`, `env/`) → [[geral-decisao-2026-10-28-estrutura-backend]].
- Regra geral dos dois repositórios, desde a criação do projeto: nomes de arquivos e de entidades em **inglês** e **kebab-case**; identificadores no código em PascalCase e camelCase; parâmetro de rota sempre `$id.tsx` → [[geral-decisao-2026-10-28-estrutura-frontend]] e [[geral-decisao-2026-10-28-estrutura-backend]].
- 2026-10-29: a camada MCP, o staging e o teste com Playwright por outro agente **continuam no plano**; a primeira etapa é justamente deixar o projeto no ar.
- Enunciado oficial do teste técnico (Elite Dev na Verzel) fornecido em 2026-10-29: fonte da verdade nº 1 → [[enunciado-teste-tecnico]].
- Componentes: registro consultado antes de criar, shadcn/ui primeiro, componentes pequenos e sem repetição → [[geral-decisao-2026-10-28-criacao-de-componentes]] e [[registro-de-componentes]].
- Toda funcionalidade criada no frontend é testada com Playwright por uma **subthread de teste** (outro agente), que só testa e reporta bugs; sem testes unitários ou de componente no frontend → [[geral-decisao-2026-10-28-testes-frontend-playwright]].
- Contrato do projeto v0.2 (2026-10-27), escrito por mim com a IA e ainda em validação: requisitos, regras de negócio, arquitetura proposta, riscos, testes, plano e perguntas → [[contrato-do-projeto]].
- Do contrato (itens `[DECIDIDO]`): prazo real de **4 dias** (o enunciado fala em 7; **substituído em 2026-10-29**, ver o item seguinte); **todos os 5 opcionais** serão feitos; deploy obrigatório; desenvolvimento com IA permitido; sou júnior e aprender é objetivo do projeto → [[contrato-visao-escopo-e-papeis]].
- 2026-10-29 (09:06): o prazo real passou de 4 dias para **24 horas** a partir de agora. Oficialmente estou no **terceiro dia**: nos três primeiros dias não avancei muito além dos requisitos e da arquitetura. Vou trabalhar sem pausa.
- Camada MCP no backend para expor as rotas e testar o fluxo pela Claude; sempre que uma feature e uma rota forem criadas, a MCP é atualizada → [[geral-decisao-2026-10-29-camada-mcp]].
- 2026-10-29: hospedagem: backend e banco no **GCP**, frontend na **Vercel**, os dois repositórios no GitHub com CI/CD validando a integração. Custo zero: a aplicação fica no ar no máximo 7 dias, é avaliada em menos de 1 hora e depois é fechada → [[geral-decisao-2026-10-29-hospedagem]].

## O que já foi feito
- 2026-10-28: cofre montado com a estrutura `orquestra/` e alinhado ao processo das etapas vitais ([[diario-2026-10-28]]).
- 2026-10-28: stack, organização do frontend e do backend e regras de componentes registradas como decisões; registro de componentes criado ([[diario-2026-10-28]]).
- 2026-10-28: Obsidian CLI disponível nas sessões pelo servidor MCP `obsidian-cli`; causa da falha registrada em [[bug-obsidian-cli-mcp-nao-carrega-2026-10-28]].
- 2026-10-29: camada MCP do backend registrada como decisão ([[diario-2026-10-29]]).
- 2026-10-29: enunciado do teste técnico guardado e mapeado contra o contrato ([[enunciado-teste-tecnico]]); regra de nomes em inglês + kebab-case nas decisões de estrutura.
- 2026-10-29: contrato do projeto v0.2 registrado em `referencias/`, uma nota por seção, a partir de [[contrato-do-projeto]] ([[diario-2026-10-29]]).
- 2026-10-29: hospedagem decidida (GCP + Vercel, CI/CD pelo GitHub) e propagada nas decisões de stack, na camada MCP e no contrato ([[geral-decisao-2026-10-29-hospedagem]]).
- 2026-10-29: links dos repositórios, pasta local e regra de acesso nas etapas de programação registrados ([[diario-2026-10-29]]).
- 2026-10-29: [[contrato-do-projeto]] atualizado para a v0.3 com o cenário atual (M-01 a M-10).
- 2026-10-29: pendências respondidas: branches, configuração do GCP, entrega, dial, motivação, `@@map`, testes E2E e mudança do contrato ([[diario-2026-10-29]]).

## Tempo disponível
- **24 horas** a partir de 2026-10-29 09:06 (substitui os 4 dias do contrato). Entrega em **2026-10-30 09:00** (confirmado pelo humano).
- Ritmo: trabalho contínuo, sem pausa.
- O plano de 4 dias de [[contrato-processo-e-plano]] não cabe mais; precisa ser refeito para 24 horas.

## Dial e modelo de IA
- Dial: medio
- Modelo de IA: 

## Áreas sensíveis
(onde ler bugs e referências antes de mexer)
- Lances, carteira, liquidação, cancelamento e auditoria: regras em [[contrato-regras-de-negocio]], técnica em [[contrato-arquitetura]] e testes T-01 a T-06 em [[contrato-testes]].
- Rotas do backend: criar, alterar ou remover rota mexe na camada MCP; ler [[geral-decisao-2026-10-29-camada-mcp]].
- Componentes do frontend: ler [[registro-de-componentes]] e [[geral-decisao-2026-10-28-criacao-de-componentes]] antes de criar qualquer componente.
- Busca no cofre (Obsidian CLI): se as ferramentas `obsidian_*` faltarem ou a CLI falhar, ler [[bug-obsidian-cli-mcp-nao-carrega-2026-10-28]] antes de buscar nos `.md`.

## Mapa
- Roteiro: [[geral-plano]]
- Decisões: [[geral-decisao-2026-10-29-padrao-de-branches]], [[geral-decisao-2026-10-29-hospedagem]], [[geral-decisao-2026-10-29-camada-mcp]], [[geral-decisao-2026-10-28-testes-frontend-playwright]], [[geral-decisao-2026-10-28-stack-frontend]], [[geral-decisao-2026-10-28-stack-backend]], [[geral-decisao-2026-10-28-estrutura-frontend]], [[geral-decisao-2026-10-28-estrutura-backend]], [[geral-decisao-2026-10-28-criacao-de-componentes]]
- Bugs: [[bug-obsidian-cli-mcp-nao-carrega-2026-10-28]]
- Enunciado: [[enunciado-teste-tecnico]]
- Contrato: [[contrato-do-projeto]] (requisitos, regras, arquitetura proposta, plano e perguntas Q)
- Referências: [[registro-de-componentes]], [[manual-da-orquestra]], [[manual-do-cerebro]]

## Interpretação do agente
(separada dos fatos; marcar [a confirmar] quando for suposição)
- As versões foram registradas como informadas, sem checagem contra os registros do npm.
- Lances ao vivo (concorrência) e a verificação de adulteração do histórico passaram a constar como áreas sensíveis, com base no contrato; o contrato ainda está em validação ([[contrato-pontos-para-validar]]).
- Os itens `[PROPOSTO]` do contrato (AD-01 a AD-10, RN-10, fora do escopo, plano de 4 dias) ainda não são decisões do cofre.

### 🔗 Conexões
- Mapa: [[moc-orquestra]]
- Regras: [[manual-da-orquestra]], [[manual-do-cerebro]]
