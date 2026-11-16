---
aliases: [Dinheiro em centavos, Livro de movimentos, Money as integer cents, Chave de idempotência]
tags: [estudos/programacao]
tipo: conceito
status: rascunho
criado: 2026-11-16
origem: projeto Stonebid (stonebid-vault, AD-07 e RN-16 do contrato, decisões movimentos-da-liquidacao, estorno-no-cancelamento, saldo-na-recusa-do-lance e limites-do-deposito; T5l de carteira-e-lotes-plano-correcoes), 2026-10-29 e 2026-10-30
---
# 💰 Dinheiro em centavos num livro de movimentos

> [!tldr] Em uma linha
> Dinheiro é inteiro em centavos, o saldo é calculado de um livro de movimentos só de acréscimo, e entrada ambígua ou repetida não vira dinheiro.

É o caderninho da cantina: ninguém apaga a linha do fiado, só escreve uma nova "pagou". O saldo é a soma do caderno, nunca um número rabiscado à parte.

> [!note] A regra e como aplicar
> 1. **Centavos inteiros** do banco à tela, nunca ponto flutuante; erro se corrige com movimento novo.
> 2. **Fórmula do saldo** escrita uma vez: ex.: `disponível = total − comprometido`, `comprometido = reservas − liberações − estornos`. Todo tipo novo de movimento entra na fórmula **antes** de ser gravado.
> 3. Débito de valor reservado = liberação + débito, na mesma transação; só o débito tiraria o valor duas vezes.
> 4. **Entrada ambígua recusada:** "1,234", "1,2,3", "0,001" dão erro com o formato esperado ("100,00"), sem envio.
> 5. **Chave de idempotência** no cabeçalho (`Idempotency-Key`), gerada uma vez e mantida até o sucesso ou a troca do valor; repetição devolve 200 com a mesma resposta.
> 6. Recusa por saldo devolve o disponível em `details`, para a pessoa saber quanto falta.

> [!warning] Armadilha
> Chave nova a cada clique em "enviar": a resposta se perde, a pessoa tenta de novo e deposita duas vezes. E um tipo de movimento com sentido novo, gravado sem mudar a fórmula, cria dinheiro.

> [!tip] Quando abrir esta nota
> Ao modelar carteira, saldo, crédito, estoque com reserva ou qualquer campo de valor digitado.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** saldo derivado é rastreável; campo "saldo" editado não é.
* **Ponto 2:** o parser de valor recusa o que pode ser lido de dois jeitos.
* **Ponto 3:** a idempotência mora na chave **e** no índice único do banco, e a [[Auditoria confere os dados derivados|auditoria]] confere o livro.

### 🔗 Conexões
- Mapa: [[MOC Programação]]
- Relacionadas: [[Tarefa agendada idempotente com disparo na leitura]], [[Regra de concorrência decidida dentro da trava]]
- Próxima: [[Sessão entre domínios com JWT no cabeçalho]]
