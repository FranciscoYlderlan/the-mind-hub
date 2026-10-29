---
aliases: [Modelo de dados, Entidades do Stonebid, Data model, Modelo conceitual]
tags: [estudos/programacao]
tipo: referencia
tema: requisitos
status: rascunho
criado: 2026-10-29
origem: Contrato do Projeto Stonebid v0.2 (2026-10-27), seção 7
---
# 📜 Contrato: modelo de dados (conceitual)

> [!tldr] Em uma linha
> As cinco "coisas" do sistema (usuário, lote, lance, movimento da carteira, comprovante) e o que cada uma guarda.

É a **lista de gavetas do arquivo** antes de comprar o móvel: decide o que guardar em cada uma sem pensar ainda no modelo do armário. Seção 7 do [[contrato-do-projeto|contrato]] no texto vigente (v0.3).

Aqui não há tabelas de banco nem código: só as "coisas" do sistema e o que cada uma precisa guardar.

| Entidade | O que guarda | Pontos de atenção |
|---|---|---|
| Usuário | Nome, e-mail, hash da senha, papel | Um papel por conta. Nome e e-mail nunca aparecem em páginas públicas. |
| Lote | Leiloeiro, **cópia do item** (título, imagem, atributos), lance inicial, incremento mínimo, início, fim original, fim atual, cancelamento, resultado, vencedor, valor final, **cabeça da cadeia** (número, hash e selo do último lance) | A cópia do item dispensa a API externa. O fim atual muda com a prorrogação. A cabeça muda a cada lance e congela na liquidação. |
| Lance | Lote, número de ordem (1, 2, 3…), licitante, valor, instante (do servidor), hash do lance anterior, **hash do próprio lance**, selo do lance | Só inserção. A numeração não pode ter buracos. |
| Movimento da carteira | Usuário, tipo (depósito, comprometimento, liberação, débito, crédito, estorno), valor, lote (se houver), instante, chave de idempotência | Nunca se edita um movimento. Um erro se corrige com um movimento novo. |
| Comprovante | Identificador público aleatório, lote, pseudônimo do vencedor, valor, data e hora da liquidação, contagem de lances, hash final e selo | Sem dados pessoais. Item e link da auditoria não se guardam: vêm do lote e da rota ([[geral-decisao-2026-10-29-comprovante-e-hash]]). |

> [!info] Por que isso importa
> Pressman e Sommerville ensinam a modelar antes de codificar (identificar as classes ou entidades do domínio e como se relacionam). Errar um modelo no papel custa minutos. Errar no código, no meio da entrega, custa o projeto. Um exemplo é o campo `fim atual`, separado do `fim original`: sem ele, a auditoria não consegue explicar uma prorrogação.

> [!tip] Quando abrir esta nota
> Antes de escrever o schema do Prisma ou uma migração ([[geral-decisao-2026-10-28-stack-backend]]).

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** o lote guarda uma **cópia do item**; nada público depende da API externa.
* **Ponto 2:** lance e movimento da carteira são só inserção; erro se corrige com registro novo.
* **Ponto 3:** `fim original` e `fim atual` separados, para a auditoria explicar a prorrogação ([[contrato-arquitetura]]).

### 🔗 Conexões
- Mapa: [[contrato-do-projeto]] · [[moc-orquestra]]
- Relacionadas: [[contrato-regras-de-negocio]], [[contrato-arquitetura]]
- Próxima: [[contrato-arquitetura]]
