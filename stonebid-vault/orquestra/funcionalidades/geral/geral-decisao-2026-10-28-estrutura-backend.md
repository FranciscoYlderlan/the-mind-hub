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
src/
├── domain/           # Regras de negócio (Entities, interfaces de Repositories)
├── infra/            # Preocupações externas (frameworks, implementações de banco, HTTP)
│   ├── http/         # Controllers, Routes e Middlewares
│   ├── repositories/ # Implementações concretas dos repositórios
│   └── factories/    # Factories de injeção de dependência
├── env/              # Configuração e validação das variáveis de ambiente
├── types/            # Tipos globais e de terceiros
├── app.ts            # Inicialização da aplicação e registro de plugins
└── server.ts         # Entry point do servidor HTTP
```

- **Princípios:**
  - **Clean Architecture:** separação entre regra de negócio (`domain/`) e infraestrutura (`infra/`).
  - **Inversão de dependência:** repositórios são interfaces no `domain/`; a implementação concreta mora em `infra/repositories/`, o que permite trocar o provedor de banco.
  - **Validação de schema:** todo dado de entrada e toda variável de ambiente é validado em tempo de execução com zod.
  - **Tratamento de erro funcional:** respostas de erro consistentes e gestão de erro centralizada.
  - **Ferramentas:** ESLint + Prettier para lint e formatação; Vitest no lugar de Jest (integração com TypeScript).
- **Alteração:** 2026-10-28: Biome trocado por ESLint + Prettier, alinhado com [[geral-decisao-2026-10-28-stack-backend]].
- **Motivo:** escalabilidade e manutenção, pela separação de responsabilidades (texto do humano).
- **Consequências:**
  - `domain/` não importa nada de `infra/`, Fastify ou Prisma.
  - Controllers não falam com o Prisma direto: passam pelo repositório, montado nas `factories/`.
  - Env lido só por `env/`, nunca `process.env` solto no código.
  - Implementação concreta dos repositórios usa Prisma sobre PostgreSQL.
  - Stack e ferramentas: [[geral-decisao-2026-10-28-stack-backend]].
- **Em aberto:**
  - A árvore não mostra onde ficam os casos de uso (use cases/services) nem os testes E2E [a confirmar].

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[geral-plano]]
- Projeto: [[geral-contexto]]
- Relacionadas: [[geral-decisao-2026-10-28-stack-backend]]
- Regras: [[manual-da-orquestra]]
