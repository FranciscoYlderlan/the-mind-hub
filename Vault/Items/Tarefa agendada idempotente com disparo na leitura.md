---
aliases: [Liquidação idempotente, Servidor que dorme, Idempotent scheduled job, Agendador com plano B]
tags: [estudos/programacao]
tipo: conceito
status: rascunho
criado: 2026-11-16
origem: projeto Stonebid (stonebid-vault, decisão disparo-da-liquidacao, AD-08 do contrato-arquitetura e decisão hospedagem), 2026-10-30
---
# ⏰ Tarefa agendada idempotente com disparo na leitura

> [!tldr] Em uma linha
> Tarefa que "tem de acontecer" dispara por dois caminhos (agendador e leitura) e é idempotente, para rodar exatamente uma vez.

É o despertador com soneca e o vizinho que bate na porta: se um falhar, o outro acorda você, e acordar duas vezes não faz você ir ao trabalho duas vezes. Host gratuito ou com zero instâncias mínimas **dorme**, e o agendador dentro do processo dorme junto. Um prazo vencido (fechar leilão, expirar pedido) ficaria parado.

> [!note] A regra e como aplicar
> 1. **Dois disparos:** um agendador curto no processo (ex.: a cada 5 s, um lote limitado de itens vencidos) e a execução na leitura, em toda rota que mostra o item.
> 2. **Idempotência** (idempotency): trave a linha, cheque se já foi feito (ex.: coluna `settledAt`) e só então execute.
> 3. **Segunda barreira no banco:** índice único no efeito (ex.: um comprovante por item).
> 4. Desligue o agendador nos testes e prove o disparo duplo: N disparos simultâneos, um efeito só.

> [!warning] Armadilha
> Servidor cobrado por requisição limita a CPU entre requisições: o agendador em segundo plano para mesmo com a instância de pé. Só a leitura salva.

> [!tip] Quando abrir esta nota
> Ao escrever qualquer "quando o prazo vencer, faça X" em servidor que pode dormir.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** agendador sozinho não garante nada em host que dorme; a leitura cobre o buraco.
* **Ponto 2:** dois disparos só são seguros com idempotência: trava, checagem e índice único.
* **Ponto 3:** a prova é o [[Teste de corrida com janela forçada|teste de disparo duplo]], que falha sem a trava.

### 🔗 Conexões
- Mapa: [[MOC Programação]]
- Relacionadas: [[Regra de concorrência decidida dentro da trava]], [[Dinheiro em centavos num livro de movimentos]]
- Próxima: [[Tempo real por SSE com recarga de reserva]]
