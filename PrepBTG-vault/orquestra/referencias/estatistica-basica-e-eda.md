---
aliases: [Estatística básica, Análise exploratória, EDA, Exploratory data analysis]
tags: [estudos/programacao]
tipo: referencia
tema: treino
status: em-uso
criado: 2026-11-05
origem: Dica do colega do time ([[relato-do-colega-do-time]]); decisão em [[geral-decisao-2026-11-05-trilha-sql-e-python]]
---
# 📊 Estatística Básica e Análise Exploratória

> [!tldr] Em uma linha
> Antes de qualquer regra, olhar os dados em Python: formato, nulos, duplicados, distribuição e um gráfico simples.

É **o check-up antes do treino na academia**: pressão, peso e histórico antes de montar a ficha. A análise exploratória (EDA) é o passo 1 e 2 do [[esqueleto-de-6-passos]] feito com dados. Treina no caso C8 de [[casos-de-treino-em-6-passos]].

---

> [!info] As 5 bibliotecas do `.venv`
> - **pandas:** tabelas em Python (DataFrame); recebe o resultado do SQL e faz a análise.
> - **matplotlib:** gráficos básicos; o `.plot()` do pandas usa ela por baixo.
> - **statsmodels:** estatística clássica; MAD para o z-score robusto e testes simples.
> - **duckdb:** banco analítico dentro do Python, sem servidor; consulta Parquet com SQL.
> - **pyarrow:** motor que lê e grava Parquet para o pandas.
> Em uma frase: o MySQL guarda, o SQL extrai, o pandas analisa, o matplotlib mostra, o statsmodels mede, e o pyarrow com o duckdb cuidam do Parquet.

> [!note] Roteiro da primeira olhada (caso C8)
> 1. **Formato:** `df.shape`, `df.dtypes`, `df.head()`.
> 2. **Nulos e duplicados:** `df.isna().sum()`, `df.duplicated(subset=[...]).sum()`.
> 3. **Resumo:** `df.describe(percentiles=[.5, .9, .99])`.
> 4. **Distribuição:** histograma e boxplot do `valor` em escala log.
> 5. **Outliers:** z-score robusto contra o histórico do cliente.
> 6. **Hipóteses:** 2 ou 3 frases do que parece estranho e qual regra testaria.

| Medida | O que diz | pandas / statsmodels |
|---|---|---|
| Média e mediana | Centro; se muito diferentes, há valores enormes puxando | `mean()`, `median()` |
| Desvio padrão | Quanto os valores se espalham em torno da média | `std()` |
| Percentis | "90% das transações ficam abaixo de X" | `quantile([.9, .99])` |
| z-score | Quantos desvios uma linha está da média | `(x - mean) / std` |
| MAD (desvio absoluto mediano) | O desvio padrão robusto a outliers | `statsmodels.robust.mad` |
| Resumo completo | Média, desvio, assimetria, curtose | `statsmodels.stats.descriptivestats.describe` |

> [!example] Esqueleto do gráfico
> ```python
> import numpy as np, matplotlib.pyplot as plt
> fig, ax = plt.subplots(1, 2, figsize=(10, 4))
> np.log10(df['valor']).hist(bins=50, ax=ax[0]); ax[0].set_title('log10(valor)')
> df.boxplot(column='valor', by='segmento', ax=ax[1]); ax[1].set_yscale('log')
> plt.tight_layout(); plt.show()
> ```

> [!warning] Armadilha
> Valor de transação é muito assimétrico: poucos valores enormes. Média e desvio padrão ficam distorcidos. Use **mediana, percentil e MAD** como referência e olhe em escala log. Saber dizer isso em voz alta conta ponto.

> [!tip] Quando abrir esta nota
> No começo de todo cenário com dados, antes da primeira regra.

## 🎒 Kit de bolso (aula de 2026-11-09)
Uma ideia = fórmula + analogia + custo em big data ([[geral-decisao-2026-11-09-modulo-rapido-de-estatistica]]).

| Medida | Fórmula | Analogia | ⚡ Big data |
|---|---|---|---|
| Média | Σ valores ÷ n | A conta do bar dividida igual: o champanhe de um infla todo mundo | Barata: cada nó soma a sua parte e depois junta |
| Mediana | O valor do meio da fila ordenada | O bilionário entra no bar e a mediana nem pisca | Cara: precisa ordenar tudo; na nuvem, versão aproximada |
| Desvio padrão (σ) | √(Σ(x − média)² ÷ n) | O batimento do cliente: estável = σ pequeno, o pico aparece | Barato (somas); calcular **por cliente**, nunca no banco inteiro |
| z-score | (x − média) ÷ σ; suspeito se > 3 | O radar: quantas vezes acima do limite **daquela** rua | CTE com `AVG` e `STDDEV` por cliente → `JOIN` → `valor > media + 3 * desvio` |
| Percentil e quartis | P90 = 90% abaixo; Q1 = P25, mediana = P50, Q3 = P75 | A fila por altura | Ordenar é caro: percentil aproximado ou tabela pré-agregada |
| Cerca do IQR | Q3 + 1,5 × (Q3 − Q1) | A turma do meio da fila; quem passa muito dela é suspeito | Não se deixa puxar pelos gigantes |

> [!example] Números de bolso (💸, histórico de um PF)
> - 800, 900, 1.000, 1.100, 1.200 → média 1.000, σ ≈ 141; um PIX de 9.000 dá z ≈ 57 → suspeito.
> - Com um 48.000 no histórico → média 8.833, mediana 1.050: a média não representa.
> - **Mascaramento:** o gigante no histórico infla o σ, e o z-score deixa de pegar o 9.000; a cerca do IQR continua pegando. Por isso, em dado assimétrico, a régua é mediana e IQR.

> [!info] Boxplot = foto aérea da fila por altura
> **Caixa** = os 50% do meio (de Q1 a Q3; largura = IQR). **Linha dentro** = mediana. **Bigodes** = até o menor e o maior valor dentro da cerca. **Pontos soltos** = além de Q3 + 1,5 × IQR, os candidatos a alerta. Caixa estreita = cliente previsível; mediana fora do centro ou um bigode mais comprido = assimetria. Um boxplot **por segmento** mostra que PF e PJ têm réguas diferentes.

> [!example] Resposta-modelo: analista que fecha alertas rápido demais (🚨)
> - **Régua de quem:** prazo (`DATEDIFF(data_encerramento, data_geracao)`, só encerrados, 12 meses) **por regra**; quem é julgado é o analista, contra os colegas na mesma regra.
> - **Assimétrico:** sim, poucos alertas parados por meses puxam a média; usar mediana.
> - **Régua:** a cauda é a **de baixo**; a cerca Q1 − 1,5 × IQR dá negativa em prazo, então a régua é o **P10** da regra. Por analista: % dos alertas abaixo do P10 (normal ≈ 10%). Agravante: rápido **e** `FALSO_POSITIVO`.
> - **Custo:** filtro sargable de 12 meses → CTE `prazos` → CTE `regua` (percentil aproximado, 8 linhas, vai inteira no `JOIN`) → `GROUP BY` analista com `SUM(CASE…)` e `100.0 *`.
> - Módulos que a questão puxa: M1, M2, M3, M5 e M6, mais a estatística.

> [!quote] Frase pronta
> "Fiz um boxplot do valor por segmento. A caixa é o comportamento normal (IQR) e o que passa de Q3 + 1,5 × IQR é outlier. Prefiro essa régua ao z-score porque valor de transação é assimétrico, e os quartis não se deixam puxar pelos gigantes."

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** SQL extrai, pandas explora: formato, nulos, duplicados, `describe`, gráfico.
* **Ponto 2:** z-score robusto (mediana e MAD) é mais uma régua de referência, ao lado de renda, histórico e pares.
* **Ponto 3:** Dado assimétrico pede mediana e escala log; média sozinha engana.

### 🔗 Conexões
- Mapa: [[moc-orquestra]]
- Decisão: [[geral-decisao-2026-11-05-trilha-sql-e-python]], [[geral-decisao-2026-11-09-modulo-rapido-de-estatistica]]
- Relacionadas: [[tratamento-de-nulos]], [[sql-window-functions-mysql]], [[casos-de-treino-em-6-passos]], [[relato-do-colega-do-time]]
