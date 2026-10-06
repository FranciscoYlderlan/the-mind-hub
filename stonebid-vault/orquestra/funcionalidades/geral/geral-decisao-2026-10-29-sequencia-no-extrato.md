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
- **Decisão:** no I2, `WalletMovement` ganha uma coluna de sequência **global** crescente (identity do banco), e o extrato ordena por ela. Dentro de uma carteira os números pulam. Aprovada pelo humano em 2026-10-29 23:01; numeração global aprovada em 2026-10-30 08:4x ([[lances-plano]], ponto 1).
- **Alteração:** a numeração é global, não por carteira: o lance grava o RELEASE na carteira do antigo líder, e um contador por carteira travaria duas carteiras, com risco de deadlock em lances cruzados.
- **Motivo:** movimentos gravados na mesma operação (um lance que bloqueia um valor e libera outro) saem com o mesmo horário e sem ordem garantida; a sequência dá ordem estável e ajuda a auditoria a reconstruir o saldo.
- **Consequências:** a migração do I2 cria a coluna e preenche os movimentos já gravados pela ordem de criação; a sequência é única no banco inteiro, gerada pelo próprio banco na inserção, sem trava extra de carteira; até o I2, o extrato segue ordenado pelo horário.

### 🔗 Conexões
- Funcionalidade: [[carteira-e-lotes-contexto]]
- Plano: [[carteira-e-lotes-plano]], [[lances-plano]]
- Contrato: [[contrato-modelo-de-dados]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
