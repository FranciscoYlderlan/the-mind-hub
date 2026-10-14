---
aliases: [Estado lido sob a trava, Sequência global, Fronteira exata, Check inside the lock]
tags: [estudos/programacao]
tipo: conceito
status: rascunho
criado: 2026-11-16
origem: projeto Stonebid (stonebid-vault, decisões cancelamento-ao-vivo, historico-de-lances-no-i2, sequencia-no-extrato, limite-do-anti-sniping e lot-ended-no-cancelamento; lances-plano), 2026-10-29 e 2026-10-30
---
# 🔒 Regra de concorrência decidida dentro da trava

> [!tldr] Em uma linha
> Trave primeiro, leia o estado depois e decida ali dentro; a ordem vem do banco, e a fronteira de tempo é um número exato.

É o caixa do mercado que só confere o preço depois de puxar o produto para a esteira: olhar a prateleira antes não vale, porque alguém pode trocar a etiqueta no caminho. Checar "tem lances?" ou "já acabou?" antes da trava é olhar a prateleira.

> [!note] A regra e como aplicar
> 1. **Estado dentro da trava:** `SELECT ... FOR UPDATE` na linha do item; só então leia contagem, prazo e líder.
> 2. Toda operação concorrente no mesmo item (ação, cancelamento, fechamento) usa a **mesma trava** e uma função de domínio só, que devolve o motivo da recusa.
> 3. **Sequência global** gerada pelo banco (identity) para ordenar movimentos; contador por conta travaria duas contas e arrisca deadlock em operações cruzadas.
> 4. Trava de leitura mais leve na conta (ex.: `FOR NO KEY UPDATE`) evita que operações cruzadas travem uma à outra.
> 5. **Fronteira exata:** escreva o limite em milissegundos e o sinal (ex.: `<= 120000 ms` prorroga; `agora >= fim` já é encerrado) e teste o instante exato.

> [!warning] Armadilha
> Estado calculado pelo relógio (ex.: "ao vivo") não cabe em índice único parcial; aí a barreira é trava por chave, como `pg_advisory_xact_lock`.

> [!tip] Quando abrir esta nota
> Ao escrever "só um por vez", prazo com prorrogação ou cancelamento que concorre com outra ação.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** decisão tomada fora da trava é palpite.
* **Ponto 2:** horários iguais não dão ordem; a sequência do banco dá.
* **Ponto 3:** a prova é o [[Teste de corrida com janela forçada]], falhando sem a trava.

### 🔗 Conexões
- Mapa: [[MOC Programação]]
- Relacionadas: [[Teste de corrida com janela forçada]], [[Tarefa agendada idempotente com disparo na leitura]]
- Próxima: [[Dinheiro em centavos num livro de movimentos]]
