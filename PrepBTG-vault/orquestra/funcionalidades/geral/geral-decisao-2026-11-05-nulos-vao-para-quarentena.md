---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-05
substitui: 
aliases: [Decisão sobre nulos, COALESCE só com rastreio]
---
# ✅ Dado crítico ausente vai para a quarentena; COALESCE só com rastreio

- **Proposta (plano):** P4, proposta pela IA a partir do [[relato-do-colega-do-time]].
- **Decisão:** valor, data e cliente de transação ausentes **nunca** são preenchidos: a linha vai para a quarentena com o motivo. `COALESCE` vale para fallback entre fontes, com uma coluna dizendo de qual fonte veio, ou para exibição. Detalhes em [[tratamento-de-nulos]].
- **Alteração:** nenhuma.
- **Motivo:** preencher dado de transação muda somas e médias sem deixar rastro, o que quebra a auditoria.
- **Consequências:** toda solução do cenário 3 mostra a contagem de nulos por coluna e por origem e a quarentena com o motivo.

### 🔗 Conexões
- Funcionalidade: [[banco-mocado-contexto]]
- Plano: [[banco-mocado-plano]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
