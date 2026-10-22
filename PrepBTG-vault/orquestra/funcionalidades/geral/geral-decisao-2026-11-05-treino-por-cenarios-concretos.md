---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-05
substitui: 
aliases: [Treino por cenários concretos, Sem pergunta aberta no treino, Concrete scenarios]
---
# ✅ Treino só com cenários concretos, nos 6 passos e no pipeline

- **Proposta (plano):** o caso C8 abria com uma pergunta aberta, sem cenário, sobre a primeira olhada nos dados. Foi proposto pela IA a partir do [[relato-do-colega-do-time]].
- **Decisão:** todo caso de treino traz um **cenário concreto**, no padrão dos cenários genéricos de [[roteiros-dos-cenarios-genericos]]: contexto de negócio, o dado envolvido e uma pergunta fechada da head. A resposta segue o [[esqueleto-de-6-passos]] e o pipeline de [[geral-decisao-2026-11-05-trilha-sql-e-python]] (SQL extrai, Python analisa). Pergunta aberta, sem cenário, não conta como treino.
- **Alteração:** o caso C8 de [[casos-de-treino-em-6-passos]] é reescrito como cenário concreto. As técnicas de análise exploratória (Q0.1 a Q0.4 de [[questoes-por-cenario]]) continuam, como os primeiros passos desse cenário.
- **Motivo:** o humano quer aplicar conhecimento num problema com cara de teste real. Pergunta vaga não dá onde aplicar e não treina desenvoltura.
- **Consequências:** a IA escreve o novo enunciado do C8 no início da T0b de [[banco-mocado-plano]]. C1 a C7 já seguem o padrão.

### 🔗 Conexões
- Funcionalidade: [[banco-mocado-contexto]]
- Plano: [[banco-mocado-plano]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
