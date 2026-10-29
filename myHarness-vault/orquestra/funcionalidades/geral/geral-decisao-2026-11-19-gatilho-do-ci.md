---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-19
substitui: 
---
# ✅ CI roda em PR e em push na main

- **Proposta (plano):** dúvida do [[diario-2026-11-19]]: `ci.yml` em todo push e PR ou só em algumas branches.
- **Decisão:** o `ci.yml` roda em todo `pull_request` e em `push` só na branch `main`.
- **Alteração:** ponto do gatilho de [[geral-decisao-2026-11-19-ci-no-github]], que segue aprovada com a linha reescrita.
- **Motivo:** resposta do humano em 2026-11-19 (opção recomendada).
- **Consequências:** push nas branches dos subagentes não gasta minutos do Actions; o PR mostra o ✔ antes do merge e a `main` é conferida depois dele. O `ci.yml` do esqueleto, hoje com `push:` sem filtro, muda (escopo `setup`).

### 🔗 Conexões
- Projeto: [[geral-contexto]]
- Plano: [[geral-plano]]
- Regras: [[manual-da-orquestra]]
- Decisão de origem: [[geral-decisao-2026-11-19-ci-no-github]]
