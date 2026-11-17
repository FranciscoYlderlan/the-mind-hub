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
- Container do MySQL: `mysql-compliance`. Uso o DBeaver para rodar as consultas (2026-11-06).
- Vejo o meu papel como quem programa, analisa, captura e exibe a informação para os analistas decidirem; não sou eu quem toma a decisão final (2026-11-06).

## O que já foi feito
- 2026-11-05: funcionalidade registrada no cofre, sem implementação ([[diario-2026-11-05]]).
- 2026-11-05: ambiente `mysql-estudos` entregue em .zip: docker-compose com MySQL 8.4, schema de Compliance/PLD, cerca de 67 mil transações simuladas, 1,9 mil alertas, listas restritivas e PEP, staging com problemas de qualidade, banco `gabarito` com 62 casos plantados para os cenários 1, 2, 3 e 5, e scripts Python (`conexao.py`, `teste_conexao.py`, exemplos). Testado carregando em MariaDB 10.11; ainda não rodado no MySQL 8.4 do humano.
- 2026-11-05: questões registradas em [[questoes-por-cenario]] e plano de treino em [[banco-mocado-plano]].
- 2026-11-05: T0 concluída: o humano subiu o `mysql-estudos` no WSL e confirmou o ambiente pronto. Próximo: T1 (cenário 3).
- 2026-11-05: o humano trouxe os 3 cenários genéricos originais, o [[esqueleto-de-6-passos]] e 7 exemplos de window functions em PostgreSQL. Viraram [[roteiros-dos-cenarios-genericos]], [[casos-de-treino-em-6-passos]] e [[sql-window-functions-mysql]] (traduzidos para MySQL). Decisão: [[geral-decisao-2026-11-05-esqueleto-de-6-passos]].
- 2026-11-05: conversa com um colega do time da vaga ([[relato-do-colega-do-time]]). Viraram 3 decisões (trilha SQL e Python, Parquet e partição, nulos na quarentena), as notas [[tratamento-de-nulos]] e [[estatistica-basica-e-eda]], o caso C8, as questões Q0.1 a Q0.4 e Q3.10 a Q3.12 e a tarefa T0b.
- 2026-11-06: formato do teste chegou (SQL e discursivas de decisão). Viraram [[questoes-sql-de-prova]], [[questoes-tomada-de-decisao]], o placar [[banco-mocado-plano-evolucao]] e a reta final T8 a T11 no plano.
- 2026-11-06: diagnóstico começou por D2 (gabarito pedido); o humano pediu SQL primeiro ([[geral-decisao-2026-11-06-sql-antes-das-discursivas]]). Cópia do banco exportada por mysqldump e lida pela IA: [[esquema-do-banco-compliance]]. Próximo: S2.
- 2026-11-06: o S2 mostrou que preciso revisar SQL do zero. Viraram a [[trilha-sql-didatica]] (M0 a M8), o [[banco-mocado-plano-registro-sql]] para o agente avaliador e [[geral-decisao-2026-11-06-trilha-didatica-antes-dos-drills]]. Próximo: M0.
- 2026-11-06: M0 feito (O0.1, O0.3 e O0.5+6 feitos; O0.2, O0.4 e C0 pulados), registrado em [[banco-mocado-plano-registro-sql]]. O M0 ficou abaixo do meu nível. Nova regra: progresso a cada questão ([[geral-decisao-2026-11-06-progresso-a-cada-questao]]). Próximo: M1.
- 2026-11-07: M1 feito (O1.1 a O1.6 e C1), registrado em [[banco-mocado-plano-registro-sql]]. Erros que voltaram: condição do enunciado esquecida e nome de coluna. Nova regra: toda solução na versão performática ([[geral-decisao-2026-11-07-solucao-performatica-big-data]]). Próximo: M2.
- 2026-11-07: M2 feito (O2.1 a O2.6 e C2), registrado em [[banco-mocado-plano-registro-sql]]. Primeira rodada do agente avaliador: score geral 72,4, M1 e M2 em Consolidação, erros recorrentes `SINTAXE` e `COND`. Achados de negócio na sessão: depósitos em espécie colados abaixo de R$ 10 mil (R02, fracionamento) e o `HAVING` de volume escondendo os canais de espécie (`CAIXA`, `AGENCIA`). Próximo: M3.
- 2026-11-08: M3 feito (O3.1 a O3.5 e C3, depois da tratativa do avaliador), registrado em [[banco-mocado-plano-registro-sql]]. Novas regras: até 6 questões por módulo ([[geral-decisao-2026-11-08-ate-6-questoes-por-modulo]]) e resumir a tabela grande antes de juntar ([[geral-decisao-2026-11-07-solucao-performatica-big-data]], item 7). Erro que voltou: `COND`. Achados de negócio: PF com remessa de R$ 265 mil ao Iêmen de madrugada; PF com débitos de até 50 vezes a renda anual; nas R05 e R06, 86% dos alertas com score a partir de 70 foram falso positivo. Próximo: M4.
- 2026-11-08: M4 feito (O4.1 a O4.4 e C4; a bônus, transações acima da média geral, ficou opcional), registrado em [[banco-mocado-plano-registro-sql-m3-a-m8]]. As aulas de `LEFT JOIN` e anti-join só funcionaram refeitas em passos pequenos, com tabelas de brinquedo. Nova regra: 5 questões e 1 bônus ([[geral-decisao-2026-11-08-cinco-questoes-e-bonus]]). Erros: apelido de subconsulta usado fora dela (`SINTAXE`) e `COUNT(*)` depois do `LEFT JOIN` (`GRAN`). Achado: 15 contas ativas de PJ com faturamento acima da média paradas em 2026. Próximo: M5.
- 2026-11-08: M5 feito (O5.1 a O5.4 e C5; a bônus ficou opcional), registrado em [[banco-mocado-plano-registro-sql-m3-a-m8]]. As aulas só assentaram refeitas com analogias do dia a dia (cestos, mãos levantadas, provas na gaveta) e degraus de uma ideia só antes das questões. Erros: sintaxe de datas (`INTERVAL`, aspas na unidade, `<` contra `>`) e o percentual (divisão invertida, `CASE` com a pergunta errada). Achados: 95% a 98% de falso positivo nas 5 maiores regras, contando só os encerrados; 27 de 42 clientes ALTO com KYC vencido há mais de 24 meses. Avaliador do M5 rodado (score geral 65,8, em [[banco-mocado-plano-registro-sql]]).
- 2026-11-08: M6 começado e pausado em 2 de 5 (O6.1 e O6.2), para o humano ver o M7 antes de um simulado com um amigo às 15h. O humano corrigiu a razão da O6.2 (crédito ÷ renda). Achado: um PF com renda de R$ 1,2 mil recebeu 50,47 vezes a renda anual em 2026 (Otávio Barbosa Marques).
- 2026-11-08: M7 começado e pausado em 2 de 5 (O7.1 e O7.2) para o simulado das 15h, registrado em [[banco-mocado-plano-registro-sql-m3-a-m8]]. Erro central: gaveta da janela por conta em vez de cliente, remendada com `GROUP BY`. Achados: a maior transação do banco é um câmbio de R$ 1,73 milhão recebido dos EUA pela Nunes Empreendimentos Ltda; o cliente 438 (ALTO) movimentou R$ 183,7 milhões, 7 vezes o 2º do nível.
- 2026-11-09: reaula de M5 e M7 para o teste, registrada em [[diario-2026-11-09]]. No M7: 4 ideias (espremedor contra etiqueta, `ROW_NUMBER`/`RANK`, `LAG` e janela de 7 dias, `PARTITION BY` da tabela contra o da janela) e o E1 montado junto (último alerta por cliente e % por desfecho, com o total por subconsulta). Erros: `OVER` sem `ORDER BY` dá o total do grupo, não o acumulado; faltou reduzir com `GROUP BY` antes de janelar.
- 2026-11-09: revisão leve do dia do teste feita (10h13 a 11h20): M0, M1, M2, M3, M4 e M6, uma questão discursiva por módulo, e depois M5 e M7 com o mesmo formato (até 11h55); M8 ficou fora (nunca estudado). Raciocínio certo em todos. Pontos a levar para a prova: dizer o custo (o W da fórmula), o 2º `GROUP BY` por cliente depois do `JOIN` quando o pedido soma todas as contas, "não existe linha onde a chave combina" no `NOT EXISTS`, e no top N por grupo o `rn <= N` numa consulta de fora (não `LIMIT`) e o filtro de data do enunciado (o `COND` voltou no M7). Próximo: módulo rápido de estatística ([[geral-decisao-2026-11-09-modulo-rapido-de-estatistica]]).
- 2026-11-09: módulo rápido de estatística dado das 12h06 às 12h23, enxugado a pedido do humano para fórmula + analogia + big data, com visuais (régua do cliente, soma barata contra ordenar caro, boxplot). Resumo no "Kit de bolso" de [[estatistica-basica-e-eda]]. Às 12h38 a aula foi refeita com o roteiro de 4 perguntas e os 3 cenários; o humano pediu a resposta-modelo da questão do analista que fecha alertas rápido (registrada no Kit de bolso) e disse que ainda não entendeu a estatística: a aula recomeça do zero, uma ideia por vez, num chat novo (item 6 da decisão).

## Tempo disponível
Até o teste de 2026-11-09, 15h ([[processo-seletivo-btg]]). Horas por dia: [a preencher].

## Dial e modelo de IA
- Dial: [a confirmar] (padrão: o do [[geral-contexto]])
- Modelo de IA: [a preencher]

## Áreas sensíveis
- Dados são **simulados**: nada de dados reais de clientes ou do BTG.
- Código só com pedido explícito ([[instrucoes-do-coach-de-entrevista]]). Nos exemplos do ambiente, só o `ex01` vem resolvido; `ex02`, `ex03` e `ex05` são esqueletos com TODOs, porque resposta-modelo lida não vale como treino.
- O gabarito fica no banco separado `gabarito`, consultado só depois de tentar.

## Mapa
- Plano: [[banco-mocado-plano]] (agenda: [[banco-mocado-plano-agenda]]) · Placar: [[banco-mocado-plano-evolucao]] · Registro da trilha: [[banco-mocado-plano-registro-sql]] (M3 em diante: [[banco-mocado-plano-registro-sql-m3-a-m8]])
- Questões: [[questoes-por-cenario]]
- Decisões: [[geral-decisao-2026-11-05-esqueleto-de-6-passos]], [[geral-decisao-2026-11-05-trilha-sql-e-python]], [[geral-decisao-2026-11-05-parquet-e-particao]], [[geral-decisao-2026-11-05-nulos-vao-para-quarentena]], [[geral-decisao-2026-11-05-conducao-do-treino]], [[geral-decisao-2026-11-06-sql-antes-das-discursivas]], [[geral-decisao-2026-11-06-trilha-didatica-antes-dos-drills]], [[geral-decisao-2026-11-06-progresso-a-cada-questao]], [[geral-decisao-2026-11-07-solucao-performatica-big-data]], [[geral-decisao-2026-11-08-cinco-questoes-e-bonus]], [[geral-decisao-2026-11-09-revisao-leve-do-dia-do-teste]], [[geral-decisao-2026-11-09-modulo-rapido-de-estatistica]]
- Bugs: (nenhum ainda)
- Referências: [[cenarios-de-pratica]], [[vaga-compliance-engineering]], [[esqueleto-de-6-passos]], [[roteiros-dos-cenarios-genericos]], [[casos-de-treino-em-6-passos]], [[sql-window-functions-mysql]], [[tratamento-de-nulos]], [[estatistica-basica-e-eda]], [[relato-do-colega-do-time]], [[questoes-sql-de-prova]], [[questoes-tomada-de-decisao]], [[esquema-do-banco-compliance]], [[trilha-sql-didatica]], [[trilha-sql-didatica-avancado]], [[trilha-sql-didatica-extras]]

## Interpretação do agente
- Os dados simulados refletem os cenários 1, 2, 3 e 5; os cenários 4 e 6 são treinados no raciocínio, usando o banco como exemplo concreto.
- [a confirmar] Ordem de treino proposta no plano: 3 → 1 → 2 → 5 → 4 → 6 → simulação mista.

### 🔗 Conexões
- Mapa: [[moc-orquestra]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
