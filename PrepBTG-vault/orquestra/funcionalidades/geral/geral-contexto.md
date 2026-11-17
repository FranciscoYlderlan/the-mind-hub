---
tipo: contexto
funcionalidade: geral
status: em-construcao
etapa-atual: 1
criado: 2026-11-05
aliases: []
---
# 🧭 PrepBTG — contexto geral

> [!tldr] Em uma linha
> Preparar o estudo de caso de Analista de Compliance Engineering no BTG Pactual, treinando em um banco de dados mocado com Python e SQL

## Objetivo e motivação
Chegar bem preparado ao estudo de caso do BTG Pactual: treinar a linha de raciocínio em cenários de Compliance e praticar solução em dados (Python ou SQL puro) num banco mocado. Motivação: o estudo de caso foi aprovado e a etapa atual é a conversa com o head do time ([[processo-seletivo-btg]]).

## Fatos que eu informei
- Candidato à vaga de **Analista de Compliance Engineering** no BTG Pactual. A descrição que enviei é uma base da mesma modalidade, não a vaga exata ([[vaga-compliance-engineering]]).
- A primeira entrevista foi em 2026-11-03, das 10h30 às 11h (Brasília), com Vitória Palhares. Foi o primeiro contato com a empresa.
- O BTG me forneceu um podcast sobre o banco como material de preparo ([[cultura-btg-podcast]]).
- Já passei pela conversa técnica com a head e pelo estudo de caso (aprovado). **Agora é a conversa com o head do time, em 2026-11-11, 18h às 18h30** ([[roteiro-conversa-com-o-head]]).
- No estudo de caso, recebo questões e apresento minha linha de raciocínio.
- As 6 questões de treino foram criadas pelo Claude com base na vaga; não são o teste real ([[cenarios-de-pratica]]).
- Pontos para preparar: AWS, saída da TM Mentoring, mudança para São Paulo, pretensão salarial e a sigla "JEV" do currículo ([[pontos-delicados]]).
- **Etapa atual (declarada por mim em 2026-11-05):** criar um ambiente com banco de dados mocado e dados simulados, para eu treinar armazenar, tratar e gerar soluções em Python ou SQL puro ([[banco-mocado-contexto]]).
- O que vou usar nesse treino: eu forneço as instruções depois.
- Currículo e carta de recomendação da TM Mentoring estão em `Anexos/` (2026-11-11).
- **Teste em 2026-11-09 (segunda), 15h**: questões de SQL e discursivas de tomada de decisão, baseadas nos cases reais da área (Petterson, 2026-11-05; [[processo-seletivo-btg]]).
- Quero praticar o máximo até o teste, em cenários diferentes, com a minha evolução avaliada (2026-11-06).
- O projeto PrepBTG no claude.ai fica **sem documentos e sem instruções**. As pastas do cofre entram no chat como referência às pastas reais do computador e são lidas ao vivo; o problema da cópia velha no projeto está resolvido (2026-11-06).

## O que já foi feito
- 2026-11-05: cofre criado com `cofre.py criar` ([[diario-2026-11-05]]).
- 2026-11-05: contexto da conversa de preparação registrado em referências: processo, vaga, cenários, pontos delicados e instruções do coach.
- 2026-11-06: formato e data do teste registrados; reta final do treino montada em [[banco-mocado-plano]] com [[questoes-sql-de-prova]], [[questoes-tomada-de-decisao]] e o placar [[banco-mocado-plano-evolucao]] ([[diario-2026-11-06]]).
- 2026-11-06: problema do contexto resolvido: o projeto do claude.ai ficou vazio e o cofre é lido só pelas pastas reais ([[diario-2026-11-06]]).
- 2026-11-07: M1 da trilha de SQL feito; nova regra de solução performática pensando em big data ([[diario-2026-11-07]]).
- 2026-11-08: M3 da trilha de SQL feito; novas regras: até 6 questões por módulo e resumir a tabela grande antes de juntar ([[diario-2026-11-08]]).
- 2026-11-08: M4 da trilha de SQL feito; nova regra: 5 questões por módulo e uma bônus ([[diario-2026-11-08]]).
- 2026-11-09: revisão leve de M0 a M7 e teste feito ([[diario-2026-11-09]]).
- 2026-11-11: teste aprovado; módulos de preparo para a conversa com o head ([[diario-2026-11-11]]).

## Tempo disponível
Teste em 2026-11-09, 15h: sexta à tarde, sábado, domingo e a manhã de segunda. Horas por dia para o treino: [a preencher].

## Dial e modelo de IA
- Dial: [a confirmar] alto | medio | baixo
- Modelo de IA: [a preencher]

## Áreas sensíveis
- [[pontos-delicados]]: ler antes de qualquer simulação com a head.
- [[instrucoes-do-coach-de-entrevista]]: regra de não criar código sem pedido explícito.

## Mapa
- Roteiro: [[geral-plano]]
- Funcionalidades: [[banco-mocado-contexto]]
- Decisões: [[geral-decisao-2026-11-05-esqueleto-de-6-passos]], [[geral-decisao-2026-11-05-trilha-sql-e-python]], [[geral-decisao-2026-11-05-parquet-e-particao]], [[geral-decisao-2026-11-05-nulos-vao-para-quarentena]], [[geral-decisao-2026-11-05-treino-por-cenarios-concretos]], [[geral-decisao-2026-11-05-conducao-do-treino]], [[geral-decisao-2026-11-06-sql-antes-das-discursivas]], [[geral-decisao-2026-11-06-trilha-didatica-antes-dos-drills]], [[geral-decisao-2026-11-06-progresso-a-cada-questao]], [[geral-decisao-2026-11-07-solucao-performatica-big-data]], [[geral-decisao-2026-11-08-ate-6-questoes-por-modulo]] (substituída), [[geral-decisao-2026-11-08-cinco-questoes-e-bonus]], [[geral-decisao-2026-11-09-revisao-leve-do-dia-do-teste]], [[geral-decisao-2026-11-09-modulo-rapido-de-estatistica]], [[geral-decisao-2026-11-11-modulos-da-conversa-com-o-head]] (nomes `geral-decisao-AAAA-MM-DD-titulo`)
- Bugs: (nenhum ainda)
- Referências: [[processo-seletivo-btg]], [[roteiro-conversa-com-o-head]], [[roteiro-conversa-com-o-head-cartao]], [[cultura-btg-podcast]], [[cultura-btg-carreira]], [[vaga-compliance-engineering]], [[cenarios-de-pratica]], [[pontos-delicados]], [[instrucoes-do-coach-de-entrevista]], [[manual-da-orquestra]], [[manual-do-cerebro]]

## Interpretação do agente
- O roteiro em [[geral-plano]] é proposta minha e aguarda aprovação. Ele põe o banco mocado como etapa 2, porque é o foco declarado, e o treino dos cenários depois dele. [a confirmar]

### 🔗 Conexões
- Mapa: [[moc-orquestra]]
- Regras: [[manual-da-orquestra]]
