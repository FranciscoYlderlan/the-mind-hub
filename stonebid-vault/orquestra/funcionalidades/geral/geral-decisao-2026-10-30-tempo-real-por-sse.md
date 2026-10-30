---
tipo: decisao
funcionalidade: sala-ao-vivo
status: aprovada
criado: 2026-10-30
substitui: 
aliases: [AD-04, Tempo real, SSE]
---
# ✅ Tempo real por SSE com barramento em memória e uma instância

- **Proposta (plano):** [[sala-ao-vivo-plano#Pontos para o aval do humano]], ponto 1.
- **Decisão:** O AD-04 de [[contrato-arquitetura]] é Server-Sent Events: rota pública `GET /lots/:id/events`, barramento em memória na API e `--max-instances=1` no Cloud Run de produção e de staging. Se o SSE cair, o web volta à recarga periódica, que cai de 15 s para 3 s enquanto o stream estiver fora. `LISTEN/NOTIFY` do Postgres fica fora. Aprovada pelo humano em 2026-10-30 11:2x.
- **Alteração:** nenhuma.
- **Motivo:** O servidor só empurra dados (o lance vai por requisição comum); o `EventSource` reconecta sozinho; uma instância dispensa um barramento entre instâncias e cabe no prazo ([[geral-decisao-2026-10-30-prazo-16h]]). A recarga cobre o risco R-05 de [[contrato-riscos]].
- **Consequências:** Cada evento leva o `LotDto` inteiro com `serverTime`; a rota é pública porque o `EventSource` não manda cabeçalho de autenticação, então nada de dado pessoal no stream (RN-15). Escalar para mais de uma instância exige decisão nova (`LISTEN/NOTIFY` ou pub/sub). A medir em staging: os 2 s do RNF-06 e se o Cloud Run segura o stream em buffer.

### 🔗 Conexões
- Funcionalidade: [[sala-ao-vivo-contexto]]
- Plano: [[sala-ao-vivo-plano]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
