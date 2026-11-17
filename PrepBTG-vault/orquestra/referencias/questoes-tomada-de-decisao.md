---
aliases: [Questões discursivas, Cases de decisão, Tomada de decisão Compliance, Decision cases]
tags: [carreira/entrevistas]
tipo: referencia
tema: treino
status: rascunho
criado: 2026-11-06
origem: Criadas pelo Claude em 2026-11-06 a partir do formato relatado por Petterson ([[processo-seletivo-btg]]) e da [[vaga-compliance-engineering]]
---
# ⚖️ Questões Discursivas de Tomada de Decisão

> [!tldr] Em uma linha
> Doze cases no estilo "o que você decide e por quê", para treinar a parte discursiva do teste de 2026-11-09.

> [!warning] Não são os cases reais do BTG
> Criados pelo Claude imitando situações comuns de Compliance num banco de investimento e banco digital. Os cases reais do teste serão outros; o que se treina aqui é **decidir com estrutura**.

Uma questão de decisão é como **um semáforo amarelo**: não existe resposta sem risco, existe a escolha que você consegue defender depois. A banca quer ver se você decide, se pesa o risco e se deixa rastro.

---

> [!note] Como responder: os 6 passos com a decisão na frente
> O esqueleto é o de [[esqueleto-de-6-passos]]. Em questão de decisão, mudam três coisas:
> - **A decisão abre a resposta**, numa frase ("Seguro a TED e escalono para o gestor de PLD"). Os 6 passos viram a justificativa.
> - **Passo 3 compara caminhos:** 2 ou 3 opções, com o custo de cada uma (risco que fica, atrito com o cliente, custo operacional).
> - **Passo 6 inclui escalonamento:** quem aprova, prazo, o que fica registrado e o que eu automatizaria para não repetir.
>
> Escrita: 8 a 12 linhas. Falada: cerca de 90 segundos.

> [!info] Base regulatória para citar (sem decorar artigo)
> - Lei 9.613/1998: lavagem de dinheiro, dever de comunicar ao COAF e de **não avisar o cliente**.
> - Resolução CVM 50/2021 (PLD/FTP no mercado de valores mobiliários), alterada em 2026-07 pela Resolução CVM 245, que reforça a diligência com jurisdições de alto risco.
> - Circular BCB 3.978/2020: PLD/FTP nas instituições do Banco Central [a confirmar: vigência e alterações recentes].
> - Abordagem baseada em risco: o controle é proporcional ao risco.

## Cases

- **D1. PEP com patrimônio novo.** Um ex-secretário estadual quer abrir conta com R$ 15 milhões vindos da venda de uma empresa da família. O comercial quer fechar até sexta. Você aprova o onboarding?
- **D2. Match de sanção com o relógio correndo.** Às 16h20 o screening barra uma TED de R$ 2 milhões: a contraparte tem 91% de similaridade com um nome de lista de sanções. O cut-off é 17h e o cliente é antigo. Libera ou segura?
- **D3. Regra que corta alerta mas perde caso.** A recalibração da R03 reduz 40% dos alertas. No teste retroativo, 2 dos 50 casos comunicados ao COAF no ano não teriam alertado. Você aprova?
- **D4. Exceção para cliente estratégico.** A diretoria comercial pede para dispensar a atualização de KYC de um grupo empresarial grande "porque o relacionamento é antigo". O cadastro venceu há 30 meses.
- **D5. Mídia negativa.** Sai notícia de que o sócio de uma PJ cliente é investigado por corrupção, sem denúncia formal. A PJ movimenta R$ 40 milhões por mês. Mantém, restringe ou encerra?
- **D6. Pipeline quebrado.** De madrugada a carga falhou e as regras de D+1 rodaram com 30% das transações. Ninguém percebeu até as 10h. O que você faz hoje e o que muda no processo?
- **D7. Colaborador e informação privilegiada.** Um analista da mesa comprou ações de uma empresa dois dias antes de o banco anunciar que assessora a oferta dela. Ele diz que não sabia. Como você conduz?
- **D8. Dado de cliente em IA pública.** Você descobre que um analista colou justificativas de alerta, com nome e CPF, numa ferramenta de IA pública para "melhorar o texto".
- **D9. Comunicar ou não ao COAF.** O caso tem sinais atípicos, mas o cliente trouxe documentação parcial que explica metade do volume. O prazo interno vence amanhã.
- **D10. Lista desatualizada.** O fornecedor da lista restritiva ficou 5 dias sem atualizar, e nesse período entraram 12 nomes novos na lista oficial.
- **D11. Três demandas, um analista.** Para esta semana: resposta a um ofício do regulador, um achado de auditoria interna e um painel pedido pela diretoria. Como você prioriza?
- **D12. Fila sem fim.** O backlog passou de 3 mil alertas e 20% estão com mais de 60 dias. A head pede um plano para as próximas duas semanas.

> [!tip] Quando abrir esta nota
> Nas sessões de decisão da reta final do [[banco-mocado-plano]] e nos simulados.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** A decisão abre a resposta; os 6 passos a justificam.
* **Ponto 2:** Decidir sem registro e sem escalonamento perde ponto, mesmo com a decisão certa.
* **Ponto 3:** Feche com o que você automatizaria: é isso que separa Compliance Engineering de Compliance.

### 🔗 Conexões
- Mapa: [[moc-orquestra]]
- Relacionadas: [[processo-seletivo-btg]], [[esqueleto-de-6-passos]], [[questoes-sql-de-prova]], [[questoes-por-cenario]], [[instrucoes-do-coach-de-entrevista]]
- Próxima: [[banco-mocado-plano-evolucao]]
