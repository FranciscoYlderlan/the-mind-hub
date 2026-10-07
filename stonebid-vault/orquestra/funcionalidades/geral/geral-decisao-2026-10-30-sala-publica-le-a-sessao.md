---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-30
substitui: [[geral-decisao-2026-10-28-estrutura-frontend]] (só "`_public` nunca lê sessão" e "dado público e dado pessoal separados", na sala do lote)
aliases: [Sala pública com sessão, Viewer na rota pública, Public room session]
---
# ✅ A sala pública do lote lê a sessão já resolvida

- **Proposta (plano):** desvio da T3 em [[sala-ao-vivo-plano]].
- **Decisão:** `routes/_public/lots/$id.tsx` lê o `user` da sessão já resolvida no layout raiz, sem consulta nova e sem redirecionar, e a sala mostra o `viewer` ("ganhando", "superado", "arrematou") que o `GET /lots/:id` devolve com JWT de licitante ([[geral-decisao-2026-10-30-viewer-no-lote]]). As outras páginas de `_public` seguem sem ler a sessão. Aprovada pelo humano em 2026-10-30 12:44.
- **Alteração:** nenhuma.
- **Motivo:** o `viewer` vem na mesma consulta do lote, então separar consulta pública e pessoal dobraria as requisições sem ganho.
- **Consequências:** como o dado pessoal entra no cache do lote, as consultas de lotes, Meus arremates e painel do leiloeiro são descartadas no login e no logout, e o stream não reaproveita `viewer` de outra sessão (correção em andamento depois da T6, ver [[sala-ao-vivo-plano]]).

### 🔗 Conexões
- Funcionalidade: [[sala-ao-vivo-contexto]]
- Plano: [[sala-ao-vivo-plano]]
- Decisões ligadas: [[geral-decisao-2026-10-28-estrutura-frontend]], [[geral-decisao-2026-10-30-viewer-no-lote]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
