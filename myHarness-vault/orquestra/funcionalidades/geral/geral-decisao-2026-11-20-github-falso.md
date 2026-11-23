---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-20
substitui: 
---
# ✅ GitHub falso nos testes enquanto a conta está sem acesso

- **Proposta (plano):** pergunta do orquestrador em 2026-11-20, às 09h31, depois de [[geral-decisao-2026-11-20-tudo-local-sem-github]]: como seguir com o que depende do GitHub (RF-03 na etapa 3, RF-27 na etapa 7, o ciclo até o PR na etapa 9 do [[geral-plano]]).
- **Decisão:** essas partes são construídas e testadas contra um GitHub falso, atrás da interface `GitHost`, como o `tools/fake-claude`. O teste com o GitHub real entra na etapa 3, num repositório de testes ([[geral-decisao-2026-11-23-github-real-na-etapa-3]]).
- **Alteração:** a forma de seguir, que estava [a confirmar] em [[geral-decisao-2026-11-20-tudo-local-sem-github]].
- **Motivo:** resposta do humano em 2026-11-20, às 09h31: "GitHub falso".
- **Consequências:** RF-03 e RF-27 passam nos verificadores contra o falso; o teste real com o GitHub entra na etapa 3 ([[geral-decisao-2026-11-23-github-real-na-etapa-3]]). Nenhum agente precisa da conta do humano.

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[geral-plano]]
- Decisão de origem: [[geral-decisao-2026-11-20-tudo-local-sem-github]]
- Teste real: [[geral-decisao-2026-11-23-github-real-na-etapa-3]]
- Regras: [[manual-da-orquestra]]
