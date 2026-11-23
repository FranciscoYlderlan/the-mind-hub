---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-23
substitui: 
---
# ✅ Uma PR por tarefa, mergeada pelo humano

- **Proposta (plano):** o humano abriu em 2026-11-23 uma PR por tarefa da G1 (#1 T4, #2 T5, #3 T1 e T2); o orquestrador perguntou se seguia assim ou voltava à PR única de [[geral-decisao-2026-11-19-branches-e-pr-unica]].
- **Decisão:** cada tarefa sobe na sua PR para a `main`, sem branch de integração. A PR só vai ao humano depois que a tarefa passa no verificador e no `pnpm check` local. Quem faz o merge é o humano, sempre por "Rebase and merge", na ordem que o orquestrador indica (a tarefa de que outra depende entra antes). Depois de cada merge, o orquestrador refaz as PRs abertas sobre a `main` nova (`rebase --committer-date-is-author-date` e `push --force-with-lease` na branch da PR, nunca na `main`).
- **Alteração:** só o ponto da PR única de [[geral-decisao-2026-11-19-branches-e-pr-unica]] muda; a branch por tarefa segue.
- **Motivo:** respostas do humano em 2026-11-23, às 16h09 ("deixe separada ... está tudo bem", "Eu (humano) clico") e às 16h22 ("você lançando as pr's e eu fazendo rebase e merge ... isso fica para o final eu resolver").
- **Consequências:** ordem da G1: #3 (T1 e T2, pronta), #4 (T3, aberta pelo orquestrador), #1 (T4, depois de corrigida e verificada), #2 (T5, depois de rebase sobre a T3 corrigida, do ajuste ao M-37 a M-40 e do verificador). A `feat/setup-g1-interfaces` não é criada. O "Rebase and merge" grava a data de commit do dia do clique (a de autor fica): a correção dessas datas fica para o fim do projeto, com o humano.

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[fundacao-plano]]
- Ponto alterado: [[geral-decisao-2026-11-19-branches-e-pr-unica]]
- GitHub: [[geral-decisao-2026-11-23-push-e-pr-no-github]]
- Regras: [[manual-da-orquestra]], [[padroes]]
