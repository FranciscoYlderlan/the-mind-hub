---
aliases: [Mapa da orquestra, Mapa do projeto, Project map]
tags: [estudos/programacao]
tipo: moc
status: em-uso
criado: 2026-11-05
origem: Manual da Orquestra
---
# 🗺️ Mapa da Orquestra — PrepBTG

> [!tldr] Em uma linha
> O mapa do cofre do projeto: daqui se chega no contexto, nas funcionalidades, nas regras e nos modelos.

## 🚦 Etapas vitais
- [[manual-da-orquestra#🚦 Etapas vitais]]: toda escrita termina em `python orquestra/modelos/cofre.py verificar .` com zero ERRO.
- [[manual-da-orquestra#🔄 Passagem de turno]]: chat novo começa por `cofre.py status` e pelo "Onde parei" do último diário.

## 🧭 Projeto
- [[CLAUDE]]: índice que os agentes leem primeiro.
- [[geral-plano]]: roteiro — em que etapa o projeto está e as notas geradas em cada etapa.
- [[geral-contexto]]: objetivo, motivação, dial e decisões que valem para o projeto todo.

## 🚧 Funcionalidades
- [[banco-mocado-contexto]]: banco de dados mocado com dados simulados para treinar em Python ou SQL puro (etapa 2). Plano de treino: [[banco-mocado-plano]].

## 📦 Arquivadas
- (nenhuma ainda)

## 🎯 Processo seletivo BTG
- [[processo-seletivo-btg]]: etapas, status e formato do estudo de caso.
- [[vaga-compliance-engineering]]: descrição-base da vaga e requisitos.
- [[cenarios-de-pratica]]: as 6 questões de treino (não são o teste real).
- [[questoes-por-cenario]]: as 51 questões concretas de cada cenário, ligadas ao banco simulado.
- [[pontos-delicados]]: AWS, TM Mentoring, mudança, salário e "JEV".
- [[instrucoes-do-coach-de-entrevista]]: como a IA age no treino.
- [[esqueleto-de-6-passos]]: o formato de toda resposta (decisão: [[geral-decisao-2026-11-05-esqueleto-de-6-passos]]).
- [[roteiros-dos-cenarios-genericos]]: cenários 1 a 3 com enunciado original, roteiro e SQL.
- [[casos-de-treino-em-6-passos]]: 8 casos curtos (C1 a C8), um conceito cada.
- [[relato-do-colega-do-time]]: como o time da vaga trabalha (SQL extrai, Python analisa).
- [[tratamento-de-nulos]]: COALESCE e a regra da quarentena.
- [[estatistica-basica-e-eda]]: análise exploratória e estatística básica em Python.
- [[sql-window-functions-mysql]]: 7 padrões de janela no dialeto do MySQL.
- [[esquema-do-banco-compliance]]: tabelas, colunas e ligações do banco `compliance`, e como a IA lê o banco.
- [[trilha-sql-didatica]]: curso de SQL em 9 módulos (M0 a M4 aqui), antes dos drills; M5 a M8 em [[trilha-sql-didatica-avancado]]; questões extras em [[trilha-sql-didatica-extras]].
- [[banco-mocado-plano-registro-sql]]: registro de cada operação da trilha e o protocolo de score do agente avaliador.
- [[questoes-sql-de-prova]]: 18 drills de SQL com tempo-alvo.
- [[questoes-tomada-de-decisao]]: 12 cases discursivos de decisão.
- [[banco-mocado-plano-evolucao]]: rubricas e placar da reta final.

## 📚 Regras e referências
- [[manual-da-orquestra]]: estrutura, papéis, fluxo e gatilhos.
- [[manual-do-cerebro]]: tom e esqueleto das notas de referência.

## 🧩 Modelos
- Notas operacionais: [[modelo-contexto]], [[modelo-plano]], [[modelo-decisao]], [[modelo-bug]], [[modelo-diario]]
- Notas de consulta: [[modelo-referencia]], [[modelo-nota]]
- Subagentes: [[modelo-briefing-subagente]], [[modelo-relatorio-subagente]]
- Repositório de código: [[modelo-claude-do-repositorio]]

## 🔗 Conexões
- Índice para agentes: [[CLAUDE]]
- Regras: [[manual-da-orquestra]]
