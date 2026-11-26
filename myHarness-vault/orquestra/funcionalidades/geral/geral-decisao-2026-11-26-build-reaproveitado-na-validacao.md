---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-26
substitui: 
---
# ✅ Build reaproveitado na validação e cache do sccache

- **Proposta (plano):** resposta do orquestrador em 2026-11-26 13h03 sobre a demora do adversarial: cada agente clonava e compilava o Tauri do zero, porque o `target/` era apagado ao fim de cada tarefa.
- **Decisão:** o verificador de fluxo principal e os adversariais da mesma funcionalidade usam um clone só e o mesmo `target/`; esse `target/` é apagado só no fim da funcionalidade, depois do último adversarial. Todo agente que compila usa o `sccache` como cache do Rust, numa pasta fora do `target/`, com limite de tamanho.
- **Alteração:** nenhuma
- **Motivo:** aval do humano em 2026-11-26, 13h04, "para garantir maior eficácia no teste".
- **Consequências:** o `target/` compartilhado vale para todos os agentes do chat, implementadores incluídos ([[geral-decisao-2026-11-26-target-unico-por-chat]]). O briefing de validação diz o caminho do clone compartilhado; o último agente da funcionalidade apaga o `target/`. Limite do cache do `sccache`: 10 GB, proposta do orquestrador [a confirmar].

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Ponto alterado: [[geral-decisao-2026-11-26-target-unico-por-chat]]
- Junto: [[geral-decisao-2026-11-26-adversarial-em-dois]], [[geral-decisao-2026-11-19-modo-simulado]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
