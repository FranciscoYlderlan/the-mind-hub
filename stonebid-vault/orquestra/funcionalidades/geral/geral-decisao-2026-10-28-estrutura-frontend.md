---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-28
substitui: 
aliases: [Organização do frontend, Pastas do stonebid-web, Frontend folder structure, Arquitetura do frontend]
---
# ✅ Organização do frontend (stonebid-web)

- **Proposta (plano):** nenhuma. A definição veio direto do humano, como base do projeto.
- **Decisão:** o `stonebid-web` segue esta estrutura, organizada por domínio (feature-based):

```
frontend/
├── .github/
│   └── workflows/
│       ├── ci.yml                   # ESLint, Prettier (checagem), tipos e build em push/PR
│       └── cd.yml                   # Deploy automático depois do CI verde na branch principal
├── public/                          # Estáticos servidos como estão (favicon, robots.txt)
├── .env.example                     # Modelo das variáveis de ambiente
├── components.json                  # [shadcn] Config da CLI (aliases e caminhos)
├── index.html
├── package.json
├── tsconfig.json                    # Alias "@/*" → "src/*"
├── vite.config.ts                   # Plugin do TanStack Router + autoCodeSplitting
│
└── src/
    ├── main.tsx                     # Entry point: monta o <App />
    │
    ├── app/                         # Composição da aplicação
    │   ├── app.tsx                  # Providers + RouterProvider
    │   ├── router.ts                # createRouter + contexto (queryClient, auth) + registro de tipos
    │   └── providers/               # Theme, QueryClient, Auth, Toaster
    │
    ├── routes/                      # TanStack Router (file-based), só a "cola"
    │   ├── __root.tsx               # Layout raiz, 404 e error boundary
    │   ├── _auth/                   # Layout sem URL: rotas públicas
    │   │   ├── route.tsx            # Redireciona se já estiver logado
    │   │   ├── login.tsx
    │   │   └── register.tsx
    │   ├── _app/                    # Layout sem URL: rotas protegidas
    │   │   ├── route.tsx            # Guard (beforeLoad) + shell com sidebar
    │   │   ├── index.tsx            # Tela inicial
    │   │   ├── feature1/
    │   │   │   ├── index.tsx
    │   │   │   └── $id.tsx
    │   │   └── feature2/
    │   │       ├── index.tsx
    │   │       └── $id.tsx
    │   └── routeTree.gen.ts         # Gerado pelo plugin do TanStack Router, nunca edite à mão
    │
    ├── features/                    # Módulos por domínio de negócio
    │   ├── feature1/
    │   │   ├── api/                 # Chamadas HTTP + queryOptions/mutations
    │   │   ├── components/          # feature1-form.tsx, feature1-list.tsx...
    │   │   ├── hooks/               # useFeature1.ts, useCreateFeature1.ts...
    │   │   ├── schemas/             # Validações zod
    │   │   ├── types/
    │   │   └── index.ts             # API pública da feature
    │   └── feature2/                # Mesma estrutura de feature1
    │
    ├── components/                  # Compartilhados entre features
    │   ├── ui/                      # [shadcn] Só pela CLI (npx shadcn@latest add), nunca escrito à mão
    │   ├── layout/                  # Sidebar, Header, AppShell, AuthShell
    │   └── common/                  # DataTable, EmptyState, PageHeader, ConfirmDialog
    │
    ├── hooks/                       # [shadcn] Hooks globais (use-mobile.ts da CLI, useDebounce.ts)
    │
    ├── lib/                         # [shadcn] Utilitários e config de bibliotecas
    │   ├── utils.ts                 # [shadcn] Função cn()
    │   ├── api-client.ts            # Instância HTTP, interceptors, tratamento de erro
    │   └── query-client.ts          # Configuração do TanStack Query
    │
    ├── config/                      # Env validado (zod), constantes, feature flags
    ├── stores/                      # Zustand: só estado de UI global (sidebar, preferências)
    ├── types/                       # Tipos globais e declarações de terceiros
    ├── assets/                      # Imagens, fontes e ícones importados no código
    └── styles/
        └── globals.css              # [shadcn] Variáveis CSS do tema + Tailwind
```

- **Nomes (humano, 2026-10-29):** regra geral dos dois repositórios, `stonebid-web` e `stonebid-api`: nomes de arquivos e de entidades em **inglês** e **kebab-case** (ex.: `auction-lot.ts`, `place-bid.ts`, `bid-history.tsx`). Vale desde a criação do projeto.
- **Como funciona:**
  - **Fluxo de uma tela:** a URL casa com um arquivo em `routes/`. Esse arquivo valida os search params, roda o `beforeLoad` (guard) e o `loader` (prefetch) e renderiza o componente de tela, que vem da feature. A feature busca os dados pelo hook que usa as **mesmas queryOptions do loader**, então o dado já está em cache quando o componente monta.
  - **Direção das dependências:** `routes → features → components / hooks / lib`. A camada de baixo nunca importa da de cima. Features não importam de outras features; o que for compartilhado sobe para `components/`, `hooks/` ou `lib/`.
  - **Responsabilidade de cada camada:**
    - `routes/`: define URL, guards, loaders e search params. Sem lógica de negócio e sem componentes próprios.
    - `features/`: tudo de um domínio (API, UI, hooks, schemas, tipos). Só se acessa pelo `index.ts`.
    - `components/`: UI sem conhecimento de negócio. `ui/` é do shadcn, `layout/` monta o shell e `common/` guarda os componentes próprios reutilizáveis.
    - `lib/` e `config/`: infraestrutura (cliente HTTP, query client, env validado).
    - `app/`: junta providers e router. O `router.ts` injeta `queryClient` e `auth` no contexto, que é como guards e loaders os acessam.
  - **Árvore de rotas gerada:** o `routeTree.gen.ts` é escrito pelo plugin do TanStack Router no Vite. Sempre que o servidor de desenvolvimento inicia, ou quando um arquivo é criado, renomeado ou apagado em `routes/`, o plugin capta a mudança e regenera o arquivo. Rota nova = arquivo novo em `routes/`; nunca registrar rota editando o `.gen`.
  - **Estado:** dados do servidor no TanStack Query; estado de UI global no Zustand, só quando realmente necessário.
  - **Obrigatórios do shadcn:** `components.json`, `components/ui`, `lib/utils.ts` e `styles/globals.css`. A pasta `hooks/` é opcional, mas a CLI a usa por padrão.
- **Alteração:** 2026-10-28: rotas e features de exemplo (`users/`, `orders/`, `auth/`) trocadas por nomes genéricos (`feature1/`, `feature2/`), para não induzir inferência sobre o domínio do problema. 2026-10-28: pasta `src/test/` retirada, porque o frontend não terá testes unitários nem de componente. 2026-10-28: pasta `.github/workflows/` acrescentada (`ci.yml` e `cd.yml`), pelo CI/CD de [[geral-decisao-2026-10-28-stack-frontend]]. 2026-10-29: explicado por que o `routeTree.gen.ts` não se edita (o plugin o regenera ao iniciar o servidor e a cada mudança em `routes/`) e que `components/ui/` só recebe componentes instalados pela CLI do shadcn (humano). 2026-10-29: regra de nomes do humano (inglês + kebab-case em arquivos e entidades, nos dois repositórios); na árvore, `App.tsx` virou `app.tsx`, `$feature1Id.tsx` virou `$id.tsx` (parâmetro de rota sempre `$id`, escolha do humano pela opção mais simples) e os exemplos de componentes e hooks passaram a mostrar o nome do arquivo. 2026-10-29: exceção dos arquivos de hook registrada nas Consequências: todo arquivo de hook em camelCase com o nome do hook (`useDebounce.ts`, `useFeature1.ts`), menos o `use-mobile.ts` gerado pelo shadcn; árvore ajustada (humano).
- **Motivo:** definição base do projeto informada pelo humano.
- **Consequências:**
  - Proibido: lógica de negócio em `routes/`, import entre features, import de camada de baixo para cima, componente próprio em `components/ui/`, componente do shadcn escrito à mão, editar `routeTree.gen.ts` (qualquer edição manual é sobrescrita na próxima geração).
  - Proibido: arquivo ou pasta fora de inglês + kebab-case (inclui componentes: `bid-panel.tsx`, nunca `BidPanel.tsx`). Exceções: arquivos gerados ou exigidos por ferramenta (`routeTree.gen.ts`, `__root.tsx`, `components/ui/` do shadcn, `vite.config.ts`).
  - Exceção de convenção, **arquivos de hook** (humano, 2026-10-29): o arquivo tem o mesmo nome do hook, em camelCase com prefixo `use`: `useDebounce.ts` exporta `useDebounce`, `useCreateFeature1.ts` exporta `useCreateFeature1`. Vale para **todo** arquivo de hook do projeto, global (`src/hooks/`) ou de feature (`features/<feature>/hooks/`). É a convenção do React: as Rules of Hooks e o lint `react-hooks` reconhecem um hook pelo prefixo `use`. Única exceção: `use-mobile.ts`, gerado pela CLI do shadcn e importado pelos componentes dela com esse nome. A exceção também está na Padronização do `CLAUDE.md`.
  - Identificadores dentro do código seguem a convenção do TypeScript: PascalCase para componentes, classes e entidades (`AuctionLot`, `BidPanel`) e camelCase para funções e variáveis (`placeBid`). O kebab-case vale só para nomes de arquivos e pastas (humano, 2026-10-29).
  - Parâmetro de rota no arquivo é sempre `$id.tsx`, lido como `params.id`.
  - Toda feature expõe só o `index.ts`; nada de importar arquivos internos de outra feature.
  - Criação de componentes segue [[geral-decisao-2026-10-28-criacao-de-componentes]].
  - `feature1/` e `feature2/` são **marcadores da estrutura**, não features do projeto. Agente não deduz domínio a partir deles: as features reais nascem cada uma com o próprio `<func>-contexto`.
  - CI e CD ficam em arquivos separados em `.github/workflows/`: o `cd.yml` só roda depois do CI verde na branch principal.
  - Toda feature criada passa pelo teste com Playwright de outro agente: [[geral-decisao-2026-10-28-testes-frontend-playwright]].


### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[geral-plano]]
- Projeto: [[geral-contexto]]
- Relacionadas: [[geral-decisao-2026-10-28-stack-frontend]], [[geral-decisao-2026-10-28-criacao-de-componentes]], [[geral-decisao-2026-10-28-testes-frontend-playwright]]
- Regras: [[manual-da-orquestra]]
