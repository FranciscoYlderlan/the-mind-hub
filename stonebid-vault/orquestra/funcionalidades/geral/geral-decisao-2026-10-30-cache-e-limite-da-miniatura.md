---
tipo: decisao
funcionalidade: carteira-e-lotes
status: aprovada
criado: 2026-10-30
substitui: 
aliases: [Cache da miniatura, Limite da miniatura, Thumbnail rate limit, IP real no Cloud Run]
---
# ✅ Cache em memória e limite por IP na rota da miniatura

- **Proposta (plano):** [[carteira-e-lotes-plano-correcoes#T5g: cache e limite da miniatura]] e T5h, valores escolhidos pelo implementador.
- **Decisão:** a rota `GET /items/images/:imageId/thumbnail` guarda as miniaturas em memória (LRU de **300 itens**, **32 MB**, validade de **24 h**; pedidos simultâneos do mesmo id fazem uma busca só; falha não entra no cache) e limita a **120 pedidos por minuto por IP**, só nessa rota (429 `TOO_MANY_REQUESTS` com `retry-after`). Aprovado pelo humano em 2026-10-30.
- **Alteração:** nenhuma nos valores. O humano pediu a correção do IP real atrás do proxy do Cloud Run (T5h): `trustProxy` por faixa `169.254.0.0/16`, o IP é a última entrada do `X-Forwarded-For`.
- **Motivo:** a rota é pública e cada pedido sem cache ia à AIC ([[geral-decisao-2026-10-29-miniatura-da-busca-pela-api]]). O `trustProxy` numérico não vale mais no Fastify 5.12.1+ (CVE-2026-16732, relato do subagente) `[a confirmar]`.
- **Consequências:** que o Cloud Run entrega a conexão a partir de `169.254.x.x` está `[a confirmar]` no Cloud Logging; se não, o limite vira um balde por instância, sem risco de falsificação, e só a faixa muda.

### 🔗 Conexões
- Funcionalidade: [[carteira-e-lotes-contexto]]
- Plano: [[carteira-e-lotes-plano-correcoes]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
