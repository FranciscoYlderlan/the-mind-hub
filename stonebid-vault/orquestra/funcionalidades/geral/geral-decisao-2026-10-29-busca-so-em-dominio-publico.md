---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-29
substitui: 
aliases: [Domínio público, is_public_domain, Filtro de domínio público, Public domain filter]
---
# ✅ Busca na API de itens só em obras de domínio público

- **Proposta (plano):** [[carteira-e-lotes-plano#Candidatos a registro]], proposta da IA; já implementado no PR #2 do `stonebid-api`.
- **Decisão:** a busca de itens no Art Institute of Chicago só traz obras com `is_public_domain` verdadeiro. Aprovada pelo humano em 2026-10-29 23:01.
- **Alteração:** nenhuma.
- **Motivo:** é a recomendação da própria AIC: os dados são CC0, mas as imagens só podem ser reusadas livremente quando a obra é de domínio público. Copiar para o banco e servir publicamente uma imagem protegida seria problema de direitos.
- **Consequências:** o leiloeiro não encontra obras protegidas na busca; toda imagem copiada para o lote pode ser servida em público ([[geral-decisao-2026-10-29-imagem-do-lote-no-banco]]).

### 🔗 Conexões
- Funcionalidade: [[carteira-e-lotes-contexto]]
- Plano: [[carteira-e-lotes-plano]]
- Decisões ligadas: [[geral-decisao-2026-10-29-api-de-itens]], [[geral-decisao-2026-10-29-imagem-do-lote-no-banco]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
