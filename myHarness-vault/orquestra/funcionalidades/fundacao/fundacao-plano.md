---
tipo: plano
funcionalidade: fundacao
status: aprovado
criado: 2026-11-19
---
# 📋 Plano — fundação (G1)

> [!warning] Proposta da IA
> Nada aqui é decisão. Decisões ficam nas notas `-decisao-` linkadas abaixo. Ordem e tarefas aprovadas pelo humano em 2026-11-19, sessão das 16h56.

## Objetivo desta rodada
Entregar as interfaces comuns do G1 da etapa 2 do [[geral-plano]], em paralelo sempre que o "Toca em" não se cruza ([[geral-decisao-2026-11-20-paralelo-por-padrao]]).

## Decisões que este plano respeita
- [[geral-decisao-2026-11-19-stack]]
- [[geral-decisao-2026-11-19-agente-por-claude-p]]
- [[geral-decisao-2026-11-19-entidades-no-sqlite]]
- [[geral-decisao-2026-11-19-gravacao-dupla]]
- [[geral-decisao-2026-11-19-data-e-hora-em-utc]]

(O dial vem do [[geral-contexto]].)

## Tarefas

### T1: trait `Integracao`
- **Faz:** interface comum das integrações (RNF-11): status, conectar e versão, com fake só em teste.
- **Toca em:** `crates/core/`
- **Depende de:** nenhuma
- **Paralelo:** não
- **Pronto quando:**
  - [x] trait e tipos de status e erro mapeados ao contrato (UC-01, CMP-03, CMP-11)
  - [x] testes unitários cobrindo os estados
- **Prova:** `cargo fmt --check`, `cargo clippy -D warnings`, `cargo test`
- **Verificação:**
  - Data: 2026-11-19
  - Critérios ✔/✘ com a prova de cada um: ✔ mapeamento a ENT-13 e ERR-01 a ERR-07 (testes `nomes_seguem_ent_13`, `ids_e_codigos_seguem_o_catalogo`, `estado_final_de_cada_erro`); ✔ 13 testes por estado, por `dyn` e genérico; ✔ só `crates/core/`, `Cargo.toml` e `Cargo.lock`; ✔ nenhuma credencial em tipo público (RN-04); ✔ commit `56437a5` na branch `feat/setup-integracao-trait`; `fmt`, `clippy`, `cargo test` e `pnpm check` passando.
  - Devolvido para correção: não

### T2: mascaramento de segredo
- **Faz:** módulo que mascara, em texto, só tokens com prefixo conhecido e o valor exato dos segredos que o núcleo guarda, sem adivinhar pelo formato ([[geral-decisao-2026-11-20-mascaramento-sem-adivinhar]]); aplicação dele no texto livre da CLI que a T1 leva ao `Display` e ao `Debug` (`ObsidianFechado.mensagem_da_cli`, `LoginClaudeCliFalhou.motivo`).
- **Toca em:** `crates/core/`
- **Depende de:** T1
- **Paralelo:** não
- **Pronto quando:**
  - [x] nenhum token com prefixo da RN-04 nem segredo guardado pelo núcleo sai em texto puro nos testes; texto sem esses segredos sai igual
- **Prova:** `cargo test`
- **Verificação:** cinco voltas e a troca de abordagem, em [[fundacao-plano-mascaramento]]. **T2 concluída** na branch `feat/setup-mascaramento-por-prefixo` (commit `8896227`).

### T3: montagem da chamada ao `claude -p`
- **Faz:** monta os argumentos (modelo, ferramentas, pastas, instruções, saída em fluxo JSON) conforme [[geral-decisao-2026-11-19-agente-por-claude-p]]; cria o `tools/fake-claude` mínimo em Rust (membro do workspace), que devolve os argumentos recebidos e emite fluxo JSON (aval do humano em 2026-11-20, sessão das 08h57).
- **Toca em:** `crates/core/`, `tools/fake-claude/`, `Cargo.toml` e `Cargo.lock` da raiz
- **Depende de:** T2
- **Paralelo:** sim, com T4
- **Pronto quando:**
  - [x] chamada montada é testada contra o `tools/fake-claude`
  - [x] `tools/fake-claude` devolve os argumentos recebidos e emite fluxo JSON
- **Prova:** `cargo test`
- **Verificação:**
  - Data: 2026-11-20
  - Critérios ✔/✘ com a prova de cada um (commit `70124c2`): ✔ chamada testada contra o `fake-claude` (`tools/fake-claude/tests/chamada_montada.rs`, ambiente limpo); ✔ fake devolve os argumentos em 3 linhas JSON (`system/init`, `fake_args`, `result/success`); ✔ escopo; ✔ `Debug` e `Display` mascarados (caminhos sem máscara, improvável); ✔ commit; ✔ CLI real 2.1.329 sem rede aceitou a chamada inteira (`dontAsk`; prompt que imita uma flag lido como texto); ✘ camada 4: token do GitHub no meio do valor passa (`REPO_URL=https://x-access-token:ghs_…@github.com/…`, `GIT_CONFIG_VALUE_0=Authorization: bearer ghp_…`); ✘ portão terminado em `\` gera comando com aspa aberta. `fmt`, `clippy`, `cargo test` e `pnpm check` passando.
  - Devolvido para correção: sim, 2026-11-20, para um implementador novo: as duas falhas, comparação de ferramenta sem diferenciar maiúsculas e `--strict-mcp-config` sempre ([[geral-decisao-2026-11-20-strict-mcp-sempre]]).
  - Correção entregue (commit `682b679`): variável sai do ambiente se o valor contém token com prefixo do GitHub em qualquer posição (mesma varredura da máscara); portão recusado quando termina em `\` ou tem `\\` (`\` no meio aceito, por causa dos caminhos do Windows na CI); maiúsculas ignoradas na repetição e no conflito; `--strict-mcp-config` em toda chamada. 62 testes passando. 
  - Segunda verificação (commit `682b679`): ✔ as quatro falhas fechadas (token em qualquer posição e caixa; `\\` no fim, dobrado e UNC recusados; maiúsculas; `--strict-mcp-config` uma vez em toda chamada); ✔ critérios 1 a 5 e 7, sem regressão; ✘ `Debug` da `EspecificacaoExecucao` mostra caminhos sem máscara (`pastas_extras`, `portao`, `mcp_config`). Efeito da regra "contém": saem também `PWD`, `LS_COLORS`, `PS1` com prefixo e palavras como `weighs_more`.
  - Devolvido para um implementador novo: caminhos mascarados no `Debug` e [[geral-decisao-2026-11-20-path-sem-a-pasta-do-token]].
  - Terceira volta (commit `07d442d`): caminhos mascarados no `Debug`; no `PATH` saem só as pastas com token (`split_paths`/`join_paths`; `PATH` todo sujo, ou com `"` no Windows, fica vazio mas presente); o fake mostra as pastas do `PATH` em `fake_args.path`. 63 testes no núcleo.
  - Terceira verificação (commit `07d442d`, 2026-11-20): ✔ nos 7 critérios e na regra do `PATH` no Linux (posição, caixa, nome `Path`, pastas vazias, `PATH` limpo intacto byte a byte, bytes não UTF-8, `PYTHONPATH` e afins saem inteiros); ✔ sem regressão; nenhum valor de ambiente além do `path` sai no fake. Não executado: o caso `"` no `PATH` do Windows e os testes `#[cfg(windows)]`; pela std, as aspas saem na separação e o comentário "o `PATH` fica vazio" em `execucao.rs` pode estar impreciso.
  - **T3 concluída** na branch `feat/setup-chamada-claude-p`.

### T4: esquema SQLite das entidades
- **Faz:** migrações das entidades do `02-entidades`, com as trocas M-23 em diante (pontos 4 e 7).
- **Toca em:** `src-tauri/migrations/`, `src-tauri/src/infra/db/`, `src-tauri/tests/db_schema.rs` e `src-tauri/tests/db_dual_write.rs` (atualizar os dois; aval do humano em 2026-11-23, 16h45)
- **Depende de:** as trocas do contrato aplicadas (já aplicadas)
- **Paralelo:** sim, com T3 e T5 (arquivos sem cruzamento; o `sqlx` já está no `src-tauri/Cargo.toml`)
- **Pronto quando:**
  - [ ] migração cria todas as entidades com as restrições do contrato
- **Prova:** `cargo test`
- **Verificação:**
  - Entregue (commit `cba8f60`, `feat/setup-esquema-sqlite`, 2026-11-20): `0002_contract_entities.sql` com 25 tabelas STRICT (ENT-15 Papel no código; ENT-25 Diário só no cofre), CHECK nomeados, datas com `IS strftime(...)`, triggers para listas JSON, `chat_anterior`, `prompt_versao` (RN-28) e versões de prompt (RF-31); `dual_write.rs` com `commit_with_vault` e ERR-51; 27 testes de banco.
  - Data: 2026-11-20
  - Critérios ✔/✘ com a prova de cada um: ✔ datas UTC com `Z` (fuso, `z`, 30/02, `24:00`, epoch recusados); ✔ gravação dupla (desfaz nos 4 caminhos, ERR-51); ✔ escopo; ✔ banco criado pela `0001` migra e reabre; ✘ `INSERT OR REPLACE` sobrescreve versão de prompt (RF-31) e `prompt_versao` (RN-28), porque o `REPLACE` não dispara o trigger de `DELETE`; ✘ ENT-07 sem a coluna `comandos` (RN-17); ✘ teste do CHECK `chat_chat_anterior_proprio` não o prova (o trigger dispara antes) e não há teste de `REPLACE`; ✘ (menor) emoji `:card_file_box:` fora da tabela de Tipos e emojis de commit (no Vault). Detalhe e ambiguidades: [[fundacao-plano-candidatos]].
  - Mergeada na `main` (`00bd9a1`, PR #1) pelo humano em 2026-11-23, com os ✘ abertos; a correção sobe numa PR nova (aval do humano, 16h36).
  - Devolvido para correção: sim, 2026-11-23, para um implementador novo, com o M-37 a M-40, na branch `feat/setup-esquema-sqlite-correcao`.
  - Correção (2026-11-23, sem commit): migração nova `0003` (a `0002` já aplicada muda o checksum no sqlx), que refaz `tarefa`, `execucao`, `relatorio`, `achado` e `escrita` com as ligações do M-37, `concluído`, `incompleta` e `comandos`; triggers `BEFORE INSERT` fecham o `REPLACE`; ERR-54 no `dual_write.rs`, registrado no Log; 12 testes novos em `infra/db/tests.rs` (o CHECK `chat_chat_anterior_proprio` agora é provado). `fmt`, `clippy` e `cargo test --lib` passam; ✘ `pnpm check`: os testes antigos `src-tauri/tests/db_schema.rs` e `db_dual_write.rs`, fora do "Toca em", usam o esquema e a API antigos. Com o aval, o mesmo implementador atualiza os dois testes.

### T5: contrato IPC do Tauri
- **Faz:** comandos e eventos entre a tela e o núcleo, com tipos gerados para o TypeScript.
- **Toca em:** `src-tauri/src/commands/`, `src-tauri/src/lib.rs`, `src/lib/`, `src/bindings/`, `Cargo.toml` e `Cargo.lock` da raiz, `src-tauri/Cargo.toml` (`tauri-specta`; aval do humano em 2026-11-20, 09h13)
- **Depende de:** T3, porque as duas tocam o `Cargo.toml` e o `Cargo.lock` da raiz (`tauri-specta`)
- **Paralelo:** sim, com T4; o combinado entre as duas são os ENT do `02-entidades` (G1)
- **Pronto quando:**
  - [ ] comandos e eventos tipados nos dois lados
- **Prova:** `pnpm check`
- **Verificação:**
  - Entregue (commit `5d0e88c`, `feat/setup-contrato-ipc`, a partir da T3 `70124c2`, 2026-11-20): 43 comandos e 7 eventos globais mais `EventoExecucao` por `Channel`, DTOs dos ENT com `DataHoraUtc`, `CodigoErro` ERR-01 a ERR-53 conferido com o `05-erros`, núcleo provisório atrás da interface `Nucleo` (sem regra), `src/bindings/index.ts` gerado por `pnpm bindings` com teste de divergência, zod em `src/lib/ipc/`; `pnpm check` passando. `tauri-specta` só existe como rc (`=2.0.0-rc.29`, `specta =2.0.0-rc.28`, `specta-typescript =0.0.15`): conflita com a S16, pede aval do humano antes do merge. Aguarda verificador.
  - Refeita sobre a `main` nova (`00bd9a1`) sem conflito, mesma árvore: `6b3f878` no container, `03e01ca` na branch da #2 (push com aval do humano em 2026-11-23, 16h39).
  - Data: 2026-11-23
  - Critérios ✔/✘ com a prova de cada um (commit `6b3f878`): ✔ 43 comandos e 7 eventos globais mais `EventoExecucao` e `InstrucaoConexao` por `Channel`, todos nos bindings (`todo_comando_esta_nos_bindings`); ✔ `pnpm check` com EXIT 0; ✔ `pnpm bindings` sem diferença; ✔ escopo (16 arquivos no "Toca em"; `Cargo.lock` só ganhou entradas); ✔ `CodigoErro` ERR-01 a ERR-53 conferido um a um, sem repetido, 53 no TS; ✔ TS e zod iguais ao Rust (mutação: campo novo e valor novo de enum quebram o `tsc`); ✔ núcleo provisório sem regra; ✔ nenhum segredo em DTO (RN-04); ✔ T3 e T4 intactas depois do rebase; ✘ `Achado` sem o campo `execucao` (ENT-10). Menores: o zod aceita fração de segundo com 10 ou mais casas, que o Rust recusa; `desconectar_integracao` devolve `desconectado` sem `nao_implementado`. Ajuste previsto ao M-37 a M-40: ERR-54, `incompleta`, `concluído`, DTO do Relatório (ENT-09) e do Critério (ENT-24).
  - Devolvido para correção: sim, 2026-11-23, para um implementador novo, junto do ajuste ao M-37 a M-40, na branch da #2.
  - Correção e ajuste (commit `f5ad5ce`, 2026-11-23): `Achado.execucao`; `Tarefa.plano` e `incompleta`; DTOs `Relatorio` (ENT-09) e `Criterio` (ENT-24, `passou`, `falhou`, `nao_verificado_presumido`) só como tipos; ERR-54; `concluido` no fio em ASCII, ligado a "concluído" do contrato por comentário; zod de data com 1 a 9 casas; `desconectar_integracao` devolve `nao_implementado`. `pnpm check` e `pnpm bindings` sem diferença. Em segunda verificação.

## Próxima tarefa e a seguinte
Em paralelo: verificador da T5 e correção da T4 (verificação e contrato M-37 a M-40); depois o ajuste da T5 ao contrato novo; cada tarefa verificada vai na sua PR.

## Prioridades
Paralelo onde o "Toca em" não se cruza ([[geral-decisao-2026-11-20-paralelo-por-padrao]]): T3 e T4 juntas, T5 depois da T3; cada tarefa passa pelo seu verificador. Cada tarefa na sua branch `feat/setup-...`; verificada, sobe na sua PR, com `pnpm check` local; o humano faz o merge por "Rebase and merge" na ordem #3 (feita), #4, #1, #2 ([[geral-decisao-2026-11-19-branches-e-pr-unica]], [[geral-decisao-2026-11-23-uma-pr-por-tarefa]]).

## Candidatos a registro
Os candidatos levantados nas tarefas T1 a T5 (contrato, ambiente, `AgentRunner`) ficam em [[fundacao-plano-candidatos]].

### 🔗 Conexões
- Funcionalidade: [[fundacao-contexto]]
- Candidatos: [[fundacao-plano-candidatos]]
- Verificação da T2: [[fundacao-plano-mascaramento]]
- Projeto: [[geral-contexto]]
- Branches: [[geral-decisao-2026-11-19-branches-e-pr-unica]]
- Mascaramento: [[geral-decisao-2026-11-20-mascaramento-sem-adivinhar]]
- Paralelo: [[geral-decisao-2026-11-20-paralelo-por-padrao]]
- MCP: [[geral-decisao-2026-11-20-strict-mcp-sempre]]
- `PATH`: [[geral-decisao-2026-11-20-path-sem-a-pasta-do-token]]
- GitHub: [[geral-decisao-2026-11-23-push-e-pr-no-github]]
- Roteiro: [[geral-plano]]
- Regras: [[manual-da-orquestra]]
