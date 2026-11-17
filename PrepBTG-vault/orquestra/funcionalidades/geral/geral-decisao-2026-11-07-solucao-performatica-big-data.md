---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-07
substitui: 
aliases: [Solução performática, Pensar em big data, Consulta otimizada, Big data first]
---
# ✅ Toda solução já na versão performática, pensando em big data

- **Proposta (plano):** pedido direto do humano no M1 de [[trilha-sql-didatica]] (2026-11-07, 08h47): "sempre pontue big data [...] desde já sempre as ações mais performáticas".
- **Decisão:** mesmo com o banco pequeno e os módulos introdutórios, toda solução de SQL (e de Python, quando entrar) é ensinada e corrigida **na versão mais performática**, com uma linha **⚡ Big data** que diz o porquê. A linha cobre, quando couber:
  1. Filtro *sargable*: coluna crua contra intervalo (`>=` e `<`), nunca função sobre a coluna no `WHERE` (`YEAR()`, `LOWER()`, `DATE()`).
  2. Colunas escolhidas em vez de `SELECT *`.
  3. `EXPLAIN` lido (`type`, `key`, `rows`, `Extra`) e o índice composto que a consulta pediria: colunas de igualdade primeiro, depois a do `ORDER BY` ou do intervalo.
  4. Perfil de qualidade numa passada só (`SUM(condição)`), em amostra ou partição antes da tabela inteira.
  5. No data lake (Parquet no S3), partição por data no lugar do índice ([[geral-decisao-2026-11-05-parquet-e-particao]]).
  6. Quem é dono do quê: em produção e no data lake, o analista **propõe** índice ou partição com o `EXPLAIN` como evidência; nas tabelas do próprio time, cria e mantém.
  7. **Resumir a tabela grande antes de juntar:** quando a consulta agrega, o `GROUP BY` vai numa subconsulta antes do `JOIN`. Exceções: o agrupamento depende de coluna de outra tabela (filtrar e resumir no menor nível possível mesmo assim); o filtro de outra tabela corta muito (juntar primeiro com ele); não há o que resumir (só filtrar e escolher colunas, sem subconsulta, que o otimizador desmonta). No garfo (dois filhos do mesmo pai), resumir antes é obrigatório para o número sair certo. A IA aponta sempre que o humano juntar antes de resumir sem um desses motivos.
  8. **Cada ferramenta pelo seu custo: o `GROUP BY` reduz, a janela compara, a CTE organiza.** O `GROUP BY` é o que mais escala: em motor distribuído, cada nó resume a sua parte antes do shuffle. A janela (`OVER (PARTITION BY ...)`) não reduz linhas: embaralha e ordena todas por partição (risco de skew), então roda **depois** de filtrar e resumir. A CTE não otimiza sozinha: o otimizador costuma colá-la na consulta. O que torna terabytes viáveis: poda de partição da **tabela** (outro `PARTITION BY`, não o da janela), filtro sargable e poucas colunas, reduzir antes de janelar, tabela pré-agregada e funções aproximadas. Onde o `GROUP BY` sofre (`COUNT(DISTINCT)` de alta cardinalidade, skew, varredura sem filtro de partição), a saída é aproximar, pré-agregar ou filtrar, não trocar por janela. Padrão: filtrar a partição → `GROUP BY` cliente/dia → janela de 7 dias sobre o resumo.
- **Alteração:** em 2026-11-07, 18h19, no M3, o humano acrescentou o item 7 e pediu para ser corrigido sempre que não o seguir. Em 2026-11-09, 06h03, na revisão do dia do teste, o humano propôs trocar `GROUP BY` por CTE e `PARTITION BY` em terabytes; a IA mostrou o custo de cada um e, a pedido (06h10), entrou o item 8 ([[geral-decisao-2026-11-09-revisao-leve-do-dia-do-teste]]).
- **Motivo:** o volume real de um banco é de bilhões de linhas; aprender o jeito performático desde o começo evita trocar de hábito depois, e o time valoriza partição e otimização ([[relato-do-colega-do-time]]).
- **Consequências:** o esqueleto de sessão de [[trilha-sql-didatica]], o "Papel da IA" de [[banco-mocado-plano]] e as regras de [[instrucoes-do-coach-de-entrevista]] ganham a linha ⚡ Big data. Fica proibido ensinar uma forma lenta sem mostrar a performática ao lado.

### 🔗 Conexões
- Funcionalidade: [[banco-mocado-contexto]]
- Plano: [[banco-mocado-plano]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
