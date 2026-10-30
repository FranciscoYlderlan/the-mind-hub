---
tipo: decisao
funcionalidade: lances
status: aprovada
criado: 2026-10-30
substitui: [[geral-decisao-2026-10-30-pseudonimo-por-hmac]] (só o tamanho do código)
aliases: [Pseudônimo de 6 dígitos]
---
# ✅ Pseudônimo com 6 dígitos

- **Proposta (plano):** [[geral-decisao-2026-10-30-pseudonimo-por-hmac]] cortou o HMAC em 4 dígitos hex no código (achado da T2b em [[lances-plano]]).
- **Decisão:** O pseudônimo é o HMAC cortado em **6 dígitos hex** em maiúsculas ("Licitante 7F3A9C"). Aprovada pelo humano em 2026-10-30 11:1x. Implementação junto com a T2a de [[sala-ao-vivo-plano]].
- **Alteração:** nenhuma.
- **Motivo:** Com 4 dígitos a colisão no mesmo lote é ~1 em 65 mil; com 6, ~1 em 16 milhões.
- **Consequências:** O pseudônimo entra no hash do lance: os lances de teste já gravados em staging e produção são apagados por uma migração e refeitos pelo seed (humano, 2026-10-30 11:2x); usuários, lotes e depósitos ficam.

### 🔗 Conexões
- Funcionalidade: [[lances-contexto]]
- Plano: [[lances-plano]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
