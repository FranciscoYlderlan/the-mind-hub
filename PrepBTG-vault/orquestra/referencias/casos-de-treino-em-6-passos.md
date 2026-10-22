---
aliases: [Casos de treino em 6 passos, Novos cenários com window functions, Practice cases, Casos C1 a C8]
tags: [carreira/entrevistas, estudos/programacao]
tipo: referencia
tema: treino
status: rascunho
criado: 2026-11-05
origem: Criados pelo Claude em 2026-11-05 a partir dos cenários genéricos, das tabelas do `mysql-estudos` e dos exemplos de window functions do humano
---
# 🏋️ Casos de Treino em 6 Passos

> [!tldr] Em uma linha
> Oito casos curtos, no mesmo formato dos cenários genéricos, cada um treinando um conceito de SQL dentro do esqueleto de 6 passos.

Os [[roteiros-dos-cenarios-genericos]] são o **treino guiado**; estes casos são o **treino livre**: só o enunciado da head e uma pergunta por passo. A resposta eu monto. O padrão de SQL de cada caso está em [[sql-window-functions-mysql]], para consultar **depois** de tentar.

> [!warning] Não é o teste real
> Casos criados pelo Claude. Dados 100% simulados. Nomes de coluna: ver o quadro "Antes de rodar" em [[roteiros-dos-cenarios-genericos]].

---

| Caso | Enunciado da head | Conceito | Liga com |
|---|---|---|---|
| **C1** Salto de recebimento | *"Uma cliente PF com renda de R$ 2 mil recebeu R$ 50 mil este mês. Como você acharia todos os casos assim, sem afogar o time?"* | Média dos meses anteriores (`AVG ... ROWS 3 PRECEDING AND 1 PRECEDING`) | Padrão 3, Q1.1 |
| **C2** Fora da curva no segmento | *"R$ 30 mil é muito ou pouco? Depende de quem recebe. Quem está no topo do próprio grupo?"* | `PERCENT_RANK`, `NTILE` por segmento | Padrão 4, Q1.2 |
| **C3** Muitos créditos pequenos | *"Vemos depósitos abaixo de R$ 10 mil que, somados no mesmo dia, passam de R$ 50 mil. Como pegar isso?"* | Janela por tempo (`RANGE ... INTERVAL 24 HOUR`) | Padrão 5, Q1.5 |
| **C4** O dinheiro não para | *"Algumas contas recebem e mandam quase tudo embora em poucas horas. Como você mede isso?"* | Próxima transação (`LEAD`) | Padrão 6, Q1.6 |
| **C5** Gente nova mandando dinheiro | *"Um cliente passou a receber de dezenas de pessoas que nunca tinham aparecido. Como contar isso?"* | Primeira ocorrência (`ROW_NUMBER ... = 1`) | Padrão 7, Q1.2 |
| **C6** A regra que só faz barulho | *"A regra R03 dobrou o volume em dois meses e quase tudo é fechado como falso positivo. O que mudou?"* | Mês contra mês (`LAG`) em `alertas` | Padrão 2, Q2.1, Q2.7 |
| **C7** A carga que rodou duas vezes | *"O job da madrugada rodou duas vezes e o painel mostra o dobro. Como você garante que isso não se repete?"* | Deduplicação (`ROW_NUMBER` por chave) e idempotência | Padrão 1, Q3.5, Q3.8 |
| **C8** Primeira olhada nos dados | Enunciado em reescrita como cenário concreto, no início da T0b ([[geral-decisao-2026-11-05-treino-por-cenarios-concretos]]) | Análise exploratória em pandas: `describe`, nulos, duplicados, histograma em log, z-score robusto | [[estatistica-basica-e-eda]], Q0.1 a Q0.4 |

---

> [!note] Uma pergunta por passo (vale para todos os casos)
> 1. **Esclarecer:** que palavra do enunciado pode ter dois sentidos? Pergunte antes de abrir o SQL.
> 2. **Referência:** "muito" ou "estranho" em relação a quê: renda, histórico ou pares?
> 3. **Simples:** qual o `WHERE` com 2 ou 3 limites que já separa o caso?
> 4. **Explicável:** que coluna `motivo` o analista lê e entende sozinho?
> 5. **Medir:** quantos casos saem, quantos são iscas e quantos o gabarito tem que eu não peguei?
> 6. **Governar:** que parâmetro precisa de versão e aprovação?

> [!example] Perguntas de aprofundamento que a head pode fazer
> - C1: "E se a cliente tiver só 1 mês de histórico?" (frame com menos de 3 meses)
> - C2: "Por que percentil e não um valor fixo?" (justiça entre segmentos)
> - C3: "E se ele espalhar em 30 horas?" (o tamanho da janela é parâmetro, não verdade)
> - C4: "E se a saída for dividida em 5 transferências?" (`LEAD` só olha a próxima)
> - C5: "Folha de pagamento também traz remetente novo?" (iscas e exceções)
> - C6: "Como provar que recalibrar não perde caso real?" (teste retroativo)
> - C7: "O reenvio chegou com valor diferente. Qual vale?" (regra de versão documentada)
> - C8: "A média é R$ 8 mil. Isso descreve o cliente típico?" (assimetria: mediana e escala log)

> [!tip] Quando abrir esta nota
> No treino livre, depois dos roteiros guiados, ou na T7 (simulação mista) do [[banco-mocado-plano]].

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** Cada caso treina **um** conceito (de janela ou de análise exploratória) dentro dos 6 passos do [[esqueleto-de-6-passos]]; a resposta usa SQL para extrair e Python para analisar.
* **Ponto 2:** Ordem: C8 → C7 → C1 → C2 → C3 → C4 → C5 → C6, seguindo o plano (olhar os dados, depois o pipeline).
* **Ponto 3:** Erro comum: escrever o SQL antes do passo 2; sem referência, o resultado não tem como ser explicado.

### 🔗 Conexões
- Mapa: [[moc-orquestra]]
- Base: [[esqueleto-de-6-passos]]
- Decisão: [[geral-decisao-2026-11-05-treino-por-cenarios-concretos]]
- Relacionadas: [[roteiros-dos-cenarios-genericos]], [[sql-window-functions-mysql]], [[questoes-por-cenario]], [[estatistica-basica-e-eda]]
- Próxima: [[sql-window-functions-mysql]]
