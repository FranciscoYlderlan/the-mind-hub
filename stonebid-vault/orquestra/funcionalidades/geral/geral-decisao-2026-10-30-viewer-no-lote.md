---
tipo: decisao
funcionalidade: sala-ao-vivo
status: aprovada
criado: 2026-10-30
substitui: 
aliases: [Indicador ganhando, RF-30]
---
# ✅ Pseudônimo do visitante no lote (RF-30)

- **Proposta (plano):** [[sala-ao-vivo-plano#Pontos para o aval do humano]], ponto 6.
- **Decisão:** `GET /lots/:id` aceita autenticação opcional: com JWT válido de licitante, o `LotDto` traz `viewer.pseudonym`; sem token ou com token inválido, `viewer` é `null` (nunca 401). O stream SSE segue público, com `viewer` nulo, e o web compara `viewer.pseudonym` com `leaderPseudonym` para mostrar "ganhando" ou "superado". Aprovada pelo humano em 2026-10-30 11:2x.
- **Alteração:** nenhuma.
- **Motivo:** O indicador do RF-30 precisa saber quem olha sem expor quem lidera.
- **Consequências:** O pseudônimo do próprio licitante só chega a ele mesmo.

### 🔗 Conexões
- Funcionalidade: [[sala-ao-vivo-contexto]]
- Plano: [[sala-ao-vivo-plano]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
