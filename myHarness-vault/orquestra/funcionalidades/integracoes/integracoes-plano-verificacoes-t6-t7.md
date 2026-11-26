---
tipo: plano
funcionalidade: integracoes
status: aprovado
criado: 2026-11-24
---
# 📋 Integrações — verificações da T6 e da T7

## T6
- 2026-11-26: tarefa criada por decisão do humano (12h39); começa num chat novo, depois do adversarial.
- 2026-11-26 13h46 (implementador, `feat/integracoes-simulado`, `701ae91`): `src/dev/nucleo-simulado.ts` sobre o `criarNucleoSimuladoDeIntegracoes` (o mesmo dos testes), `src/dev/modo-simulado.ts`, plugin do Vite que só age no `serve` com `mode simulado`, script `dev:simulado`; 3 testes vitest novos. Prova: `pnpm check` com código 0; Playwright na porta 1420 conectou GitHub (código `SIMU-1234`, conta `conta-simulada`) e Obsidian CLI (128 notas); `grep` no `dist/` de `pnpm build` sem o núcleo simulado. Fora do escopo: o núcleo simulado de `src/lib/ipc/` sobrescreve a conexão pendente no "Conectar" repetido (contornado em `src/dev/`). Dúvida: cenários por URL (ex.: `?cenario=erro`) para os verificadores. `target/` apagado (7,6 GB).
- 2026-11-26 13h55 (verificador leve, sem compilar Rust, cerca de 5 min): ✔ nos três critérios; diff só em `package.json`, `vite.config.ts` e `src/dev/`, sem Rust; `check:web` com 38 testes; Playwright na TEL-02 (GitHub com `SIMU-1234`, Obsidian CLI com 128 notas, um código só no segundo clique); `grep` no `dist/` sem o núcleo simulado. Ressalva: a prova no navegador usou o servidor do implementador, já aberto na porta 1420. **T6 concluída**; PR #15.

## T7
- 2026-11-26: tarefa criada por decisão do humano (13h10); começa num chat novo, em paralelo com a T6.
- 2026-11-26 14h05 (implementador, `fix/integracoes-conectar-repetido`, `91a4d00`; commits `69a9daa`, `c458ed2`, `835f313`, `5e937c2`, `91a4d00`, todos com push): guarda de conexão em andamento por integração no `NucleoMyHarness` (`nucleo.rs`); "Conectar" repetido recebe as mesmas instruções e o mesmo resultado (AC-157); "Desconectar" durante a conexão cancela (B2); `ClaudeCli::cancelar()` mata o login; registro no log do núcleo; `validarResposta` com zod na tela (ERR-55 fora do contrato); "Repetir" uma vez por erro. Testes: 4 no núcleo (AC-157 e B2, GitHub e Claude CLI), 1 no adaptador, 3 na tela. Prova: `pnpm check` completo no último push (22 s com o `sccache` quente). Fora do escopo: `listar` e `testar` durante a conexão mostram o GitHub `desconectado`; corrida antiga entre a checagem de `cancelado` e o `guardar`; testes do Claude CLI no núcleo só em Unix. Dúvidas: guarda no `ServicoIntegracoes` em vez do `nucleo.rs`; `conectar` cancelado no GitHub devolve ERR-02 cancelado. `target/` mantido em `/home/claude/t7/target`.
- 2026-11-26 14h12 (verificador leve, cerca de 3 min): ✔ nos quatro critérios; cada teste novo falharia sem a correção; `pnpm check` completo em 22,7 s; as duas escolhas batem com o contrato (ERR-02 `cancelado` com estado final `desconectado`; guarda no núcleo por integração). Sem bloqueante e sem "deve corrigir". Opcionais: o teste B2 do Claude não prova que o processo do `/login` morreu (`nucleo/tests.rs:513`); a conexão vive na future do primeiro pedido (`nucleo.rs:359`); `desconectar` liga a marca de cancelamento mesmo sem login (`infra/claude/mod.rs:435`). **T7 concluída**; PR #16.

## T8
- 2026-11-26: tarefa criada por aval do humano (13h56), depois da T7; despachada às 14h10 sobre a branch da T7.

### 🔗 Conexões
- Parte anterior: [[integracoes-plano-verificacoes]]
- Plano: [[integracoes-plano]]
- Funcionalidade: [[integracoes-contexto]]
- Projeto: [[geral-contexto]]
