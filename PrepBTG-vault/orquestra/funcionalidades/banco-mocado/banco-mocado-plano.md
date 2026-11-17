---
tipo: plano
funcionalidade: banco-mocado
status: proposta
criado: 2026-11-05
---
# 📋 Plano: treinar as questões no banco mocado

> [!warning] Proposta da IA
> Nada aqui é decisão. Decisões ficam nas notas `-decisao-` linkadas abaixo.

## Objetivo desta rodada
Resolver as 51 questões de [[questoes-por-cenario]] no banco `mysql-estudos`, **eu resolvendo e a IA treinando**: a IA faz o papel de head e coach ([[instrucoes-do-coach-de-entrevista]]), não entrega a resposta pronta.

## Decisões que este plano respeita
- [[geral-decisao-2026-11-05-esqueleto-de-6-passos]]: toda resposta segue os 6 passos.
- [[geral-decisao-2026-11-05-trilha-sql-e-python]]: SQL extrai, Python analisa.
- [[geral-decisao-2026-11-05-parquet-e-particao]]: Parquet com DuckDB e partição.
- [[geral-decisao-2026-11-05-nulos-vao-para-quarentena]]: nulo crítico vai para a quarentena.
- [[geral-decisao-2026-11-05-treino-por-cenarios-concretos]]: só cenário concreto, nos 6 passos e no pipeline.
- [[geral-decisao-2026-11-05-conducao-do-treino]]: listar as questões e ensinar antes de pedir.
- [[geral-decisao-2026-11-06-sql-antes-das-discursivas]]: SQL primeiro, discursivas por último.
- [[geral-decisao-2026-11-06-trilha-didatica-antes-dos-drills]]: trilha didática antes dos drills.
- [[geral-decisao-2026-11-07-solucao-performatica-big-data]]: toda solução na versão performática.
- [[geral-decisao-2026-11-08-cinco-questoes-e-bonus]]: 5 questões por módulo da trilha e uma 6ª bônus, do M4 em diante.
- Segue também [[instrucoes-do-coach-de-entrevista]] e [[banco-mocado-contexto]].

## Como cada questão roda (o ciclo de trabalho)
Em blocos do Pomodoro Curto 15-5 (no Vault): 15 min de foco, 5 de pausa, pausa longa a cada 3 blocos. Uma questão por bloco; questão grande ocupa 2.

1. **Ler e perguntar (2 min):** escrevo as perguntas de esclarecimento que faria à head.
2. **Hipótese (2 min):** o que espero achar e em que tabela.
3. **Extrair com SQL, analisar com Python:** SQL para consultar e agregar; pandas para explorar, limpar e analisar, com estatística básica e um gráfico simples ([[geral-decisao-2026-11-05-trilha-sql-e-python]]).
4. **Salvar:** a solução em `python/solucoes/cenarioN/qN_M.sql` ou `.py`, com 2 ou 3 linhas de comentário sobre o raciocínio.
5. **Conferir:** só depois de terminar, `gabarito.casos_plantados` do cenário.
6. **Falar:** ao fim do cenário, resposta nos 6 passos ([[esqueleto-de-6-passos]]) e a versão de 90 segundos em voz alta.
7. **Treino com a IA:** colo o resultado no chat; a IA pergunta como a head, **uma pergunta por vez**, e dá o feedback depois.

## Papel da IA em cada sessão
- Antes de pedir execução, lista todas as questões do caso; antes de pedir resposta, ensina o que eu ainda não vi e mostra o formato esperado.
- Apresenta a questão como a head, sem dica da solução.
- Só dá dica se eu pedir, em degraus: (1) qual tabela olhar, (2) qual técnica, (3) esqueleto da consulta. Nunca a solução inteira sem pedido explícito.
- Revisa meu SQL ou Python quando eu colar: correção, legibilidade, falsos positivos e explicabilidade.
- Feedback no formato do coach: o que ficou bom, o que faltou, o que reordenar.
- Mostra o progresso a cada questão; pulada conta como feita ([[geral-decisao-2026-11-06-progresso-a-cada-questao]]).
- Ensina e corrige sempre a versão mais performática, com a linha ⚡ Big data ([[geral-decisao-2026-11-07-solucao-performatica-big-data]]). Quando a consulta agrega, resume a tabela grande antes de juntar e aponta quando eu não faço isso.

## Tarefas

### T0: subir o ambiente
- **Faz:** descompactar `mysql-estudos.zip` em `~/docker/containers`, `docker compose up -d`, criar o `.venv`, rodar `teste_conexao.py` e o `ex01`.
- **Toca em:** WSL, `~/docker/containers/mysql-estudos`
- **Depende de:** nenhuma
- **Paralelo:** não
- **Pronto quando:**
  - [x] `teste_conexao.py` lista 9 tabelas com linhas
  - [x] conexão funciona também do Windows (`localhost:3306`)
- **Prova:** saída do `teste_conexao.py` colada no chat
- **Verificação:**
  - Data: 2026-11-05
  - Critérios ✔/✘ com a prova de cada um: ✔ ambiente no ar, confirmado pelo humano no chat ("está tudo pronto"); a saída do `teste_conexao.py` não foi colada.
  - Devolvido para correção: não

### T0b: Primeira olhada e Parquet
- **Faz:** a IA escreve o cenário concreto do C8; eu instalo `pandas`, `matplotlib`, `statsmodels`, `duckdb` e `pyarrow` no `.venv` e resolvo Q0.1 a Q0.4 dentro desse cenário; exportar as tabelas para Parquet por mês (Q3.11) e fazer a primeira consulta no DuckDB.
- **Toca em:** `transacoes`, `clientes`, pasta `parquet/` do `mysql-estudos`
- **Depende de:** T0
- **Paralelo:** não
- **Pronto quando:**
  - [ ] notebook ou script com formato, nulos, duplicados, `describe` e 1 gráfico
  - [ ] Parquet gravado e lido pelo DuckDB com a mesma contagem do MySQL
  - [ ] resposta de 90 s do C8 falada e com feedback
- **Prova:** contagem igual no MySQL e no DuckDB; gráfico gerado
- **Verificação:**
  - Data:
  - Critérios ✔/✘ com a prova de cada um:
  - Devolvido para correção:

### T1: Cenário 3, pipeline (prioridade de treino)
- **Faz:** Q3.1 a Q3.10 (e Q3.12 depois da T0b). Q3.2 a Q3.4 em SQL e em Python, com reconciliação. É lacuna minha e gera a tabela limpa usada no cenário 6.
- **Toca em:** `stg_transacoes_bruto`, `transacoes`
- **Depende de:** T0
- **Paralelo:** não
- **Pronto quando:**
  - [ ] tabela limpa e de quarentena gravadas
  - [ ] reconciliação com `transacoes` explicada
  - [ ] resposta de 90 s falada e com feedback
- **Prova:** contagens e somas da reconciliação; conferência com o gabarito do cenário 3
- **Verificação:**
  - Data:
  - Critérios ✔/✘ com a prova de cada um:
  - Devolvido para correção:

### T2: Cenário 1, sinais de PLD
- **Faz:** Q1.1 a Q1.9.
- **Toca em:** `clientes`, `socios_pj`, `contas`, `transacoes`, `paises_risco`
- **Depende de:** T0
- **Paralelo:** sim, com T1 se eu quiser variar
- **Pronto quando:**
  - [ ] lista priorizada de clientes com o motivo de cada um
  - [ ] iscas explicadas como não suspeitas
  - [ ] resposta de 90 s falada e com feedback
- **Prova:** achados conferidos com o gabarito do cenário 1 (acertos, faltas e falsos positivos contados)
- **Verificação:**
  - Data:
  - Critérios ✔/✘ com a prova de cada um:
  - Devolvido para correção:

### T3: Cenário 2, alertas
- **Faz:** Q2.1 a Q2.8.
- **Toca em:** `alertas`, `regras_monitoramento`
- **Depende de:** T2 (a Q2.6 usa os casos achados no cenário 1)
- **Paralelo:** não
- **Pronto quando:**
  - [ ] tabela de métricas por regra e por analista
  - [ ] proposta de recalibração com impacto estimado
  - [ ] resposta de 90 s falada e com feedback
- **Prova:** conferência com o gabarito do cenário 2
- **Verificação:**
  - Data:
  - Critérios ✔/✘ com a prova de cada um:
  - Devolvido para correção:

### T4: Cenário 5, screening
- **Faz:** Q5.1 a Q5.7.
- **Toca em:** `clientes`, `lista_restritiva`, `transacoes`, `socios_pj`
- **Depende de:** T0
- **Paralelo:** sim, com T3
- **Pronto quando:**
  - [ ] cada achado classificado em confirmado, provável ou descartado, com evidência
  - [ ] resposta de 90 s falada e com feedback
- **Prova:** conferência com o gabarito do cenário 5
- **Verificação:**
  - Data:
  - Critérios ✔/✘ com a prova de cada um:
  - Devolvido para correção:

### T5: Cenário 4, GenAI com RAG (prioridade de treino)
- **Faz:** Q4.1 a Q4.5, só raciocínio, em simulação com a IA.
- **Toca em:** `alertas` (Q4.5)
- **Depende de:** T3 (a Q4.5 liga com a Q2.3)
- **Paralelo:** não
- **Pronto quando:**
  - [ ] desenho do fluxo explicado em voz alta
  - [ ] resposta de 90 s falada e com feedback
- **Prova:** feedback do coach registrado no diário
- **Verificação:**
  - Data:
  - Critérios ✔/✘ com a prova de cada um:
  - Devolvido para correção:

### T6: Cenário 6, arquitetura na AWS (prioridade de treino)
- **Faz:** Q6.1 a Q6.6, só raciocínio, usando o pipeline do T1 como exemplo concreto.
- **Toca em:** nenhum dado novo
- **Depende de:** T1
- **Paralelo:** não
- **Pronto quando:**
  - [ ] desenho das camadas e da entrega de alertas explicado
  - [ ] fala honesta sobre a lacuna em AWS ensaiada ([[pontos-delicados]])
- **Prova:** feedback do coach registrado no diário
- **Verificação:**
  - Data:
  - Critérios ✔/✘ com a prova de cada um:
  - Devolvido para correção:

### T7: simulação mista
- **Faz:** a IA sorteia questões de cenários diferentes, sem aviso, com tempo marcado.
- **Depende de:** T1 a T6
- **Pronto quando:**
  - [ ] 2 simulações seguidas sem travar nos 6 passos
- **Prova:** feedback do coach
- **Verificação:**
  - Data:
  - Critérios ✔/✘ com a prova de cada um:
  - Devolvido para correção:

## Reta final até o teste (2026-11-09, 15h)
O teste tem SQL e discursivas de decisão sobre cases reais ([[processo-seletivo-btg]]). Estas tarefas passam na frente de T0b a T7; destas, entram as questões SQL dos cenários e as de raciocínio que viram discursiva. A nota de cada resposta vai para [[banco-mocado-plano-evolucao]].

### T8: SQL de fundamento
- **Faz:** em duas fases ([[geral-decisao-2026-11-06-trilha-didatica-antes-dos-drills]]).
  - **Fase A, trilha:** módulos M0 a M8 de [[trilha-sql-didatica]] e [[trilha-sql-didatica-avancado]], um por sessão: aula com exemplo resolvido, prática com ajuda e checagem que mede a evolução. Cada operação vai para [[banco-mocado-plano-registro-sql]]; o agente avaliador mede a evolução depois das checagens C2, C5 e C8 e escolhe o reforço.
  - **Fase B, retomada:** S1 a S18 de [[questoes-sql-de-prova]], com tempo, escrevendo **sem rodar** antes; os que saírem fracos são refeitos.
- **Toca em:** banco `compliance` ([[esquema-do-banco-compliance]])
- **Depende de:** T0
- **Pronto quando:**
  - [ ] checagens C0 a C5 feitas com autonomia A ou B (C6 a C8 até onde o tempo deixar)
  - [ ] score do agente avaliador em "Pronto" ou "Domínio" nos módulos M0 a M5
  - [ ] linha de base dos drills no placar, na retomada
  - [ ] nível 2 acertado sem rodar em 2 de cada 3
- **Prova:** linhas do [[banco-mocado-plano-registro-sql]] e do placar em [[banco-mocado-plano-evolucao]]

### T9: decisões
- **Faz:** D1 a D12 de [[questoes-tomada-de-decisao]], mais Q1.9, Q2.7, Q2.8, Q3.9 e Q5.6 de [[questoes-por-cenario]] e uma resposta curta de Q4.2 e Q6.1 (com a fala honesta de [[pontos-delicados]]). Diagnóstico com D2 e D3, depois do SQL.
- **Proposta de recalibração** [a confirmar com o humano]: cada case é cobrado no papel do engenheiro: que dados eu traria, o que eles mostram e que recomendação eu levo a quem decide ("recomendo X, quem aprova é Y"). Resposta-modelo do D2 já dada na sessão de 2026-11-06.
- **Depende de:** T8 ([[geral-decisao-2026-11-06-sql-antes-das-discursivas]])
- **Pronto quando:**
  - [ ] todos os D respondidos uma vez; os 4 piores refeitos
  - [ ] média ≥ 13/18 nos últimos 4
- **Prova:** linhas do placar

### T10: simulados no formato da prova
- **Faz:** a IA monta uma prova surpresa (3 SQL + 3 discursivas, com tempo), eu respondo, ela corrige pela rubrica. As questões SQL vêm de cenários diferentes (1, 2, 3 e 5), cada uma fechada com 2 frases de "o que isso muda na decisão".
- **Depende de:** T8 e T9 começadas
- **Pronto quando:**
  - [ ] Simulado 2 com nota maior que o 1 e sem critério em 0
- **Prova:** placar dos dois simulados

### T11: aquecimento do dia do teste
- **Faz:** segunda de manhã, no máximo 45 min: 3 drills de nível 1, 1 case falado, leitura de [[esqueleto-de-6-passos]] e dos erros comuns de [[questoes-sql-de-prova]]. Nada novo depois das 11h.
- **Pronto quando:**
  - [ ] feito até as 11h de 2026-11-09

### Agenda proposta
A agenda por dia e por turno, até segunda, e o que se corta com menos horas: [[banco-mocado-plano-agenda]].

## Próxima tarefa e a seguinte
Aula de estatística básica do zero, num chat novo, uma ideia por vez (5 ideias com checagem, depois o roteiro de 4 perguntas nos 3 cenários e 1 questão discursiva), antes do teste das 15h (itens 5 e 6 de [[geral-decisao-2026-11-09-modulo-rapido-de-estatistica]]; base no "Kit de bolso" de [[estatistica-basica-e-eda]]); a revisão leve de M0 a M7 foi concluída em 2026-11-09 ([[geral-decisao-2026-11-09-revisao-leve-do-dia-do-teste]]). As questões pendentes de M6 e M7 de [[trilha-sql-didatica-avancado]], a retomada dos drills e a T9 ficam fora do dia.

## Prioridades
1. T8. 2. T9. 3. T10. 4. T11. 5. Questões SQL e de raciocínio de T1 a T7 que cabem na agenda. T0b (Parquet e EDA em Python) fica para depois do teste, salvo se o formato confirmado pedir Python [a confirmar com o humano].

## Candidatos a registro
- Decisão: ordem dos cenários (3 → 1 → 2 → 5 → 4 → 6 → mista), se o humano aprovar.

### 🔗 Conexões
- Funcionalidade: [[banco-mocado-contexto]]
- Questões: [[questoes-por-cenario]]
- Reta final: [[banco-mocado-plano-agenda]], [[trilha-sql-didatica]], [[trilha-sql-didatica-avancado]], [[trilha-sql-didatica-extras]], [[banco-mocado-plano-registro-sql]], [[questoes-sql-de-prova]], [[questoes-tomada-de-decisao]], [[banco-mocado-plano-evolucao]], [[esquema-do-banco-compliance]]
- Roteiros e casos: [[roteiros-dos-cenarios-genericos]], [[casos-de-treino-em-6-passos]], [[sql-window-functions-mysql]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
