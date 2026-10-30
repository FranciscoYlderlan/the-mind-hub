---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-29
substitui: 
aliases: [DEPOSIT_LIMIT_EXCEEDED, Erro do teto do depósito, Deposit limit error]
---
# ✅ Depósito acima do teto responde com o código DEPOSIT_LIMIT_EXCEEDED

- **Proposta (plano):** [[carteira-e-lotes-plano#Candidatos a registro]], proposta da IA; já implementado no PR #1 do `stonebid-api`.
- **Decisão:** depósito acima do teto é recusado com o código próprio `DEPOSIT_LIMIT_EXCEEDED`, e não com o `VALIDATION_ERROR` genérico; a resposta traz o valor do teto. Aprovada pelo humano em 2026-10-29 23:01.
- **Alteração:** nenhuma.
- **Motivo:** a tela mostra uma mensagem específica com o teto, e o teste prova a regra pelo código, sem depender do texto da mensagem.
- **Consequências:** o web trata `DEPOSIT_LIMIT_EXCEEDED` à parte dos erros de validação de campo; valor zero ou negativo continua como `VALIDATION_ERROR`.

### 🔗 Conexões
- Funcionalidade: [[carteira-e-lotes-contexto]]
- Plano: [[carteira-e-lotes-plano]]
- Decisões ligadas: [[geral-decisao-2026-10-29-limites-do-deposito]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
