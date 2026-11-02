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
  - Critérios ✔/✘ com a prova de cada um: ✔ mapeamento a ENT-13 e ERR-01 a ERR-07 (testes `nomes_seguem_ent_13`, `ids_e_codigos_seguem_o_catalogo`, `estado_final_de_cada_erro`); ✔ 13 testes por estado, por `dyn` e genérico; ✔ só `crates/core/`, `Cargo.toml` e `Cargo.lock`; ✔ nenhuma credencial em tipo público (RN-04); ✔ commit `feafd97` na branch `feat/setup-integracao-trait`; `fmt`, `clippy`, `cargo test` e `pnpm check` passando.
  - Devolvido para correção: não

### T2: mascaramento de segredo
- **Faz:** módulo que mascara, em texto, só tokens com prefixo conhecido e o valor exato dos segredos que o núcleo guarda, sem adivinhar pelo formato ([[geral-decisao-2026-11-20-mascaramento-sem-adivinhar]]); aplicação dele no texto livre da CLI que a T1 leva ao `Display` e ao `Debug` (`ObsidianFechado.mensagem_da_cli`, `LoginClaudeCliFalhou.motivo`).
- **Toca em:** `crates/core/`
- **Depende de:** T1
- **Paralelo:** não
- **Pronto quando:**
  - [x] nenhum token com prefixo da RN-04 nem segredo guardado pelo núcleo sai em texto puro nos testes; texto sem esses segredos sai igual
- **Prova:** `cargo test`
- **Verificação:**
  - Data: 2026-11-19
  - Critérios ✔/✘ com a prova de cada um: ✘ texto livre (8 de 69 casos adversariais vazam: `Bearer` com valor entre aspas ou após quebra de linha, `token=` e `--token` com quebra de linha, `Bearer:`/`bearer=`, XML e `=>`, token como usuário de URL; prefixo em maiúsculas); ✔ `Segredo` sem valor no `Debug` e no `Display`; ✔ campos da T1 como `TextoMascarado`; ✔ testes dos formatos cobertos; ✔ só `crates/core/`, sem dependência nova, commit `45b204f`. Excesso de máscara em prosa (`token: expirado há pouco tempo`).
  - Devolvido para correção: sim, 2026-11-19, para um implementador novo (vazamentos e excesso de máscara); corrigido em `4be7722`.
  - Segunda volta (2026-11-19): ✘ 73 de 83 casos passam; vazam senha com `&` fora de aspas e token antigo como usuário de URL com senha; excesso de máscara depois de `--token` com espaço e depois do esquema do `Authorization`; `api key` com espaço sem máscara. ✔ `Segredo` e `TextoMascarado`, testes dos vazamentos da primeira volta, escopo e commit.
  - Terceira volta: aval do humano em 2026-11-19, sessão das 17h27, para um implementador novo, só nesses pontos.
  - Terceira volta (2026-11-20, commit `7c6f82e`): ✔ nenhum vazamento em 109 casos; ✔ testes, escopo e commit; ✘ excesso de máscara na mensagem padrão do clap (`--token <TOKEN>` lido como tag XML apaga o resto). Opcional: `Authorization: Digest` mascara `username=` e deixa o hash de `response` à vista.
  - Quarta volta: 2026-11-20, para um implementador novo, só nesses dois pontos.
  - Quarta volta (commit `c0e07eb`): ✔ dica do clap intacta; ✔ `Digest` mascarado até o fim da linha; ✘ regressão: tag XML sem fechamento na mesma linha deixou de mascarar (4 vazamentos que o `7c6f82e` cobria).
  - Quinta volta: interrompida em 2026-11-20 pela troca de abordagem ([[geral-decisao-2026-11-20-mascaramento-sem-adivinhar]]). A T2 é refeita na branch `feat/setup-mascaramento-por-prefixo`, a partir da T1 (`feafd97`); a branch `feat/setup-mascaramento-segredo` fica fora da PR.
  - Refeita (commit `85dbb72`, 2026-11-20): ✔ valor guardado, sem heurística, prosa intacta, `Segredo` e `TextoMascarado`, escopo e commit; ✘ segredo guardado dentro de um token deixa o resto do token à vista. Lacuna: token depois de `%20` ou `%3D` não mascarado (fronteira). Opcional: prefixo nu (`ghs_`) mascarado.
  - Devolvido para um implementador novo: trechos unidos numa passada só; prefixo sem exigir fronteira; prefixo só vira token com pelo menos 1 caractere depois.
  - Segunda verificação da refeita (commit `b2dde90`, 2026-11-20): ✔ nos 6 critérios. 1932 casos de token sem vazamento; segredo guardado dentro, colado ou encavalado sem pedaço à vista; prefixo nu intacto; 35 frases de prosa e erro de CLI iguais; `Segredo` e `TextoMascarado` sem valor; só `crates/core/`; `pnpm check` passando. Efeito aceito: palavra com prefixo no meio é mascarada dali em diante (`desk-ant-abc` → `de••••`).
  - **T2 concluída** na branch `feat/setup-mascaramento-por-prefixo`.

### T3: montagem da chamada ao `claude -p`
- **Faz:** monta os argumentos (modelo, ferramentas, pastas, instruções, saída em fluxo JSON) conforme [[geral-decisao-2026-11-19-agente-por-claude-p]]; cria o `tools/fake-claude` mínimo em Rust (membro do workspace), que devolve os argumentos recebidos e emite fluxo JSON (aval do humano em 2026-11-20, sessão das 08h57).
- **Toca em:** `crates/core/`, `tools/fake-claude/`, `Cargo.toml` e `Cargo.lock` da raiz
- **Depende de:** T2
- **Paralelo:** sim, com T4
- **Pronto quando:**
  - [ ] chamada montada é testada contra o `tools/fake-claude`
  - [ ] `tools/fake-claude` devolve os argumentos recebidos e emite fluxo JSON
- **Prova:** `cargo test`
- **Verificação:**
  - Data: 2026-11-20
  - Critérios ✔/✘ com a prova de cada um (commit `4393810`): ✔ chamada testada contra o `fake-claude` (`tools/fake-claude/tests/chamada_montada.rs`, ambiente limpo); ✔ fake devolve os argumentos em 3 linhas JSON (`system/init`, `fake_args`, `result/success`); ✔ escopo; ✔ `Debug` e `Display` mascarados (caminhos sem máscara, improvável); ✔ commit; ✔ CLI real 2.1.329 sem rede aceitou a chamada inteira (`dontAsk`; prompt que imita uma flag lido como texto); ✘ camada 4: token do GitHub no meio do valor passa (`REPO_URL=https://x-access-token:ghs_…@github.com/…`, `GIT_CONFIG_VALUE_0=Authorization: bearer ghp_…`); ✘ portão terminado em `\` gera comando com aspa aberta. `fmt`, `clippy`, `cargo test` e `pnpm check` passando.
  - Devolvido para correção: sim, 2026-11-20, para um implementador novo: as duas falhas, comparação de ferramenta sem diferenciar maiúsculas e `--strict-mcp-config` sempre ([[geral-decisao-2026-11-20-strict-mcp-sempre]]).
  - Correção entregue (commit `1a0c889`): variável sai do ambiente se o valor contém token com prefixo do GitHub em qualquer posição (mesma varredura da máscara); portão recusado quando termina em `\` ou tem `\\` (`\` no meio aceito, por causa dos caminhos do Windows na CI); maiúsculas ignoradas na repetição e no conflito; `--strict-mcp-config` em toda chamada. 62 testes passando. 
  - Segunda verificação (commit `1a0c889`): ✔ as quatro falhas fechadas (token em qualquer posição e caixa; `\\` no fim, dobrado e UNC recusados; maiúsculas; `--strict-mcp-config` uma vez em toda chamada); ✔ critérios 1 a 5 e 7, sem regressão; ✘ `Debug` da `EspecificacaoExecucao` mostra caminhos sem máscara (`pastas_extras`, `portao`, `mcp_config`). Efeito da regra "contém": saem também `PWD`, `LS_COLORS`, `PS1` com prefixo e palavras como `weighs_more`.
  - Devolvido para um implementador novo: caminhos mascarados no `Debug` e [[geral-decisao-2026-11-20-path-sem-a-pasta-do-token]].

### T4: esquema SQLite das entidades
- **Faz:** migrações das entidades do `02-entidades`, com as trocas M-23 em diante (pontos 4 e 7).
- **Toca em:** `src-tauri/migrations/`, `src-tauri/src/infra/db/`
- **Depende de:** as trocas do contrato aplicadas (já aplicadas)
- **Paralelo:** sim, com T3 e T5 (arquivos sem cruzamento; o `sqlx` já está no `src-tauri/Cargo.toml`)
- **Pronto quando:**
  - [ ] migração cria todas as entidades com as restrições do contrato
- **Prova:** `cargo test`
- **Verificação:**
  - Entregue (commit `e57f4bf`, `feat/setup-esquema-sqlite`, 2026-11-20): `0002_contract_entities.sql` com 25 tabelas STRICT (ENT-15 Papel no código; ENT-25 Diário só no cofre), CHECK nomeados, datas com `IS strftime(...)`, triggers para listas JSON, `chat_anterior`, `prompt_versao` (RN-28) e versões de prompt (RF-31); `dual_write.rs` com `commit_with_vault` e ERR-51; 27 testes de banco. Em verificação.
  - Data: 
  - Critérios ✔/✘ com a prova de cada um:
  - Devolvido para correção:

### T5: contrato IPC do Tauri
- **Faz:** comandos e eventos entre a tela e o núcleo, com tipos gerados para o TypeScript.
- **Toca em:** `src-tauri/src/commands/`, `src-tauri/src/lib.rs`, `src/lib/`, `src/bindings/`, `Cargo.toml` e `Cargo.lock` da raiz, `src-tauri/Cargo.toml` (`tauri-specta`; aval do humano em 2026-11-20, 09h13)
- **Depende de:** T3, porque as duas tocam o `Cargo.toml` e o `Cargo.lock` da raiz (`tauri-specta`)
- **Paralelo:** sim, com T4; o combinado entre as duas são os ENT do `02-entidades` (G1)
- **Pronto quando:**
  - [ ] comandos e eventos tipados nos dois lados
- **Prova:** `pnpm check`
- **Verificação:**
  - Data: 
  - Critérios ✔/✘ com a prova de cada um:
  - Devolvido para correção:

## Próxima tarefa e a seguinte
T3 (montagem da chamada ao `claude -p`) e T4 (esquema SQLite), em paralelo, ambas a partir da branch da T2; depois a T5.

## Prioridades
Paralelo onde o "Toca em" não se cruza ([[geral-decisao-2026-11-20-paralelo-por-padrao]]): T3 e T4 juntas, T5 depois da T3; cada tarefa passa pelo seu verificador. Cada tarefa na sua branch `feat/setup-...`; no fim, juntas na branch de integração `feat/setup-g1-interfaces`, com `pnpm check` local, numa PR única ([[geral-decisao-2026-11-19-branches-e-pr-unica]]).

## Candidatos a registro
- Teste `mensagens_seguem_o_catalogo` não cobre ERR-04 a ERR-06 (observação do verificador da T1).
- `a_partir_do_erro` leva ERR-05 a ERR-07 a desconectado mesmo vindo de sem login ou não instalado; sem efeito na T1, revisar na etapa 3.
- Link de instalação do ERR-01: tela ou núcleo, decidir na etapa 3.
- Para o `AgentRunner` (etapa 3): portão inexistente sai com 127, que a CLI não trata como bloqueio (a ferramenta roda sem o portão); passar `stdin` nulo (sem ele, a CLI espera 3 s); limite de cerca de 32 mil caracteres da linha de comando no Windows.
- Regra "contém" da camada 4 tira variáveis legítimas além do `PATH` (`PWD`, `LS_COLORS`, `PS1`, palavras como `weighs_more`); revisar se o agente precisar delas.
- Pontos do contrato levantados na T4, para o humano: ligações que faltam (`Tarefa.plano`, `Relatório.execucao`, `Achado.execucao`, `Escrita.cofre`); tarefa incompleta do ERR-49 sem forma de gravar; regras que dependem do papel fora do banco; `concluído` × `concluido` entre Relatório e Execução; ERR-51 diz "nada foi gravado" mesmo quando o desfazer do cofre falha; falta o campo que liga linha a nota (AC-148).
- Lição de SQLite: CHECK com `=` passa quando a expressão dá NULL; usar `IS`.
- Escolhas da T3 a revisar na tarefa do `harness-gate`: `--tools` só com nomes internos; gancho sem o papel.
- Ambiente: `cargo clippy --workspace` exige GTK e WebKitGTK (`libwebkit2gtk-4.1-dev`, `libgtk-3-dev`, `libayatana-appindicator3-dev`, `librsvg2-dev`).

### 🔗 Conexões
- Funcionalidade: [[fundacao-contexto]]
- Projeto: [[geral-contexto]]
- Branches: [[geral-decisao-2026-11-19-branches-e-pr-unica]]
- Mascaramento: [[geral-decisao-2026-11-20-mascaramento-sem-adivinhar]]
- Paralelo: [[geral-decisao-2026-11-20-paralelo-por-padrao]]
- MCP: [[geral-decisao-2026-11-20-strict-mcp-sempre]]
- `PATH`: [[geral-decisao-2026-11-20-path-sem-a-pasta-do-token]]
- Roteiro: [[geral-plano]]
- Regras: [[manual-da-orquestra]]
