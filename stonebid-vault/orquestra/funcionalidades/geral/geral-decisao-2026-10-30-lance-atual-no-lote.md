---
tipo: decisao
funcionalidade: lances
status: aprovada
criado: 2026-10-30
substitui: 
aliases: [Lance atual no lote, currentBidCents, leaderId, Current bid column]
---
# ✅ Lance atual e líder gravados no lote

- **Proposta (plano):** [[lances-plano#Pontos para o aval do humano]], ponto 3.
- **Decisão:** o `Lot` guarda `currentBidCents` e `leaderId`, além da cabeça da cadeia, atualizados na mesma transação do lance. Aprovada pelo humano em 2026-10-30 08:4x.
- **Alteração:** nenhuma.
- **Motivo:** a vitrine e a sala leem o lance atual numa consulta só, sem juntar com o último lance.
- **Consequências:** é uma cópia derivada da cadeia; a auditoria do I4 confere as colunas contra o último lance. Nenhuma rota escreve nelas fora da transação do lance.

### 🔗 Conexões
- Funcionalidade: [[lances-contexto]]
- Plano: [[lances-plano]]
- Contrato: [[contrato-modelo-de-dados]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
