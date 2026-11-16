---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-26
substitui: geral-decisao-2026-11-26-apagar-target-depois-do-build
---
# ✅ Um target só por chat

- **Proposta (plano):** resposta do orquestrador em 2026-11-26, 13h43: cada agente apagava o seu `target/` ao fim da tarefa, e o próximo compilava o Tauri do zero.
- **Decisão:** num mesmo chat, implementadores e validadores reaproveitam o `target/` já compilado, com o `sccache` como cache do Rust. O `target/` não se apaga ao fim da tarefa; apaga-se no fim da funcionalidade, depois do último adversarial. O relatório diz o caminho do `target/` e o que foi apagado.
- **Alteração:** nenhuma
- **Motivo:** aval do humano em 2026-11-26, 13h45.
- **Consequências:** substitui a [[geral-decisao-2026-11-26-apagar-target-depois-do-build]]. A [[geral-decisao-2026-11-26-build-reaproveitado-na-validacao]] segue com o ponto do `target/` reescrito. Disco do container: o orquestrador confere o espaço livre antes de despachar quem compila.

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[integracoes-plano]]
- Substitui: [[geral-decisao-2026-11-26-apagar-target-depois-do-build]]
- Ponto alterado: [[geral-decisao-2026-11-26-build-reaproveitado-na-validacao]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
