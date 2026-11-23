---
tipo: plano
funcionalidade: fundacao
status: aprovado
criado: 2026-11-23
---
# 📋 Plano — fundação: verificação da T4 (esquema SQLite)

Histórico da verificação da T4 do [[fundacao-plano]], separado por tamanho.

- **Verificação:**
  - Entregue (commit `cba8f60`, `feat/setup-esquema-sqlite`, 2026-11-20): `0002_contract_entities.sql` com 25 tabelas STRICT (ENT-15 Papel no código; ENT-25 Diário só no cofre), CHECK nomeados, datas com `IS strftime(...)`, triggers para listas JSON, `chat_anterior`, `prompt_versao` (RN-28) e versões de prompt (RF-31); `dual_write.rs` com `commit_with_vault` e ERR-51; 27 testes de banco.
  - Data: 2026-11-20
  - Critérios ✔/✘ com a prova de cada um: ✔ datas UTC com `Z` (fuso, `z`, 30/02, `24:00`, epoch recusados); ✔ gravação dupla (desfaz nos 4 caminhos, ERR-51); ✔ escopo; ✔ banco criado pela `0001` migra e reabre; ✘ `INSERT OR REPLACE` sobrescreve versão de prompt (RF-31) e `prompt_versao` (RN-28), porque o `REPLACE` não dispara o trigger de `DELETE`; ✘ ENT-07 sem a coluna `comandos` (RN-17); ✘ teste do CHECK `chat_chat_anterior_proprio` não o prova (o trigger dispara antes) e não há teste de `REPLACE`; ✘ (menor) emoji `:card_file_box:` fora da tabela de Tipos e emojis de commit (no Vault). Detalhe e ambiguidades: [[fundacao-plano-candidatos]].
  - Mergeada na `main` (`00bd9a1`, PR #1) pelo humano em 2026-11-23, com os ✘ abertos; a correção sobe numa PR nova (aval do humano, 16h36).
  - Devolvido para correção: sim, 2026-11-23, para um implementador novo, com o M-37 a M-40, na branch `feat/setup-esquema-sqlite-correcao`.
  - Correção (2026-11-23, sem commit): migração nova `0003` (a `0002` já aplicada muda o checksum no sqlx), que refaz `tarefa`, `execucao`, `relatorio`, `achado` e `escrita` com as ligações do M-37, `concluído`, `incompleta` e `comandos`; triggers `BEFORE INSERT` fecham o `REPLACE`; ERR-54 no `dual_write.rs`, registrado no Log; 12 testes novos em `infra/db/tests.rs` (o CHECK `chat_chat_anterior_proprio` agora é provado). `fmt`, `clippy` e `cargo test --lib` passam; ✘ `pnpm check`: os testes antigos `src-tauri/tests/db_schema.rs` e `db_dual_write.rs`, fora do "Toca em", usam o esquema e a API antigos. Com o aval, o mesmo implementador atualizou os dois testes: commit `2b66b09`, `pnpm check` passando (banco: 12 + 21 + 6 + 1 testes), ENT-07 e ENT-09 aprovados (M-41 e M-42) sem contradição no esquema. Mergeada na `main` pelo humano (PR #5, `e118161`, mesmo patch do `2b66b09`) antes do verificador.
  - Segunda verificação (commit `e118161`, 2026-11-23): ✔ nos 6 critérios: M-37 a M-42 no esquema (ligações NOT NULL, `concluído`, `incompleta`, `comandos`, `criterios` no núcleo; datas UTC); os ✘ da primeira fechados (`REPLACE`, upsert e `UPDATE OR REPLACE` recusados em versão de prompt e `prompt_versao`; CHECK `chat_chat_anterior_proprio` provado pelo UPDATE); banco da `0001` e da `0002` migra e reabre sem perda; ERR-54 e ERR-51 nos 4 caminhos; escopo de 6 arquivos; commit no padrão. `pnpm check` EXIT 0. Banco da `0002` com linha em `tarefa`, `relatorio` ou `escrita` não abre (para na `0002`, sem perda). Achados menores em [[fundacao-plano-candidatos]].
  - **T4 concluída** na `main`.

### 🔗 Conexões
- Plano: [[fundacao-plano]]
- Funcionalidade: [[fundacao-contexto]]
- Candidatos: [[fundacao-plano-candidatos]]
- Gravação dupla: [[geral-decisao-2026-11-19-gravacao-dupla]]
