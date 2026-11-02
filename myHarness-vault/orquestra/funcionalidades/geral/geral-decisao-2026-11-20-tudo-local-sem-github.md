---
tipo: decisao
funcionalidade: geral
status: substituida
criado: 2026-11-20
substitui: 
---
# ✅ Tudo local, sem PR, enquanto a conta do GitHub está sem acesso

- **Proposta (plano):** etapa 2 do [[geral-plano]]: a T3 a T5 do [[fundacao-plano]] seriam juntadas numa PR única ([[geral-decisao-2026-11-19-branches-e-pr-unica]]), e o GitHub do projeto ainda não existia ([[geral-decisao-2026-11-19-repositorio-e-ambiente]]).
- **Decisão:** a produção segue toda local. Nenhuma PR é aberta. Cada tarefa fica na sua branch; as branches do mesmo processo se juntam numa branch de integração local, com `pnpm check` local; o merge na `main` é local e pede a confirmação do humano. A falta do GitHub não para a produção.
- **Alteração:** a "PR única" de [[geral-decisao-2026-11-19-branches-e-pr-unica]] vira a branch de integração local; o "GitHub [a preencher]" de [[geral-decisao-2026-11-19-repositorio-e-ambiente]] vira esta nota. As duas seguem aprovadas, com a linha reescrita.
- **Motivo:** resposta do humano em 2026-11-20, às 09h27: "a PR ainda não irá ser aberta ... vamos fazer tudo local ... pois tive um problema com o acesso ao meu github e não consigo acessar a conta mas isso não deve ser um impedimento na produção".
- **Consequências:** o CI do GitHub ([[geral-decisao-2026-11-19-ci-no-github]], [[geral-decisao-2026-11-19-gatilho-do-ci]]) não roda; a prova é local (`pnpm check` e os ganchos do `lefthook`). Nada de push. Partes que dependem do GitHub nas etapas seguintes (RF-03, RF-27, o ciclo até o PR da etapa 9) seguem contra um GitHub falso ([[geral-decisao-2026-11-20-github-falso]]).

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[fundacao-plano]], [[geral-plano]]
- Forma de seguir: [[geral-decisao-2026-11-20-github-falso]]
- Decisões alteradas: [[geral-decisao-2026-11-19-branches-e-pr-unica]], [[geral-decisao-2026-11-19-repositorio-e-ambiente]]
- Regras: [[manual-da-orquestra]]
