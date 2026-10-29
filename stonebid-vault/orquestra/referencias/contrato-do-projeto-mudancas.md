---
aliases: [Mudanças da v0.3, Mudanças do contrato, Contract changes, M-01 a M-12]
tags: [estudos/programacao]
tipo: referencia
tema: requisitos
status: rascunho
criado: 2026-10-29
origem: Contrato do Projeto Stonebid v0.2 (2026-10-27) + mudanças aprovadas em 2026-10-29; dividida de contrato-do-projeto pelo limite de palavras
---
# 📜 Contrato: mudanças da v0.3

> [!tldr] Em uma linha
> As mudanças aprovadas sobre o contrato v0.2 (M-01 a M-12): onde divergem das notas de seção, vale o que está aqui.

É o **aditivo do contrato de aluguel**: o contrato original continua valendo, e o aditivo diz só o que mudou e desde quando. Parte do hub [[contrato-do-projeto]], dividida dele quando passou do limite de palavras.

## 🔄 Mudanças da v0.3 (2026-10-29)

Entraram pelo protocolo de mudança da seção 13.4, com o aval do humano. Cada linha diz o que mudou em relação à v0.2 e onde está a decisão.

| # | Mudança | Seções afetadas | Onde está |
|---|---|---|---|
| M-01 | Prazo de 4 dias → **24 horas**; entrega em 2026-10-30 09:00; trabalho contínuo. O plano de 4 dias precisa ser refeito com corte de escopo | 1, 2, 9, 11 | [[geral-contexto]] |
| M-02 | Tecnologias definidas (a seção 12 deixa de ser `[PENDENTE]`) | 12 | [[geral-decisao-2026-10-28-stack-frontend]], [[geral-decisao-2026-10-28-stack-backend]], [[contrato-tecnologias]] |
| M-03 | Organização de pastas: frontend por features; backend em Clean Architecture (`domain/`, `application/use-cases/`, `infra/`, `env/`), testes E2E em `test/e2e/`, Prisma com `@@map` em snake_case | 8 | [[geral-decisao-2026-10-28-estrutura-frontend]], [[geral-decisao-2026-10-28-estrutura-backend]] |
| M-04 | Nomes de arquivos, pastas e entidades em inglês e kebab-case nos dois repositórios; identificadores em PascalCase/camelCase | 8, 13 | [[geral-decisao-2026-10-28-estrutura-frontend]], [[geral-decisao-2026-10-28-estrutura-backend]] |
| M-05 | Hospedagem: GCP (Cloud Run com 1 instância mínima, Cloud SQL `db-f1-micro`, Workload Identity Federation, alerta de US$ 50) + Vercel; staging como segundo serviço no Cloud Run | 6, 8, 9 | [[geral-decisao-2026-10-29-hospedagem]] |
| M-06 | CI/CD no GitHub Actions nos dois repositórios (`ci.yml` e `cd.yml`; deploy só depois do CI verde) | 8, 10, 13 | [[geral-decisao-2026-10-28-stack-frontend]], [[geral-decisao-2026-10-28-stack-backend]] |
| M-07 | **Camada MCP** no backend (`src/infra/mcp/`, uma tool por rota, ligada em local e staging, não em produção), entra no contrato enquanto estiver no projeto | 4, 8 | [[geral-decisao-2026-10-29-camada-mcp]] |
| M-08 | **Teste do frontend com Playwright** feito por agentes de IA (subthread de teste), como instrução de teste e não como suíte no repositório; sem testes unitários e de componente no frontend | 10, 13 | [[geral-decisao-2026-10-28-testes-frontend-playwright]] |
| M-09 | Branches: `main` (produção), `staging` e de trabalho `tipo/ID-descricao-curta` (ex.: `feat/RN-04-incremento-minimo`); boilerplate inicial direto na `main` | 11, 13 | [[geral-decisao-2026-10-29-padrao-de-branches]] |
| M-10 | Componentes do frontend: registro consultado antes de criar, shadcn/ui só pela CLI | 13 | [[geral-decisao-2026-10-28-criacao-de-componentes]], [[registro-de-componentes]] |
| M-11 | **Testes:** o teste só sai do escopo junto com o requisito que prova. Ficam sempre T-01 a T-09 e T-10a (cancelamento sem lances); T-10b (estorno) sai com o OPC-2 e T-11 com a RN-18. RNF-12: testes de todo requisito implementado, com um comando e no CI | 6, 10, 11 | [[geral-decisao-2026-10-29-testes-no-escopo]] |
| M-12 | **Comprovante e auditoria:** o Lance guarda também o próprio hash; o Lote guarda a cabeça da cadeia (`head_seq`, `head_hash`, `head_seal`), atualizada a cada lance, no lugar de "contagem e hash final"; o Comprovante é uma fotografia selada da liquidação (`public_id`, lote, pseudônimo, valor, data, contagem, hash final e selo). Item e link da auditoria se derivam. A auditoria da 8.1 confere também os selos da cabeça e do comprovante | 4, 7, 8, 14 | [[geral-decisao-2026-10-29-comprovante-e-hash]] |

**Continua da v0.2 sem mudança:** visão, papéis, RF, RN, RNF (menos o RNF-12, ver M-11), modelo de dados (menos lance, lote e comprovante, ver M-12) e riscos; os **5 opcionais** seguem no escopo; deploy obrigatório. Testes: ver M-11.

**Ainda em aberto na v0.3:**
- Perguntas Q-01 a Q-15 de [[contrato-pontos-para-validar]], incluindo o tempo real (AD-04) e a API pública de itens.
- Plano refeito para 24 horas (corte de escopo a partir de [[contrato-processo-e-plano]]).
- Seção E6 do enunciado ("Como enviar": repositórios públicos e relato do uso de IA), que o contrato não cobre ([[enunciado-teste-tecnico]]).
- Itens `[PROPOSTO]` da seção 8 (AD-01 a AD-10) que não viraram decisão.

> [!tip] Quando abrir esta nota
> Antes de seguir o texto de qualquer nota `contrato-*`: conferir se uma mudança M-xx o substitui.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** onde a nota de seção (v0.2) diverge desta tabela, vale a tabela.
* **Ponto 2:** cada mudança aponta para a nota de decisão que a criou.
* **Ponto 3:** testes seguem o requisito que provam (M-11, [[geral-decisao-2026-10-29-testes-no-escopo]]).
* **Ponto 4:** contagem e hash final só valem com selo; o comprovante é uma fotografia selada (M-12, [[geral-decisao-2026-10-29-comprovante-e-hash]]).

### 🔗 Conexões
- Mapa: [[contrato-do-projeto]] · [[moc-orquestra]]
- Relacionadas: [[geral-decisao-2026-10-29-comprovante-e-hash]], [[contrato-testes]], [[contrato-processo-e-plano]], [[geral-contexto]]
- Próxima: [[contrato-visao-escopo-e-papeis]]
