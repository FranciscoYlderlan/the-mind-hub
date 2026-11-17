---
aliases: [Conversa com o colega do BTG, Dicas de quem está no time, Insider tips, O que o time usa no dia a dia]
tags: [carreira/entrevistas]
tipo: referencia
tema: vaga
status: em-uso
criado: 2026-11-05
origem: Conversa do humano com um colega que trabalha no time da vaga (relato em áudio transcrito, 2026-11-05)
---
# 🗣️ Relato do Colega do Time

> [!tldr] Em uma linha
> Quem está no time da vaga trabalha assim: SQL para consultar, Python para explorar, limpar e analisar, com estatística básica e gráfico simples.

É **a dica de quem já jogou a fase**: não entrega o mapa inteiro, mas diz onde está a armadilha. O humano confirmou que o colega é **do time da vaga** ([[vaga-compliance-engineering]]), então o relato pesa mais que a leitura da descrição.

---

> [!note] O que ele falou (fatos do relato)
> 1. Treinar com um dataset fictício guardado em algum formato rápido, como **Parquet**, e consultar em cima dele.
> 2. Limpar dados **só com SQL** e também **com Python**, para mostrar que sabe mexer com dados.
> 3. Saber usar **COALESCE** (quando o dado não vem).
> 4. **Partição**: ele usava muito no Oracle; "o pessoal ganha um pontinho".
> 5. **Estatística básica**: desvio padrão, como os dados estão organizados; biblioteca **statsmodels**.
> 6. **Gráfico simples**, só para enxergar os dados.
> 7. No dia a dia dele: **análise exploratória toda em Python; SQL só para consulta**.

> [!info] Para onde cada ponto foi
> | Ponto | Decisão | Onde treinar |
> |---|---|---|
> | 2, 5, 6, 7 | [[geral-decisao-2026-11-05-trilha-sql-e-python]] | [[estatistica-basica-e-eda]], caso C8 de [[casos-de-treino-em-6-passos]] |
> | 1, 4 | [[geral-decisao-2026-11-05-parquet-e-particao]] | Q3.10 a Q3.12 de [[questoes-por-cenario]] |
> | 3 | [[geral-decisao-2026-11-05-nulos-vao-para-quarentena]] | [[tratamento-de-nulos]] |

> [!tip] Quando abrir esta nota
> Antes do estudo de caso real, para lembrar o que o time valoriza no dia a dia.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** O fluxo do time é SQL extrai, Python analisa: mostrar os dois na mesma solução.
* **Ponto 2:** Parquet, partição e COALESCE são vocabulário do dia a dia: usar com naturalidade.
* **Ponto 3:** Estatística básica e um gráfico simples fecham a análise; não precisa de modelo sofisticado.

### 🔗 Conexões
- Mapa: [[moc-orquestra]]
- Relacionadas: [[vaga-compliance-engineering]], [[esqueleto-de-6-passos]], [[banco-mocado-plano]]
