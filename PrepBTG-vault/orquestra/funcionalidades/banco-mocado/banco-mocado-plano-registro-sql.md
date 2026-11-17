---
tipo: plano
funcionalidade: banco-mocado
status: proposta
criado: 2026-11-06
aliases: [Registro da trilha de SQL, Desempenho em SQL, Score de SQL, SQL performance log]
---
# 📝 Registro de desempenho da trilha de SQL

> [!tldr] Em uma linha
> Onde cada operação da [[trilha-sql-didatica]] fica registrada, e a régua que um agente avaliador usa para medir a minha evolução e escolher o próximo reforço. Na trilha, o score mede aprendizado, não aprovação.

## Como registrar (a IA de treino entrega, o orquestrador grava)
Uma linha por operação ou checagem, no fechamento da sessão. Nada é apagado: refazer uma operação gera linha nova.

| Campo | O que vai |
|---|---|
| Data | AAAA-MM-DD e hora de início |
| Item | código da operação (`O3.4`), da extra (`X3.2`) ou da checagem do módulo (`C3`) |
| Granularidade | `certa` ou `errada`, dita antes de rodar a consulta |
| Autonomia | código da tabela abaixo |
| Tentativas | quantas vezes rodou até o resultado certo |
| Tempo | minutos, só para ver a evolução (sem cobrança na trilha) |
| Erros | códigos do catálogo abaixo, separados por vírgula |
| Nota da IA | uma frase: o que ficou bom e o que faltou |

### Autonomia
| Código | Significa | Pontos |
|---|---|---|
| A | certo sozinho na primeira execução | 4 |
| B | certo sozinho, depois de rodar e corrigir | 3 |
| C | certo com dica de degrau 1 ou 2 (tabela, técnica) | 2 |
| D | certo com dica de degrau 3 (esqueleto) | 1 |
| E | precisou da solução (depois refaz uma variante) | 0 |
| P | pulada: simples demais ou fora de hora; conta como feita no progresso ([[geral-decisao-2026-11-06-progresso-a-cada-questao]]) | fora do score |

### Catálogo de erros
`GRAN` granularidade ou soma inflada · `CAMINHO` pulou a tabela de ligação · `DATA` intervalo com hora ou formato · `NULO` nulo mal tratado · `GROUP` coluna fora do `GROUP BY` · `FILTRO` `WHERE` contra `HAVING` ou filtro do `LEFT JOIN` no lugar errado · `DIV` divisão ou arredondamento · `JANELA` `PARTITION BY` ou `ORDER BY` da janela errado · `SINTAXE` vírgula, alias, parêntese · `NEGOCIO` conceito do domínio (crédito, débito, PEP, desfecho) · `COND` condição pedida no enunciado que ficou fora do `WHERE`.

## Protocolo do agente avaliador
O agente lê só esta nota, a [[banco-mocado-plano-registro-sql-m3-a-m8]] e a [[trilha-sql-didatica]]. Ele não conversa com o humano.

1. **Score do módulo (0 a 100):** soma dos pontos de autonomia ÷ (4 × itens) × 100, contando só a **última** tentativa de cada item. A checagem pesa 2. Itens `P` ficam fora da conta (não somam nem dividem); módulo só com `P` fica sem score. As extras (`X`) e as variantes das mini-aulas do avaliador (`MA-<erro>.<n>`) ficam fora do score do módulo e entram só na evolução.
2. **Evolução:** para cada item refeito, a diferença de pontos entre a primeira e a última tentativa. É o número que mostra o aprendizado.
3. **Score geral:** média dos módulos feitos, ponderada pelo número de itens.
4. **Erro recorrente:** código que aparece em 3 ou mais itens, em qualquer módulo.
5. **Faixa e tratativa:**

| Score do módulo | Faixa | Tratativa |
|---|---|---|
| < 50 | Reforço | nova aula do módulo por outro ângulo e operações-variantes (mesma técnica, outra tabela) antes de seguir |
| 50 a 74 | Consolidação | seguir, mas abrir as 2 próximas sessões com 1 variante dos itens C, D ou E |
| 75 a 89 | Pronto | seguir; o drill que o módulo prepara entra na retomada |
| ≥ 90 | Domínio | seguir; o módulo só volta como pergunta-relâmpago |

Erro recorrente vira uma **mini-aula de 5 min** com 3 variantes na sessão seguinte, seja qual for a faixa.

6. **Saída do agente:** uma tabela (módulo, score, faixa), o score geral, os erros recorrentes e a tratativa de cada um. O orquestrador grava a saída em "Histórico de scores" e põe a tratativa no "Onde parei" do diário.

**Quando o agente roda:** depois das checagens C2, C5 e C8, e sempre que o humano pedir.

## Registro
| Data | Item | Granularidade | Autonomia | Tentativas | Tempo | Erros | Nota da IA |
|---|---|---|---|---|---|---|---|
| 2026-11-06 | S2 (antes da trilha) | — | não tentou | — | — | NEGOCIO | Não sabia o que é crédito; isso mostrou a necessidade da trilha |
| 2026-11-06 12h00 | O0.1 | — | B | 2 | — | SINTAXE | Achou sozinho que `table_rows` vinha 0 em `alertas` contra 1.936 do `COUNT(*)`; errou a ordem `WHERE`/`ORDER BY`; não confirmou as 3 maiores com `COUNT(*)` |
| 2026-11-06 21h38 | O0.2 | — | P | — | — | — | Achou bobo; a IA explicou granularidade com o extrato bancário |
| 2026-11-06 21h48 | O0.3 | — | A | 1 | — | — | Consulta do `key_column_usage` com os dois filtros; entendeu por que há `NULL` (chave primária); ligação `pais_contraparte` dada pela IA |
| 2026-11-06 22h05 | O0.4 | — | P | — | — | — | Já domina `DISTINCT` |
| 2026-11-06 22h11 | O0.5 + O0.6 | — | A | 1 | — | SINTAXE | Período, hora e nulos numa consulta só, números certos; apelido repetido na última coluna |
| 2026-11-06 22h14 | C0 | — | P | — | — | — | Pulada por proposta da IA: o M0 ficou abaixo do nível; dúvidas foram de sintaxe e funções (`GROUP_CONCAT`), não de raciocínio |
| 2026-11-07 08h06 | O1.1 | — | A | 1 | — | — | Certo e já ordenado por risco; a IA explicou que `ENUM` ordena pela posição declarada, não pelo alfabeto |
| 2026-11-07 08h10 | O1.2 | — | C | 3 | 3 | SINTAXE | `COUNT(nome, risco_kyc)` deu erro de sintaxe; depois a lista sem ordem; com a explicação, saiu certa e formatada com `FORMAT(..., 'de_DE')` em apelido diferente da coluna, de propósito |
| 2026-11-07 08h25 | O1.3 | — | C | 2 | 6 | COND | Esqueceu `tipo = 'PIX'`; achou com a dica de olhar a coluna `tipo` no resultado |
| 2026-11-07 08h35 | O1.4 | — | C | 1 | 7 | DATA | A IA adiantou a explicação por engano; o humano provou no banco (5060 − 4911 = 149 do dia 31); usou `BETWEEN` até `'2026-02-01'`, que inclui a meia-noite do dia seguinte |
| 2026-11-07 08h43 | O1.5 | — | A | 1 | 8 | — | `IN` e `LIKE` certos (1469 e 292); perguntou de collation e de como forçar comparação sem diferenciar maiúsculas |
| 2026-11-07 10h05 | O1.6 | — | A | 1 | — | — | 156 abertos, ordem certa, `EXPLAIN` lido; não explicou por que `= NULL` dá 0 (a IA explicou) |
| 2026-11-07 10h12 | C1 | — | C | 3 | 5 | COND, SINTAXE | Faltavam `direcao = 'C'` e o fim do ano (`< '2027-01-01'`), resultado certo por sorte; depois `credito` no lugar de `direcao`; filtro sargable, colunas escolhidas e formatação certos sozinho |
| 2026-11-07 10h35 | O2.1 | — | A | 1 | 9 | — | Certo de primeira; perguntou como pôr a linha de total, e a IA ensinou `WITH ROLLUP`, `GROUP_CONCAT(DISTINCT ...)` e `COALESCE` (precisou de uma 2ª explicação, com as "caixas") |
| 2026-11-07 11h11 | O2.2 | certa | C | 3 | 4 | SINTAXE, COND | `GROUP BY (a, b)` entre parênteses (erro 1241, valor de linha); depois ordenou pelos rótulos e não pela contagem; com a explicação, `ORDER BY Total DESC` |
| 2026-11-07 12h39 | O2.3 | — | A | 1 | 1 | — | Quatro agregações certas; faltaram rótulo primeiro e apelidos; viu a concentração do `DEPOSITO_ESPECIE` perto do topo, e a IA ligou ao fracionamento (R02) |
| 2026-11-07 12h43 | O2.4 | — | C | 1 | 4 | GRAN | Leu `COUNT(DISTINCT analista)` como "alertas por analista" (são 6 analistas); `COUNT(*)` e `COUNT(coluna)` certos; não rodou antes de responder |
| 2026-11-07 12h48 | O2.5 | certa | D | 3 | 7 | COND, FILTRO | `WHERE` do falso positivo certo; esqueceu o "mais de 200"; disse que o `GROUP BY` filtra grupos e pôs o `SELECT` antes do `GROUP BY` na ordem de execução; com o esqueleto do `HAVING`, saiu (com `>=` no lugar de `>`) |
| 2026-11-07 13h03 | O2.6 | — | B | 2 | 7 | SINTAXE | `direcao = 'C'` e função de data fora do `WHERE` certos sozinho; `ORDER BY ASC` sem coluna |
| 2026-11-07 13h15 | C2 | — | B | 2 | 12 | — | `GROUP BY`, `HAVING` e `ORDER BY` certos sozinho; faltou a coluna `canal` no `SELECT` (números sem rótulo); não leu o que o `HAVING` escondeu (`CAIXA` e `AGENCIA`) |

As linhas do M3 em diante ficam em [[banco-mocado-plano-registro-sql-m3-a-m8]].

## Histórico de scores
| Data | Agente | Score geral | Módulos | Erros recorrentes | Tratativa |
|---|---|---|---|---|---|
| 2026-11-07 13h25 | avaliador, depois da C2 | 72,4 (55 ÷ 76) | M0 91,7 Domínio · M1 68,8 Consolidação · M2 68,8 Consolidação | `SINTAXE` (6 itens), `COND` (4 itens) | M3 e M4 abrem com 1 variante de um item C/D (O1.2, O1.3, O1.4, C1, O2.2, O2.4, O2.5) e com as mini-aulas de 5 min: `SINTAXE` (corrigir `SELECT regra_codigo COUNT(*) FROM alertas HAVING COUNT(*) > 200 GROUP BY regra_codigo`; PF com `risco_kyc IN ('MEDIO','ALTO')` e nome `LIKE 'A%'`; contas por `tipo_conta` ordenadas pelo apelido) e `COND` (créditos PIX acima de 50 mil em 2026, com checklist das 3 condições; falsos positivos da R05 ou R06 com `score_risco >= 70`, parênteses no `OR`; PJ de risco ALTO com `faturamento_anual` acima de 10 milhões). Nenhum item refeito ainda, sem evolução a medir |
| 2026-11-08 11h20 | avaliador, depois da C5 | 65,8 (100 ÷ 152) | M0 91,7 Domínio · M1 68,8 · M2 71,9 · M3 60,7 · M4 58,3 · M5 54,2 (M1 a M5 em Consolidação; M3 = 67,9 se a O3.4 otimizada ficar fora) | `SINTAXE` (13 itens), `COND` (13), `GRAN` (5), `DATA` (3) | Plano enxuto pedido pelo humano: sem mini-aulas de 3 variantes; checklist antes de rodar (vírgula antes do `FROM`, parênteses, `ROUND(x, 2)`, alias; Quem, O quê, Quando, Quanto, Quantos, Ordem); a `GRAN` treinada dentro do M6. Evolução: O2.5 +1, O3.2 +2, O5.3 +2, O3.4 −2 [a confirmar: se a O3.4 otimizada é o mesmo item]; recodificar a C5 com `FILTRO` e `DIV` [a confirmar] |

## Mudanças
- 2026-11-06: registro criado junto com a [[trilha-sql-didatica]] ([[geral-decisao-2026-11-06-trilha-didatica-antes-dos-drills]]).
- 2026-11-08: código `MA-<erro>.<n>` para as variantes das mini-aulas do avaliador, fora do score, como as extras.
- 2026-11-07: código de erro `COND` criado no catálogo: o M1 teve duas condições do enunciado esquecidas, e nenhum código existente descrevia isso.

### 🔗 Conexões
- Funcionalidade: [[banco-mocado-contexto]]
- Plano (nota original): [[banco-mocado-plano]]
- Trilha: [[trilha-sql-didatica]]
- Registro do M3 em diante: [[banco-mocado-plano-registro-sql-m3-a-m8]]
- Placar dos drills: [[banco-mocado-plano-evolucao]]
