---
tipo: plano
funcionalidade: integracoes
status: aprovado
criado: 2026-11-26
---
# 📋 Integrações — plano da T8

## T8: núcleo e infra num crate sem Tauri e hook leve
- **Faz:** move `src-tauri/src/infra/` e a lógica do `Nucleo` (`commands/nucleo.rs` e `commands/integracoes.rs`, sem o que é do Tauri) para um crate novo sem Tauri (`crates/app`); o `Channel` do Tauri fica atrás de um trait ou função; `src-tauri` fica só com o registro dos comandos, os eventos e o `lib.rs`. Os testes do núcleo, da infra e do banco passam a rodar sem GTK e sem WebKit. Script novo `check:rapido` (fmt, clippy e testes dos crates sem Tauri, mais o `check:web`) no hook pre-push; `pnpm check` completo segue no `CI` e no fim da tarefa.
- **Toca em:** `Cargo.toml`, `crates/`, `src-tauri/`, `package.json`, `lefthook.yml`
- **Depende de:** T7 (parte da branch dela)
- **Paralelo:** não (move os arquivos que as outras tarefas tocam)
- **Pronto quando:**
  - [ ] `cargo test -p my-harness-core -p my-harness-app` roda num container sem GTK e sem WebKit, com todos os testes que hoje estão em `src-tauri` (menos os que precisam do Tauri)
  - [ ] `pnpm check:rapido` no hook pre-push; `pnpm check` completo passando; comportamento e bindings sem mudança
- **Prova:** `pnpm check`; `check:rapido` num container sem as bibliotecas do GTK, com o tempo medido
- **Verificação:** histórico em [[integracoes-plano-verificacoes-t6-t7#T8]].

### 🔗 Conexões
- Plano: [[integracoes-plano]]
- Verificações: [[integracoes-plano-verificacoes-t6-t7]]
- Funcionalidade: [[integracoes-contexto]]
- Projeto: [[geral-contexto]]
