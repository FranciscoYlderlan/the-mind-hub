---
aliases: [Esqueleto de 6 passos, Roteiro de resposta do estudo de caso, Answer framework, Como montar a resposta]
tags: [carreira/entrevistas]
tipo: referencia
tema: treino
status: em-uso
criado: 2026-11-05
origem: Esqueleto fornecido pelo humano em 2026-11-05 ([[geral-decisao-2026-11-05-esqueleto-de-6-passos]])
---
# 🧱 Esqueleto de 6 Passos

> [!tldr] Em uma linha
> Toda resposta do estudo de caso segue 6 passos fixos: esclarecer, definir a referência, simples antes de sofisticado, acionável, medir e governar.

É como **a receita de bolo da avó**: a ordem dos passos nunca muda, o que muda é o sabor. Na hora da pergunta, eu não gasto energia decidindo *por onde começar*: começo sempre pelo passo 1. Vale para os [[cenarios-de-pratica]], para as [[questoes-por-cenario]] e para os [[casos-de-treino-em-6-passos]].

---

| Passo | Por que importa | Pergunta que eu me faço |
|---|---|---|
| **1. Esclarecer** | Evita resolver o problema errado. Em Compliance, "falso positivo" ou "movimentação" mudam a solução conforme a definição. | O que exatamente estão pedindo, com que dado, para quem e em que prazo? |
| **2. Definir a referência** | Anomalia só existe em relação a algo (perfil, pares, histórico). Sem referência, não dá para dizer o que é "incompatível". | Incompatível **com o quê**? Declarado, histórico do próprio cliente ou pares do segmento? |
| **3. Simples antes de sofisticado** | Regras são auditáveis e o regulador espera isso. Entregam valor rápido. ML entra depois, para o que as regras não pegam. | Qual a regra mais simples que já separa o caso? O que ela não pega? |
| **4. Acionável e explicável** | O resultado só vale se o analista consegue agir. Cada alerta leva o motivo e o contexto. | O analista lê o alerta e sabe **por que** ele existe e **o que** olhar? |
| **5. Medir e validar** | Sem métrica não dá para saber se melhorou. Medir também o que está deixando de capturar. | Qual a precisão? Qual a cobertura? Como provo com teste retroativo? |
| **6. Governar** | Em banco tudo é rastreável: logs, versões, aprovações. A vaga cita isso. | Quem aprovou a regra, qual versão rodou e onde fica a evidência? |

> [!note] Passo 1 na prática: o método das 5 lacunas
> Diante do enunciado, procure o que falta saber em cada caixa. Cada lacuna vira uma pergunta à head.
> 1. **Objetivo:** para que serve o trabalho e o que muda com a resposta?
> 2. **O dado:** o que é cada linha, de onde vem, que período cobre, já foi limpo?
> 3. **Definições:** que termo pode ter dois sentidos (unidade, sinal do valor, "suspeito")?
> 4. **Quem usa:** quem recebe o resultado e o que faz com ele?
> 5. **Entrega:** prazo, formato e o que é "pronto"?
> Bastam 3 ou 4 perguntas. **Teste:** se a head responder A ou B, eu faria algo diferente? Se não, corte a pergunta.
> **Hipótese:** antes de abrir os dados, pense na natureza deles (os valores são parecidos ou alguns muito maiores? que sujeira um sistema costuma deixar? todos os clientes se comportam igual?) e escreva um palpite para os dados testarem.

> [!note] Como o SQL entra em cada passo
> 1. **Esclarecer:** `SHOW COLUMNS` e a primeira olhada em pandas ([[estatistica-basica-e-eda]]) para ver o dado real antes de supor.
> 2. **Referência:** janelas (`OVER`) para comparar com o histórico (`LAG`, `AVG ... ROWS`) ou com os pares (`PERCENT_RANK`, `NTILE`); em Python, mediana, percentil e z-score robusto.
> 3. **Simples:** `WHERE` com 2 ou 3 limites claros, antes de qualquer score.
> 4. **Explicável:** coluna `motivo` montada com `CONCAT_WS`, mais os números que dispararam o alerta.
> 5. **Medir:** `GROUP BY regra` com taxa de falso positivo, precisão e casos perdidos.
> 6. **Governar:** versão da regra, data de execução e parâmetros gravados junto do resultado.
> Padrões prontos: [[sql-window-functions-mysql]].

> [!warning] Armadilha comum
> Pular do passo 1 direto para "eu usaria machine learning". A head quer ver os passos 2 e 3 antes: referência clara e regra simples, explicável para o auditor.

> [!example] Fechamento falado
> Depois dos 6 passos, uma versão de cerca de **90 segundos** em voz alta: uma frase por passo.

> [!tip] Quando abrir esta nota
> No começo de cada simulação, antes de responder a primeira pergunta da head.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** A ordem é fixa: esclarecer, referência, regra simples, alerta explicável, métrica, governança.
* **Ponto 2:** O passo 2 é o coração em PLD: "incompatível" sempre tem um "com o quê".
* **Ponto 3:** Erro comum: medir só falso positivo e esquecer o que a regra **deixa passar**.

### 🔗 Conexões
- Mapa: [[moc-orquestra]]
- Decisão: [[geral-decisao-2026-11-05-esqueleto-de-6-passos]], [[geral-decisao-2026-11-05-conducao-do-treino]]
- Relacionadas: [[cenarios-de-pratica]], [[roteiros-dos-cenarios-genericos]], [[casos-de-treino-em-6-passos]], [[sql-window-functions-mysql]]
- Próxima: [[roteiros-dos-cenarios-genericos]]
