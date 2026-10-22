---
tipo: plano
funcionalidade: geral
status: proposta
criado: 2026-11-05
---
# 🧭 Roteiro — PrepBTG

> [!tldr] Onde o projeto está
> Etapa atual: **1. Definir o roteiro do projeto** (em-construcao)

> [!warning] Proposta da IA até eu aprovar
> As etapas nascem como proposta. Aprovadas, viram a nota `geral-decisao-AAAA-MM-DD-roteiro` e este plano passa a `status: aprovado`. Mudar a lista de etapas é uma nova decisão.

Uma seção por etapa, na ordem em que o projeto acontece. Status: `planejada → em-construcao → em-verificacao → concluida → arquivada`. Etapa concluída tem data e links para as notas geradas nela. A linha "Etapa atual" acima é sincronizada por `cofre.py status --atualizar`.

## 1. Definir o roteiro do projeto
- **Status:** em-construcao
- **Objetivo:** listar as etapas gerais do projeto, da primeira à entrega.
- **Pronto quando:** etapas aprovadas numa nota de decisão.
- **Funcionalidades:** (nenhuma)
- **Notas geradas:** [[processo-seletivo-btg]], [[vaga-compliance-engineering]], [[cenarios-de-pratica]], [[pontos-delicados]], [[instrucoes-do-coach-de-entrevista]]
- **Concluída em:** 

## 2. Criar o banco mocado
- **Status:** concluida
- **Objetivo:** montar um ambiente com banco de dados mocado e dados simulados para treinar armazenar, tratar e gerar soluções em Python ou SQL puro. Foco declarado pelo humano em 2026-11-05.
- **Pronto quando:** o ambiente `mysql-estudos` sobe no WSL do humano e o `teste_conexao.py` lista as 9 tabelas (tarefa T0 de [[banco-mocado-plano]]).
- **Funcionalidades:** [[banco-mocado-contexto]]
- **Notas geradas:** [[questoes-por-cenario]], [[banco-mocado-plano]]
- **Concluída em:** 2026-11-05

## 3. Treinar os cenários no banco mocado
- **Status:** em-construcao
- **Objetivo:** resolver os cenários de prática com linha de raciocínio e solução em Python ou SQL, começando pelos de maior lacuna (3, 4 e 6).
- **Pronto quando:** reta final (T8 a T11) de [[banco-mocado-plano]] cumprida até 2026-11-09; T1 a T7 entram até onde o tempo deixar.
- **Funcionalidades:** (nenhuma; o treino segue [[banco-mocado-plano]], sobre o ambiente de [[banco-mocado-contexto]])
- **Notas geradas:** [[trilha-sql-didatica]], [[trilha-sql-didatica-avancado]], [[trilha-sql-didatica-extras]], [[banco-mocado-plano-registro-sql]], [[geral-decisao-2026-11-07-solucao-performatica-big-data]], [[geral-decisao-2026-11-08-ate-6-questoes-por-modulo]], [[geral-decisao-2026-11-08-cinco-questoes-e-bonus]]
- **Concluída em:** 

## 4. Simular o estudo de caso
- **Status:** planejada
- **Objetivo:** ensaiar no formato do teste: SQL e discursivas de decisão com tempo, mais a versão falada de 90 segundos.
- **Pronto quando:** 2 simulados (T10 de [[banco-mocado-plano]]) com o segundo melhor que o primeiro em [[banco-mocado-plano-evolucao]].
- **Funcionalidades:** (nenhuma)
- **Notas geradas:** (nenhuma ainda)
- **Concluída em:** 

## 5. Estudo de caso real
- **Status:** concluida
- **Objetivo:** fazer o teste em 2026-11-09, 15h (SQL e discursivas de decisão sobre cases reais, [[processo-seletivo-btg]]) e registrar no cofre o que caiu.
- **Pronto quando:** estudo de caso entregue.
- **Funcionalidades:** (nenhuma)
- **Notas geradas:** (nenhuma; resultado: aprovado, em [[processo-seletivo-btg]])
- **Concluída em:** 2026-11-09

## 6. Conversa com o head do time
- **Status:** em-construcao
- **Objetivo:** chegar à conversa de 2026-11-11, 18h (30 min), alinhado à cultura do BTG e ao que o head espera.
- **Pronto quando:** módulos M1 a M6 de [[roteiro-conversa-com-o-head]] feitos e a conversa registrada em [[processo-seletivo-btg]].
- **Funcionalidades:** (nenhuma)
- **Notas geradas:** [[cultura-btg-podcast]], [[cultura-btg-carreira]], [[roteiro-conversa-com-o-head]], [[roteiro-conversa-com-o-head-cartao]], [[geral-decisao-2026-11-11-modulos-da-conversa-com-o-head]]
- **Concluída em:** 

### 🔗 Conexões
- Projeto: [[geral-contexto]]
- Mapa: [[moc-orquestra]]
- Regras: [[manual-da-orquestra]]
