---
aliases: [Tecnologias do contrato, Critérios de escolha de tecnologia, API pública de itens, Seção 12 do contrato]
tags: [estudos/programacao]
tipo: referencia
tema: requisitos
status: rascunho
criado: 2026-10-29
origem: Contrato do Projeto Stonebid v0.2 (2026-10-27), seção 12
---
# 📜 Contrato: tecnologias

> [!tldr] Em uma linha
> A tabela de escolhas de tecnologia que o contrato deixou em aberto, os critérios para decidir e o que o cofre já decidiu.

É a **lista de ferramentas da caixa**: o contrato diz o tipo de ferramenta, a decisão escolhe a marca. Seção 12 do [[contrato-do-projeto|contrato]] v0.2, copiada sem reinterpretar, mais uma coluna com a situação no cofre.

## 12. Tecnologias `[PENDENTE]`

Você decide e preenche ao final da discussão, usando as versões mais recentes. Cada escolha deve virar uma decisão registrada (o que, as alternativas, o porquê).

| Camada | Escolha | Versão | Por quê |
|---|---|---|---|
| Front-end (React, com ou sem framework) | [A PREENCHER] | | |
| Back-end (Node.js ou Python, e o framework) | [A PREENCHER] | | |
| Banco de dados | [A PREENCHER] | | |
| Tempo real (AD-04) | [A PREENCHER] | | |
| Testes | [A PREENCHER] | | |
| Contêineres (Docker Compose) | [A PREENCHER] | | |
| Hospedagem do deploy | [A PREENCHER] | | |
| API pública de itens | [A PREENCHER] | | |
| Estilo e tema | [A PREENCHER] | | |
| Organização dos repositórios | [A PREENCHER]: dois repositórios (`stonebid-web` e `stonebid-api`) ou um repositório `stonebid` com as pastas `web` e `api` | | |

**Critérios para decidir:**

1. Você já conhece a tecnologia? (Reduz o R-09.)
2. O banco oferece transações e bloqueio adequados para o AD-03? Bancos relacionais tornam isso mais direto. Bancos NoSQL pedem mais cuidado.
3. O host do deploy suporta a técnica de tempo real escolhida e não "dorme" a ponto de quebrar o AD-08?
4. A documentação é boa e a comunidade é ativa?
5. É gratuita ou barata?
6. É fácil de testar?

**Ideias de API pública** (verifique limites de uso e termos antes de decidir, pois não os conferi): obras de arte (acervos de museus com API aberta, como Art Institute of Chicago e The Met), cartas colecionáveis (Scryfall), livros (Open Library), discos (MusicBrainz e Cover Art Archive). Procure uma que não exija chave, tenha imagens estáveis e atributos suficientes para montar um lote.

> [!info] Por que isso importa
> Sommerville e Pressman tratam a escolha de tecnologia como uma decisão de projeto que deve responder aos requisitos e às restrições, e não o contrário. Os dois também discutem o reuso de software e de serviços de terceiros, que é o caso da API externa.

## 🤖 Situação no cofre (interpretação do agente, 2026-10-29)

| Camada | O que o cofre já decidiu | Nota |
|---|---|---|
| Front-end | React 19.3 + Vite 8.3.4, TanStack Router e Query, Zustand, zod, shadcn/ui | [[geral-decisao-2026-10-28-stack-frontend]] |
| Back-end | Fastify v5.12.7 (Node) | [[geral-decisao-2026-10-28-stack-backend]] |
| Banco de dados | PostgreSQL latest, via Prisma v8 (relacional, atende o critério 2) | [[geral-decisao-2026-10-28-stack-backend]] |
| Tempo real (AD-04) | Não decidido | — |
| Testes | Vitest no backend; Playwright no frontend, por outro agente | [[geral-decisao-2026-10-28-testes-frontend-playwright]] |
| Contêineres | Docker + Compose | [[geral-decisao-2026-10-28-stack-backend]] |
| Hospedagem do deploy | Não decidida [a confirmar] | — |
| API pública de itens | Não decidida (Q-13) | — |
| Estilo e tema | Tailwind CSS v4.3 + shadcn/ui | [[geral-decisao-2026-10-28-stack-frontend]] |
| Organização dos repositórios | Dois repositórios: `stonebid-web` e `stonebid-api` | [[geral-contexto]] |

> [!tip] Quando abrir esta nota
> Ao escolher a hospedagem, o mecanismo de tempo real ou a API de itens: usar os critérios acima e registrar a escolha numa nota de decisão.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** quase toda a stack já está decidida; faltam **tempo real, hospedagem e API de itens**.
* **Ponto 2:** tempo real e hospedagem se decidem juntos (critério 3 e risco R-05 de [[contrato-riscos]]).
* **Ponto 3:** a API de itens deve dispensar chave e ter imagens estáveis.

### 🔗 Conexões
- Mapa: [[contrato-do-projeto]] · [[moc-orquestra]]
- Relacionadas: [[geral-decisao-2026-10-28-stack-frontend]], [[geral-decisao-2026-10-28-stack-backend]], [[contrato-arquitetura]]
- Próxima: [[contrato-trabalho-com-a-ia]]
