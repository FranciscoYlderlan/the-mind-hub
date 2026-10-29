---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-29
substitui: 
aliases: [Hospedagem do deploy, Onde o Stonebid roda, Deploy no GCP e na Vercel, Hosting decision]
---
# ✅ Hospedagem: backend e banco no GCP, frontend na Vercel, CI/CD pelo GitHub

- **Proposta (plano):** comparação da IA no chat de 2026-10-29 entre GCP, AWS e Railway para o backend e o banco, com custo zero até a entrega. A IA recomendou o Railway pela simplicidade e apontou o GCP como opção mais segura em prazo de crédito (90 dias contra 30).
- **Decisão:** o humano escolheu o **GCP** (texto do humano: "perfeito então será utilizado a gcp").
  - **Backend (`stonebid-api`):** Google Cloud, em contêiner a partir do Dockerfile do repositório.
  - **Banco (PostgreSQL):** Google Cloud.
  - **Frontend (`stonebid-web`):** **Vercel** (fato do humano: "o frontend irei deployar na vercel pois é gratuito").
  - **Integração:** os dois repositórios no **GitHub com CI/CD** (GitHub Actions) para validar a integração antes de publicar.
- **Alteração:** o humano preferiu o GCP à recomendação da IA (Railway). A configuração abaixo foi proposta pela IA e **aprovada pelo humano em 2026-10-29** (resposta: "ok").
- **Motivo:** custo zero garantido até a entrega. Os US$ 300 de crédito para conta nova duram 90 dias e cobrem com folga o uso previsto. Dados do humano: a aplicação fica no ar **no máximo 7 dias**, é avaliada pela equipe em **menos de 1 hora**, e o maior uso são as ~24h de desenvolvimento; depois, o projeto é fechado.

## 💰 Custo previsto (estimativa da IA, 2026-10-29)
| Item | Estimativa por mês | Em 7 dias |
|---|---|---|
| Cloud SQL Postgres `db-f1-micro` em São Paulo + ~10 GB de disco | ~US$ 15 (instância US$ 12, preço de tabela da Bytebase) | ~US$ 3,50 |
| Cloud Run 1 vCPU / 512 MiB, 1 instância sempre ligada, cobrança por instância | ~US$ 65–70 (cálculo da IA: taxa de região tier 1 + ~40%) | ~US$ 16 |
| Artifact Registry e tráfego | < US$ 1 | centavos |
| **Total** | **~US$ 85** | **~US$ 20, coberto pelos US$ 300 → R$ 0 do bolso** |

- O GCP não cobra enquanto a conta não for ativada como paga, mesmo se o crédito acabar. O cartão pedido no cadastro só confirma a identidade (pode aparecer uma autorização temporária, estornada).
- A Vercel no plano gratuito (Hobby) não tem custo.

## 🛠️ Configuração (proposta da IA, aprovada em 2026-10-29)
- **Região:** `southamerica-east1` (São Paulo), para o menor atraso até a equipe avaliadora no Brasil.
- **Backend no Cloud Run:** imagem no Artifact Registry; **1 instância mínima** e **cobrança por instância** (CPU sempre alocada). Assim o serviço não "dorme" (sem cold start no tempo real, RNF-06) e o agendador da liquidação (AD-08) roda entre as requisições. Na cobrança por requisição, a CPU fica limitada fora das requisições e um agendador em segundo plano não é confiável.
- **Banco no Cloud SQL:** PostgreSQL `db-f1-micro`, conectado ao Cloud Run pela integração nativa do Cloud SQL; `DATABASE_URL` como segredo, nunca no repositório.
- **CD do backend:** GitHub Actions autentica no GCP por Workload Identity Federation (sem chave JSON de conta de serviço guardada), faz o build, publica a imagem e faz o deploy no Cloud Run depois do CI verde. As migrações do Prisma (`prisma migrate deploy`) rodam no pipeline antes de trocar a versão.
- **CD do frontend:** deploy na Vercel depois do CI verde (Vercel CLI no GitHub Actions ou integração nativa Vercel + GitHub). A URL da API entra como variável de ambiente do build.
- **CORS e HTTPS:** a API aceita só a origem da Vercel; Cloud Run e Vercel já entregam HTTPS (RNF-01, RNF-07).
- **Staging** (exigido pela [[geral-decisao-2026-10-29-camada-mcp]]): um segundo serviço no Cloud Run com `MCP_ENABLED=true` e um banco separado na mesma instância do Cloud SQL; no frontend, os deploys de *preview* da Vercel. Branch de staging: `staging` ([[geral-decisao-2026-10-29-padrao-de-branches]]).
- **Controle de gasto:** alerta de orçamento no GCP (ex.: US$ 50) criado junto com o projeto.

## Consequências
- O destino do CD deixa de estar em aberto nas decisões de stack: [[geral-decisao-2026-10-28-stack-backend]] (Cloud Run + Cloud SQL) e [[geral-decisao-2026-10-28-stack-frontend]] (Vercel).
- Nenhum deploy manual: tudo que vai para o ar passa pelo CI verde no GitHub. Segredos do GCP e da Vercel ficam nos *secrets* do GitHub e no Secret Manager, nunca no repositório.
- O tempo real (AD-04 de [[contrato-arquitetura]]) segue em aberto, mas o host não o bloqueia: o Cloud Run aceita WebSocket e Server-Sent Events. Testar no host real logo no primeiro deploy (risco R-05 de [[contrato-riscos]]), lembrando que o Cloud Run encerra conexões longas no tempo limite da requisição; o cliente deve reconectar.
- O frontend na Vercel e a API no Cloud Run ficam em domínios diferentes: a sessão de login deve funcionar entre origens (cookie `SameSite=None; Secure` ou token no cabeçalho) [a confirmar na implementação].
- **Depois da avaliação:** excluir o projeto inteiro no GCP (derruba Cloud Run, Cloud SQL e imagens de uma vez) e o projeto na Vercel.
- Trocar de hospedagem exige nova decisão.

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[geral-plano]]
- Projeto: [[geral-contexto]]
- Relacionadas: [[geral-decisao-2026-10-29-padrao-de-branches]], [[geral-decisao-2026-10-28-stack-backend]], [[geral-decisao-2026-10-28-stack-frontend]], [[geral-decisao-2026-10-29-camada-mcp]], [[contrato-tecnologias]], [[contrato-requisitos-nao-funcionais]], [[contrato-riscos]], [[enunciado-teste-tecnico]]
- Regras: [[manual-da-orquestra]]
