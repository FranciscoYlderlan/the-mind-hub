---
tipo: plano
funcionalidade: integracoes
status: aprovado
criado: 2026-11-24
---
# 📋 Integrações — histórico das verificações

Parte do [[integracoes-plano]] (dividida pelo limite de palavras): o que cada verificador achou, tarefa por tarefa, a partir dos relatórios.

## T0a
- Entregue em 2026-11-24: `1813855` (branch `feat/integracoes-ajuste-ipc`); `nucleo.rs` desfeito; `Criterio` já sem `descricao`.
- 2026-11-24: ✔ nos 6 critérios (catálogo de 55 códigos igual em Rust, TS e zod; `pnpm check`; `pnpm bindings` sem diferença; só o "Toca em"). Opcionais: link de doc do Rust no comentário dos bindings; zod não confere `id` com `codigo` (já vinha da `main`). PR #8 aberta.

## T0b
- Entregue em 2026-11-24: `2f6001a` (branch `feat/integracoes-ajuste-banco`); verificador despachado.
- 2026-11-24: ✔ nos 6 critérios, com um "deve corrigir": apagava o banco em qualquer falha de migração (sonda: checksum errado da `0002` apagou os dados). Restrição aprovada pelo humano; devolvida para um implementador novo. Opcional: teste do `DbError::Delete`.
- 2026-11-24 (segunda): ✔ nos 6 critérios (sondas de checksum, Dirty e banco travado). Opcionais: testes de Dirty e banco travado no repositório; apagar `-wal`/`-shm` antes do banco. **T0b concluída**; PR #11.

## T1
- Entregue em 2026-11-24: `82223f2` (branch `feat/integracoes-claude-cli`), `claude --version`, `claude auth status --json` e `claude auth login`; `fake-claude` com modo cenário. ERR-53 sai como ERR-05 pelo trait (ponte provisória até a T4); `desconectar` sem logout da CLI [a confirmar]; verificação depois da T2b.
- 2026-11-24: ✘ bloqueante (neto órfão no tempo esgotado). Correção `56a5d96` (branch `feat/integracoes-claude-cli-correcao`): grupo de processos no Unix (`rustix`), `taskkill /T /F` no Windows (Job Object exige `unsafe`, proibido no workspace), `conta` mascarada; `cargo check` do Windows não roda no container. Segunda verificação junto da T4.

## T2
- Entregue em 2026-11-24: `70b1457` (branch `feat/integracoes-obsidian-cli`), cliente MCP por HTTP (`OBSIDIAN_MCP_URL`) e servidor falso; ERR-53 só pela API do adaptador, não pelo trait; contagem de notas exige `obsidian_files` no servidor real [a preencher]; verificação aguarda as respostas do humano.
- 2026-11-24: ✔ nos 5 critérios, sem bloqueante; contra o servidor real 1.1.0, `notas_indexadas=Some(75)`. Deve corrigir (T4/T5): ERR-53 e número de notas pelo trait e pelo IPC. **T2 concluída**; PR #12.

## T2b
- 2026-11-24: entregue (1.1.0, `obsidian_files`, `--http` só em 127.0.0.1, porta 27180); provas com `obsidian` falso por stdio e HTTP e com o cliente da T2; aplicado no `Vault` pelo orquestrador. Notas no `Vault`: Servidor MCP da Obsidian CLI e Ligar o servidor MCP da Obsidian CLI (no Vault), ligadas no MOC Programação (no Vault). CLI real (humano, 08h11): `obsidian vault=Vault files ext=md total` devolve `75`, só o número, igual à contagem dos `.md` da pasta; formato que o cliente da T2 lê. Pelo servidor em `--http` no Windows (08h14): `obsidian_files` devolve `"75"`. Do WSL e de contêiner com `--network host`, depois do WSL em `mirrored` (08h33): `HTTP/1.1 200` ([[geral-decisao-2026-11-24-wsl-em-mirrored]]). **T2b concluída.**

## T3
- Despachada em 2026-11-24 07h45 (branch `feat/integracoes-github-oauth`).
- Entregue: `26105b1` (device flow, `keyring`, GitHub falso, 16 testes).
- 2026-11-24: ✔ nos 6 critérios, sem bloqueante (RNF-05 conferido; sem aws-lc/openssl). Para a T4: ERR-53 pela trait; corrida no desconectar (checar `cancelado` antes de gravar); máscara do `access_token` no corpo do erro. Opcional: `CofreDoSistema` sem teste (fica para o teste manual). **T3 concluída**; PR #10 aberta.

## Tci
- 2026-11-24: entregue `4d82609`, PR #9. `CI` (15h47, humano): Linux ✔; Windows ✘ nos testes da lib `my-harness` com `0xc0000139 STATUS_ENTRYPOINT_NOT_FOUND` (binário de teste sem o manifesto do comctl32 v6, problema conhecido do Tauri no Windows). Correção despachada: manifesto embutido em todos os binários no Windows MSVC (`new_without_app_manifest`).

## T4
- 2026-11-24: entregue `c0a2fb7` sobre merges de T0a, T2, T3 e T1; merge da correção da T1 em `dafcacb` (conflito no `Cargo.lock`, resolvido pelo orquestrador). ERR-53 no `ErroIntegracao`, `ServicoIntegracoes`, `ErroIpc::Interno` removido, máscara do núcleo com o token, `.env.example` e `compose.yaml` (`network_mode: host`). Pontos: registro do ERR-53 fora do Log (ENT-12 exige `execucao`); "desconectada" só em memória; `notas_indexadas` fora do DTO; variável `MYHARNESS_OBSIDIAN_COFRE` criada sem aval. Em verificação.

## T5
- 2026-11-24: entregue `f3004ae` (branch `feat/integracoes-painel`, sobre a T0a): CMP-03, TEL-02 com CMP-11, instruções, mensagens do catálogo, núcleo simulado nos testes, 17 testes novos. Pontos: link do ERR-01 [a confirmar]; `obsidian://open` na janela real [a confirmar]; AC-128 depende do DTO. Em verificação.

## Verificações de 2026-11-24 à tarde
- Tci: `ffa1d17` (manifesto do Windows embutido nos binários de teste); `CI` da #9 verde em Linux e Windows.
- T4 (`dafcacb`, inclui a T1 corrigida): ✔ nos 8 critérios, sem bloqueante; a sonda do neto pelo núcleo inteiro não deixa processo. Deve corrigir: `listar` troca `não instalado` por `desconectado`. Registro do ERR-53/55 fora do Log levado ao humano (M-48). Opcionais: corrida residual no GitHub entre `cancelado` e `gravar`; desconectar durante conectar do Claude CLI; dois conectar simultâneos. **T1 e T4 concluídas**; PR #13.
- T5 (`f3004ae`): sem bloqueante; deve corrigir: textos de erro fora do catálogo (sufixo do ERR-02 e textos de reserva), conta ausente no CMP-03 (AC-01), `checar` passando por cima de `desconectar`, falta de guarda em conectar, desconectar e repetir, e base na T0a em vez da T4 (usa `ErroIpc` `interno`, removido). Tudo para a T4b.

### 🔗 Conexões
- Plano: [[integracoes-plano]]
- Funcionalidade: [[integracoes-contexto]]
- Projeto: [[geral-contexto]]
