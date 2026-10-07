---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-30
substitui: [[geral-decisao-2026-10-28-estrutura-frontend]] (só a rota da auditoria) e [[geral-decisao-2026-10-29-comprovante-e-hash]] (só a rota do link da auditoria)
aliases: [Caminho da auditoria, Rota da auditoria, Audit route]
---
# ✅ Auditoria do lote no web em /lots/:id/audit

- **Proposta (plano):** [[sala-ao-vivo-plano#Candidatos a registro]] e dúvida (a) de [[diario-2026-10-30-sala-ao-vivo]].
- **Decisão:** a página pública da auditoria do lote (I4) fica em `/lots/:id/audit` no `stonebid-web`, em `_public`, o mesmo caminho do `auditPath` que a API devolve no comprovante (contrato da T1). Aprovada pelo humano em 2026-10-30 12:44.
- **Alteração:** nenhuma.
- **Motivo:** o `auditPath` da API e o link do comprovante (T4) já usam esse caminho; nada no ar precisa mudar.
- **Consequências:** o I4 cria a rota `/lots/:id/audit`; até lá o link "auditoria" do comprovante leva a 404 (achado do verificador de código da T6, aceito até o I4).

### 🔗 Conexões
- Funcionalidade: [[sala-ao-vivo-contexto]]
- Plano: [[sala-ao-vivo-plano]]
- Decisões ligadas: [[geral-decisao-2026-10-28-estrutura-frontend]], [[geral-decisao-2026-10-29-comprovante-e-hash]], [[geral-decisao-2026-10-30-rotas-publicas-do-i3]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
