---
tipo: decisao
funcionalidade: carteira-e-lotes
status: aprovada
criado: 2026-10-30
substitui: 
aliases: [RN-19, Obra única por lote, Item leiloado uma vez, One lot per artwork]
---
# ✅ RN-19: uma obra só tem um lote em aberto e não volta depois de vendida

- **Proposta (plano):** regra trazida pelo humano; casos de borda e indicador propostos pela IA.
- **Decisão:** humano, 2026-10-30 06:31: "um mesmo item pode ser leiloado uma única vez, caso tenha sido vendido ou em aberto. Motivação já que são obras de arte são items únicos". Respostas às perguntas da IA:
  - a obra (mesmo id do item na AIC) fica **bloqueada** para lote novo quando há lote dela **Agendado, Ao vivo ou Arrematado**;
  - fica **livre** de novo quando os lotes dela foram **Cancelados** ou **encerraram sem lances**;
  - na busca do catálogo do leiloeiro, a obra bloqueada mostra o **selo** "Em leilão" ou "Vendido", com link para o lote, e o botão de criar fica **desabilitado**.
- **Alteração:** nenhuma; o humano escolheu as opções recomendadas.
- **Motivo:** obras de arte são itens únicos.
- **Consequências:** RN-19 em [[contrato-regras-de-negocio]] (M-15 em [[contrato-do-projeto-mudancas]]). A API recusa com 409 e garante um só lote em pedidos simultâneos; a busca devolve a situação de cada obra.

### 🔗 Conexões
- Funcionalidade: [[carteira-e-lotes-contexto]]
- Plano: [[carteira-e-lotes-plano-correcoes]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
