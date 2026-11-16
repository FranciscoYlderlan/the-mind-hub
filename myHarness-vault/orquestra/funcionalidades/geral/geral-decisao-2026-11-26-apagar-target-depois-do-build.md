---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-26
substitui: 
---
# ✅ Apagar o target depois do build

- **Proposta (plano):** relatório do implementador da T4b em 2026-11-26: o disco do container encheu com os `target/` de clones anteriores (22,5 GB) e a compilação parou com `ld Bus error`.
- **Decisão:** todo agente que compila e gera a pasta `target/` a apaga ao terminar a tarefa, para não acumular arquivos de build; na validação de uma funcionalidade, o `target/` compartilhado é apagado só no fim dela ([[geral-decisao-2026-11-26-build-reaproveitado-na-validacao]]).
- **Alteração:** nenhuma
- **Motivo:** pedido do humano em 2026-11-26, 09h12 e 09h17; regra só deste projeto.
- **Consequências:** o orquestrador põe a regra só no briefing de quem compila, em uma frase, sem mudar o modelo de briefing, que fica sucinto. O relatório diz o que foi apagado. O `target/` de um clone em uso por outro agente não se apaga.

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[geral-plano]]
- Onde surgiu: [[integracoes-plano-verificacoes]]
- Ponto alterado: [[geral-decisao-2026-11-26-build-reaproveitado-na-validacao]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
