---
tipo: decisao
funcionalidade: lances
status: aprovada
criado: 2026-10-30
substitui: 
aliases: [Pseudônimo do licitante, AD-09, Bidder pseudonym]
---
# ✅ Pseudônimo do licitante por HMAC com segredo próprio

- **Proposta (plano):** [[lances-plano#Pontos para o aval do humano]], ponto 2.
- **Decisão:** o pseudônimo público do licitante num lote é `HMAC-SHA256(segredo do pseudônimo, "pseudonym:v1" + lotId + bidderId)` cortado num código curto em maiúsculas ("Licitante 7F3A"). O segredo é próprio, separado do segredo do selo. Aprovada pelo humano em 2026-10-30 08:4x.
- **Alteração:** nenhuma.
- **Motivo:** o pseudônimo entra no hash do lance ([[geral-decisao-2026-10-29-comprovante-e-hash]]), então não pode mudar depois do primeiro lance. Sem segredo (SHA-256 puro), quem tem a lista de ids reverte o pseudônimo; com segredo, não dá para ligar o mesmo usuário entre lotes (AD-09 de [[contrato-arquitetura]], RN-15).
- **Consequências:** o segredo do pseudônimo nunca é trocado depois do primeiro lance gravado; trocar o segredo do selo não muda pseudônimos; os dois segredos ficam no Secret Manager (staging e produção) e nunca no banco.

### 🔗 Conexões
- Funcionalidade: [[lances-contexto]]
- Plano: [[lances-plano]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
