---
aliases: [SQL de prova, Drills de SQL, Treino rápido de SQL, SQL drills]
tags: [carreira/entrevistas, estudos/programacao]
tipo: referencia
tema: treino
status: rascunho
criado: 2026-11-06
origem: Criadas pelo Claude em 2026-11-06 para o formato de teste relatado por Petterson ([[processo-seletivo-btg]]), usando o banco `mysql-estudos`
---
# ⏱️ Questões de SQL de Prova (com tempo)

> [!tldr] Em uma linha
> Dezoito exercícios curtos de SQL, com tempo-alvo, cobrindo as técnicas que mais caem em prova, todos no banco `compliance`.

As questões de [[questoes-por-cenario]] são **o treino de jogo**; estas são **o treino de fundamento**: passe, chute, cabeceio. Em prova, o tempo some na técnica que você não tem automática. Os padrões de janela estão em [[sql-window-functions-mysql]].

> [!warning] Regras do drill
> - Cronômetro ligado. Estourou o tempo-alvo: anote quanto levou e siga.
> - Escreva primeiro **sem rodar** (como se fosse no papel), depois rode e corrija. Contam as duas notas.
> - Antes de rodar, diga: qual é a granularidade do resultado (uma linha por quê?).

## Nível 1: base (alvo 4 min cada)
- **S1.** Quantidade de clientes por tipo (PF/PJ) e por nível de risco, ordenado do maior para o menor.
- **S2.** Os 10 clientes com maior soma de créditos em 2026.
- **S3.** Clientes que **nunca** geraram alerta (anti-join: `LEFT JOIN ... IS NULL` e `NOT EXISTS`, as duas formas).
- **S4.** Regras com mais de 100 alertas fechados como falso positivo (`HAVING`).
- **S5.** Classifique as transações em faixas de valor com `CASE` e conte quantas há em cada faixa.
- **S6.** Percentual de alertas por desfecho dentro de cada regra (soma 100% por regra).

## Nível 2: intermediário (alvo 7 min cada)
- **S7.** Para cada cliente, a maior transação e a data dela (`ROW_NUMBER` ou subconsulta correlacionada).
- **S8.** Top 3 clientes por volume **dentro de cada** nível de risco (janela com `PARTITION BY`).
- **S9.** Volume mensal por cliente e a variação contra o mês anterior (`LAG`).
- **S10.** Saldo acumulado das movimentações de uma conta ao longo do tempo (`SUM() OVER`).
- **S11.** Clientes de risco ALTO sem revisão de KYC há mais de 24 meses (`TIMESTAMPDIFF`), tratando data nula com `COALESCE`.
- **S12.** Remessas para países de `paises_risco` com o nome do cliente e do país (três tabelas no `JOIN`).

## Nível 3: cara de case (alvo 12 min cada)
- **S13.** Deduplicar a `stg_transacoes_bruto`: uma linha por transação, ficando com a versão mais recente (`ROW_NUMBER` em CTE).
- **S14.** PF com 3 ou mais depósitos em espécie entre R$ 8 mil e R$ 10 mil em qualquer janela de 7 dias (self-join ou janela por intervalo).
- **S15.** Sócios que aparecem em mais de uma PJ e a soma do volume dessas PJs.
- **S16.** Por analista: alertas fechados e uma aproximação da mediana e do p90 do tempo de encerramento (no MySQL não há `PERCENTILE_CONT`: usar `NTILE` ou `PERCENT_RANK`).
- **S17.** Taxa de alerta que virou comunicação ao COAF por regra e por mês, só para regras com pelo menos 20 alertas no mês.
- **S18.** Reconciliar duas tabelas: contagem e soma por dia na staging limpa e em `transacoes`, mostrando só os dias que divergem (`FULL OUTER JOIN` não existe no MySQL: usar `UNION`).

> [!info] Erros que derrubam nota em prova
> `JOIN` que duplica linhas e infla a soma · `COUNT(*)` contando nulo de `LEFT JOIN` · filtro do lado direito no `WHERE` que vira `INNER JOIN` · `GROUP BY` sem todas as colunas não agregadas · divisão inteira no percentual · data com hora cortando o último dia do intervalo.

> [!tip] Quando abrir esta nota
> Na retomada (T8, fase B, do [[banco-mocado-plano]]), depois dos módulos da [[trilha-sql-didatica]] e da [[trilha-sql-didatica-avancado]].

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** Fundamento antes de case: janela, anti-join, CTE e agregação condicional precisam sair sem pensar.
* **Ponto 2:** Escrever sem rodar primeiro simula o teste e mostra a lacuna real.
* **Ponto 3:** Granularidade dita em voz alta antes de rodar evita o erro mais comum, a soma inflada por `JOIN`.

### 🔗 Conexões
- Mapa: [[moc-orquestra]]
- Relacionadas: [[trilha-sql-didatica]], [[questoes-por-cenario]], [[sql-window-functions-mysql]], [[questoes-tomada-de-decisao]], [[banco-mocado-contexto]]
- Próxima: [[banco-mocado-plano-evolucao]]
