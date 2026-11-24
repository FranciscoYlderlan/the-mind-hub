---
tipo: plano
funcionalidade: integracoes
status: aprovado
criado: 2026-11-23
---
# 📋 Integrações — plano

> [!warning] Proposta da IA
> Nada aqui é decisão. Decisões ficam nas notas `-decisao-` linkadas abaixo.

## Objetivo desta rodada
Etapa 3 do [[geral-plano]]: as três integrações reais atrás da trait `Integracao` (RF-01 a RF-03), o painel de status (RF-04) e, antes delas, os ajustes herdados da fundação. Uma PR por tarefa ([[geral-decisao-2026-11-23-uma-pr-por-tarefa]]).

## Decisões que este plano respeita
- [[geral-decisao-2026-11-23-comandos-na-tela-de-execucao]], [[geral-decisao-2026-11-23-falha-interna]], [[geral-decisao-2026-11-23-filtro-de-comandos-so-comentario]], [[geral-decisao-2026-11-23-banco-antigo-apagado]] (T0a e T0b)
- [[geral-decisao-2026-11-19-github-oauth-proprio]], [[geral-decisao-2026-11-23-github-real-na-etapa-3]], [[geral-decisao-2026-11-20-github-falso]] (T3)
- [[geral-decisao-2026-11-24-erro-generico-por-fronteira]], [[geral-decisao-2026-11-24-servidor-mcp-do-obsidian]], [[geral-decisao-2026-11-24-desconectar-sem-logout]], [[geral-decisao-2026-11-24-escopo-repo-no-github]], [[geral-decisao-2026-11-24-cofre-da-integracao-por-variavel]], [[geral-decisao-2026-11-24-estado-da-integracao-com-notas-e-erro]]
- [[geral-decisao-2026-11-20-mascaramento-sem-adivinhar]], [[geral-decisao-2026-11-20-strict-mcp-sempre]], [[geral-decisao-2026-11-20-paralelo-por-padrao]], [[geral-decisao-2026-11-23-tauri-specta-rc]]

## Tarefas

### T0a: comandos e FALHA_INTERNA no IPC
- **Faz:** `comandos` no DTO `Execucao` (M-41); ERR-55 `FALHA_INTERNA` no `CodigoErro` (M-43); DTO `Criterio` sem `descricao` se tiver; bindings TS e schemas zod regerados.
- **Toca em:** `src-tauri/src/commands/` (`dto.rs`, `erro.rs`, testes), `src/bindings/`, `src/lib/ipc/`
- **Depende de:** nenhuma
- **Paralelo:** sim, com T0b, T1, T2 e T3
- **Pronto quando:**
  - [x] DTO `Execucao` com `comandos` igual ao ENT-07 e ERR-55 no catálogo de códigos, nos três lados (Rust, TS, zod)
  - [x] `pnpm check` passando
- **Prova:** `pnpm check`; diff dos bindings
- **Verificação:**
  - Entregue em 2026-11-24: `1813855` (branch `feat/integracoes-ajuste-ipc`); `nucleo.rs` desfeito; `Criterio` já sem `descricao`.
  - 2026-11-24: ✔ nos 6 critérios (catálogo de 55 códigos igual em Rust, TS e zod; `pnpm check`; `pnpm bindings` sem diferença; só o "Toca em"). Opcionais: link de doc do Rust no comentário dos bindings; zod não confere `id` com `codigo` (já vinha da `main`). PR #8 aberta.

### T0b: comentário do filtro e banco antigo recriado
- **Faz:** corrige o comentário do filtro de `comandos` na migração `0003` sem mudar o SQL; banco anterior à `0003` que não abre é apagado e recriado na abertura, sem quebrar o checksum do sqlx.
- **Toca em:** `src-tauri/migrations/`, `src-tauri/src/infra/db/`, `src-tauri/tests/db_*.rs`
- **Depende de:** nenhuma
- **Paralelo:** sim, com T0a, T1, T2 e T3
- **Pronto quando:**
  - [ ] banco de antes da `0003` apagado e recriado só quando a `0003` para pelo NOT NULL, com teste; outra falha de migração (ex.: checksum errado da `0001` ou `0002`) volta como erro sem apagar, com teste
  - [ ] banco já na `0003` abre sem erro de checksum, com teste
  - [ ] `pnpm check` passando
- **Prova:** `pnpm check`
- **Verificação:**
  - Entregue em 2026-11-24: `2f6001a` (branch `feat/integracoes-ajuste-banco`); verificador despachado.
  - 2026-11-24: ✔ nos 6 critérios, com um "deve corrigir": apagava o banco em qualquer falha de migração (sonda: checksum errado da `0002` apagou os dados). Restrição aprovada pelo humano; devolvida para um implementador novo. Opcional: teste do `DbError::Delete`.
  - 2026-11-24 (segunda): ✔ nos 6 critérios (sondas de checksum, Dirty e banco travado). Opcionais: testes de Dirty e banco travado no repositório; apagar `-wal`/`-shm` antes do banco. **T0b concluída**; PR #11.

### T1: Claude CLI (RF-01)
- **Faz:** implementação da trait `Integracao` para o Claude CLI: acha o executável (caminho opcional), lê a versão, checa a autenticação e inicia o `/login` da CLI quando falta.
- **Toca em:** `src-tauri/src/infra/claude/`, `src-tauri/src/infra/process/` (só o que for novo), `src-tauri/Cargo.toml` se precisar de dependência
- **Depende de:** nenhuma
- **Paralelo:** sim, com T0a, T0b, T2 e T3
- **Pronto quando:**
  - [ ] status conectado, sem login e não instalado com versão, com testes sobre processo falso
  - [ ] ERR-01, ERR-04 e ERR-53 conforme o catálogo; mensagem da CLI mascarada (AC-154)
  - [ ] AC-01, AC-02, AC-03, AC-88, AC-153, AC-154 cobertos por teste
- **Prova:** `pnpm check`
- **Verificação:**
  - Entregue em 2026-11-24: `82223f2` (branch `feat/integracoes-claude-cli`), `claude --version`, `claude auth status --json` e `claude auth login`; `fake-claude` com modo cenário. ERR-53 sai como ERR-05 pelo trait (ponte provisória até a T4); `desconectar` sem logout da CLI [a confirmar]; verificação depois da T2b.
  - 2026-11-24: ✘ bloqueante (neto órfão no tempo esgotado). Correção `56a5d96` (branch `feat/integracoes-claude-cli-correcao`): grupo de processos no Unix (`rustix`), `taskkill /T /F` no Windows (Job Object exige `unsafe`, proibido no workspace), `conta` mascarada; `cargo check` do Windows não roda no container. Segunda verificação junto da T4.

### T2: Obsidian CLI (RF-02)
- **Faz:** implementação da trait para a Obsidian CLI: Obsidian aberto, servidor MCP respondendo, cofre acessível e número de notas indexadas.
- **Toca em:** `src-tauri/src/infra/obsidian/`, `src-tauri/src/infra/mcp/` (só o que for novo), `src-tauri/Cargo.toml` se precisar
- **Depende de:** nenhuma
- **Paralelo:** sim, com T0a, T0b, T1 e T3
- **Pronto quando:**
  - [ ] status e número de notas; ERR-03 com a mensagem da CLI mascarada; ERR-53
  - [ ] AC-05, AC-89, AC-128, AC-153, AC-154 cobertos por teste
- **Prova:** `pnpm check`
- **Verificação:**
  - Entregue em 2026-11-24: `70b1457` (branch `feat/integracoes-obsidian-cli`), cliente MCP por HTTP (`OBSIDIAN_MCP_URL`) e servidor falso; ERR-53 só pela API do adaptador, não pelo trait; contagem de notas exige `obsidian_files` no servidor real [a preencher]; verificação aguarda as respostas do humano.
  - 2026-11-24: ✔ nos 5 critérios, sem bloqueante; contra o servidor real 1.1.0, `notas_indexadas=Some(75)`. Deve corrigir (T4/T5): ERR-53 e número de notas pelo trait e pelo IPC. **T2 concluída**; PR #12.

### T2b: servidor MCP da Obsidian CLI com total de notas e HTTP
- **Faz:** o `obsidian-cli-mcp.js` (no `Vault`, `Modelos/Orquestra/`) ganha uma ferramenta de listar arquivos com total e transporte HTTP local ([[geral-decisao-2026-11-24-servidor-mcp-do-obsidian]]); depois, `cofre.py sincronizar` nos cofres.
- **Toca em:** `Vault/Modelos/Orquestra/obsidian-cli-mcp.js` (o orquestrador aplica; o implementador entrega a mudança no relatório)
- **Depende de:** nenhuma
- **Paralelo:** sim, com T3
- **Pronto quando:**
  - [x] `obsidian_files` devolve o total de `.md` do cofre; o servidor atende por HTTP local e segue atendendo como hoje
  - [x] o cliente da T2 lê o número de notas do servidor real (AC-128)
  - [x] nota no `Vault` explicando o servidor MCP da Obsidian CLI por inteiro (o que é, ferramentas, transportes, como instalar e ligar, como validar, ligação com o bug "Obsidian CLI via MCP não carrega"), escrita pelo orquestrador seguindo o Manual do Meu Cérebro no Obsidian (no Vault)
- **Prova:** chamada real pelo MCP ao `Vault` e ao `myHarness-vault`
- **Verificação:**
  - 2026-11-24: entregue (1.1.0, `obsidian_files`, `--http` só em 127.0.0.1, porta 27180); provas com `obsidian` falso por stdio e HTTP e com o cliente da T2; aplicado no `Vault` pelo orquestrador. Notas no `Vault`: Servidor MCP da Obsidian CLI e Ligar o servidor MCP da Obsidian CLI (no Vault), ligadas no MOC Programação (no Vault). CLI real (humano, 08h11): `obsidian vault=Vault files ext=md total` devolve `75`, só o número, igual à contagem dos `.md` da pasta; formato que o cliente da T2 lê. Pelo servidor em `--http` no Windows (08h14): `obsidian_files` devolve `"75"`. Do WSL e de contêiner com `--network host`, depois do WSL em `mirrored` (08h33): `HTTP/1.1 200` ([[geral-decisao-2026-11-24-wsl-em-mirrored]]). **T2b concluída.**

### T3: GitHub por OAuth device flow (RF-03)
- **Faz:** device flow com o app OAuth próprio (`client_id` do `.env`), token no cofre de credenciais do sistema (Gerenciador de Credenciais no Windows), status com conta e escopos; GitHub falso atrás do `GitHost` nos testes automáticos.
- **Toca em:** `src-tauri/src/infra/github/`, `src-tauri/src/infra/secrets/`, `.env.example`, `src-tauri/Cargo.toml`
- **Depende de:** `client_id` do app OAuth: `Ov23li904l2z5LWigHyr` (humano, 2026-11-24)
- **Paralelo:** sim, com T0a, T0b, T1 e T2
- **Pronto quando:**
  - [x] AC-01, AC-04, AC-90, AC-127, AC-129, AC-153 cobertos por teste contra o GitHub falso
  - [x] token nunca em texto puro em log, banco ou erro (RNF-05)
  - [ ] um teste manual contra o GitHub real, no repositório de testes `FranciscoYlderlan/myharness-teste`
- **Prova:** `pnpm check`; busca automatizada pelo token (RNF-05)
- **Verificação:**
  - Despachada em 2026-11-24 07h45 (branch `feat/integracoes-github-oauth`).
  - Entregue: `26105b1` (device flow, `keyring`, GitHub falso, 16 testes).
  - 2026-11-24: ✔ nos 6 critérios, sem bloqueante (RNF-05 conferido; sem aws-lc/openssl). Para a T4: ERR-53 pela trait; corrida no desconectar (checar `cancelado` antes de gravar); máscara do `access_token` no corpo do erro. Opcional: `CofreDoSistema` sem teste (fica para o teste manual). **T3 concluída**; PR #10 aberta.

### Tci: CI verde na `main`
- **Faz:** corrige o que o `CI` acusou na primeira execução (PR #8) e já estava na `main`: `clippy::result_large_err` no `DualWriteError` (Rust estável 1.100) e `dead_code` no `path_filtrado` no Windows.
- **Toca em:** `src-tauri/src/infra/db/dual_write.rs`, `crates/core/src/domain/execucao.rs` (só `cfg` de teste)
- **Depende de:** nenhuma
- **Paralelo:** sim; as PRs de tarefa só passam no `CI` depois dela
- **Pronto quando:**
  - [ ] `CI` verde em Linux e Windows na PR dela
- **Prova:** clippy estável com `-D warnings`; `pnpm check`; `CI` da PR
- **Verificação:**

### T4: núcleo liga as três integrações
- **Faz:** o `Nucleo` provisório passa a usar T1, T2 e T3 em `listar`, `testar`, `conectar` e `desconectar`, com os eventos de instrução de conexão.
- **Toca em:** `src-tauri/src/commands/nucleo.rs`, `src-tauri/src/commands/erro.rs`, `src-tauri/src/lib.rs`, `crates/core/src/domain/integracao.rs`, adaptadores de T1 e T2 (só o mapeamento do erro)
- **Depende de:** T1, T2, T3
- **Paralelo:** não
- **Pronto quando:**
  - [ ] "Desconectar" do Claude CLI só no MyHarness, sem logout ([[geral-decisao-2026-11-24-desconectar-sem-logout]])
  - [ ] um teste só prova que qualquer falha não catalogada vira ERR-53 com o motivo mascarado no Log ([[geral-decisao-2026-11-24-erro-generico-por-fronteira]])
  - [ ] comandos IPC devolvem o estado real das três; RN-08 bloqueia ação sem integração
  - [ ] variante de ERR-53 no `ErroIntegracao` (`crates/core`), para T1 e T2 devolverem a falha inesperada pelo trait
  - [ ] `compose.yaml` com o backend na rede do WSL e `OBSIDIAN_MCP_URL` no `.env.example` ([[geral-decisao-2026-11-24-wsl-em-mirrored]])
  - [ ] GitHub: checar `cancelado` antes de gravar o token e mascarar o `access_token` no corpo de erro (verificação da T3)
  - [ ] `ErroIpc::Interno` e `MotivoInterno` retirados; o `nao_implementado()` usa ERR-55 ([[geral-decisao-2026-11-23-falha-interna]]); bindings regerados
  - [ ] `pnpm check` passando
- **Prova:** `pnpm check`
- **Verificação:**
  - 2026-11-24: entregue `c0a2fb7` sobre merges de T0a, T2, T3 e T1; merge da correção da T1 em `dafcacb` (conflito no `Cargo.lock`, resolvido pelo orquestrador). ERR-53 no `ErroIntegracao`, `ServicoIntegracoes`, `ErroIpc::Interno` removido, máscara do núcleo com o token, `.env.example` e `compose.yaml` (`network_mode: host`). Pontos: registro do ERR-53 fora do Log (ENT-12 exige `execucao`); "desconectada" só em memória; `notas_indexadas` fora do DTO; variável `MYHARNESS_OBSIDIAN_COFRE` criada sem aval. Em verificação.

### T4b: estado da integração com notas e erro (M-46)
- **Faz:** `notas_indexadas` e `erro` no estado da integração (núcleo, DTO da IPC, bindings e zod) e na TEL-02 (número de notas no cartão da Obsidian CLI; motivo do ERR-53 vindo de `listar`); `ESCOPOS_PADRAO = ["repo"]` sem `[a confirmar]` ([[geral-decisao-2026-11-24-escopo-repo-no-github]]).
- **Toca em:** `crates/core/src/domain/integracao.rs`, `src-tauri/src/commands/`, `src-tauri/src/infra/{obsidian,github}/`, `src/bindings/`, `src/lib/ipc/`, `src/features/integracoes/`
- **Depende de:** T4 e T5 verificadas
- **Paralelo:** não
- **Pronto quando:**
  - [ ] AC-128 na API e na tela; motivo do ERR-53 na TEL-02 também depois de `listar`
  - [ ] `pnpm check` passando
- **Prova:** `pnpm check`
- **Verificação:**

### T5: painel de status (RF-04, CMP-03, CMP-11)
- **Faz:** indicadores no canto superior direito e a TEL-02 com a ação "Conectar" e as instruções (código do device flow, `/login`).
- **Toca em:** `src/features/integracoes/`, `src/app/main-window.tsx`
- **Depende de:** T0a, T4
- **Paralelo:** não
- **Pronto quando:**
  - [ ] AC-91 e AC-153 na tela
  - [ ] AC de UC-01 e TEL-02 passando no verificador de fluxo principal e no adversarial, pela API e na tela
- **Prova:** `pnpm check`; verificadores do fim da funcionalidade
- **Verificação:**
  - 2026-11-24: entregue `f3004ae` (branch `feat/integracoes-painel`, sobre a T0a): CMP-03, TEL-02 com CMP-11, instruções, mensagens do catálogo, núcleo simulado nos testes, 17 testes novos. Pontos: link do ERR-01 [a confirmar]; `obsidian://open` na janela real [a confirmar]; AC-128 depende do DTO. Em verificação.

## Próxima tarefa e a seguinte
- Agora: T0a, T0b, T1 e T2 em paralelo; T3 assim que o `client_id` existir.
- Depois: T4 e T5; ao fim, verificador de fluxo principal e adversarial.

## Prioridades
- T0a e T0b fecham pendências herdadas e são pequenas; T3 é a mais sensível (token).

## Candidatos a registro
- `Cargo.toml` e `Cargo.lock` podem conflitar entre T1, T2 e T3 (G2): cada PR é refeita sobre a `main` antes do merge.

### 🔗 Conexões
- Funcionalidade: [[integracoes-contexto]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
