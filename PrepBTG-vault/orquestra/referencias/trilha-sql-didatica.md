---
aliases: [Trilha de SQL, Plano didático de SQL, Revisão de SQL do zero, SQL learning path]
tags: [carreira/entrevistas, estudos/programacao]
tipo: referencia
tema: treino
status: em-uso
criado: 2026-11-06
origem: Criada pelo Claude em 2026-11-06 a pedido do humano, depois do S2 de [[questoes-sql-de-prova]] mostrar a necessidade de revisar SQL; perfil lido no Vault (Quem Sou Eu, AuDHD, Atenção em túnel, Cronotipo matutino, Pomodoro Curto 15-5, Sensibilidade à rejeição)
---
# 🧱 Trilha Didática de SQL

> [!tldr] Em uma linha
> Um curso curto de SQL no banco `compliance`: cada módulo **ensina** um conjunto de técnicas, me faz praticar com ajuda e mede quanto eu evoluí, até eu ter a base para os 18 drills de [[questoes-sql-de-prova]].

A trilha é como **autoescola antes do exame do Detran**. O instrutor explica o pedal, dirige do meu lado, me deixa errar na rua calma e só depois me leva para a baliza. O exame (os drills) vem no fim, quando eu já tenho as aulas. Durante as aulas, errar é parte do trabalho.

---

## Como cada sessão roda (esqueleto fixo)
O formato é sempre o mesmo, e o conteúdo muda a cada módulo: rotina que acalma, novidade que mantém o interesse (AuDHD, no Vault). Blocos do Pomodoro Curto 15-5 (no Vault).

1. **Abertura (3 min):** a IA resume o módulo anterior em 3 linhas e faz 1 pergunta-relâmpago de revisão.
2. **Aula (1º bloco):** a IA ensina cada item do "Aprendo" do módulo: o que é, para que serve no compliance, a sintaxe, **um exemplo resolvido e rodado** na cópia do banco e os erros comuns. Para `GROUP BY`, `HAVING`, `WITH ROLLUP` e `JOIN`, a IA usa a analogia das **caixas** (linhas na mesa, caixas, etiquetas), pedida pelo humano. Pergunto à vontade; aqui não há nota ([[geral-decisao-2026-11-05-conducao-do-treino]]).
3. **Prática guiada (1ª operação):** fazemos juntos. A IA pensa em voz alta, eu digito e rodo.
4. **Prática (demais operações):** eu digo a granularidade ("uma linha por ___"), escrevo, rodo no DBeaver quantas vezes quiser e colo no chat a consulta e as primeiras linhas. A IA corrige **explicando o porquê**. Travou: a IA ensina de novo por outro ângulo antes de dar a resposta. Se eu pedir a solução, ela mostra, e eu refaço uma variante sozinho.
5. **Extras, se eu pedir (1 bloco opcional):** uma por vez, de [[trilha-sql-didatica-extras]]: a mesma técnica de uma operação já feita, em outra situação, nunca conteúdo novo.
6. **Checagem do módulo:** um exercício parecido, feito por mim. Mede quanto aprendi; não aprova nem reprova. Se não sair, a IA reensina o ponto e dá uma variante. Depois dela, a **bônus**, se eu quiser.
7. **Fechamento (3 min):** a IA entrega as linhas do registro ([[banco-mocado-plano-registro-sql]]) e diz o próximo módulo, para o "Onde parei".

> [!warning] Regras do perfil
> - **Um módulo por sessão.** Trocar de assunto no meio custa energia (Atenção em túnel, no Vault).
> - **Aula de módulo novo de manhã; prática e revisão à tarde.** Cronotipo matutino (no Vault).
> - **Medir o que eu fiz e quanto evoluí**, não quanto errei (Sensibilidade à rejeição, no Vault).
> - **Tempo anotado, sem cobrança.** Serve para ver a evolução; a cobrança de tempo fica para os drills.
> - **⚡ Big data sempre:** toda solução vem na versão mais performática, com uma linha dizendo por quê (filtro sargable, colunas escolhidas, `EXPLAIN`, índice ou partição) ([[geral-decisao-2026-11-07-solucao-performatica-big-data]]).
> - **5 questões por módulo, checagem incluída, e uma 6ª bônus**, do M4 em diante: cada questão junta mais de uma técnica do "Aprendo"; a bônus não traz conteúdo novo, e pular não faz perder nada ([[geral-decisao-2026-11-08-cinco-questoes-e-bonus]]).
> - **Resumir a tabela grande antes de juntar:** quando a consulta agrega, o `GROUP BY` vai na subconsulta antes do `JOIN`; a IA aponta sempre que eu juntar antes sem motivo ([[geral-decisao-2026-11-07-solucao-performatica-big-data]], item 7).
> - **Progresso a cada questão:** feita ou pulada, a IA mostra antes da próxima quantas foram feitas, quais faltam (com a checagem) e em que módulo da trilha estou, no formato fixo da decisão (barra `▰▱` com 1 bloco por questão, "N de T" e as linhas Feitas, Agora, Falta e Trilha). Pulada conta como feita e a IA não insiste nela ([[geral-decisao-2026-11-06-progresso-a-cada-questao]]).

---

## Módulos M0 a M4 (base)
Cada operação usa só o que já foi ensinado. As setas indicam para qual drill a técnica prepara. M5 a M8 e a retomada: [[trilha-sql-didatica-avancado]].

### M0. Descobrir um banco que eu não conheço
**Aprendo:** `SHOW TABLES`, `DESCRIBE`, as tabelas da `information_schema` (`tables`, `columns`, `key_column_usage`), `SELECT * ... LIMIT`, `DISTINCT`, `MIN`/`MAX`, `COUNT(*)` contra `COUNT(coluna)`; e o raciocínio de chave primária, chave estrangeira e "o que é uma linha".
A IA ensina os comandos e o raciocínio; o que o banco `compliance` contém, **eu descubro**, com dicas e não com respostas. A nota [[esquema-do-banco-compliance]] só aparece depois da checagem.
- **O0.1 Quais tabelas existem e qual é a maior?** Dica: `SHOW TABLES`; `table_rows` da `information_schema.tables` é aproximado. Confirme as 3 maiores com `COUNT(*)`.
- **O0.2 O que é uma linha de cada tabela?** Dica: `LIMIT 5` e `DESCRIBE` (`Key = PRI`). Complete "uma linha de X é um(a) ___".
- **O0.3 Como as tabelas se ligam?** Dica: colunas `_id` com o mesmo nome; `key_column_usage`. Qual tabela fica no meio do caminho?
- **O0.4 Que valores uma coluna de categoria aceita?** Dica: `SELECT DISTINCT`. Código que eu não entendo no negócio: pergunto à IA.
- **O0.5 Que período os dados cobrem, e as datas têm hora?** Dica: `MIN()` e `MAX()`.
- **O0.6 Onde estão os buracos?** Dica: `COUNT(*)` menos `COUNT(coluna)` são os nulos.
- **Checagem:** meu mapa escrito por mim: tabelas, o que é uma linha de cada uma, ligações e 3 armadilhas. A IA aponta o que falta com perguntas.

### M1. Filtrar e ordenar (`SELECT`, `WHERE`, `ORDER BY`, `LIMIT`)
**Aprendo:** escolher colunas e dar apelido (`AS`); comparar (`=`, `<>`, `>`, `>=`); juntar condições com `AND`, `OR` e parênteses; `IN`, `BETWEEN`, `LIKE` com `%`; `IS NULL`; ordenar (`ASC`, `DESC`) e cortar (`LIMIT`); filtrar data que tem hora.
- **O1.1** Nome e risco dos clientes PJ.
- **O1.2** Clientes PF de risco ALTO, da maior para a menor `renda_mensal`.
- **O1.3** Créditos (`direcao = 'C'`) em PIX acima de R$ 50 mil, os 20 maiores.
- **O1.4** Transações de janeiro de 2026 de dois jeitos: `>= '2026-01-01' AND < '2026-02-01'` e `BETWEEN '2026-01-01' AND '2026-01-31'`. Por que a contagem muda?
- **O1.5** `IN` e `LIKE`: depósitos e saques em espécie; contrapartes com "Ltda" no nome.
- **O1.6** `IS NULL`: alertas ainda sem `data_encerramento`.
- **Checagem:** os 10 maiores créditos em TED de 2026, com data e valor. → S2

### M2. Agrupar e contar (`COUNT`, `SUM`, `AVG`, `GROUP BY`, `HAVING`)
**Aprendo:** o que uma função de agregação faz com várias linhas; `GROUP BY` como "uma linha por grupo"; a regra das colunas não agregadas; `COUNT(*)`, `COUNT(coluna)` e `COUNT(DISTINCT)`; `WHERE` antes de agrupar e `HAVING` depois; agrupar por mês.
- **O2.1** Total de clientes; depois por `tipo_pessoa`.
- **O2.2** Por `tipo_pessoa` **e** `risco_kyc`, do maior para o menor. → S1
- **O2.3** Soma, média, mínimo e máximo de `valor` por `tipo` de transação.
- **O2.4** Em `alertas`: `COUNT(*)`, `COUNT(data_encerramento)` e `COUNT(DISTINCT analista)`. Por que dão números diferentes?
- **O2.5** Regras com mais de 200 alertas (`HAVING`); depois, só contando os FALSO_POSITIVO (`WHERE` filtra linhas antes, `HAVING` filtra grupos depois). → S4
- **O2.6** Volume de créditos por mês com `DATE_FORMAT(data_hora, '%Y-%m')`.
- **Checagem:** quantidade e soma de transações por `canal`, só os canais com mais de 5 mil transações.

### M3. Juntar tabelas (`JOIN`)
**Aprendo:** o que o `JOIN` faz linha a linha; `ON` com a chave certa; apelido de tabela; atravessar uma tabela do meio; granularidade antes e depois do `JOIN`; por que a soma infla quando se juntam duas tabelas "filhas" (o garfo, ensinado na aula).
- **O3.1** Cada conta com o nome do cliente.
- **O3.2** Quantas contas cada cliente tem e quem tem mais de uma, resumindo `contas` antes de juntar.
- **O3.3** Transações com o nome do cliente (dois `JOIN`), 20 linhas.
- **O3.4** Soma de créditos de 2026 por cliente, resumindo por conta antes de juntar. Por que o ranking por conta é diferente? → S2
- **O3.5** Remessas para países de `paises_risco`, com nome do cliente e do país (quatro tabelas). → S12
- **Checagem:** os 10 clientes PF com maior soma de **débitos** em 2026.

### M4. O que falta (`LEFT JOIN`, anti-join, subconsulta)
**Aprendo:** `LEFT JOIN` e o `NULL` que ele cria; anti-join com `IS NULL` e com `NOT EXISTS`; onde pôr o filtro (`ON` ou `WHERE`); subconsulta com `IN`; subconsulta que devolve um valor só.
- **O4.1** Alertas por cliente com `LEFT JOIN`, mostrando quem tem zero. `COUNT(*)` ou `COUNT(a.alerta_id)`?
- **O4.2** Clientes sem nenhum alerta, de dois jeitos: `LEFT JOIN ... WHERE a.alerta_id IS NULL` e `NOT EXISTS`. O resultado bate? → S3
- **O4.3** A armadilha: alertas COMUNICADO_COAF por cliente, com zero para quem não tem; o filtro da tabela da direita no `WHERE` vira `INNER JOIN`. Mover para o `ON` e comparar.
- **O4.4** `IN` com subconsulta: clientes com alguma remessa (`CAMBIO_ENVIO`) para país de risco.
- **Checagem:** contas ativas sem nenhuma transação em 2026, de clientes PJ com `faturamento_anual` acima da média dos PJ (anti-join e subconsulta de um valor só).
- **Bônus:** transações acima da média geral.

> [!tip] Quando abrir esta nota
> No começo de cada sessão de SQL, para ver o módulo da vez, e no fechamento, para marcar a checagem.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** Primeiro a aula com exemplo resolvido, depois a prática com ajuda, por último a checagem.
* **Ponto 2:** Errar na prática é o treino; a checagem mede evolução, não aprova.
* **Ponto 3:** Granularidade dita antes da consulta evita o erro mais comum, a soma inflada.

### 🔗 Conexões
- Mapa: [[moc-orquestra]]
- Relacionadas: [[trilha-sql-didatica-extras]], [[esquema-do-banco-compliance]], [[questoes-sql-de-prova]], [[banco-mocado-plano]]
- Próxima: [[trilha-sql-didatica-avancado]]
