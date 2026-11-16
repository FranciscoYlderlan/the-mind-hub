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

## Decisões tomadas
- [[geral-decisao-2026-11-26-teste-leve-na-tarefa]], [[geral-decisao-2026-11-26-validacao-em-modo-dev]], [[geral-decisao-2026-11-26-target-unico-por-chat]]

> [!tip] Onde parei
> - **Próximo passo:** (1) T6 (`dev:simulado`) e T7 (conectar repetido, B2 e opcionais da tela; [[bug-conectar-repetido-abre-segundo-fluxo-2026-11-26]]) em paralelo, cada uma por um implementador, com `sccache`; PR por tarefa; (1b) depois do merge, verificador de fluxo principal e os dois adversariais (API e tela) de novo, com o clone e o `target/` compartilhados; (2) teste manual do humano com o GitHub real e o `/login` do Claude CLI; (3) fluxos em `geral-plano-teste-humano`; etapa 3 concluída e `status --atualizar`.
> - **PRs:** #8 a #14 na `main`; nenhuma PR da etapa 3 aberta.
> - **Ambiente:** todo o código está na `main` do GitHub (#8 a #14); nenhum trabalho vive só em container. Container do implementador precisa de GTK e WebKit para o hook pre-push; implementador apaga o `target/` ao fim da tarefa ([[geral-decisao-2026-11-26-apagar-target-depois-do-build]]); na validação, `target/` compartilhado até o fim da funcionalidade ([[geral-decisao-2026-11-26-build-reaproveitado-na-validacao]]).
> - **Threads abertas:** link de instalação do ERR-01 e `obsidian://open` na janela real `[a confirmar]`; login com stdin fechado; "Desconectar" com ERR-53 do cofre deixa o token, e o próximo "Conectar" reconecta sem device flow (adversarial, fora do escopo); limite de 10 GB do cache do `sccache` `[a confirmar]`; `stonebid-vault` com 1 ERRO no `verificar`; contrato das decisões de hoje no início das etapas 4, 5, 7 e 8; as duas notas de conceito em "Candidatos"; recusa rápida no loopback do Windows como proposta, se o atraso de ~2 s no ERR-53 incomodar.
> - **Dúvidas para o humano:** faixa do teto de tokens do projeto, quando ligado, `[a preencher]` (perguntar no início da etapa 4).

### 🔗 Conexões
- Mapa: [[moc-orquestra]]
- Parte anterior: [[diario-2026-11-26]]
- Funcionalidades tocadas: [[geral-contexto]], [[integracoes-plano]]
- Projeto: [[geral-contexto]]
