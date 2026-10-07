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
Resolver as 44 questões de [[questoes-por-cenario]] no banco `mysql-estudos`, **eu resolvendo e a IA treinando**: a IA faz o papel de head e coach ([[instrucoes-do-coach-de-entrevista]]), não entrega a resposta pronta.

## Decisões que este plano respeita
- (nenhuma nota de decisão ainda; segue [[instrucoes-do-coach-de-entrevista]] e [[banco-mocado-contexto]])

## Como cada questão roda (o ciclo de trabalho)
Em blocos do Pomodoro Curto 15-5 (no Vault): 15 min de foco, 5 de pausa, pausa longa a cada 3 blocos. Uma questão por bloco; questão grande ocupa 2.

1. **Ler e perguntar (2 min):** escrevo as perguntas de esclarecimento que faria à head.
2. **Hipótese (2 min):** o que espero achar e em que tabela.
3. **Explorar com SQL:** primeiro `SELECT` pequeno, depois agrego. Python só quando o SQL fica difícil (janelas de tempo, texto, gráficos).
4. **Salvar:** a solução em `python/solucoes/cenarioN/qN_M.sql` ou `.py`, com 2 ou 3 linhas de comentário sobre o raciocínio.
5. **Conferir:** só depois de terminar, `gabarito.casos_plantados` do cenário.
6. **Falar:** ao fim do cenário, resposta nos 5 blocos e a versão de 90 segundos em voz alta.
7. **Treino com a IA:** colo o resultado no chat; a IA pergunta como a head, **uma pergunta por vez**, e dá o feedback depois.

## Papel da IA em cada sessão
- Apresenta a questão como a head, sem dica.
- Só dá dica se eu pedir, em degraus: (1) qual tabela olhar, (2) qual técnica, (3) esqueleto da consulta. Nunca a solução inteira sem pedido explícito.
- Revisa meu SQL ou Python quando eu colar: correção, legibilidade, falsos positivos e explicabilidade.
- Feedback no formato do coach: o que ficou bom, o que faltou, o que reordenar.

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

### T1: Cenário 3, pipeline (prioridade de treino)
- **Faz:** Q3.1 a Q3.9. Começa por aqui porque é lacuna minha e gera a tabela limpa usada no cenário 6.
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
  - [ ] 2 simulações seguidas sem travar na estrutura dos 5 blocos
- **Prova:** feedback do coach
- **Verificação:**
  - Data:
  - Critérios ✔/✘ com a prova de cada um:
  - Devolvido para correção:

## Próxima tarefa e a seguinte
T1 (cenário 3) e depois T2 (cenário 1).

## Prioridades
1. T0. 2. T1, T5 e T6 (maiores lacunas, ver [[cenarios-de-pratica]]). 3. T2, T3, T4. 4. T7. [a confirmar: tempo disponível até o teste real]

## Candidatos a registro
- Decisão: ordem dos cenários (3 → 1 → 2 → 5 → 4 → 6 → mista), se o humano aprovar.

### 🔗 Conexões
- Funcionalidade: [[banco-mocado-contexto]]
- Questões: [[questoes-por-cenario]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
