---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-28
substitui: 
aliases: [Organização do backend, Pastas do stonebid-api, Clean Architecture do backend, Backend folder structure]
---
# ✅ Organização do backend (stonebid-api)

- **Proposta (plano):** nenhuma. A definição veio direto do humano, como base do projeto.
- **Decisão:** o `stonebid-api` segue Clean Architecture com estrutura orientada a domínio:

```
.github/
└── workflows/
    ├── ci.yml        # ESLint, Prettier, Vitest e build em push/PR
    └── cd.yml        # Deploy automático depois do CI verde na branch principal
prisma/               # schema.prisma, migrations e seed
test/
└── e2e/              # Testes E2E do backend (Vitest), fora do src/
Dockerfile
docker-compose.yml    # API + PostgreSQL no ambiente local
.env.example          # Modelo das variáveis de ambiente, sem valores reais
src/
├── domain/           # Regras de negócio (Entities, interfaces de Repositories)
├── application/      # Camada de aplicação
│   └── use-cases/    # Casos de uso: orquestram o domain pelas interfaces dos repositórios
├── infra/            # Preocupações externas (frameworks, implementações de banco, HTTP)
│   ├── http/         # Controllers, Routes e Middlewares
│   ├── mcp/          # Camada MCP: uma tool por rota, atualizada a cada feature/rota nova
│   ├── repositories/ # Implementações concretas dos repositórios
│   └── factories/    # Factories de injeção de dependência
├── env/              # Configuração e validação das variáveis de ambiente
├── types/            # Tipos globais e de terceiros
├── app.ts            # Inicialização da aplicação e registro de plugins
└── server.ts         # Entry point do servidor HTTP
```

- **Nomes (humano, 2026-10-29):** regra geral dos dois repositórios, `stonebid-web` e `stonebid-api`: nomes de arquivos e de entidades em **inglês** e **kebab-case** (ex.: `auction-lot.ts`, `place-bid.ts`, `bid-history.tsx`). Vale desde a criação do projeto.
- **Princípios:**
  - **Clean Architecture:** separação entre regra de negócio (`domain/`) e infraestrutura (`infra/`).
  - **Casos de uso em `application/use-cases/` (humano, 2026-10-29):** a camada de aplicação fica entre `domain/` e `infra/`. Direção das dependências: `infra → application → domain`.
  - **Inversão de dependência:** repositórios são interfaces no `domain/`; a implementação concreta mora em `infra/repositories/`, o que permite trocar o provedor de banco.
  - **Validação de schema:** todo dado de entrada e toda variável de ambiente é validado em tempo de execução com zod.
  - **Tratamento de erro funcional:** respostas de erro consistentes e gestão de erro centralizada.
  - **Ferramentas:** ESLint + Prettier para lint e formatação; Vitest no lugar de Jest (integração com TypeScript).
- **Alteração:** 2026-10-28: Biome trocado por ESLint + Prettier, alinhado com [[geral-decisao-2026-10-28-stack-backend]]. 2026-10-28: raiz do repositório acrescentada à árvore: `.github/workflows/` (`ci.yml` e `cd.yml`, pelo CI/CD), `prisma/`, `Dockerfile`, `docker-compose.yml` e `.env.example`. 2026-10-29: camada `application/useCases/` acrescentada (respondendo o "Em aberto" dos casos de uso). 2026-10-29: pasta `infra/mcp/` acrescentada, pela [[geral-decisao-2026-10-29-camada-mcp]]. 2026-10-29: regra de nomes do humano (inglês + kebab-case em arquivos e entidades, nos dois repositórios); a pasta `useCases/` virou `use-cases/`. 2026-10-29: `test/e2e/` acrescentada à árvore e `@@map` em snake_case (respostas do humano ao "Em aberto").
- **Motivo:** escalabilidade e manutenção, pela separação de responsabilidades (texto do humano).
- **Consequências:**
  - `domain/` não importa nada de `application/`, `infra/`, Fastify ou Prisma; `application/` não importa nada de `infra/`.
  - Controllers chamam casos de uso de `application/use-cases/`, montados nas `factories/`.
  - Controllers não falam com o Prisma direto: passam pelo repositório, montado nas `factories/`.
  - Proibido: arquivo, pasta ou entidade fora de inglês + kebab-case (ex.: `domain/entities/auction-lot.ts`, `application/use-cases/place-bid.ts`, `infra/http/controllers/place-bid-controller.ts`). Exceções: arquivos exigidos por ferramenta (`schema.prisma`, `Dockerfile`, `docker-compose.yml`).
  - Identificadores dentro do código seguem a convenção do TypeScript: PascalCase para componentes, classes e entidades (`AuctionLot`, `BidPanel`) e camelCase para funções e variáveis (`placeBid`). O kebab-case vale só para nomes de arquivos e pastas (humano, 2026-10-29).
  - Env lido só por `env/`, nunca `process.env` solto no código.
  - Implementação concreta dos repositórios usa Prisma sobre PostgreSQL.
  - CI e CD ficam em arquivos separados em `.github/workflows/`: o `cd.yml` só roda depois do CI verde na branch principal.
  - Schema, migrations e seed do Prisma ficam em `prisma/`, fora do `src/`; o acesso ao banco no código continua só em `infra/repositories/`.
  - Stack e ferramentas: [[geral-decisao-2026-10-28-stack-backend]].
  - Feature ou rota nova só está pronta com a tool correspondente em `infra/mcp/`: [[geral-decisao-2026-10-29-camada-mcp]].
- **Resolvido (humano, 2026-10-29):**
  - Testes E2E do backend em `test/e2e/`, na raiz do repositório, fora do `src/`.
  - No Prisma, models em PascalCase (`AuctionLot`) com tabelas e colunas mapeadas em **snake_case** por `@@map`/`@map` (ex.: `@@map("auction_lots")`).

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[geral-plano]]
- Projeto: [[geral-contexto]]
- Relacionadas: [[geral-decisao-2026-10-28-stack-backend]], [[geral-decisao-2026-10-29-camada-mcp]]
- Regras: [[manual-da-orquestra]]
