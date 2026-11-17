---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-09
substitui: 
aliases: [Revisão do dia do teste, Revisão leve M0 a M8, Três cenários reaproveitados, Fórmula da resposta]
---
# ✅ Revisão do dia do teste: reaula de M5 e M7, depois M0 a M8 leve, com 3 cenários fixos

- **Proposta (plano):** pedido do humano no chat de 2026-11-09, 05h58, depois do simulado de ontem com um amigo (nota 7: conhecia os conceitos, mas faltaram cenários de big data para usar de exemplo nas respostas).
- **Decisão:**
  1. **Prazo:** teste hoje às 15h; tudo concluído até **10h30**, para sobrar tempo de descanso e preparo. Blocos do Pomodoro Curto 15-5.
  2. **Ordem e profundidade:**
     - **M5 e M7: reaula didática completa**, porque o humano sentiu dificuldade e não se sentiu à vontade com o assunto. Não é revisão leve: aula em passos pequenos, uma ideia por vez, com tabela de brinquedo quando ajudar, exemplo resolvido em um dos 3 cenários. Pelo tempo do dia, o número de perguntas é reduzido sem perder o didático: **4 ideias por módulo, cada uma aberta por uma analogia do cotidiano**, **2 checagens curtas** por módulo (nas ideias que mais caem) e, no fim, **exercícios obrigatórios que juntos cobrem todos os conceitos do módulo** (no M5 foram 3, cada um combinando mais de uma ideia). A aula curta do M5 dada no chat de planejamento não conta como reaula.
     - **M0, M1, M2, M3, M4, M6 e M8: revisão didática leve**, em poucas linhas por módulo, mas ainda didática (o que é, para que serve, exemplo curto no cenário).
  3. **Por módulo na revisão (M0, M1, M2, M3, M4, M6 e M8):** poucas linhas de aula, **1 questão só por módulo**, sem extra, para andar mais rápido (pedido do humano em 2026-11-09, 10h20), **discursiva e sem código**: o humano explica em palavras a linha de raciocínio e as operações que faria para resolver o problema, porque a sintaxe já está firmada (pedido de 10h25); a IA corrige o raciocínio, não a sintaxe; e sempre uma linha **⚡ Big data**: por que usar a técnica e que problema ela resolve, no contexto do BTG, só com o que já foi estudado (item 11). Barra de progresso no formato fixo de [[geral-decisao-2026-11-06-progresso-a-cada-questao]], com 1 bloco por módulo (8 no total: M0, M1, M2, M3, M4, M6, M5 e M7). Depois da reaula, **M5 e M7 também entram na revisão leve**, por último, com o mesmo formato (aula curta e 1 questão discursiva), a pedido do humano em 2026-11-09, 11h26.
  4. **Três cenários fixos**, reaproveitados em todas as técnicas (nenhum cenário novo, para não encher a cabeça):
     - 💸 **PIX fracionado** (`transacoes`): milhões de PIX por dia; um cliente quebra R$ 200 mil em vários PIX de R$ 9 mil para fugir do alerta.
     - 🚨 **Fila de alertas** (`alertas`): milhares de alertas; qual regra só gera falso positivo e quanto tempo leva para fechar.
     - 📥 **Carga bruta** (`stg_transacoes_bruto`): dados de vários sistemas como texto, com espaços, duplicados e datas em formatos diferentes.
  5. **Fórmula da resposta na prova:** "No cenário X, o problema é Y. Uso a técnica Z porque, em big data, ela W." O **W** diz o **custo** da técnica (o que ela lê, reduz ou embaralha), não só o que ela faz. Exemplo: "No PIX fracionado, o problema é achar soma alta feita de valores pequenos. Filtro pela partição do mês, reduzo com `GROUP BY` para cliente/dia e só então aplico a janela de 7 dias, porque a janela não reduz linhas e, sobre o bruto, embaralharia e ordenaria bilhões de registros."
  6. **Onde cada conteúdo entra na revisão:**

| Conteúdo | Módulo |
|---|---|
| Sargable: função na coluna contra linha de corte calculada uma vez | M1, retomado no M5 com `INTERVAL` |
| Ordem de execução e precedência: a ordem lógica das cláusulas e as funções aninhadas de dentro para fora (ex.: `COUNT(DISTINCT TRIM(col))`) | M2 |
| Resumir antes de juntar (item 7 de [[geral-decisao-2026-11-07-solucao-performatica-big-data]]) | M3 |
| Funções de linha e como iterar sobre elas: `CAST`, `TRIM`, `COALESCE`, `NULLIF`, `LEAST`/`GREATEST` (min e max na linha) contra `MIN`/`MAX` (agregação), no cenário 📥 | M5 |
| Tabela pré-agregada: a CTE organiza, a pré-agregada persiste | M6 |
| `PARTITION BY` da tabela contra o da janela (a diferença e o porquê de cada um); reduzir antes de janelar; `FIRST_VALUE`/`LAST_VALUE` (o MySQL não tem `FIRST()`/`LAST()` de agregação); deduplicar com `ROW_NUMBER` | M7 |
| Estatística: média, desvio padrão, mediana, quartis, percentil e outliers num subconjunto (IQR e z-score); funções aproximadas (`APPROX_COUNT_DISTINCT`, `approx_percentile`) | M8 |

  7. **Contexto de big data por módulo** (a linha ⚡ de cada módulo responde "por que usar e que problema resolve no BTG"). O porquê geral: o BTG lida com **volume** (milhões de PIX por dia e anos de histórico para PLD), **velocidade** (monitoramento contínuo e prazo regulatório de comunicação ao COAF), **variedade** (vários sistemas de origem, dado chegando como texto) e **custo** (motor de nuvem cobra pelo dado lido). Os problemas que a técnica certa resolve: achar fracionamento no meio de bilhões de PIX, reduzir a fila de falso positivo, achar KYC vencido de cliente de risco alto e unificar fontes sujas.

| Módulo | Ponto de big data | Cenário |
|---|---|---|
| M0 | Descobrir sem varrer: metadados (`information_schema`, `table_rows` aproximado) e amostra com `LIMIT` ou uma partição antes de `COUNT(*)` na tabela inteira | 💸 |
| M1 | Sargable (coluna crua contra intervalo), **poda de partição** pela data e colunas escolhidas em vez de `SELECT *` (armazenamento colunar só lê o que pede) | 💸 |
| M2 | O `GROUP BY` escala (agregação parcial em cada nó antes do shuffle); `COUNT(DISTINCT)` de alta cardinalidade é o caro, e a saída é aproximar | 🚨 |
| M3 | Resumir antes de juntar; a tabela pequena (contas, regras) vai inteira para cada nó (broadcast join); o garfo infla a soma | 💸 |
| M4 | Anti-join com `NOT EXISTS` (o motor para no primeiro achado); `NOT IN` com nulo devolve vazio; lista literal enorme no `IN` contra subconsulta | 🚨 |
| M5 | Agregação condicional faz **uma leitura só** no lugar de várias consultas; linha de corte com `INTERVAL` mantém o filtro sargable | 🚨 |
| M6 | A CTE organiza mas não otimiza; a **tabela pré-agregada** (resumo diário por cliente) persiste e evita varrer o bruto a cada consulta | 💸 |
| M7 | A janela não reduz linhas (embaralha e ordena tudo, risco de skew): **reduzir antes de janelar**; o `PARTITION BY` da tabela poda leitura, o da janela só agrupa o cálculo | 💸 📥 |
| M8 | Self-join por intervalo explode (cada linha contra muitas) e a janela por intervalo lê uma vez; estatística exata (mediana, percentil) é cara e as funções aproximadas resolvem; `UNION ALL` evita a ordenação de deduplicar do `UNION` | 💸 🚨 |

  8. **Formato dos exercícios (todos os módulos):** enunciado **no estilo da prova**, em linguagem de negócio, com **todo** requisito (filtros, prazos, recortes) escrito no próprio texto e **sem** dica de técnica, filtro ou esqueleto; escolher o caminho é parte do exercício. Pedido do humano em 2026-11-09, 08h13. Na revisão leve, a resposta é discursiva (item 3).
  9. **Analogia na abertura** de cada ideia e de cada explicação de peça nova, porque deixa a ideia clara e visual (pedido do humano em 2026-11-09, 06h26).
  10. **Ordem de execução em todo exemplo de código:** sempre que possível, numerar a ordem lógica em que a consulta roda, **em uma linha resumida, nunca em tabela** (pedido do humano em 2026-11-09, 08h48 e 08h52): `WITH → FROM → JOIN/ON → WHERE → GROUP BY → agregações → HAVING → janelas (OVER) → SELECT (apelidos) → DISTINCT → ORDER BY → LIMIT`. Funções aninhadas são lidas e pontuadas **de dentro para fora** (ex.: em `SUM(SUM(valor)) OVER ()`, o `SUM` de dentro é agregação e o de fora é janela).
  11. **Tom da revisão leve de M0 a M8:** leveza e consolidação, um módulo por vez, em linguagem didática. **Nada de conteúdo além da primeira passagem da trilha**: a aula, a questão e a linha ⚡ só usam técnicas e funções que o humano já estudou; ponto do quadro do item 7 que não foi visto fica de fora. Quando houver um caminho mais simples já conhecido (ex.: subconsulta do total no lugar de `SUM(COUNT(*)) OVER ()`), ele é o caminho da revisão. Objetivo: chegar ao teste calmo, sem a sensação de que falta matéria (pedido do humano em 2026-11-09, 09h43 e 09h49). A única exceção do dia é o módulo rápido de estatística, pedido explícito do humano às 11h56 ([[geral-decisao-2026-11-09-modulo-rapido-de-estatistica]]).
- **Motivo:** no simulado, o conceito estava certo e a nota caiu por falta de exemplo concreto; cenários poucos e repetidos mostram o mesmo problema resolvido por técnicas diferentes, o que ajuda a comparar sem sobrecarregar (Atenção em túnel, no Vault).
- **Consequências:** a questão única por módulo da revisão leve e os exercícios reduzidos de M5 e M7 valem só para hoje; a regra de 5 questões e bônus ([[geral-decisao-2026-11-08-cinco-questoes-e-bonus]]) continua para a trilha normal. A linha ⚡ Big data segue o item 8 de [[geral-decisao-2026-11-07-solucao-performatica-big-data]].

### 🔗 Conexões
- Funcionalidade: [[banco-mocado-contexto]]
- Trilha: [[trilha-sql-didatica]], [[trilha-sql-didatica-avancado]]
- Projeto: [[geral-contexto]]
- Diário: [[diario-2026-11-09]]
- Seguinte: [[geral-decisao-2026-11-09-modulo-rapido-de-estatistica]]
