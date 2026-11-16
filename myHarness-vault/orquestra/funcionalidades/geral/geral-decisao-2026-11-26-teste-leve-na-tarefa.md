---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-26
substitui: 
---
# ✅ Teste leve durante a tarefa e check completo uma vez

- **Proposta (plano):** resposta do orquestrador em 2026-11-26, 13h43, sobre a demora dos testes: cada agente rodava o `pnpm check` inteiro (clippy e testes do workspace Rust, com o Tauri e o WebKit) várias vezes, e o hook pre-push o repetia a cada push.
- **Decisão:** durante a tarefa, o implementador roda só o teste do que mudou: mudança só de tela, `pnpm check:web`; mudança no Rust, só `cargo test -p <crate> <filtro>` do módulo tocado. O `pnpm check` completo roda uma vez por tarefa, antes do último push. Os pushes do meio vão com `LEFTHOOK=0`; o `CI` da PR roda o check completo em Linux e Windows.
- **Alteração:** nenhuma
- **Motivo:** aval do humano em 2026-11-26, 13h45 ("testes leves e rápidos que validem tão bem quanto").
- **Consequências:** o briefing do implementador diz os comandos leves e o check completo no fim. Push depois de cada commit segue valendo. O relatório traz o tempo de cada prova. Junto: [[geral-decisao-2026-11-26-validacao-em-modo-dev]], [[geral-decisao-2026-11-26-target-unico-por-chat]].

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[integracoes-plano]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
