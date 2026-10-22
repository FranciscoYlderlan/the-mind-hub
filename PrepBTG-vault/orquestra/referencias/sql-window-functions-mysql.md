---
aliases: [Window functions no MySQL, Funções de janela, SQL window functions, Padrões de SQL do treino]
tags: [estudos/programacao, carreira/entrevistas]
tipo: referencia
tema: treino
status: rascunho
criado: 2026-11-05
origem: 7 exemplos de window functions do humano (escritos em PostgreSQL), traduzidos pelo Claude para o MySQL 8.4 do `mysql-estudos` em 2026-11-05
---
# 🪟 Window Functions no MySQL (7 padrões)

> [!tldr] Em uma linha
> Os 7 padrões de janela do treino, já no dialeto do MySQL 8.4, com os ajustes que deixam cada um mais correto.

Uma window function é **a régua do lado do caderno**: mede cada linha sem arrancar a página. O `GROUP BY` resume o caderno inteiro numa linha; a janela mantém o detalhe e põe o agregado ao lado. Os padrões servem aos [[casos-de-treino-em-6-passos]] e aos [[roteiros-dos-cenarios-genericos]].

> [!note] Como explicar na entrevista
> 1. `PARTITION BY` define o grupo ("para cada cliente").
> 2. `ORDER BY` define a ordem dentro do grupo.
> 3. O frame (`ROWS` ou `RANGE ... BETWEEN`) define quais linhas entram no cálculo.
> 4. Diferença para `GROUP BY`: a janela não colapsa as linhas.
> 5. Famílias: ranking (`ROW_NUMBER`, `RANK`, `DENSE_RANK`, `NTILE`, `PERCENT_RANK`), deslocamento (`LAG`, `LEAD`) e agregação (`SUM`, `AVG`, `COUNT` com `OVER`).
> 6. Janela não entra no `WHERE` do mesmo nível: envolva numa CTE ou subquery.

> [!warning] Os exemplos originais eram PostgreSQL
> O banco do treino é MySQL 8.4. Troque assim:
>
> | PostgreSQL | MySQL 8.4 |
> |---|---|
> | `DATE_TRUNC('month', d)::date` | `DATE(DATE_FORMAT(d, '%Y-%m-01'))` |
> | `INTERVAL '24 hours'` | `INTERVAL 24 HOUR` |
> | `prox_data - data_hora <= INTERVAL '2 hours'` | `prox_data <= data_hora + INTERVAL 2 HOUR` |
> | `prox_data - data_hora` (duração) | `TIMESTAMPDIFF(MINUTE, data_hora, prox_data)` |
> | `generate_series` (calendário) | `WITH RECURSIVE` |
>
> `WINDOW w AS (...)`, `PERCENT_RANK`, `NTILE`, `LAG`, `LEAD` e `RANGE` com intervalo de data funcionam igual no MySQL 8.

---

## Padrão 1: últimas N por cliente (`ROW_NUMBER`)
```sql
SELECT *
FROM (
  SELECT cliente_id, transacao_id, tipo, valor, data_hora,
         ROW_NUMBER() OVER (PARTITION BY cliente_id ORDER BY data_hora DESC) AS rn
  FROM transacoes
) t
WHERE rn <= 3;
```
Troque o `ORDER BY` por `valor DESC` para as maiores. O mesmo molde deduplica: `PARTITION BY` na chave e `rn = 1` fica com a versão que vale (C7).

## Padrão 2: mês contra mês (`LAG`), sem buraco de mês
```sql
WITH RECURSIVE meses AS (
  SELECT DATE('2026-01-01') AS mes
  UNION ALL
  SELECT mes + INTERVAL 1 MONTH FROM meses WHERE mes < DATE('2026-10-01')
),
mensal AS (
  SELECT cliente_id, DATE(DATE_FORMAT(data_hora, '%Y-%m-01')) AS mes,
         SUM(valor) AS total_recebido
  FROM transacoes
  WHERE tipo = 'CREDITO'
  GROUP BY cliente_id, mes
),
grade AS (
  SELECT c.cliente_id, m.mes, COALESCE(x.total_recebido, 0) AS total_recebido
  FROM (SELECT DISTINCT cliente_id FROM mensal) c
  CROSS JOIN meses m
  LEFT JOIN mensal x ON x.cliente_id = c.cliente_id AND x.mes = m.mes
)
SELECT cliente_id, mes, total_recebido,
       LAG(total_recebido) OVER w AS mes_anterior,
       ROUND(total_recebido / NULLIF(LAG(total_recebido) OVER w, 0), 2) AS multiplo
FROM grade
WINDOW w AS (PARTITION BY cliente_id ORDER BY mes)
ORDER BY cliente_id, mes;
```
A `grade` resolve o cuidado do original: sem ela, o `LAG` pega o último mês **com dados**, não o mês anterior.

## Padrão 3: mês atual contra a média dos 3 anteriores e contra a renda
```sql
WITH mensal AS (
  SELECT cliente_id, DATE(DATE_FORMAT(data_hora, '%Y-%m-01')) AS mes,
         SUM(valor) AS total_recebido
  FROM transacoes
  WHERE tipo = 'CREDITO'
  GROUP BY cliente_id, mes
),
base AS (
  SELECT m.cliente_id, m.mes, m.total_recebido, c.renda_declarada,
         AVG(m.total_recebido) OVER hist AS media_3m,
         COUNT(*)              OVER hist AS meses_na_media
  FROM mensal m
  JOIN clientes c ON c.cliente_id = m.cliente_id
  WINDOW hist AS (PARTITION BY m.cliente_id ORDER BY m.mes
                  ROWS BETWEEN 3 PRECEDING AND 1 PRECEDING)
)
SELECT cliente_id, mes, total_recebido, ROUND(media_3m, 2) AS media_3m, renda_declarada,
       ROUND(total_recebido / NULLIF(media_3m, 0), 1)        AS x_historico,
       ROUND(total_recebido / NULLIF(renda_declarada, 0), 1) AS x_renda
FROM base
WHERE meses_na_media = 3
  AND total_recebido > 5 * media_3m
  AND total_recebido > 3 * renda_declarada
ORDER BY total_recebido - media_3m DESC;
```
O frame termina em `1 PRECEDING` para o próprio salto não "esconder" a anomalia. O `meses_na_media = 3` é o ajuste: no original, um cliente com 1 mês de histórico já entrava com média de 1 mês. Caso da Tabata (renda 2.000, média 2.100, mês 50.000): `x_historico` ≈ 23,8 e `x_renda` = 25.

## Padrão 4: ranking e percentil dentro do segmento
```sql
WITH mensal AS (
  SELECT cliente_id, SUM(valor) AS total_recebido
  FROM transacoes
  WHERE tipo = 'CREDITO'
    AND data_hora >= '2026-10-01' AND data_hora < '2026-11-01'
  GROUP BY cliente_id
),
ranking AS (
  SELECT c.segmento, m.cliente_id, m.total_recebido,
         RANK()         OVER (PARTITION BY c.segmento ORDER BY m.total_recebido DESC) AS posicao,
         PERCENT_RANK() OVER (PARTITION BY c.segmento ORDER BY m.total_recebido)      AS percentil
  FROM mensal m
  JOIN clientes c ON c.cliente_id = m.cliente_id
)
SELECT * FROM ranking
WHERE percentil >= 0.99
ORDER BY segmento, posicao;
```
Para faixas fixas, `NTILE(10)` (decis) no lugar do `PERCENT_RANK`. Segmento pequeno distorce percentil: conte os clientes por segmento antes.

## Padrão 5: fracionamento em 24 horas (janela por tempo)
```sql
WITH janela AS (
  SELECT cliente_id, transacao_id, data_hora, valor,
         COUNT(*)   OVER w AS qtd_24h,
         SUM(valor) OVER w AS soma_24h,
         MAX(valor) OVER w AS maior_24h
  FROM transacoes
  WHERE tipo = 'CREDITO'
  WINDOW w AS (PARTITION BY cliente_id ORDER BY data_hora
               RANGE BETWEEN INTERVAL 24 HOUR PRECEDING AND CURRENT ROW)
)
SELECT * FROM janela
WHERE qtd_24h >= 5
  AND soma_24h >= 50000
  AND maior_24h < 10000
ORDER BY soma_24h DESC;
```
`RANGE` conta tempo; `ROWS` conta linhas. Ajuste: no original, `valor < 10000` filtrava só a linha atual; o `maior_24h` garante que **todas** as transações da janela são pequenas. O mesmo cliente aparece em várias linhas seguidas: para a lista final, agrupe por cliente.

## Padrão 6: conta de passagem (`LEAD`)
```sql
WITH seq AS (
  SELECT cliente_id, transacao_id, tipo, valor, data_hora,
         LEAD(tipo)      OVER w AS prox_tipo,
         LEAD(valor)     OVER w AS prox_valor,
         LEAD(data_hora) OVER w AS prox_data
  FROM transacoes
  WINDOW w AS (PARTITION BY cliente_id ORDER BY data_hora)
)
SELECT cliente_id, transacao_id,
       valor AS valor_entrada, prox_valor AS valor_saida,
       data_hora AS data_entrada, prox_data AS data_saida,
       TIMESTAMPDIFF(MINUTE, data_hora, prox_data) AS minutos_ate_saida
FROM seq
WHERE tipo = 'CREDITO'
  AND prox_tipo = 'DEBITO'
  AND prox_data <= data_hora + INTERVAL 2 HOUR
  AND prox_valor >= 0.9 * valor
ORDER BY valor DESC;
```
Olha só a próxima transação. Saída dividida em várias: some os débitos numa janela por tempo, como no padrão 5.

## Padrão 7: contrapartes novas por mês
```sql
WITH primeiras AS (
  SELECT cliente_id, contraparte_id, data_hora,
         ROW_NUMBER() OVER (PARTITION BY cliente_id, contraparte_id ORDER BY data_hora) AS rn
  FROM transacoes
  WHERE tipo = 'CREDITO'
)
SELECT cliente_id, DATE(DATE_FORMAT(data_hora, '%Y-%m-01')) AS mes,
       COUNT(*) AS remetentes_novos
FROM primeiras
WHERE rn = 1
GROUP BY cliente_id, mes
ORDER BY remetentes_novos DESC;
```
O primeiro mês de cada cliente sempre tem "todo mundo novo": compare com os meses seguintes, não com zero.

> [!tip] Quando abrir esta nota
> Depois de tentar um caso sozinho, para conferir o padrão. Antes de rodar: nomes de coluna em [[roteiros-dos-cenarios-genericos]].

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** Janela = detalhe + agregado na mesma linha; partição, ordem e frame explicam qualquer uma.
* **Ponto 2:** No MySQL: `DATE_FORMAT`, `INTERVAL 24 HOUR`, `TIMESTAMPDIFF` e `WITH RECURSIVE`.
* **Ponto 3:** Três ajustes de correção: mês sem dado (padrão 2), histórico curto (padrão 3) e filtro só na linha atual (padrão 5).

### 🔗 Conexões
- Mapa: [[moc-orquestra]]
- Base: [[esqueleto-de-6-passos]]
- Relacionadas: [[casos-de-treino-em-6-passos]], [[roteiros-dos-cenarios-genericos]], [[questoes-por-cenario]]
