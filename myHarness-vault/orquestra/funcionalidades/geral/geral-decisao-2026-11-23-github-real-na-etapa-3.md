---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-23
substitui: 
---
# ✅ Teste com o GitHub real na etapa 3, num repositório de testes

- **Proposta (plano):** pergunta do orquestrador em 2026-11-23, às 16h34: com a conta do GitHub de volta, o teste real continua só na etapa 9 ([[geral-decisao-2026-11-20-github-falso]]) ou entra antes.
- **Decisão:** o teste com o GitHub real entra na etapa 3 (Integrações) do [[geral-plano]], contra um repositório só de testes, nunca o `MyHarness`. O GitHub falso atrás do `GitHost` segue nos testes automáticos.
- **Alteração:** o ponto "teste real só na etapa 9" da [[geral-decisao-2026-11-20-github-falso]], que segue aprovada com a linha reescrita.
- **Motivo:** respostas do humano em 2026-11-23: "Real test earlier" (16h36) e "Etapa 3, repo de teste" (16h45).
- **Consequências:** o repositório de testes é `FranciscoYlderlan/myharness-teste`, criado pelo humano em 2026-11-23 (17h45); RF-03 passa também contra o GitHub real nessa etapa.

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[geral-plano]]
- Decisão de origem: [[geral-decisao-2026-11-20-github-falso]]
