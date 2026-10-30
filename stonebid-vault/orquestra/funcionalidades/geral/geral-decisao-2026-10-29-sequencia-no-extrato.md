---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-29
substitui: 
aliases: [Sequência no extrato, seq do movimento, Ordem do extrato, Movement sequence]
---
# ✅ Coluna de sequência nos movimentos da carteira (I2)

- **Proposta (plano):** [[carteira-e-lotes-plano#Candidatos a registro]], proposta da IA, para o I2.
- **Decisão:** no I2, `WalletMovement` ganha uma coluna de sequência crescente por carteira, e o extrato ordena por ela. Aprovada pelo humano em 2026-10-29 23:01.
- **Alteração:** nenhuma.
- **Motivo:** movimentos gravados na mesma operação (um lance que bloqueia um valor e libera outro) saem com o mesmo horário e sem ordem garantida; a sequência dá ordem estável e ajuda a auditoria a reconstruir o saldo.
- **Consequências:** a migração do I2 cria a coluna e preenche os movimentos já gravados pela ordem de criação; a sequência é única por carteira e gerada dentro da mesma transação do movimento; até o I2, o extrato segue ordenado pelo horário.

### 🔗 Conexões
- Funcionalidade: [[carteira-e-lotes-contexto]]
- Plano: [[carteira-e-lotes-plano]]
- Contrato: [[contrato-modelo-de-dados]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
