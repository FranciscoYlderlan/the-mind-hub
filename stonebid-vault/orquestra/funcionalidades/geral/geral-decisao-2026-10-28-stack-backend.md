---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-28
substitui: 
aliases: [Tecnologias do backend, Stack do stonebid-api, Backend stack]
---
# ✅ Stack do backend (stonebid-api)

- **Proposta (plano):** nenhuma. A definição veio direto do humano, como base do projeto, sem proposta da IA antes.
- **Decisão:** o repositório `stonebid-api` usa estas tecnologias e versões. Nenhuma versão é travada: vale a versão citada ou mais recente.

| Tecnologia | Versão | Observação |
|---|---|---|
| Node | latest | |
| Fastify | v5.12.7 ou mais recente | Framework web de alta performance e baixo overhead |
| TypeScript | — | TypeScript first, com build otimizado |
| Prisma | 7.10.1 ou mais recente da linha 7 ([[geral-decisao-2026-10-29-prisma-7]]) | ORM |
| PostgreSQL | latest | Banco de dados do Prisma |
| zod | 4.6 ou mais recente | Schemas, inferência de tipos e validação de env |
| Vitest | v5.0.5 ou mais recente | Testes unitários e E2E |
| ESLint | latest | Lint |
| Prettier | latest | Formatação |
| Docker + Docker Compose | — | Dockerfile e Compose prontos para uso |
| GitHub Actions | — | CI/CD integrado ao GitHub: lint, testes e build em todo push/PR; deploy automático depois do CI verde |

- **Alteração:** 2026-10-28: Jest e Biome retirados. Testes só com Vitest; lint e formatação com ESLint + Prettier; banco PostgreSQL; Node e PostgreSQL na versão mais recente. 2026-10-28: GitHub Actions ampliado de CI (teste e lint) para CI/CD integrado ao GitHub, igual ao frontend. 2026-10-29: destino do CD definido: Cloud Run com o banco no Cloud SQL, no GCP ([[geral-decisao-2026-10-29-hospedagem]]). Versões sem trava: Fastify v5.12.7, Prisma v8, zod 4.6 e Vitest v5.0.5 valem a citada ou mais recente.
- **Motivo:** definição base do projeto informada pelo humano. Vitest no lugar de Jest, pela integração com TypeScript.
- **Consequências:**
  - Todo dado que entra (body, params, query) e toda variável de ambiente é validado em tempo de execução com zod.
  - CI no GitHub Actions roda lint, testes (Vitest) e build em todo push/PR; PR com CI vermelho não entra.
  - CD no GitHub Actions faz o deploy automático do `stonebid-api` quando o CI passa na branch principal. Destino do deploy: Cloud Run, com o PostgreSQL no Cloud SQL (GCP), pela [[geral-decisao-2026-10-29-hospedagem]]; branch principal `main`, pela [[geral-decisao-2026-10-29-padrao-de-branches]].
  - Segredos do deploy (banco, segredo do HMAC etc.) ficam nos *secrets* do GitHub, nunca no repositório.
  - A aplicação sobe em contêiner (Dockerfile + Compose), o que prepara o deploy exigido pelo projeto.
  - Estrutura de pastas e princípios: [[geral-decisao-2026-10-28-estrutura-backend]].
  - Proibido: Jest e Biome no `stonebid-api`.
  - Ambiente local sobe o PostgreSQL pelo Docker Compose.
  - 2026-10-29: SDK oficial de MCP para TypeScript entra no backend, pela [[geral-decisao-2026-10-29-camada-mcp]].
  - Versões sem trava: no `package.json`, faixa que aceita a citada ou mais recente (não a versão exata).
  - Trocar framework, ORM, banco ou ferramenta de teste/lint exige nova decisão.

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[geral-plano]]
- Projeto: [[geral-contexto]]
- Relacionadas: [[geral-decisao-2026-10-28-stack-frontend]], [[geral-decisao-2026-10-29-camada-mcp]], [[geral-decisao-2026-10-29-hospedagem]]
- Regras: [[manual-da-orquestra]]
