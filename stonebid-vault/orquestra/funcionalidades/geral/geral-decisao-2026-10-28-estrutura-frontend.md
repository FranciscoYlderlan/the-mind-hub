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
    │   ├── App.tsx                  # Providers + RouterProvider
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
    │   │   │   └── $feature1Id.tsx
    │   │   └── feature2/
    │   │       ├── index.tsx
    │   │       └── $feature2Id.tsx
    │   └── routeTree.gen.ts         # Gerado automaticamente, não edite
    │
    ├── features/                    # Módulos por domínio de negócio
    │   ├── feature1/
    │   │   ├── api/                 # Chamadas HTTP + queryOptions/mutations
    │   │   ├── components/          # Feature1Form, Feature1List...
    │   │   ├── hooks/               # useFeature1, useCreateFeature1...
    │   │   ├── schemas/             # Validações zod
    │   │   ├── types/
    │   │   └── index.ts             # API pública da feature
    │   └── feature2/                # Mesma estrutura de feature1
    │
    ├── components/                  # Compartilhados entre features
    │   ├── ui/                      # [shadcn] Gerado pela CLI, não coloque componentes próprios aqui
    │   ├── layout/                  # Sidebar, Header, AppShell, AuthShell
    │   └── common/                  # DataTable, EmptyState, PageHeader, ConfirmDialog
    │
    ├── hooks/                       # [shadcn] Hooks globais (use-mobile, useDebounce)
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

- **Como funciona:**
  - **Fluxo de uma tela:** a URL casa com um arquivo em `routes/`. Esse arquivo valida os search params, roda o `beforeLoad` (guard) e o `loader` (prefetch) e renderiza o componente de tela, que vem da feature. A feature busca os dados pelo hook que usa as **mesmas queryOptions do loader**, então o dado já está em cache quando o componente monta.
  - **Direção das dependências:** `routes → features → components / hooks / lib`. A camada de baixo nunca importa da de cima. Features não importam de outras features; o que for compartilhado sobe para `components/`, `hooks/` ou `lib/`.
  - **Responsabilidade de cada camada:**
    - `routes/`: define URL, guards, loaders e search params. Sem lógica de negócio e sem componentes próprios.
    - `features/`: tudo de um domínio (API, UI, hooks, schemas, tipos). Só se acessa pelo `index.ts`.
    - `components/`: UI sem conhecimento de negócio. `ui/` é do shadcn, `layout/` monta o shell e `common/` guarda os componentes próprios reutilizáveis.
    - `lib/` e `config/`: infraestrutura (cliente HTTP, query client, env validado).
    - `app/`: junta providers e router. O `router.ts` injeta `queryClient` e `auth` no contexto, que é como guards e loaders os acessam.
  - **Estado:** dados do servidor no TanStack Query; estado de UI global no Zustand, só quando realmente necessário.
  - **Obrigatórios do shadcn:** `components.json`, `components/ui`, `lib/utils.ts` e `styles/globals.css`. A pasta `hooks/` é opcional, mas a CLI a usa por padrão.
- **Alteração:** 2026-10-28: rotas e features de exemplo (`users/`, `orders/`, `auth/`) trocadas por nomes genéricos (`feature1/`, `feature2/`), para não induzir inferência sobre o domínio do problema. 2026-10-28: pasta `src/test/` retirada, porque o frontend não terá testes unitários nem de componente. 2026-10-28: pasta `.github/workflows/` acrescentada (`ci.yml` e `cd.yml`), pelo CI/CD de [[geral-decisao-2026-10-28-stack-frontend]].
- **Motivo:** definição base do projeto informada pelo humano.
- **Consequências:**
  - Proibido: lógica de negócio em `routes/`, import entre features, import de camada de baixo para cima, componente próprio em `components/ui/`, editar `routeTree.gen.ts`.
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
