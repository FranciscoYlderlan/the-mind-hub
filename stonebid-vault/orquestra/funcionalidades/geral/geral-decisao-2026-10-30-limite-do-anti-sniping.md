---
tipo: decisao
funcionalidade: sala-ao-vivo
status: aprovada
criado: 2026-10-30
substitui: 
aliases: [Anti-sniping, RN-10]
---
# ✅ Limite exato do anti-sniping

- **Proposta (plano):** [[sala-ao-vivo-plano#Pontos para o aval do humano]], ponto 5.
- **Decisão:** Lance aceito com 120 000 ms ou menos até o fim muda o fim para `max(endsAt, instante do lance + 2 min)`, na mesma transação do lance, com o lote travado. O fim nunca diminui e não há limite de prorrogações (RN-10, Q-03 opção A). Aprovada pelo humano em 2026-10-30 11:2x.
- **Alteração:** nenhuma.
- **Motivo:** O limite "2 min ou menos" precisa ser exato para o T-04 (lance a exatamente 2 min do fim).
- **Consequências:** A regra vai para o README; o lance no instante exato do fim continua `LOT_ENDED`.

### 🔗 Conexões
- Funcionalidade: [[sala-ao-vivo-contexto]]
- Plano: [[sala-ao-vivo-plano]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
