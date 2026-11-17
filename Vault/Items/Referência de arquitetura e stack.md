---
aliases: [Arquitetura de partida, Stack de referência, Reference architecture and stack, Que arquitetura eu proponho num projeto novo]
tags: [estudos/programacao]
tipo: referencia
status: em-uso
criado: 2026-11-16
origem: Decisões de estrutura, stack, criação de componentes e testes do stonebid-vault (2026-10-28 e 2026-10-29), generalizadas pela regra S25 do pacote aprovado em 2026-11-16
---
# 🏛️ Referência de arquitetura e stack

> [!tldr] Em uma linha
> A arquitetura e as tecnologias de partida (frontend e backend) que o agente propõe ao criar um cofre de projeto de software, para o humano ajustar em vez de partir do zero.

É a **planta-modelo da construtora**: o cliente não desenha a casa do nada; recebe uma planta testada e risca o que quer mudar. Regra que manda propor: S25 do [[Padrão de projeto de software]]; quando, no passo a passo de [[Criar um novo cofre]].

Na raiz do repositório de código fica `docs/contrato/`, o [[Contrato funcional]] que frontend e backend seguem (Q01 do [[Manual da Orquestra - Perfil projeto prático|perfil]]):

```
docs/contrato/   README.md (índice), 00-requisitos a 08-criterios-de-aceite, mudancas.md
```

Versões: a mais recente estável no momento da proposta, sem trava (S16). Nada aqui é decisão: a proposta vai para a seção "Proposta de arquitetura e stack" do `geral-plano` do projeto novo e vira decisão só com o aval do humano. Dentro do cofre de projeto, esta nota é citada como texto "Referência de arquitetura e stack (no Vault)", nunca como wikilink.

---

## 1. 🖥️ Frontend

| Peça | Proposta | Observação |
|---|---|---|
| Base | React + Vite + TypeScript | Projeto iniciado pelo guia oficial do shadcn/ui para Vite |
| Estilo e UI | Tailwind CSS + shadcn/ui | Componentes do shadcn só pela CLI (`npx shadcn@latest add`) |
| Rotas | TanStack Router (file-based) | Só a gestão de rotas, sem framework full-stack |
| Dados do servidor | TanStack Query | O loader da rota e o hook da tela usam as mesmas `queryOptions` |
| Estado de UI global | Zustand | Só quando precisa; nunca guarda dado da API |
| Validação | zod | Todo campo de entrada com schema tirado do ENT do contrato e mensagem por violação (S26); também search params e env |
| Qualidade | ESLint + Prettier + checagem de tipos | No CI, em todo push e PR |
| Teste | Verificador de fluxo principal e adversarial, agentes com Playwright | Ao final de cada funcionalidade, executam os AC de `docs/contrato/`; sem suíte de E2E de interface no repositório; quem implementou não testa |

```
src/
├── app/          providers e router (injeta queryClient e auth no contexto)
├── routes/       só a "cola": URL, guards, loaders, search params; árvore gerada nunca editada
├── features/<f>/ api, components, hooks, schemas, types; acesso só pelo index.ts
├── components/   ui/ (só shadcn), layout/ (shells), common/ (próprios reutilizáveis)
├── hooks/  lib/  config/ (env validado)  stores/  types/  assets/  styles/
```

- **Direção:** `routes → features → components / hooks / lib`; uma feature não importa outra (S13).
- **Layouts sem URL, uma regra cada:** público (abre para todos, nunca redireciona), só para quem não entrou, só para quem entrou (guard com `?redirect` validado como caminho interno).
- **Mesma tela em dois níveis de acesso:** duas rotas, um componente, a parte que muda por slot (S10).

## 2. ⚙️ Backend

| Peça | Proposta | Observação |
|---|---|---|
| Runtime e framework | Node + Fastify + TypeScript | |
| Banco e ORM | PostgreSQL + Prisma | Models em PascalCase, tabelas e colunas em snake_case por `@map` |
| Validação | zod | Toda entrada e toda variável de ambiente |
| Teste | Vitest | Unitário e E2E (`test/e2e/`, fora do `src/`); ao final de cada funcionalidade, os mesmos dois agentes executam os AC pela API (HTTP ou camada MCP, S23) |
| Qualidade | ESLint + Prettier | |
| Ambiente | Docker + Docker Compose | API e banco locais |
| CI/CD | GitHub Actions | `ci.yml` e `cd.yml` separados (S04, só com deploy) |

```
src/
├── domain/                regras de negócio: entidades e interfaces dos repositórios
├── application/use-cases/ casos de uso, orquestram o domain
├── infra/                 http/ (controllers, rotas), repositories/, factories/, mcp/ (opcional, S23)
├── env/                   único leitor do env
├── app.ts  server.ts
prisma/  test/e2e/  Dockerfile  docker-compose.yml  .env.example
```

- **Clean Architecture:** `infra → application → domain`; o domain não conhece framework nem ORM.
- **Inversão de dependência:** repositório é interface no domain, implementação em `infra/repositories/`; controller nunca fala com o ORM direto.
- **Erro centralizado** com código próprio (S15).

> [!tip] Quando abrir esta nota
> Ao criar um cofre de projeto prático de software, para montar a proposta de arquitetura e stack em linguagem leiga antes do aval.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** Partida pronta, não decisão: o humano ajusta e o aval vira as decisões de estrutura e stack do [[Manual da Orquestra - Perfil projeto prático|projeto]].
* **Ponto 2:** Camadas com uma direção só, nos dois lados, validação com zod em toda borda e o contrato em `docs/contrato/` como fonte das regras da tela.
* **Ponto 3:** Limite: foi tirada de um projeto web com prazo curto; projeto de outro tipo (mobile, CLI, dados) pede outra proposta.

### 🔗 Conexões
- Mapa: [[MOC Programação]]
- Relacionadas: [[Padrão de projeto de software]], [[Criar um novo cofre]], [[Manual da Orquestra - Perfil projeto prático]], [[Contrato funcional]]
