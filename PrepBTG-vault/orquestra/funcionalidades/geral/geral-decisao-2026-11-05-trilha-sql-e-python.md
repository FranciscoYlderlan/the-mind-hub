---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-05
substitui: 
aliases: [Decisão da trilha SQL e Python, SQL extrai Python analisa]
---
# ✅ Todo cenário com dados segue a trilha SQL extrai, Python analisa

- **Proposta (plano):** P1, P3, P6 e P7, propostas pela IA a partir do [[relato-do-colega-do-time]]. Antes, o [[banco-mocado-plano]] usava Python só quando o SQL ficava difícil.
- **Decisão:** nos cenários com dados, SQL extrai e agrega; Python (pandas) explora, limpa e analisa, com estatística básica e um gráfico simples. A limpeza do cenário 3 (Q3.2 a Q3.4) é feita **em SQL e em Python**, com reconciliação entre os dois. Entra o caso C8 (primeira olhada nos dados) e a nota [[estatistica-basica-e-eda]].
- **Alteração:** nenhuma em relação às propostas.
- **Motivo:** o humano confirmou que o colega é **do time da vaga**, e no time a análise exploratória é toda em Python, com SQL só para consulta.
- **Consequências:** o ciclo de trabalho do plano muda no passo 3; toda solução de cenário com dados tem SQL + notebook ou script Python + 1 gráfico; o ambiente precisa de `pandas`, `matplotlib` e `statsmodels` no `.venv`.

### 🔗 Conexões
- Funcionalidade: [[banco-mocado-contexto]]
- Plano: [[banco-mocado-plano]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
