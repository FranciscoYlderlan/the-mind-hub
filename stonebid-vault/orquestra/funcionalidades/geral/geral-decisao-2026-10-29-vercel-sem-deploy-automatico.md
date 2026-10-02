---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-29
substitui: 
aliases: [vercel.json, deploymentEnabled, Deploy só pelo CD]
---
# ✅ Vercel sem deploy automático pelo Git (só o cd.yml publica)

- **Proposta (plano):** [[esqueleto-plano#Candidatos a registro]]; já implementado na etapa 2 ([[diario-2026-10-29-esqueleto]]).
- **Decisão:** o `stonebid-web` tem `vercel.json` com `git.deploymentEnabled: false`: a integração Git da Vercel não publica nada; quem publica é só o `cd.yml` do GitHub Actions. Aprovada pelo humano em 2026-10-29 22:23.
- **Alteração:** nenhuma.
- **Motivo:** sem isso, todo push publicaria duas vezes (Vercel e Actions) e publicaria mesmo com CI vermelho.
- **Consequências:** nenhum deploy do web fora do `cd.yml` ([[geral-decisao-2026-10-29-modo-de-implementacao]]).

### 🔗 Conexões
- Funcionalidade: [[esqueleto-contexto]]
- Plano: [[esqueleto-plano]]
- Decisões ligadas: [[geral-decisao-2026-10-29-modo-de-implementacao]], [[geral-decisao-2026-10-29-hospedagem]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
