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
- [[geral-decisao-2026-11-24-erro-generico-por-fronteira]], [[geral-decisao-2026-11-24-servidor-mcp-do-obsidian]], [[geral-decisao-2026-11-24-desconectar-sem-logout]]
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

### T2b: servidor MCP da Obsidian CLI com total de notas e HTTP
- **Faz:** o `obsidian-cli-mcp.js` (no `Vault`, `Modelos/Orquestra/`) ganha uma ferramenta de listar arquivos com total e transporte HTTP local ([[geral-decisao-2026-11-24-servidor-mcp-do-obsidian]]); depois, `cofre.py sincronizar` nos cofres.
- **Toca em:** `Vault/Modelos/Orquestra/obsidian-cli-mcp.js` (o orquestrador aplica; o implementador entrega a mudança no relatório)
- **Depende de:** nenhuma
- **Paralelo:** sim, com T3
- **Pronto quando:**
  - [ ] `obsidian_files` devolve o total de `.md` do cofre; o servidor atende por HTTP local e segue atendendo como hoje
  - [ ] o cliente da T2 lê o número de notas do servidor real (AC-128)
  - [ ] nota no `Vault` explicando o servidor MCP da Obsidian CLI por inteiro (o que é, ferramentas, transportes, como instalar e ligar, como validar, ligação com o bug "Obsidian CLI via MCP não carrega"), escrita pelo orquestrador seguindo o Manual do Meu Cérebro no Obsidian (no Vault)
- **Prova:** chamada real pelo MCP ao `Vault` e ao `myHarness-vault`
- **Verificação:**

### T3: GitHub por OAuth device flow (RF-03)
- **Faz:** device flow com o app OAuth próprio (`client_id` do `.env`), token no cofre de credenciais do sistema (Gerenciador de Credenciais no Windows), status com conta e escopos; GitHub falso atrás do `GitHost` nos testes automáticos.
- **Toca em:** `src-tauri/src/infra/github/`, `src-tauri/src/infra/secrets/`, `.env.example`, `src-tauri/Cargo.toml`
- **Depende de:** `client_id` do app OAuth: `Ov23li904l2z5LWigHyr` (humano, 2026-11-24)
- **Paralelo:** sim, com T0a, T0b, T1 e T2
- **Pronto quando:**
  - [ ] AC-01, AC-04, AC-90, AC-127, AC-129, AC-153 cobertos por teste contra o GitHub falso
  - [ ] token nunca em texto puro em log, banco ou erro (RNF-05)
  - [ ] um teste manual contra o GitHub real, no repositório de testes `FranciscoYlderlan/myharness-teste`
- **Prova:** `pnpm check`; busca automatizada pelo token (RNF-05)
- **Verificação:**
  - Despachada em 2026-11-24 07h45 (branch `feat/integracoes-github-oauth`).

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
  - [ ] `ErroIpc::Interno` e `MotivoInterno` retirados; o `nao_implementado()` usa ERR-55 ([[geral-decisao-2026-11-23-falha-interna]]); bindings regerados
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
