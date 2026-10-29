---
aliases: [Modelo de dados, Entidades do StoneBid, Data model, Modelo conceitual]
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

É a **lista de gavetas do arquivo** antes de comprar o móvel: decide o que guardar em cada uma sem pensar ainda no modelo do armário. Seção 7 do [[contrato-do-projeto|contrato]] v0.2, copiada sem reinterpretar.

> [!warning] Prazo mudou em 2026-10-29
> O prazo real passou de 4 dias para **24 horas** (a partir de 2026-10-29 09:06; entrega em 2026-10-30 09:00). Onde esta nota fala em 4 dias ou em "dia 3", vale o prazo novo; o texto do contrato segue como estava até a v0.3. Fato registrado em [[geral-contexto]].

Aqui não há tabelas de banco nem código: só as "coisas" do sistema e o que cada uma precisa guardar.

| Entidade | O que guarda | Pontos de atenção |
|---|---|---|
| Usuário | Nome, e-mail, hash da senha, papel | Um papel por conta. Nome e e-mail nunca aparecem em páginas públicas. |
| Lote | Leiloeiro, **cópia do item** (título, imagem, atributos), lance inicial, incremento mínimo, início, fim original, fim atual, cancelamento, resultado, vencedor, valor final, contagem e hash final do histórico | A cópia do item dispensa a API externa. O fim atual muda com a prorrogação. |
| Lance | Lote, número de ordem (1, 2, 3…), licitante, valor, instante (do servidor), hash do lance anterior, selo do lance | Só inserção. A numeração não pode ter buracos. |
| Movimento da carteira | Usuário, tipo (depósito, comprometimento, liberação, débito, crédito, estorno), valor, lote (se houver), instante, chave de idempotência | Nunca se edita um movimento. Um erro se corrige com um movimento novo. |
| Comprovante | Identificador público aleatório, lote, resultado, hash final | Sem dados pessoais. |

> [!info] Por que isso importa
> Pressman e Sommerville ensinam a modelar antes de codificar (identificar as classes ou entidades do domínio e como se relacionam). Errar um modelo no papel custa minutos. Errar no código, no dia 3, custa o projeto. Um exemplo é o campo `fim atual`, separado do `fim original`: sem ele, a auditoria não consegue explicar uma prorrogação.

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
