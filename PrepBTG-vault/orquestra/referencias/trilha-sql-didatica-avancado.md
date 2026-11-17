---
aliases: [Trilha de SQL avançada, Módulos M5 a M8, Janelas e CTE na prática, Advanced SQL path]
tags: [carreira/entrevistas, estudos/programacao]
tipo: referencia
tema: treino
status: em-uso
criado: 2026-11-06
origem: Criada pelo Claude em 2026-11-06 a pedido do humano, depois do S2 de [[questoes-sql-de-prova]] mostrar a necessidade de revisar SQL; perfil lido no Vault (Quem Sou Eu, AuDHD, Atenção em túnel, Cronotipo matutino, Pomodoro Curto 15-5, Sensibilidade à rejeição)
---
# 🧗 Trilha Didática de SQL: Avançado

> [!tldr] Em uma linha
> Os módulos M5 a M8 da [[trilha-sql-didatica]] (lógica, CTE, janelas e cara de case) e a retomada dos drills.

Esta parte é como **cozinhar depois de saber cortar e refogar**. Com a base dos módulos M0 a M4, as receitas compostas são só técnicas conhecidas em outra ordem. O formato de sessão é o mesmo da primeira nota, com 5 questões por módulo e uma bônus ([[geral-decisao-2026-11-08-cinco-questoes-e-bonus]]).

---

### M5. Lógica e datas (`CASE`, `COALESCE`, percentual, datas)
**Aprendo:** `CASE WHEN` para criar categorias; agregação condicional; percentual com `ROUND` e sem divisão inteira; `COALESCE` para nulo; `DATEDIFF`, `TIMESTAMPDIFF` e `DATE_FORMAT`; `CURDATE()` e `INTERVAL` para montar a linha de corte de um filtro sargable.
- **O5.1** Faixas de valor com `CASE` (até 1 mil, até 10 mil, até 50 mil, acima) e a contagem de cada faixa. → S5
- **O5.2** Agregação condicional e percentual: por regra, `SUM(CASE WHEN desfecho = 'FALSO_POSITIVO' THEN 1 ELSE 0 END)` e o percentual de cada desfecho com `ROUND` (no MySQL, `/` já dá decimal; `DIV` corta). → S6
- **O5.3** `TIMESTAMPDIFF(MONTH, ...)`: clientes de risco ALTO sem revisão de KYC há mais de 24 meses. → S11
- **O5.4** `DATEDIFF` e `COALESCE`: dias entre geração e encerramento de cada alerta, com o analista nulo como `'SEM_ANALISTA'`.
- **Checagem:** percentual de transações em espécie por `segmento` do cliente.
- **Bônus:** média de dias até o encerramento por `desfecho` e o percentual encerrado em até 30 dias.

### M6. Organizar com CTE (`WITH`)
**Aprendo:** `WITH` como "tabela temporária com nome"; encadear CTEs; filtrar sobre um agregado; quando a subconsulta no `FROM` basta.
- **O6.1** Reescrever a O3.4 como CTE `creditos_2026`.
- **O6.2** Duas CTEs encadeadas: créditos de 2026 por conta e por cliente; depois a razão créditos ÷ renda anual dos PF, com 2 casas (um sinal de PLD; os 7 PF sem renda ficam com razão nula).
- **O6.3** Filtro sobre o agregado da CTE: clientes PJ com volume anual acima do `faturamento_anual`.
- **O6.4** A mesma consulta como subconsulta no `FROM` e como CTE: qual se lê melhor?
- **Checagem:** por regra e mês, alertas gerados e quantos viraram COMUNICADO_COAF. → S17
- **Bônus:** a mesma checagem com a taxa de comunicação em percentual, com o `ROUND` do M5.

### M7. Funções de janela (`OVER`)
Apoio: [[sql-window-functions-mysql]].
**Aprendo:** a diferença entre agrupar e janelar (a janela não junta linhas); `OVER`, `PARTITION BY` e `ORDER BY` da janela; `ROW_NUMBER`, `RANK`, `DENSE_RANK`; `LAG`; soma acumulada; converter texto com `STR_TO_DATE` e `CAST`; particionamento de tabela (`PARTITION BY RANGE`, uma partição por mês, poda de partições no `EXPLAIN`) para big data, ao lado do `PARTITION BY` da janela.
- **O7.1** `PARTITION BY`: numerar as transações de cada cliente da maior para a menor e ficar com a 1ª. → S7
- **O7.2** Top 3 clientes por volume dentro de cada nível de risco, com `ROW_NUMBER`, `RANK` e `DENSE_RANK` lado a lado: o que muda nos empates? → S8
- **O7.3** `LAG` e soma acumulada: volume mensal por cliente, o mês anterior e o acumulado com `SUM() OVER (ORDER BY ...)`. → S9, S10
- **O7.4** Converter texto da `stg_transacoes_bruto` (`STR_TO_DATE`, `CAST`) e deduplicar com `ROW_NUMBER` em CTE. → S13
- **Checagem:** a segunda maior transação de cada cliente PJ.
- **Bônus:** a variação percentual do volume mensal contra o mês anterior (`LAG` e `ROUND`).

### M8. Cara de case
**Aprendo:** self-join (a tabela com ela mesma); janela por intervalo de tempo; `NTILE` e `PERCENT_RANK`; `UNION` e `UNION ALL`; montar uma consulta grande em CTEs pequenas.
- **O8.1** Transações da mesma conta com até 7 dias de diferença, de dois jeitos: self-join e janela por intervalo, `COUNT(*) OVER (PARTITION BY ... ORDER BY data_hora RANGE BETWEEN INTERVAL 7 DAY PRECEDING AND CURRENT ROW)` (roda no MySQL 8; na cópia da IA, a conferência é pelo self-join). → S14
- **O8.2** Sócios em mais de uma PJ: `COUNT(DISTINCT cliente_pj_id) > 1`. → S15
- **O8.3** `NTILE(10)` e `PERCENT_RANK` para aproximar mediana e p90. → S16
- **O8.4** `UNION` e `UNION ALL`; simular `FULL OUTER JOIN`. → S18
- **Checagem:** clientes PJ com 3 ou mais créditos PIX acima de R$ 40 mil em 7 dias.
- **Bônus:** contrapartes que aparecem em `lista_restritiva` pelo nome ou pelo documento, as duas buscas unidas com `UNION`.

---

## Depois da trilha: a retomada
Com os 9 módulos feitos, volto aos drills de [[questoes-sql-de-prova]], de S1 a S18, escritos **sem rodar** primeiro e com tempo. A nota de cada um vai para o placar de [[banco-mocado-plano-evolucao]].

| Drill | Módulos que preparam |
|---|---|
| S1, S4 | M2 |
| S2, S12 | M1, M3 |
| S3 | M4 |
| S5, S6, S11 | M5 |
| S7 a S10, S13 | M6, M7 |
| S14 a S18 | M6, M7, M8 |

> [!info] Se o tempo apertar
> Até o teste, a ordem de corte é: M8 inteiro (fica só a ideia de cada técnica), depois o acumulado da O7.3 e os empates da O7.2. M0 a M5 nunca saem: eles cobrem os drills de nível 1 e a base de todo o resto.

> [!tip] Quando abrir esta nota
> Depois da checagem do M4, e para saber qual módulo prepara cada drill na retomada.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** CTE organiza; janela calcula sem juntar linhas.
* **Ponto 2:** Os drills de nível 3 são técnicas dos módulos anteriores combinadas em CTEs pequenas.
* **Ponto 3:** Erro comum: pular para janela (M7) sem `JOIN` e `GROUP BY` automáticos.

### 🔗 Conexões
- Mapa: [[moc-orquestra]]
- Relacionadas: [[trilha-sql-didatica-extras]], [[sql-window-functions-mysql]], [[questoes-sql-de-prova]], [[banco-mocado-plano-evolucao]]
- Próxima: [[questoes-sql-de-prova]]
- Nota original: [[trilha-sql-didatica]]
