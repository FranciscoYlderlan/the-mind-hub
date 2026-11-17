---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-09
substitui: 
aliases: [Módulo rápido de estatística, Estatística no dia do teste, Desvio padrão e outliers, Quick statistics module]
---
# ✅ Módulo rápido de estatística básica antes do teste, discursivo, no cenário de big data do BTG

- **Proposta (plano):** pedido do humano no chat de 2026-11-09, 11h56, logo depois de concluir a revisão leve ([[geral-decisao-2026-11-09-revisao-leve-do-dia-do-teste]]): o tema pode cair como pergunta discursiva no teste.
- **Decisão:**
  1. **Um módulo rápido, leve e didático**, num chat novo, antes do descanso. Objetivo: ajudar a **raciocinar** sobre dados, nunca criar dúvida. Um caminho só por pergunta, sem lista de alternativas.
  2. **As 4 perguntas-guia** (são as perguntas que o teste pode fazer, e cada uma vira uma ideia do módulo):
     - Qual é o desvio padrão? (o que mede, em palavras)
     - A média representa bem esse conjunto de dados? (média contra mediana; valor de transação é assimétrico)
     - Existe algum valor suspeito? (z-score: quantos desvios um valor está da média)
     - Como achar em SQL os valores acima de 3 desvios padrões da média? (`AVG` e `STDDEV` numa CTE, depois o filtro `valor > media + 3 * desvio`)
     - Mais: **quartis e percentil** em palavras ("90% das transações ficam abaixo de X"; mediana é o percentil 50; o IQR é a faixa do meio).
  3. **Formato:** o da revisão leve (itens 9 e 10 de [[geral-decisao-2026-11-09-revisao-leve-do-dia-do-teste]]): analogia na abertura de cada ideia, exemplo curto num dos 3 cenários fixos (de preferência 💸 PIX fracionado, com o histórico de um cliente), ordem de execução em uma linha quando houver código, e **1 questão discursiva** no fim, respondida em palavras, com a fórmula da resposta (item 5 daquela decisão).
  4. **⚡ Big data no BTG**, em uma linha por ideia: média e desvio padrão são somas que cada nó calcula na sua parte e depois junta (baratas); mediana e percentil exatos precisam ordenar tudo (caros), por isso motores de nuvem oferecem versões aproximadas; o desvio deve ser calculado **por cliente** (o histórico dele), não sobre o banco inteiro, porque um R$ 200 mil é normal para uma PJ grande e suspeito para um PF de renda baixa.
  5. **Formato visual e enxuto** (pedido do humano em 2026-11-09, 12h17 e 12h18): pouco texto; cada ideia é **fórmula + analogia + paralelo de big data**, e o que puder vira visual. Os visuais que funcionaram: a régua do cliente interativa (PIX de hoje e o "bilionário no bar" mexendo média, mediana, faixa de 1σ, linha de 3σ e caixa Q1–Q3), o par "soma barata (cada nó soma e junta) contra ordenar caro (embaralha bilhões)" e o boxplot anotado (caixa, mediana, bigodes, cerca e ponto suspeito). Linha ou marca dentro de forma colorida usa cor que contraste nos dois modos (no modo escuro a mediana sumiu dentro da caixa).
  6. **Aula do zero, uma ideia por vez** (pedidos de 12h23 e 12h41): o humano ainda não entendeu a estatística e quer internalizar para aplicar com autonomia em cenários diversos. A aula vai em **5 ideias**, cada uma com números pequenos de brinquedo, analogia, linha ⚡ e **1 checagem curta** antes da próxima: (1) média e mediana, com o bilionário no bar; (2) desvio padrão, com o batimento do cliente; (3) z-score e o SQL de 3 desvios, com o radar; (4) percentil, quartis e boxplot, com a fila por altura; (5) cerca do IQR e mascaramento. Só no fim entram o roteiro de 4 perguntas (régua de quem? assimétrico? qual régua? quanto custa?) e o mesmo roteiro nos 3 cenários fixos, com o cuidado de que outlier em dado sujo pode ser erro de carga. Fecha com 1 questão discursiva.
  7. **Sem conteúdo além disso:** `NTILE`, `PERCENT_RANK`, MAD e funções aproximadas só aparecem como nome, se aparecerem; nada de sintaxe nova para decorar.
- **Alteração:** nenhuma.
- **Motivo:** o simulado de ontem tirou nota por falta de exemplo concreto, e estatística (desvio, outlier, percentil) é a linguagem das regras de PLD; uma passagem curta e discursiva dá vocabulário para a prova sem abrir dúvida nova.
- **Consequências:** o resumo da aula fica em [[estatistica-basica-e-eda]] (seção "Kit de bolso"). É a única matéria nova do dia, por pedido explícito; a regra de "nada além da primeira passagem" do item 11 da revisão leve continua para o resto. Base de consulta: [[estatistica-basica-e-eda]].

### 🔗 Conexões
- Funcionalidade: [[banco-mocado-contexto]]
- Plano: [[banco-mocado-plano]]
- Projeto: [[geral-contexto]]
- Relacionadas: [[estatistica-basica-e-eda]], [[geral-decisao-2026-11-09-revisao-leve-do-dia-do-teste]]
- Diário: [[diario-2026-11-09]]
