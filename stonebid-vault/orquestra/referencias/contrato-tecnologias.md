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
> As escolhas de tecnologia do projeto, cada uma com a sua decisão, a que falta e os critérios para decidir.

É a **lista de ferramentas da caixa**: o contrato diz o tipo de ferramenta, a decisão escolhe a marca. Seção 12 do [[contrato-do-projeto|contrato]], no texto vigente (v0.3): cada camada com a escolha e a decisão que a registrou.

## 12. Tecnologias

Cada escolha vira uma decisão registrada (o que, as alternativas, o porquê). Falta uma, marcada `[PENDENTE]`. Nenhuma versão é travada: vale a citada ou mais recente (o sinal `+`).

| Camada | Escolha | Decisão |
|---|---|---|
| Front-end | React 19.3+ e Vite 8.3.4+, TanStack Router e Query, Zustand, zod, shadcn/ui | [[geral-decisao-2026-10-28-stack-frontend]] |
| Back-end | Fastify v5.12.7+ (Node) | [[geral-decisao-2026-10-28-stack-backend]] |
| Banco de dados | PostgreSQL latest, via Prisma 7.10.1+ ([[geral-decisao-2026-10-29-prisma-7]]; relacional, atende o critério 2) | [[geral-decisao-2026-10-28-stack-backend]] |
| Tempo real (AD-04) | `[PENDENTE]` | — |
| Testes | Vitest no backend; Playwright no frontend, por outro agente | [[geral-decisao-2026-10-28-testes-frontend-playwright]] |
| Contêineres | Docker + Compose | [[geral-decisao-2026-10-28-stack-backend]] |
| Hospedagem do deploy | Backend e banco no GCP (Cloud Run + Cloud SQL); frontend na Vercel; CI/CD no GitHub Actions | [[geral-decisao-2026-10-29-hospedagem]] |
| API pública de itens | Art Institute of Chicago, sem chave (Q-13) | [[geral-decisao-2026-10-29-api-de-itens]] |
| Estilo e tema | Tailwind CSS v4.3+ e shadcn/ui | [[geral-decisao-2026-10-28-stack-frontend]] |
| Organização dos repositórios | Dois repositórios: `stonebid-web` e `stonebid-api` | [[geral-contexto]] |

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

> [!tip] Quando abrir esta nota
> Ao escolher a hospedagem, o mecanismo de tempo real ou a API de itens: usar os critérios acima e registrar a escolha numa nota de decisão.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** quase toda a stack já está decidida; falta **tempo real**; a API de itens é a do Art Institute of Chicago ([[geral-decisao-2026-10-29-api-de-itens]]); a hospedagem foi decidida em 2026-10-29 ([[geral-decisao-2026-10-29-hospedagem]]).
* **Ponto 2:** com a hospedagem decidida (Cloud Run aceita WebSocket e SSE), falta só escolher o tempo real (AD-04), conferindo o critério 3 e o risco R-05 de [[contrato-riscos]].
* **Ponto 3:** a API de itens deve dispensar chave e ter imagens estáveis.

### 🔗 Conexões
- Mapa: [[contrato-do-projeto]] · [[moc-orquestra]]
- Relacionadas: [[geral-decisao-2026-10-28-stack-frontend]], [[geral-decisao-2026-10-28-stack-backend]], [[geral-decisao-2026-10-29-hospedagem]], [[contrato-arquitetura]]
- Próxima: [[contrato-trabalho-com-a-ia]]
