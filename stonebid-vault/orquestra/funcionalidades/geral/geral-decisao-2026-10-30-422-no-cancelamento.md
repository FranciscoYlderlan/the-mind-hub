---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-30
aliases: [422 no cancelamento, Validação do motivo, Unprocessable cancel reason]
---
# ✅ 422 só na validação do motivo do cancelamento

- **Proposta (plano):** desvio da T2a em [[sala-ao-vivo-plano]], achado do verificador de código da T6.
- **Decisão:** o motivo do cancelamento fora de 3 a 280 caracteres dá 422; o resto da API segue com 400 `VALIDATION_ERROR`. Fica como exceção registrada, sem mudar o código. Aprovada pelo humano em 2026-10-30 12:44.
- **Alteração:** nenhuma.
- **Motivo:** mudar agora mexe em API e web perto da entrega das 16:00 sem ganho para o usuário.
- **Consequências:** novas validações seguem o 400 `VALIDATION_ERROR`; o 422 vale só para o motivo do cancelamento.

### 🔗 Conexões
- Funcionalidade: [[sala-ao-vivo-contexto]]
- Plano: [[sala-ao-vivo-plano]]
- Decisões ligadas: [[geral-decisao-2026-10-30-motivo-do-cancelamento-gravado]], [[geral-decisao-2026-10-28-estrutura-backend]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
