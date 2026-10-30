---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-29
substitui: 
aliases: [Seed em produção, Lotes do seed em produção, Seed lots in production]
---
# ✅ Lotes do seed também em produção

- **Proposta (plano):** [[carteira-e-lotes-plano#Candidatos a registro]], proposta da IA.
- **Decisão:** o seed cria os lotes de teste (agendado, ao vivo e encerrado) em staging **e** em produção, além dos usuários de teste. Aprovada pelo humano em 2026-10-29 23:01.
- **Alteração:** nenhuma.
- **Motivo:** a aplicação é de teste e será avaliada em produção: a vitrine não pode abrir vazia, e o avaliador precisa de um lote ao vivo para disputar (R-10, RNF-01).
- **Consequências:** o `db:seed` do CD roda nos dois ambientes; o seed precisa ser reexecutável sem duplicar lotes; um lote do seed já encerrado na hora da avaliação é risco conhecido (R-10 de [[contrato-riscos]]).

### 🔗 Conexões
- Funcionalidade: [[carteira-e-lotes-contexto]]
- Plano: [[carteira-e-lotes-plano]]
- Decisões ligadas: [[geral-decisao-2026-10-29-seed-com-imagem-fixa]], [[geral-decisao-2026-10-29-hospedagem]]
- Acesso: [[acesso-de-teste]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
