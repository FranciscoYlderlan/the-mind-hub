---
tipo: plano
funcionalidade: geral
status: aprovado
criado: 2026-11-27
---
# 📋 Etapa 7 — Plano de delegação e despacho de subagentes: tarefas

Base comum e lacunas em [[geral-plano-etapas-4-a-7]]; o `harness-gate` é a B5 e o executor é dono único da E4-T4.

- **AC da etapa:** plano-delegacao AC-07, 11 a 15, 62 a 65, 71, 95, 96, 130 a 133, 144, 145; despacho-subagentes AC-16 a 20, 58, 60, 69, 70, 73, 82, 84, 93, 97 a 99, 116, 123, 126, RNF-06, RNF-07, RNF-10, RNF-02 e RNF-09 medidos; worktree-pr AC-39 a 41, 74, 114.
- **Já existe:** tabelas `plano_delegacao`, `tarefa` (gatilho do "Aprovar"), `execucao` (gatilhos contra `git push`, `merge`, `gh pr merge`), `relatorio`, `criterio`; ERR-09 a 17, 44, 49 no `CodigoErro`; `GitHost` só com OAuth; `infra/git` vazio.
- **E7-T1 formato do plano e do relatório** — `PlanoProposto` e validação pura (ERR-49, ERR-12, faixa por tipo) e `RelatorioSubagente` — `crates/core/src/domain/plano.rs` — B1, B2 — AC-14, 71, 144, 145 (regra).
- **E7-T3 adaptador git** — worktree e branch `tipo/ID-descricao`, commits à frente, push do núcleo com token só no ambiente do git (askpass), conflito — `crates/app/src/infra/git/` — nenhuma — AC-41, 73, 114 (parte).
- **E7-T4 `GitHost` com PR** — `abrir_pr`, `estado_pr`, `listar_prs` no real e no falso — `crates/app/src/infra/github/` — nenhuma — AC-39, 114.
- **E7-T5 runner do subagente** — `cwd` na worktree, ambiente limpo, vigia de queda (1 s) e de silêncio (parâmetro) sobre o executor da E4-T4 — `infra/agente/` (em série com a E4-T4) — E4-T4 — AC-19, 126; RNF-07 com SIGKILL no `fake-claude`.
- **E7-T6 escalonador e briefing** (lógica pura) — quem inicia e quem vai à fila (`teto`, `toca_em`, `recurso`, `depende_de`), briefing por papel dentro do teto, adversarial só com objetivo e acesso — `crates/core/src/application/{escalonador,briefing}.rs` — E7-T1 — AC-17, 62, 64, 70, 71, 73, 97.
- **E7-T7 núcleo do plano** — receber, validar, contar devoluções, gravação dupla (`VaultSide` falso até a E5-T7), pendência, ler, trocar modelo (ERR-11), aprovar (ERR-06), pedir alteração, recusar — `servicos/delegacao/` — E7-T1 — AC-11 a 15, 62 a 65, 95, 96, 144, 145.
- **E7-T8 TEL-03** (CMP-12, CMP-13) com cenários `?cenario=plano-*` e 500 ms contra duplo clique — `src/features/plano/` — B1, B4 — AC-14, 130 a 133, 145.
- **E7-T9 entrega pelo núcleo** — push e PR depois do relatório, ordem por `depende_de`, `reordenar_prs`, consulta do merge, ERR-31 — `servicos/entrega/` — T1, T3, T4 — AC-39 a 41, 114.
- **E7-T10 despacho** — o aval chama o escalonador: worktree (ERR-16), política e portão, `--add-dir`, `prompt_versao`, RN-03 (ERR-15), fila — `servicos/despacho/` — B5, T3, T5, T6, T7 — AC-11, 16, 17, 60, 70, 73, 97, 116. Em série: **E7-T11** acompanhamento e relatório (AC-18 a 20, 69, 98, 126).
- **E7-T12 abas por papel** (CMP-04 da E4-T8) e **E7-T13 cartões de progresso** (CMP-05) — `src/features/subagentes/` — B4 — AC-17, 19, 93, 99, 123, 126.
- **E7-T14 parâmetros da etapa 7** no catálogo da E4-T3 — agentes por tipo, devoluções 2 (1 a 5), briefing 3 mil tokens (1 mil a 8 mil), relatório 1,5 mil (500 a 4 mil), silêncio 10 min (2 a 60), consulta do merge 60 s.
- **E7-T15 CMP-18 Entregas** — lista de PRs com ordem e reordenar — AC-39, 40.
- **Provas baratas:** RNF-06 por tabela na B5 e na T10; RNF-07 na T5; RNF-02 com `PerformanceObserver` no simulado; RNF-09 num ciclo simulado; RNF-10 com estimativa e 3 despachos reais no teste do humano.
- **Cadeia crítica:** B1 → T1 → T7 → T10 → T11; começar T1, T5 e T6 assim que a base comum fechar.

### 🔗 Conexões
- Plano conjunto: [[geral-plano-etapas-4-a-7]]
- Roteiro: [[geral-plano]]
- Projeto: [[geral-contexto]]
