---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-30
substitui: 
aliases: [Demonstração do ADULTERADO, Adulterado só no CI, Tampered demo]
---
# ✅ O veredito ADULTERADO é provado só no T-06 do CI

- **Proposta (plano):** ponto 6 de [[auditoria-publica-plano]], 2026-10-30 13:1x, com três opções: só no CI, lote adulterado no seed ou adulteração por SQL em staging.
- **Decisão:** humano escolheu "só no T-06 do CI" em 2026-10-30 13:2x. Nenhum lote fica adulterado no ar; o ADULTERADO é provado pelos testes e explicado no README.
- **Alteração:** nenhuma.
- **Motivo:**
  - O seed roda também em produção ([[geral-decisao-2026-10-29-seed-tambem-em-producao]]): um lote adulterado de propósito apareceria para o avaliador como dado real corrompido.
  - Adulterar em staging pelo Cloud Shell custaria tempo perto da entrega das 16:00 ([[geral-decisao-2026-10-30-prazo-16h]]).
- **Consequências:**
  - O verificador no Chrome confere só o ÍNTEGRO e a página; o ADULTERADO fica com o T-06 e com o Playwright da API simulada.

### 🔗 Conexões
- Funcionalidade: [[auditoria-publica-contexto]]
- Relacionadas: [[geral-decisao-2026-10-30-auditoria-publica]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
