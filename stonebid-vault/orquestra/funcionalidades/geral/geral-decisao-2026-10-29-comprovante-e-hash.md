---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-29
substitui: 
aliases: [Comprovante e hash, Selo da cabeça da cadeia, Comprovante selado, Hash do lance, Truncamento do histórico, Receipt and hash chain]
---
# ✅ Comprovante selado, hash guardado no lance e cabeça da cadeia no lote (M-12)

- **Proposta (plano):** sugestão da IA no chat de 2026-10-29 (12:25–13:19), a partir de duas divergências apontadas pelo humano:
  - o que o comprovante guarda: [[contrato-modelo-de-dados]] lista identificador, lote, resultado e hash final; o item 4 da seção 8.1 de [[contrato-arquitetura]] confere "a contagem e o hash final" guardados no comprovante; o RF-51 ([[contrato-requisitos-funcionais]]) e a Q-09 ([[contrato-pontos-para-validar]]) incluem valor, data, pseudônimo e link da auditoria;
  - o Lance guarda "hash do lance anterior" e "selo", mas não o próprio hash, que a auditoria diz recalcular.
- **Decisão:** humano aprovou ("pode atualizar com a nova proposta de solução") em 2026-10-29 13:22.
  - **Lance** guarda também o **próprio hash**. Campos: `seq`, `lot_id`, `bidder_id`, `amount_cents`, `created_at`, `prev_hash`, `hash`, `seal`.
    - `hash = SHA-256` da serialização em ordem fixa: `JSON.stringify(["v1", lotId, seq, pseudonym, amountCents, createdAtMs, prevHash])` (array, nunca objeto).
    - No hash entra o **pseudônimo** derivado do `bidder_id` (AD-09), não o id: trocar o licitante no banco muda o pseudônimo e quebra o hash; a cadeia de hashes pode ser recalculada por qualquer pessoa, só o selo exige o servidor.
    - `created_at` com precisão de milissegundos (`@db.Timestamptz(3)`), serializado como número em milissegundos.
    - Lance 1: `prev_hash = SHA-256("genesis:" + lotId)`.
    - `seal = HMAC-SHA256(segredo, "bid:v1" + hash)`.
  - **Lote** guarda a **cabeça da cadeia**: `head_seq`, `head_hash` e `head_seal = HMAC(segredo, "head:v1" + lotId + seq + hash)`, atualizados na mesma transação do lance (a linha do lote já fica travada pela serialização da AD-03). Na liquidação a cabeça congela e é a "contagem e hash final" do contrato (os dois campos deixam de existir à parte).
  - **Comprovante** é uma fotografia selada da liquidação. Guarda: `public_id` (16 bytes aleatórios em base64url, RF-52), `lot_id` (único), `winner_pseudonym`, `amount_cents`, `settled_at`, `bid_count`, `final_hash` e `seal = HMAC(segredo, "receipt:v1" + todos esses campos)`.
    - **Não guarda, deriva:** o item (cópia imutável no lote, RN-13), o link da auditoria (rota `/auditoria/:lotId`; gravar a URL prende o registro ao domínio do deploy), o "resultado" (comprovante só existe para lote arrematado; o resultado fica no lote) e nenhum dado pessoal (RN-15).
    - A **tela** do comprovante mostra tudo o que o RF-51 e a Q-09 pedem: item, valor, data e hora, pseudônimo, hash final e link da auditoria.
  - **Uma função só** `seal(tag, ...campos)` para os três selos; as etiquetas `bid:v1`, `head:v1` e `receipt:v1` impedem que um selo de um tipo sirva para outro.
  - **A auditoria (8.1) passa a conferir:**
    1. A numeração vai de 1 a *n*, sem buracos.
    2. Para cada lance: hash recalculado igual ao guardado (senão, conteúdo editado), selo confere e `prev_hash` igual ao hash do anterior (senão, inserção ou remoção).
    3. *n*, o último hash e o `head_seal` batem com a cabeça do lote.
    4. Se houver comprovante: o selo confere, `bid_count` e `final_hash` batem, e pseudônimo e valor batem com o último lance.
    5. O vencedor e o valor batem com a liquidação e com o extrato.
  - **Camada extra (opcional):** `REVOKE UPDATE, DELETE` na tabela de lances para o usuário que a aplicação usa no banco; os testes de adulteração (T-06) usam outro usuário.
- **Alteração:** nenhuma.
- **Motivo:**
  - Furo encontrado: na v0.2, contagem e hash final ficam **sem selo** no lote e no comprovante. Quem apaga o último lance pode também gravar ali a contagem *n−1* e o hash do lance *n−1*, que já está no banco; a cadeia que sobra é válida e a auditoria diria ÍNTEGRO. O caso "último lance apagado" do T-06 ([[contrato-testes]]) falharia.
  - Com o selo da cabeça e do comprovante, reescrever o resumo exige um selo novo, impossível sem o segredo; a etiqueta diferente impede copiar um selo de lance que já está no banco.
  - A cabeça atualizada a cada lance detecta o truncamento **também com o lote ao vivo**, não só depois da liquidação.
  - Guardar o hash do lance dá o diagnóstico que o RF-61 pede (primeiro registro inconsistente: conteúdo editado × registro inserido ou removido) e evita recalcular o anterior a cada lance novo.
  - O comprovante guarda só o que não se deriva, mais o que a auditoria confere: concilia o modelo de dados, a 8.1, o RF-51 e a Q-09.
  - Custo estimado: cerca de 1 a 2 horas (três colunas no lance e no lote, uma tabela pequena e uma função de selo) [a confirmar na implementação].
- **Consequências:**
  - Schema Prisma: `Bid` com `hash`; `Lot` com `headSeq`, `headHash`, `headSeal` no lugar de "contagem e hash final"; `Receipt` com os campos acima ([[geral-decisao-2026-10-28-stack-backend]], `@@map` em snake_case por [[geral-decisao-2026-10-28-estrutura-backend]]).
  - O segredo do HMAC é variável de ambiente do servidor, nunca no banco nem no repositório.
  - O T-06 cobre os 5 casos: íntegro, valor editado, lance apagado no meio, lance inserido e último lance apagado (com o lote ao vivo e depois da liquidação).
  - **Limite para o README:** quem tiver o banco **e** o segredo, ou um backup antigo com uma cabeça anterior, ainda forja o histórico; só uma âncora externa resolveria, fora do escopo.
  - Proibido: guardar contagem ou hash final sem selo; serializar o hash a partir de objeto; guardar nome, e-mail ou URL da auditoria no comprovante.
  - Afeta as seções 4 (RF-51), 7 e 8.1 do contrato e a Q-09; registrada como M-12 em [[contrato-do-projeto-mudancas]].

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[geral-plano]]
- Projeto: [[geral-contexto]]
- Relacionadas: [[contrato-modelo-de-dados]], [[contrato-arquitetura]], [[contrato-requisitos-funcionais]], [[contrato-pontos-para-validar]], [[contrato-testes]], [[contrato-do-projeto-mudancas]]
- Regras: [[manual-da-orquestra]]
