---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-26
substitui: 
---
# ✅ Núcleo e infra num pacote Rust sem Tauri

- **Proposta (plano):** [[integracoes-plano-t8#T8]]: os testes do núcleo compilavam o Tauri e o WebKit, e cada push esperava minutos.
- **Decisão:** o núcleo Rust tem três pacotes: `crates/core` (regras e casos de uso, sem Tauri), `crates/app` (pacote `my-harness-app`: o `Nucleo`, os DTO, os erros e a `infra`, sem Tauri) e `src-tauri` (só o registro dos comandos, os eventos, o `lib.rs` e a configuração do app). As migrações do SQLite e os testes do banco moram em `crates/app`.
- **Alteração:** nenhuma
- **Motivo:** aval do humano em 2026-11-26, 13h56 (T8 depois do merge da T7); entregue nas PRs #17 e #18, `main` em `26923aa`.
- **Consequências:** teste leve do Rust é `cargo test -p my-harness-app <filtro>` ou `-p my-harness-core`, sem GTK nem WebKit. O hook pre-push roda o `pnpm check:rapido`. Código novo de núcleo ou integração vai em `crates/app`, nunca em `src-tauri`. Só este ponto muda na [[geral-decisao-2026-11-19-estrutura]].

### 🔗 Conexões
- Funcionalidade: [[integracoes-contexto]]
- Plano: [[integracoes-plano-t8]]
- Decisão que muda: [[geral-decisao-2026-11-19-estrutura]]
- Junto: [[geral-decisao-2026-11-26-teste-leve-na-tarefa]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
