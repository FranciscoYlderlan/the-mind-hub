---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-23
substitui: 
---
# ✅ Uma PR por tarefa, mergeada pelo humano

- **Proposta (plano):** o humano abriu em 2026-11-23 uma PR por tarefa da G1 (#1 T4, #2 T5, #3 T1 e T2); o orquestrador perguntou se seguia assim ou voltava à PR única de [[geral-decisao-2026-11-19-branches-e-pr-unica]].
- **Decisão:** cada tarefa sobe na sua PR para a `main`, sem branch de integração. A PR só vai ao humano depois que a tarefa passa no verificador e no `pnpm check` local. Quem clica em "merge" é o humano, na ordem que o orquestrador indica (a tarefa de que outra depende entra antes).
- **Alteração:** só o ponto da PR única de [[geral-decisao-2026-11-19-branches-e-pr-unica]] muda; a branch por tarefa segue.
- **Motivo:** respostas do humano em 2026-11-23, às 16h09: "deixe separada ... está tudo bem" e "Eu (humano) clico".
- **Consequências:** ordem da G1: #3 (T1 e T2, pronta), #4 (T3, aberta pelo orquestrador), #1 (T4, depois de corrigida e verificada), #2 (T5, depois de rebase sobre a T3 corrigida, do ajuste ao M-37 a M-40 e do verificador). A `feat/setup-g1-interfaces` não é criada.

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[fundacao-plano]]
- Ponto alterado: [[geral-decisao-2026-11-19-branches-e-pr-unica]]
- GitHub: [[geral-decisao-2026-11-23-push-e-pr-no-github]]
- Regras: [[manual-da-orquestra]], [[padroes]]
