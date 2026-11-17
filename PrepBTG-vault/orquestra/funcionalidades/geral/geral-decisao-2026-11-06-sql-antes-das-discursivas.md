---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-06
substitui: 
aliases: [SQL antes das discursivas, Ordem da reta final, Discursivas por último]
---
# ✅ SQL antes das discursivas na reta final

- **Proposta (plano):** [[banco-mocado-plano#T9: decisões]] abria o diagnóstico de linha de base pelas discursivas D2 e D3.
- **Decisão:** a reta final começa pelo SQL (T8) e deixa as discursivas de decisão (T9) por último.
- **Alteração:** a ordem do diagnóstico foi invertida a pedido do humano.
- **Motivo:** o humano avaliou as discursivas como acima do conhecimento atual dele. Ele vê o papel do Compliance Engineer como quem programa, analisa, captura e exibe a informação para que os analistas, mesmo sem saber programar, tomem as melhores decisões.
- **Consequências:** T8 vem antes de T9 na agenda do [[banco-mocado-plano]]. As discursivas continuam no plano, porque o teste as cobra ([[processo-seletivo-btg]]), mas só depois do SQL.

### 🔗 Conexões
- Funcionalidade: [[banco-mocado-contexto]]
- Plano: [[banco-mocado-plano]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
