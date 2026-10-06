---
tipo: decisao
funcionalidade: sala-ao-vivo
status: aprovada
criado: 2026-10-30
substitui: 
aliases: [Extrato da liquidação]
---
# ✅ Movimentos da carteira na liquidação

- **Proposta (plano):** [[sala-ao-vivo-plano#Pontos para o aval do humano]], ponto 3.
- **Decisão:** Na liquidação com vencedor, a carteira do vencedor recebe RELEASE + DEBIT do valor final e a do leiloeiro um CREDIT do mesmo valor, na mesma transação. Perdedores não recebem nada: o valor deles já foi liberado quando foram superados (RN-08). Aprovada pelo humano em 2026-10-30 11:2x.
- **Alteração:** nenhuma.
- **Motivo:** `computeBalance` calcula o comprometido como COMMIT − RELEASE; só um DEBIT tiraria o valor duas vezes do disponível do vencedor.
- **Consequências:** A fórmula do saldo não muda. O total recebido pelo leiloeiro (RF-24) é a soma dos CREDIT de liquidação.

### 🔗 Conexões
- Funcionalidade: [[sala-ao-vivo-contexto]]
- Plano: [[sala-ao-vivo-plano]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
