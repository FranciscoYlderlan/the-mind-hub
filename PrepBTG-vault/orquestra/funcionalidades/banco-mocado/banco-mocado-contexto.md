---
tipo: contexto
funcionalidade: banco-mocado
status: concluida
etapa: 2
criado: 2026-11-05
aliases: [Banco de dados mocado, Mock database, Ambiente de treino com dados simulados]
---
# 🧭 Banco mocado de treino

> [!tldr] Em uma linha
> Um ambiente com banco de dados mocado e dados simulados, onde o humano treina armazenar e tratar dados e gerar soluções em Python ou SQL puro.

## Objetivo e motivação
Preparar o estudo de caso do BTG Pactual ([[processo-seletivo-btg]]) praticando em dados, e não só na teoria. A vaga pede Python e SQL ([[vaga-compliance-engineering]]), e os [[cenarios-de-pratica]] precisam de dados para serem resolvidos de verdade.

## Fatos que eu informei
- A etapa atual do projeto é **criar o ambiente**: um banco de dados mocado com dados simulados.
- O uso é específico para o meu treino: armazenar esses dados, tratá-los e gerar soluções **em Python ou em SQL puro**.
- Banco: **MySQL**, em Docker dentro do **WSL** (Ubuntu) no Windows. Pasta: `\\wsl.localhost\Ubuntu\home\ylderlan\docker\containers`. IP do WSL informado: 172.25.227.200.
- A conexão também é feita por **script em Python** para as análises.
- Os dados devem ser de **banco** (o BTG é banco).
- O papel principal da IA nesta funcionalidade é **me treinar** (2026-11-05).

## O que já foi feito
- 2026-11-05: funcionalidade registrada no cofre, sem implementação ([[diario-2026-11-05]]).
- 2026-11-05: ambiente `mysql-estudos` entregue em .zip: docker-compose com MySQL 8.4, schema de Compliance/PLD, cerca de 67 mil transações simuladas, 1,9 mil alertas, listas restritivas e PEP, staging com problemas de qualidade, banco `gabarito` com 62 casos plantados para os cenários 1, 2, 3 e 5, e scripts Python (`conexao.py`, `teste_conexao.py`, exemplos). Testado carregando em MariaDB 10.11; ainda não rodado no MySQL 8.4 do humano.
- 2026-11-05: questões registradas em [[questoes-por-cenario]] e plano de treino em [[banco-mocado-plano]].
- 2026-11-05: T0 concluída: o humano subiu o `mysql-estudos` no WSL e confirmou o ambiente pronto. Próximo: T1 (cenário 3).

## Tempo disponível
[a preencher]

## Dial e modelo de IA
- Dial: [a confirmar] (padrão: o do [[geral-contexto]])
- Modelo de IA: [a preencher]

## Áreas sensíveis
- Dados são **simulados**: nada de dados reais de clientes ou do BTG.
- Código só com pedido explícito ([[instrucoes-do-coach-de-entrevista]]). Nos exemplos do ambiente, só o `ex01` vem resolvido; `ex02`, `ex03` e `ex05` são esqueletos com TODOs, porque resposta-modelo lida não vale como treino.
- O gabarito fica no banco separado `gabarito`, consultado só depois de tentar.

## Mapa
- Plano: [[banco-mocado-plano]]
- Questões: [[questoes-por-cenario]]
- Decisões: (nenhuma ainda)
- Bugs: (nenhum ainda)
- Referências: [[cenarios-de-pratica]], [[vaga-compliance-engineering]]

## Interpretação do agente
- Os dados simulados refletem os cenários 1, 2, 3 e 5; os cenários 4 e 6 são treinados no raciocínio, usando o banco como exemplo concreto.
- [a confirmar] Ordem de treino proposta no plano: 3 → 1 → 2 → 5 → 4 → 6 → simulação mista.

### 🔗 Conexões
- Mapa: [[moc-orquestra]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
