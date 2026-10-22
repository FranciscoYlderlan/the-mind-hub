---
tipo: plano
funcionalidade: banco-mocado
status: proposta
criado: 2026-11-08
aliases: [Registro da trilha de SQL do M3 em diante, Desempenho em SQL M3 a M8, SQL performance log M3+]
---
# 📝 Registro de desempenho da trilha de SQL: M3 a M8

> [!tldr] Em uma linha
> As linhas do registro da [[trilha-sql-didatica]] do M3 em diante, com os mesmos campos, códigos e protocolo do [[banco-mocado-plano-registro-sql]].

## Registro
| Data | Item | Granularidade | Autonomia | Tentativas | Tempo | Erros | Nota da IA |
|---|---|---|---|---|---|---|---|
| 2026-11-07 14h24 | MA-SINTAXE.1 | — | A | 1 | 2 | — | Achou a vírgula e a ordem `HAVING`/`GROUP BY` (a IA tinha dito 3 erros; eram 2) |
| 2026-11-07 14h30 | MA-SINTAXE.2 | — | C | 2 | 13 | COND | Sintaxe do `IN` e do `LIKE` certa; faltou `tipo_pessoa = 'PF'` (12 linhas em vez de 6); `LOWER(nome)` desnecessário com collation `ci` e não sargable; perguntou de acento e de produção com 50 milhões |
| 2026-11-07 14h49 | MA-SINTAXE.3 | — | A | 1 | 6 | — | Apelido sem `AS`; a IA mostrou o erro silencioso da vírgula faltando |
| 2026-11-07 15h05 | MA-COND.1 | — | C | 2 | 6 | COND, DATA | O checklist juntou "créditos em PIX" num item só; faltaram `direcao = 'C'` e o fim do intervalo (`< '2027-01-01'`) |
| 2026-11-07 15h16 | MA-COND.2 | — | A | 1 | 5 | — | Usou `IN` e desviou da armadilha do `OR` sem parênteses (776 linhas contra 101) |
| 2026-11-07 15h17 | MA-COND.3 | — | P | — | — | — | Achou simples |
| 2026-11-07 16h36 | O2.5 (variante) | — | C | 2 | 5 | COND | Analistas com mais de 280 falsos positivos: `WHERE` certo; faltou o "mais de 280", que saiu com uma dica de cláusula; apelido no `HAVING`. Na O2.5 tinha sido D |
| 2026-11-07 18h10 | O3.1 | — | D | 1 | 3 | — | Prática guiada: molde com lacunas dado pela IA; certo de primeira (681 linhas) |
| 2026-11-07 18h15 | O3.2 | — | C | 3 | 3 | SINTAXE, COND | `GROUP BY cliente_id` ambíguo (erro 1052); depois faltou o `HAVING`; agrupou pela chave, não pelo nome |
| 2026-11-07 18h25 | O3.2 (refeita) | — | A | 1 | 6 | — | Reescreveu sozinho a versão que resume `contas` antes de juntar; faltou o `DESC` |
| 2026-11-07 18h39 | O3.3 | — | A | 1 | 9 | — | Dois saltos certos; subconsulta sem `GROUP BY` desnecessária (o `EXPLAIN` mostrou o otimizador desmontando) |
| 2026-11-07 19h00 | O3.4 | — | C | 4 | 17 | SINTAXE, COND | `JOIN` escrito depois do `WHERE` (duas vezes), vírgula antes do `FROM`, `client_id`; faltou o `LIMIT`; ordenou pelo número e não pelo texto do `FORMAT` |
| 2026-11-07 19h51 | O3.4 (otimizada) | — | E | 3 | 5 | GROUP, GRAN | Resumiu `contas` em vez de `transacoes`, com `conta_id` fora do `GROUP BY`; a IA mostrou a solução; a variante refeita é a C3 |
| 2026-11-08 04h00 | O3.5 | — | A | 1 | 15 | — | Quatro tabelas certas (14 remessas); `ORDER BY` de `ENUM` em `DESC` deixou `ALTO_RISCO` no fim; 12 colunas; viu o PF com R$ 265 mil para o Iêmen |
| 2026-11-08 04h14 | C3 | — | C | 3 | 2 | COND | Estrutura otimizada sozinho (resume `transacoes` por conta, junta `contas` e `clientes`, dois `SUM`); faltaram `tipo_pessoa = 'PF'` e o `LIMIT 10` |
| 2026-11-08 05h32 | O4.1 | — | C | 2 | 29 | GRAN | 1ª: `NOT EXISTS` (só os 36 sem alerta, com `COUNT(*)` = 1 contando a linha do cliente); 2ª sozinho: resumiu `alertas` antes de juntar, `LEFT JOIN` e `COALESCE` (520 linhas, 36 zeros, soma 1.936) |
| 2026-11-08 05h38 | O4.2 | — | A | 1 | 6 | — | Os dois jeitos certos (36 = 36, mesma lista); `IS NULL` na coluna do `ON` |
| 2026-11-08 06h21 | O4.3 | — | C | 2 | 8 | GRAN | `WHERE` 16 linhas, `ON` 520; `COUNT(*)` deu 1 para quem tem zero; `COALESCE` com um argumento só; o porquê da diferença foi explicado pela IA a pedido |
| 2026-11-08 06h56 | O4.4 | — | C | 5 | 29 | SINTAXE, GRAN, COND | `pais_risco`, vírgula no `GROUP BY`, subconsulta sem apelido e `t.` fora dela; perguntou como usar `contas` como ponte sem agrupar (a IA explicou); `COUNT(*)` no lugar de `SUM(mv.qtd)`; acrescentou `CAMBIO_ENVIO` (4 clientes, 14 remessas) |
| 2026-11-08 08h55 | C4 | — | C | 3 | 41 | SINTAXE, COND | Com a O4.5 dentro: `NOT EXISTS` com 2026 dentro e média dos PJ em subconsulta certos de primeira; `cli.` fora da subconsulta (duas vezes) e faltou o `DESC` (15 contas) |
| 2026-11-08 09h43 | O5.1 | — | D | 1 | 10 | — | Prática guiada com lacunas; certo de primeira (4 faixas, soma 66.871); não disse a granularidade |
| 2026-11-08 10h03 | O5.2 | — | C | 2 | 15 | SINTAXE | Com os degraus P2.a e P2.b (faltou o `CASE`); pulou o P2.c e fez a questão inteira com `CONCAT` e `ORDER BY` pela conta numérica; trocou para `COUNT(desfecho)` depois da explicação dos abertos |
| 2026-11-08 10h21 | O5.3 | — | E | 3 | 12 | SINTAXE, DATA | P3.a sem `SELECT` e com `'MONTH'` entre aspas; P3.b certo com `CURDATE()`; o filtro de 24 meses foi mostrado pela IA (o `INTERVAL` não tinha sido ensinado; mini-aula) |
| 2026-11-08 10h30 | O5.3 (variante) | — | C | 3 | 7 | DATA | `- 36 - MONTH` sem `INTERVAL`, depois `>` no lugar de `<`; na 3ª, certo com `INTERVAL 3 YEAR` (37 clientes) |
| 2026-11-08 10h41 | O5.4 | — | A | 1 | 9 | COND | Pulou o P4.b; `TIMESTAMPDIFF(DAY)` no lugar de `DATEDIFF` (881 de 1.780 diferem em 1 dia); faltou o `COALESCE`, sem efeito porque os 156 sem analista são os abertos |
| 2026-11-08 11h09 | C5 | — | C | 5 | 25 | SINTAXE, COND | Vírgula antes do `FROM`; filtro de espécie no `ON` (perdeu o total); `CASE` de PF ou PJ; divisão invertida escondida com `COALESCE`; `tipo_pessoa` até a 4ª; faltou o `, 2` |
| 2026-11-08 11h27 | O6.1 | — | A | 1 | 60 | — | O3.4 como CTE certa de primeira (Ramos Distribuidora, R$ 86,5 milhões); filtro todo dentro do rascunho; não disse a granularidade antes de rodar; `GROUP BY` só pela chave |
| 2026-11-08 12h30 | O6.2 | errada | D | 3 | 46 | COND, SINTAXE | Pediu o problema de negócio em passos; corrigiu a razão da IA (crédito ÷ renda, não entrada + saída ÷ renda); granularidade dita como relação 1:N; faltaram PF (filtrou PJ), `, 2` e `LIMIT`; a 2ª CTE veio com esqueleto e não foi rodada |
| 2026-11-08 13h41 | O7.1 | errada | E | 5 | 31 | JANELA, GROUP, SINTAXE | `ROW_NUMBER` em CTE e filtro fora certos; gaveta por conta (640 linhas para 520 clientes), tentou remendar com `GROUP BY` (erro 1055 no modo estrito); pediu a solução; depois `conta_id` ambíguo e, na 5ª, gaveta por `ct.cliente_id` certa |
| 2026-11-08 14h14 | O7.2 | certa | D | 3 | 23 | SINTAXE, COND | Resumiu por cliente antes de juntar; faltaram vírgula, apelido `rank` (palavra reservada), `<= 3` invertido e `risco_kyc` no `SELECT`; o lado a lado das três funções veio no código mostrado pela IA a pedido |

### 🔗 Conexões
- Nota original: [[banco-mocado-plano-registro-sql]]
- Funcionalidade: [[banco-mocado-contexto]]
- Trilha: [[trilha-sql-didatica]]
