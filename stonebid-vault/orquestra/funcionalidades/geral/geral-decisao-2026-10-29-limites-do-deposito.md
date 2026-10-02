---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-29
substitui: 
aliases: [Teto do depósito, Limites do depósito, Q-10]
---
# ✅ Depósito simulado: maior que zero, teto configurável, sem saque (Q-10)

- **Proposta (plano):** [[carteira-e-lotes-plano#Pendente de aval antes da T1 (proposta da IA)]]
- **Decisão:** o depósito é maior que zero, tem teto por depósito configurável por variável de ambiente (padrão R$ 10.000,00, ou 1.000.000 centavos) e não há saque. Aprovada pelo humano em 2026-10-29 22:23.
- **Alteração:** nenhuma.
- **Motivo:** a proposta do contrato, com o valor padrão do teto proposto pela IA.
- **Consequências:** acima do teto o servidor recusa com o código `DEPOSIT_LIMIT_EXCEEDED` e o valor do teto ([[geral-decisao-2026-10-29-codigo-do-teto-do-deposito]]); a rota de saque não existe.

### 🔗 Conexões
- Funcionalidade: [[carteira-e-lotes-contexto]]
- Plano: [[carteira-e-lotes-plano]]
- Decisões ligadas: [[geral-decisao-2026-10-29-codigo-do-teto-do-deposito]]
- Contrato: [[contrato-pontos-para-validar]], [[contrato-requisitos-funcionais]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
