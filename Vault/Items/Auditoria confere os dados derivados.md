---
aliases: [Auditoria de derivados, Coluna derivada na mesma transação, Derived data audit, Conferência da auditoria]
tags: [estudos/programacao]
tipo: conceito
status: rascunho
criado: 2026-11-16
origem: projeto Stonebid (stonebid-vault, decisões auditoria-publica, achados-da-t5-da-auditoria, lance-atual-no-lote e estorno-no-cancelamento), 2026-10-30
---
# 🔍 Auditoria confere os dados derivados

> [!tldr] Em uma linha
> A cadeia íntegra não basta: a auditoria confere também tudo o que deriva dela (comprovante, extrato, colunas de cópia), lido numa transação só.

É conferir o extrato do banco e também o recibo da loja: as notas batem entre si, mas se alguém sumiu com o recibo, a compra "nunca aconteceu". Derivados sem selo são a porta lateral do [[Histórico à prova de adulteração com hash encadeado|histórico selado]].

> [!note] A regra e como aplicar
> 1. **Coluna derivada** (ex.: valor atual e líder copiados no item) só muda na **mesma transação** do registro; nenhuma rota escreve nela fora dali.
> 2. A auditoria confere cada cópia contra a cadeia: valor atual igual ao último registro; sem registros, vazio.
> 3. Existência nos dois sentidos: estado "vendido" **exige** comprovante e o lançamento; "não vendido" **proíbe** os dois.
> 4. Movimentos de dinheiro: exatamente um débito e o crédito correspondente, no valor do último registro.
> 5. Leia tudo numa transação `REPEATABLE READ`, recalcule a cada acesso, `Cache-Control: no-store`.
> 6. Prove cada adulteração por SQL direto no banco de teste, não como dado de demonstração.

> [!warning] Armadilha
> Conferir o comprovante "se existir": apagar o comprovante, o débito e trocar o resultado passava como íntegro sem o segredo.

> [!tip] Quando abrir esta nota
> Ao escrever o verificador de um registro selado, ou ao criar uma coluna que copia dado de outra tabela.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** cada derivado sem selo precisa de uma conferência contra a cadeia.
* **Ponto 2:** ausência também é adulteração: confira "tem de ter" e "não pode ter".
* **Ponto 3:** limite declarado: cadeia vazia com cabeça zerada ainda passa; registre no README em vez de esconder.

### 🔗 Conexões
- Mapa: [[MOC Programação]]
- Relacionadas: [[Histórico à prova de adulteração com hash encadeado]], [[Dinheiro em centavos num livro de movimentos]]
- Próxima: [[Regra de concorrência decidida dentro da trava]]
