---
tipo: contexto
funcionalidade: geral
status: em-construcao
etapa-atual: 3
criado: 2026-10-28
aliases: [Contexto do Stonebid, Visão geral do projeto, Project overview]
---
# 🧭 Stonebid — contexto geral

> [!tldr] Em uma linha
> Casa de leilões online com lances ao vivo, saldo simulado, comprovante compartilhável e histórico de lances auditável por qualquer pessoa.

## Objetivo e motivação
O Stonebid é uma casa de leilões online. O leiloeiro monta lotes a partir de itens de uma API pública, e licitantes disputam cada lote com lances ao vivo, usando um saldo simulado. Quem vence recebe um comprovante compartilhável por link. Qualquer pessoa, sem login, pode auditar o histórico de lances de um lote e verificar se ele foi adulterado. A aplicação precisa estar no ar (deploy).

Motivação: teste técnico Elite Dev da Verzel e aprendizado.

## Fatos que eu informei
(o agente preserva sem reinterpretar; fato substituído sai daqui e fica no diário)
- Dois repositórios no GitHub, `stonebid-web` (frontend) e `stonebid-api` (backend): https://github.com/FranciscoYlderlan/stonebid-api e https://github.com/FranciscoYlderlan/stonebid-web. Pasta do projeto no computador: `C:\Users\Ylderlan\Documents\Projetos\stonebid`.
- 2026-10-29: branches `main` (produção), `staging` e de trabalho `tipo/ID-descricao-curta` (ex.: `feat/RN-04-incremento-minimo`); boilerplate inicial direto na `main` → [[geral-decisao-2026-10-29-padrao-de-branches]].
- 2026-10-29: configuração do GCP aprovada (São Paulo, Cloud Run com 1 instância mínima, Cloud SQL `db-f1-micro`, Workload Identity Federation, alerta de US$ 50, staging como segundo serviço) → [[geral-decisao-2026-10-29-hospedagem]].
- 2026-10-29: Prisma com `@@map` em snake_case; testes E2E do backend em `test/e2e/` na raiz → [[geral-decisao-2026-10-28-estrutura-backend]].
- 2026-10-29: camada MCP e Playwright entram no contrato como mudança → [[contrato-do-projeto]].
- 2026-10-29: sempre que for etapa de programação em algum dos repositórios, o acesso é permitido para essa etapa (regra em `CLAUDE.md`, seção "Repositórios e acesso").
- Stack do frontend (nenhuma versão travada: a citada ou mais recente): React 19.3+, Vite 8.3.4+, Tailwind CSS v4.3+, TanStack Router v1+ (só rotas, não o framework), TanStack Query v5+, Zustand latest (só UI global; tema no `next-themes`), TypeScript 6, zod 4.6+, shadcn/ui (iniciado pelo guia oficial para Vite), Node 26.13.0+, npm, ESLint + Prettier, Playwright, CI/CD com GitHub Actions → [[geral-decisao-2026-10-28-stack-frontend]].
- Stack do backend (nenhuma versão travada: a citada ou mais recente): Fastify v5.12.7+, Prisma 7.10.1+ (linha 7, [[geral-decisao-2026-10-29-prisma-7]]) sobre PostgreSQL, zod 4.6+, Node e PostgreSQL latest, Vitest v5.0.5+ (sem Jest), ESLint + Prettier (sem Biome), Docker/Compose e CI/CD com GitHub Actions → [[geral-decisao-2026-10-28-stack-backend]].
- Frontend organizado por features (`routes → features → components/hooks/lib`), com nomes genéricos (`feature1`, `feature2`) na estrutura para não induzir o domínio → [[geral-decisao-2026-10-28-estrutura-frontend]].
- Backend em Clean Architecture (`domain/`, `application/use-cases/`, `infra/`, `env/`) → [[geral-decisao-2026-10-28-estrutura-backend]].
- Regra geral dos dois repositórios, desde a criação do projeto: nomes de arquivos e de entidades em **inglês** e **kebab-case**; identificadores no código em PascalCase e camelCase; parâmetro de rota sempre `$id.tsx` → [[geral-decisao-2026-10-28-estrutura-frontend]] e [[geral-decisao-2026-10-28-estrutura-backend]]. Exceção registrada: todo arquivo de hook se chama como o hook, em camelCase (`useDebounce.ts`), convenção do React; só o `use-mobile.ts` do shadcn fica como a CLI gera ([[geral-decisao-2026-10-28-estrutura-frontend]]).
- 2026-10-29: a camada MCP, o staging e o teste com Playwright por outro agente **continuam no plano**; a primeira etapa é justamente deixar o projeto no ar.
- Enunciado oficial do teste técnico (Elite Dev na Verzel) fornecido em 2026-10-29: fonte da verdade nº 1 → [[enunciado-teste-tecnico]].
- Componentes: registro consultado antes de criar, shadcn/ui primeiro, componentes pequenos e sem repetição → [[geral-decisao-2026-10-28-criacao-de-componentes]] e [[registro-de-componentes]].
- 2026-10-29: reuso de componentes é **padrão de todo o projeto**: compor antes de criar, sem copiar telas, extrair na segunda repetição; motivação: DRY, uma representação única de cada conhecimento; "reutilização de componentes bem arquitetados é princípio de clean code e de uma boa arquitetura" → [[geral-decisao-2026-10-28-criacao-de-componentes]].
- 2026-10-29: páginas públicas do RF-03 no layout `_public/`; a sala do lote tem duas rotas (`/lots/:id` só para ver e `/bidding/:id` com lance) que compõem o mesmo componente; `/` é a vitrine → [[geral-decisao-2026-10-28-estrutura-frontend]].
- Toda funcionalidade criada no frontend é testada com Playwright por uma **subthread de teste** (outro agente), que só testa e reporta bugs; sem testes unitários ou de componente no frontend → [[geral-decisao-2026-10-28-testes-frontend-playwright]].
- Contrato do projeto v0.3 (2026-10-29; histórico de mudanças em [[contrato-do-projeto-mudancas]]), escrito por mim com a IA, com as perguntas da seção 14 ainda em validação (Q-06, Q-07, Q-09, Q-10, Q-13 e Q-14 já respondidas): requisitos, regras de negócio, arquitetura proposta, riscos, testes, plano e perguntas → [[contrato-do-projeto]].
- Do contrato (itens `[DECIDIDO]`): **todos os 5 opcionais** serão feitos; deploy obrigatório; desenvolvimento com IA permitido; sou júnior e aprender é objetivo do projeto → [[contrato-visao-escopo-e-papeis]].
- 2026-10-29 (09:06): prazo real contado a partir de agora, hoje até **2026-10-30 16:00** (o enunciado fala em 7 dias; a cronologia do prazo está em [[diario-2026-10-29]] e [[geral-decisao-2026-10-30-prazo-16h]]). Oficialmente estou no **terceiro dia**: nos três primeiros dias não avancei muito além dos requisitos e da arquitetura. Vou trabalhar sem pausa.
- 2026-10-29 (12:28): aprovada a regra dos testes: o teste só sai do escopo junto com o requisito que prova; T-01 a T-09 e T-10a ficam sempre → [[geral-decisao-2026-10-29-testes-no-escopo]].
- 2026-10-29 (13:22): aprovada a solução do comprovante e da auditoria: hash guardado no lance, cabeça da cadeia com selo no lote e comprovante como fotografia selada da liquidação → [[geral-decisao-2026-10-29-comprovante-e-hash]].
- 2026-10-29 (13:31): aprovada a correção do cancelamento ao vivo, "vamos deixar os dois casos": lote ao vivo vai para CANCELADO sem lances; com lances, só com o `[OPC-2]` → [[geral-decisao-2026-10-29-cancelamento-ao-vivo]].
- 2026-10-29 (14:07): roteiro aprovado em 8 etapas, uma por incremento → [[geral-decisao-2026-10-29-roteiro]].
- 2026-10-29 (22:13): modo de implementação adotado como padrão (container → GitHub → Actions → GCP/Vercel; consoles e testes no ar pelo agente no Chrome) → [[geral-decisao-2026-10-29-modo-de-implementacao]].
- Camada MCP no backend para expor as rotas e testar o fluxo pela Claude; sempre que uma feature e uma rota forem criadas, a MCP é atualizada → [[geral-decisao-2026-10-29-camada-mcp]].
- 2026-10-29: hospedagem: backend e banco no **GCP**, frontend na **Vercel**, os dois repositórios no GitHub com CI/CD validando a integração. Custo zero: a aplicação fica no ar no máximo 7 dias, é avaliada em menos de 1 hora e depois é fechada → [[geral-decisao-2026-10-29-hospedagem]].

## O que já foi feito
- 2026-10-28: cofre montado com a estrutura `orquestra/` e alinhado ao processo das etapas vitais ([[diario-2026-10-28]]).
- 2026-10-28: stack, organização do frontend e do backend e regras de componentes registradas como decisões; registro de componentes criado ([[diario-2026-10-28]]).
- 2026-10-28: Obsidian CLI disponível nas sessões pelo servidor MCP `obsidian-cli`; causa da falha registrada em [[bug-obsidian-cli-mcp-nao-carrega-2026-10-28]].
- 2026-10-29: camada MCP do backend registrada como decisão ([[diario-2026-10-29]]).
- 2026-10-29: enunciado do teste técnico guardado e mapeado contra o contrato ([[enunciado-teste-tecnico]]); regra de nomes em inglês + kebab-case nas decisões de estrutura.
- 2026-10-29: padronização levada para a porta de entrada: seção Padronização e bloco `padroes` no `CLAUDE.md` (grafia `Stonebid`, enunciado citado como E1 a E6, exceção dos hooks, limite de 2073 palavras por nota), checados pelo `cofre.py verificar`; notas corrigidas ([[diario-2026-10-29]]).
- 2026-10-29: contrato do projeto v0.2 registrado em `referencias/`, uma nota por seção, a partir de [[contrato-do-projeto]] ([[diario-2026-10-29]]).
- 2026-10-29: hospedagem decidida (GCP + Vercel, CI/CD pelo GitHub) e propagada nas decisões de stack, na camada MCP e no contrato ([[geral-decisao-2026-10-29-hospedagem]]).
- 2026-10-29: links dos repositórios, pasta local e regra de acesso nas etapas de programação registrados ([[diario-2026-10-29]]).
- 2026-10-29: [[contrato-do-projeto]] atualizado para a v0.3 com o cenário atual (M-01 a M-10).
- 2026-10-29: ambiguidade dos testes T-01 a T-11 resolvida (M-11); tabela de mudanças dividida do hub para [[contrato-do-projeto-mudancas]] pelo limite de palavras.
- 2026-10-29: divergência sobre o que o comprovante e o lance guardam resolvida (M-12); furo do truncamento sem selo corrigido na proposta da 8.1 ([[geral-decisao-2026-10-29-comprovante-e-hash]]).
- 2026-10-29: tabela 5.1 corrigida para o cancelamento de lote ao vivo sem lances (M-13, [[geral-decisao-2026-10-29-cancelamento-ao-vivo]]).
- 2026-10-29: rotas públicas do RF-03 (layout `_public/`) e reuso de componentes como padrão do projeto registrados nas decisões do frontend ([[diario-2026-10-29]]).
- 2026-10-29: bug de processo corrigido: mudança de estado passa por varredura de impacto, e as notas `contrato-*` ficam só no texto vigente ([[bug-estado-anterior-preservado-apos-mudanca-2026-10-29]]).
- 2026-10-29: pendências respondidas: branches, configuração do GCP, entrega, dial, motivação, `@@map`, testes E2E e mudança do contrato ([[diario-2026-10-29]]).
- 2026-10-29: roteiro aprovado ([[geral-decisao-2026-10-29-roteiro]]); etapa 2 (esqueleto no ar) em construção.
- 2026-10-29: `stonebid-api` e `stonebid-web` montados e publicados na `main` com CI verde ([[esqueleto-contexto]]).
- 2026-10-29 22:20: etapa 2 concluída (aplicação no ar com os 3 usuários de teste); etapa 3 (carteira e lotes) em construção ([[carteira-e-lotes-contexto]]).

## Tempo disponível
- De 2026-10-29 09:06 até a entrega, em **2026-10-30 16:00**, estendida pelo humano em 2026-10-30 06:16 ([[geral-decisao-2026-10-30-prazo-16h]]).
- Ritmo: trabalho contínuo, sem pausa.
- O plano com horários até a entrega ainda não foi feito: sai dos incrementos de [[contrato-processo-e-plano]], com a linha de corte aplicada.

## Dial e modelo de IA
- Dial: medio
- Modelo de IA: Claude Opus 5.5 (`claude-opus-5-5`) [a confirmar]

## Áreas sensíveis
(onde ler bugs e referências antes de mexer)
- Lances, carteira, liquidação, cancelamento e auditoria: regras em [[contrato-regras-de-negocio]], técnica em [[contrato-arquitetura]] (com a M-12: [[geral-decisao-2026-10-29-comprovante-e-hash]]) e testes em [[contrato-testes]] (o teste só sai junto com o requisito: [[geral-decisao-2026-10-29-testes-no-escopo]]).
- Rotas do backend: criar, alterar ou remover rota mexe na camada MCP; ler [[geral-decisao-2026-10-29-camada-mcp]].
- Componentes do frontend: ler [[registro-de-componentes]] e [[geral-decisao-2026-10-28-criacao-de-componentes]] antes de criar qualquer componente.
- Busca no cofre (Obsidian CLI): se as ferramentas `obsidian_*` faltarem ou a CLI falhar, ler [[bug-obsidian-cli-mcp-nao-carrega-2026-10-28]] antes de buscar nos `.md`.

## Mapa
- Roteiro: [[geral-plano]]
- Funcionalidades: [[carteira-e-lotes-contexto]], [[esqueleto-contexto]]
- Decisões: [[geral-decisao-2026-10-30-prazo-16h]], [[geral-decisao-2026-10-30-obra-unica-por-lote]], [[geral-decisao-2026-10-30-cache-e-limite-da-miniatura]], [[geral-decisao-2026-10-29-sessao-jwt-no-cabecalho]], [[geral-decisao-2026-10-29-prisma-7]], [[geral-decisao-2026-10-29-typescript-6-no-web]], [[geral-decisao-2026-10-29-next-themes-para-o-tema]], [[geral-decisao-2026-10-29-vercel-sem-deploy-automatico]], [[geral-decisao-2026-10-29-alias-fixo-do-staging]], [[geral-decisao-2026-10-29-api-de-itens]], [[geral-decisao-2026-10-29-imagem-do-lote-no-banco]], [[geral-decisao-2026-10-29-lance-inicial-e-valor-minimo]], [[geral-decisao-2026-10-29-inicio-e-duracao-do-lote]], [[geral-decisao-2026-10-29-limites-do-deposito]], [[geral-decisao-2026-10-29-edicao-de-lote-fora]], [[geral-decisao-2026-10-29-seed-com-imagem-fixa]], [[geral-decisao-2026-10-29-seed-tambem-em-producao]], [[geral-decisao-2026-10-29-busca-so-em-dominio-publico]], [[geral-decisao-2026-10-29-codigo-do-teto-do-deposito]], [[geral-decisao-2026-10-29-sequencia-no-extrato]], [[geral-decisao-2026-10-29-miniatura-da-busca-pela-api]], [[geral-decisao-2026-10-29-node-26]], [[geral-decisao-2026-10-29-modo-de-implementacao]], [[geral-decisao-2026-10-29-roteiro]], [[geral-decisao-2026-10-29-cancelamento-ao-vivo]], [[geral-decisao-2026-10-29-comprovante-e-hash]], [[geral-decisao-2026-10-29-testes-no-escopo]], [[geral-decisao-2026-10-29-padrao-de-branches]], [[geral-decisao-2026-10-29-hospedagem]], [[geral-decisao-2026-10-29-camada-mcp]], [[geral-decisao-2026-10-28-testes-frontend-playwright]], [[geral-decisao-2026-10-28-stack-frontend]], [[geral-decisao-2026-10-28-stack-backend]], [[geral-decisao-2026-10-28-estrutura-frontend]], [[geral-decisao-2026-10-28-estrutura-backend]], [[geral-decisao-2026-10-28-criacao-de-componentes]]
- Bugs: [[bug-obsidian-cli-mcp-nao-carrega-2026-10-28]], [[bug-estado-anterior-preservado-apos-mudanca-2026-10-29]]
- Enunciado: [[enunciado-teste-tecnico]]
- Contrato: [[contrato-do-projeto]] (requisitos, regras, arquitetura proposta, plano e perguntas Q)
- Referências: [[registro-de-componentes]], [[manual-da-orquestra]], [[manual-do-cerebro]]

## Interpretação do agente
(separada dos fatos; marcar [a confirmar] quando for suposição)
- As versões foram registradas como informadas, sem checagem contra os registros do npm.
- Lances ao vivo (concorrência) e a verificação de adulteração do histórico passaram a constar como áreas sensíveis, com base no contrato; o contrato ainda está em validação ([[contrato-pontos-para-validar]]).
- Os itens `[PROPOSTO]` do contrato (AD-01 a AD-10, RN-10, fora do escopo, incrementos do plano) ainda não são decisões do cofre.

### 🔗 Conexões
- Mapa: [[moc-orquestra]]
- Regras: [[manual-da-orquestra]], [[manual-do-cerebro]]
