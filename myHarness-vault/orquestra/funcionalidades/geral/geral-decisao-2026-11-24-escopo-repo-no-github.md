---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-24
substitui: 
---
# ✅ Token do GitHub com o escopo `repo`

- **Proposta (plano):** dúvida da T3 do [[integracoes-plano]]: `ESCOPOS_PADRAO = ["repo"]` estava `[a confirmar]`.
- **Decisão:** o device flow pede o escopo `repo`, porque o MyHarness dá push e abre PR (RF-27, etapas 7 e 9 do [[geral-plano]]).
- **Alteração:** nenhuma.
- **Motivo:** resposta do humano em 2026-11-24, às 13h: "Mantém 'repo'".
- **Consequências:** o `[a confirmar]` do código da T3 sai numa tarefa seguinte; "Desconectar" só apaga o token local, e revogar no GitHub é pelo site (Settings → Applications).

### 🔗 Conexões
- Funcionalidade: [[integracoes-contexto]]
- Plano: [[integracoes-plano]]
- Projeto: [[geral-contexto]]
