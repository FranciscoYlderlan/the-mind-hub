---
tipo: diario
status: em-andamento
criado: 2026-11-26
---
# 📓 Diário 2026-11-26 — testes leves e prazo

## O que foi feito
- 13h20 (chat novo): retomada pelo "Onde parei". Clone raso da `main` `fc7e540` no container; T6 (`feat/integracoes-simulado`) e T7 (`fix/integracoes-conectar-repetido`) despachadas em paralelo, cada uma por um implementador na sua cópia, com `sccache`.
- 13h41: o humano pediu testes de no máximo 10 min, leves e que validem tão bem quanto, e build só no fim do módulo. Causa: cada agente compila o Tauri e o WebKit do zero no `pnpm check`, e o hook pre-push o repete a cada push.
- 13h45: o humano aprovou três decisões ([[geral-decisao-2026-11-26-teste-leve-na-tarefa]], [[geral-decisao-2026-11-26-validacao-em-modo-dev]], [[geral-decisao-2026-11-26-target-unico-por-chat]], que substitui a [[geral-decisao-2026-11-26-apagar-target-depois-do-build]]) e recusou um teto de tempo por agente que para e devolve o parcial, porque deixa de fora informação relevante. A regra nova foi mandada aos implementadores da T6 e da T7.
- 13h46: relatório da T6: `7ff03f7` e `701ae91` na `feat/integracoes-simulado`, com push; `pnpm check` verde; `dev:simulado` abre a TEL-02 com as três integrações e conecta; o build de produção não tem o núcleo simulado (detalhe em [[integracoes-plano-verificacoes]]). A regra nova chegou depois: o `target/` (7,6 GB) já tinha sido apagado; o `.sccache` ficou. Tempos: compilação a frio acima de 10 min, `check:web` cerca de 6 s, Playwright cerca de 10 s.

- 13h47: o humano fixou o prazo final do projeto em 2026-11-27, às 12h, e pediu para considerar o custo por hora de cada agente: sem créditos, ele só volta às 17h ([[geral-contexto]], Tempo disponível).
- 13h55: verificador leve da T6 (cerca de 5 min, sem compilar Rust): ✔ nos três critérios; **T6 concluída**, PR #15 aberta (detalhe em [[integracoes-plano-verificacoes]]).
- 13h56: respostas do humano: o orquestrador propõe um MVP para o prazo; T8 (núcleo e infra num crate sem Tauri e hook pre-push leve) depois do merge da T7; Opus em todos os subagentes.
- 14h05: relatório da T7: 5 commits com push na `fix/integracoes-conectar-repetido`, `pnpm check` completo passando (detalhe em [[integracoes-plano-verificacoes]]). Com o GTK instalado e o `sccache` quente, o check completo levou 22 s a 53 s: o gargalo é o container frio. Verificador da T7 despachado no modo leve, com o `target/` da T7.
- 13h53: o humano recusou o MVP: todas as funcionalidades até o prazo, com as etapas 4 e 7 completas ([[geral-contexto]], Tempo disponível). O contrato já cobre os 14 UC e os 157 AC.
- 14h10: T8 no [[integracoes-plano]] e despachada sobre a branch da T7, para destravar o paralelismo no Rust.
- 14h12: verificador da T7 sem bloqueante (cerca de 3 min); **T7 concluída**, PR #16 (detalhe em [[integracoes-plano-verificacoes-t6-t7]]). Ordem de merge: #15, depois #16.
- 14h15: chat em 136 mil tokens na linha Messages; passagem de turno a pedido do humano.
- 14h20: relatório da T8 no chat anterior: `02ae45a` e `a413da2` com push; `check:rapido` frio sem GTK em 2 min 04 s, quente em 22 s (detalhe em [[integracoes-plano-verificacoes-t6-t7]]). Falta o verificador.

## Decisões tomadas
- [[geral-decisao-2026-11-26-teste-leve-na-tarefa]], [[geral-decisao-2026-11-26-validacao-em-modo-dev]], [[geral-decisao-2026-11-26-target-unico-por-chat]]

> [!tip] Onde parei
> - **Prazo:** 2026-11-27, 12h; todas as funcionalidades, etapas 4 e 7 completas; Opus em todos os subagentes; custo por hora conta ([[geral-contexto]], Tempo disponível).
> - **Próximo passo:** (1) o humano mergeia a #15 (T6) e depois a #16 (T7); (2) T8 ([[integracoes-plano-t8]]): entregue na branch `refactor/setup-nucleo-sem-tauri` (`a413da2`), com push; falta rebase sobre a `main` depois da #16, verificador leve e PR; reescrever as notas com os caminhos antigos do `src-tauri` (relatório em [[integracoes-plano-verificacoes-t6-t7]]); briefings passam a usar `cargo test -p my-harness-app <filtro>` e `pnpm check:rapido`; (3) depois do merge da T8, verificador de fluxo principal e os dois adversariais (API pelos testes do núcleo; tela pelo `dev:simulado`), no modo leve ([[geral-decisao-2026-11-26-validacao-em-modo-dev]]); (4) teste manual do humano com o GitHub real e o `/login`; (5) fluxos em `geral-plano-teste-humano`, etapa 3 concluída, `status --atualizar`; (6) etapa 4 completa: contexto e plano a partir do contrato (UC-02, UC-09, UC-13, TEL-04 e a TEL-06 com todos os parâmetros das decisões de hoje), em paralelo com o que não cruza das etapas 5 e 6.
> - **PRs:** #15 (T6) e #16 (T7) abertas, prontas para o merge; #8 a #14 na `main`.
> - **Ambiente:** container novo é frio: compilação do zero e GTK e WebKit para o hook pre-push até a T8 entrar. Testes leves durante a tarefa e `pnpm check` completo uma vez ([[geral-decisao-2026-11-26-teste-leve-na-tarefa]]); um `target/` por chat, apagado no fim da funcionalidade, com `sccache` ([[geral-decisao-2026-11-26-target-unico-por-chat]]). Com o cache quente, o `pnpm check` completo leva de 22 s a 53 s. PR pelo `gh api repos/FranciscoYlderlan/MyHarness/pulls` (o GraphQL não funciona na sessão).
> - **Threads abertas:** opcionais da verificação da T7 ([[integracoes-plano-verificacoes-t6-t7]]); núcleo simulado de `src/lib/ipc/` sobrescreve a conexão pendente (T6, fora do escopo); `listar` e `testar` durante a conexão mostram o GitHub `desconectado`; corrida antiga entre `cancelado` e `guardar` no GitHub; link de instalação do ERR-01 e `obsidian://open` na janela real `[a confirmar]`; "Desconectar" com ERR-53 do cofre deixa o token; limite de 10 GB do `sccache` `[a confirmar]`; `stonebid-vault` com 1 ERRO no `verificar`; as notas de conceito candidatas de [[diario-2026-11-26]].
> - **Dúvidas para o humano:** cenários do modo simulado por URL (ex.: `?cenario=erro`) para os verificadores; faixa do teto de tokens do projeto, quando ligado, `[a preencher]` (início da etapa 4).

### 🔗 Conexões
- Mapa: [[moc-orquestra]]
- Parte anterior: [[diario-2026-11-26]]
- Funcionalidades tocadas: [[geral-contexto]], [[integracoes-plano]]
- Projeto: [[geral-contexto]]
