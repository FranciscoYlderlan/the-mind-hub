---
aliases: [Roteiros dos cenários 1 a 3, Cenários genéricos em 6 passos, Generic case scripts, Faturamento alertas e pipeline]
tags: [carreira/entrevistas, estudos/programacao]
tipo: referencia
tema: treino
status: rascunho
criado: 2026-11-05
origem: Os 3 cenários genéricos criados antes do banco mocado, fornecidos pelo humano em 2026-11-05; roteiro e SQL criados pelo Claude
---
# 🗺️ Roteiros dos Cenários Genéricos (1 a 3)

> [!tldr] Em uma linha
> Os cenários 1, 2 e 3 com o enunciado original, o roteiro dos 6 passos e consultas de exemplo no MySQL do banco mocado.

Cada roteiro é **um mapa de trilha**: mostra os pontos de parada, não anda por mim. As perguntas de cada passo são o que eu preciso responder; o SQL é a ferramenta para chegar lá. Base: [[esqueleto-de-6-passos]].

> [!warning] Não é o teste real
> Cenários genéricos criados antes do ambiente de teste. **Não são da vaga**: são sugestões de perguntas para treinar ([[cenarios-de-pratica]]).

> [!info] Antes de rodar qualquer SQL
> Os nomes de coluna abaixo são **assumidos** [a confirmar contra o `mysql-estudos`]. Rode primeiro `SHOW COLUMNS FROM compliance.transacoes;` (e das outras tabelas) e troque os nomes. Esse ajuste já é o passo 1: olhar o dado antes de supor.
>
> | Tabela | Colunas assumidas |
> |---|---|
> | `clientes` | `cliente_id`, `tipo_pessoa`, `segmento`, `cnae`, `porte`, `renda_declarada`, `faturamento_mensal`, `data_abertura`, `risco_kyc` |
> | `transacoes` | `transacao_id`, `cliente_id`, `tipo` (`CREDITO`/`DEBITO`), `valor`, `data_hora`, `contraparte_id` |
> | `alertas` | `alerta_id`, `regra_id`, `cliente_id`, `analista`, `status`, `desfecho`, `score_risco`, `data_alerta`, `data_encerramento` |
> | `stg_transacoes_bruto` | `sistema_origem`, `id_origem`, `data_evento_texto`, `valor_texto`, `recebido_em` |

---

## 1. 🏢 Faturamento incompatível (PJ)

> *"Temos uma base com milhões de empresas clientes. Queremos identificar aquelas cujo faturamento movimentado é incompatível com o porte, o CNAE e o histórico. Como você priorizaria quem o time de negócio deve analisar primeiro? Que sinais usaria e como explicaria cada alerta?"*

| Passo | O que eu preciso responder |
|---|---|
| 1. Esclarecer | "Faturamento movimentado" é só crédito? Inclui transferência entre contas do mesmo grupo? Que período? Faturamento declarado de quando? |
| 2. Referência | Três réguas: o **declarado** (x faturamento), o **histórico** da própria PJ (x média de 3 meses) e os **pares** (percentil no mesmo CNAE e porte). |
| 3. Simples | Um sinal por régua, com limite claro. Prioridade = quantos sinais + tamanho da diferença em reais. |
| 4. Explicável | Cada linha sai com o motivo em texto: "movimentou 12x o declarado; top 1% do CNAE". |
| 5. Medir | Quantas PJs por faixa de sinais? Quantas já tinham alerta? Quanto dos casos conhecidos a lista pega? |
| 6. Governar | Limites versionados, data de referência do cadastro, quem aprovou os pesos. |

```sql
-- Cenário 1: três réguas e o motivo de cada alerta (MySQL 8.4)
WITH mensal AS (
  SELECT t.cliente_id,
         DATE_FORMAT(t.data_hora, '%Y-%m-01') AS mes,
         SUM(t.valor) AS creditos
  FROM transacoes t
  JOIN clientes c ON c.cliente_id = t.cliente_id
  WHERE c.tipo_pessoa = 'PJ' AND t.tipo = 'CREDITO'
  GROUP BY t.cliente_id, mes
),
sinais AS (
  SELECT m.cliente_id, m.mes, m.creditos, c.cnae, c.porte, c.faturamento_mensal,
         m.creditos / NULLIF(c.faturamento_mensal, 0) AS x_declarado,
         m.creditos / NULLIF(AVG(m.creditos) OVER (
             PARTITION BY m.cliente_id ORDER BY m.mes
             ROWS BETWEEN 3 PRECEDING AND 1 PRECEDING), 0) AS x_historico,
         PERCENT_RANK() OVER (
             PARTITION BY c.cnae, c.porte, m.mes ORDER BY m.creditos) AS pct_pares
  FROM mensal m
  JOIN clientes c ON c.cliente_id = m.cliente_id
)
SELECT cliente_id, mes, creditos, faturamento_mensal,
       ROUND(x_declarado, 1) AS x_declarado,
       ROUND(x_historico, 1) AS x_historico,
       ROUND(pct_pares, 3)   AS pct_pares,
       (x_declarado >= 3) + (x_historico >= 5) + (pct_pares >= 0.99) AS qtd_sinais,
       CONCAT_WS('; ',
         IF(x_declarado >= 3, CONCAT('movimentou ', ROUND(x_declarado,1), 'x o faturamento declarado'), NULL),
         IF(x_historico >= 5, CONCAT(ROUND(x_historico,1), 'x a média dos 3 meses anteriores'), NULL),
         IF(pct_pares >= 0.99, 'top 1% do mesmo CNAE e porte', NULL)) AS motivo
FROM sinais
WHERE x_declarado >= 3 OR x_historico >= 5 OR pct_pares >= 0.99
ORDER BY qtd_sinais DESC, creditos - faturamento_mensal DESC;
```

> [!warning] Armadilha
> PJ grande e antiga com volume alto pode ser normal (a "isca" da Q1.4). Por isso a ordenação usa **quantidade de sinais** e não só o volume.

---

## 2. 🔔 Alertas demais, pouco valor

> *"O time de negócio reclama que a maior parte dos alertas gerados por uma regra de monitoramento é falso positivo. Como você investigaria o problema e reduziria o ruído sem deixar de capturar casos relevantes? Como mediria que melhorou?"*

| Passo | O que eu preciso responder |
|---|---|
| 1. Esclarecer | O que o time chama de falso positivo: "encerrado sem comunicação" ou "nem deveria ter disparado"? Qual regra, qual período? |
| 2. Referência | Taxa de falso positivo e precisão **por regra**, comparadas com as outras regras e com o próprio histórico mês a mês. |
| 3. Simples | Antes de trocar a regra: ajustar limite, excluir perfis óbvios (lista de exceção com dono e validade). |
| 4. Explicável | O alerta que sobra precisa trazer o motivo, para o analista não fechar no automático. |
| 5. Medir | Teste retroativo: com o novo limite, quantos alertas somem e **quantas comunicações ao COAF se perderiam**. |
| 6. Governar | Mudança de limite com antes/depois documentado, aprovação e data de vigência. |

```sql
-- Cenário 2a: retrato de cada regra
SELECT a.regra_id,
       COUNT(*) AS alertas,
       ROUND(AVG(a.desfecho = 'FALSO_POSITIVO'), 3)  AS taxa_fp,
       ROUND(AVG(a.desfecho = 'COMUNICADO_COAF'), 3) AS precisao,
       ROUND(AVG(DATEDIFF(a.data_encerramento, a.data_alerta)), 1) AS dias_medios
FROM alertas a
WHERE a.status = 'ENCERRADO'
GROUP BY a.regra_id
ORDER BY alertas DESC;

-- Cenário 2b: teste retroativo de três limites de score
WITH cortes AS (SELECT 0.3 AS corte UNION ALL SELECT 0.5 UNION ALL SELECT 0.7)
SELECT a.regra_id, c.corte,
       SUM(a.score_risco >= c.corte) AS alertas_que_ficam,
       SUM(a.score_risco <  c.corte AND a.desfecho = 'COMUNICADO_COAF') AS comunicados_perdidos
FROM alertas a
CROSS JOIN cortes c
WHERE a.status = 'ENCERRADO'
GROUP BY a.regra_id, c.corte
ORDER BY a.regra_id, c.corte;

-- Cenário 2c: analista fora da curva dentro da mesma regra
WITH por_analista AS (
  SELECT regra_id, analista, COUNT(*) AS qtd,
         AVG(desfecho = 'FALSO_POSITIVO') AS taxa_fp
  FROM alertas WHERE status = 'ENCERRADO'
  GROUP BY regra_id, analista
)
SELECT *, AVG(taxa_fp) OVER (PARTITION BY regra_id) AS media_da_regra
FROM por_analista
ORDER BY taxa_fp - AVG(taxa_fp) OVER (PARTITION BY regra_id) DESC;
```

> [!warning] Armadilha
> Reduzir volume é fácil: desliga a regra. A métrica que prova a melhora é **volume menor com zero comunicação perdida** no teste retroativo.

---

## 3. 🚰 Pipeline confiável

> *"Todo dia chegam transações de várias origens, em formatos diferentes, e alguns arquivos chegam atrasados ou duplicados. Como você desenharia o pipeline para que o dado seja confiável, auditável e reprocessável? Como saberia que algo quebrou?"*

| Passo | O que eu preciso responder |
|---|---|
| 1. Esclarecer | Quantas origens, que formatos, qual o atraso máximo aceitável, quem consome (regras em D+1?). |
| 2. Referência | A "verdade" de cada carga: contagem e soma esperadas por origem e dia (reconciliação). |
| 3. Simples | Camadas bruto → limpo → pronto. Chave única (`sistema_origem`, `id_origem`); a versão mais recente vence. |
| 4. Explicável | Linha rejeitada vai para quarentena com o motivo, nunca some; nulo crítico não se preenche ([[tratamento-de-nulos]]). Limpeza feita em SQL e em Python, com reconciliação. |
| 5. Medir | Volume por origem, atraso, % em quarentena, divergência na reconciliação. Alerta quando foge do normal. |
| 6. Governar | Toda carga com `carga_id`, horário e versão do código; reprocessar a mesma carga dá o mesmo resultado (idempotência); partição por mês permite reprocessar só o período afetado (Q3.10 a Q3.12). |

```sql
-- Cenário 3a: perfil da staging por origem
SELECT sistema_origem, COUNT(*) AS linhas,
       COUNT(DISTINCT id_origem) AS ids_distintos,
       SUM(valor_texto IS NULL OR valor_texto = '') AS sem_valor,
       MIN(recebido_em) AS primeira, MAX(recebido_em) AS ultima
FROM stg_transacoes_bruto
GROUP BY sistema_origem;

-- Cenário 3b: duplicados e a versão que vale
WITH versoes AS (
  SELECT s.*,
         ROW_NUMBER() OVER (PARTITION BY sistema_origem, id_origem
                            ORDER BY recebido_em DESC) AS versao,
         COUNT(*)     OVER (PARTITION BY sistema_origem, id_origem) AS envios
  FROM stg_transacoes_bruto s
)
SELECT * FROM versoes
WHERE envios > 1
ORDER BY sistema_origem, id_origem, versao;   -- versao = 1 é a que vale

-- Cenário 3c: datas em formatos diferentes (NULL = vai para quarentena)
SELECT data_evento_texto,
       COALESCE(STR_TO_DATE(data_evento_texto, '%Y-%m-%d %H:%i:%s'),
                STR_TO_DATE(data_evento_texto, '%d/%m/%Y %H:%i'),
                STR_TO_DATE(data_evento_texto, '%Y%m%d%H%i%s')) AS data_evento
FROM stg_transacoes_bruto
LIMIT 50;

-- Cenário 3d: reconciliação staging limpa x transacoes
SELECT 'stg_limpa' AS fonte, COUNT(*) AS linhas, SUM(valor) AS total FROM stg_limpa
UNION ALL
SELECT 'transacoes', COUNT(*), SUM(valor) FROM transacoes;

-- Cenário 3e: carga idempotente (rodar duas vezes não duplica)
-- pré-requisito: UNIQUE KEY (sistema_origem, id_origem) em stg_limpa
INSERT INTO stg_limpa (sistema_origem, id_origem, data_evento, valor, carga_id)
SELECT sistema_origem, id_origem, data_evento, valor, @carga_id
FROM stg_preparada
ON DUPLICATE KEY UPDATE data_evento = VALUES(data_evento),
                        valor = VALUES(valor),
                        carga_id = VALUES(carga_id);
```

> [!warning] Armadilha
> `STR_TO_DATE` devolve `NULL` quando o formato não bate. Contar esses `NULL` por origem é o jeito mais simples de saber que **um sistema mudou de formato** ([[questoes-por-cenario#3. Pipeline confiável (dados atrasados, duplicados e em formatos diferentes)|Q3.9]]).

> [!tip] Quando abrir esta nota
> Ao treinar os cenários 1, 2 ou 3 (T1, T2 e T3 do [[banco-mocado-plano]]), **depois** de tentar o passo 1 sozinho.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** Cenário 1 = três réguas (declarado, histórico, pares) e o motivo em texto.
* **Ponto 2:** Cenário 2 = precisão por regra e teste retroativo que conta as comunicações perdidas.
* **Ponto 3:** Cenário 3 = chave única, versão mais recente, quarentena com motivo e carga idempotente.

### 🔗 Conexões
- Mapa: [[moc-orquestra]]
- Base: [[esqueleto-de-6-passos]]
- Relacionadas: [[cenarios-de-pratica]], [[questoes-por-cenario]], [[sql-window-functions-mysql]], [[banco-mocado-contexto]]
- Próxima: [[casos-de-treino-em-6-passos]]
