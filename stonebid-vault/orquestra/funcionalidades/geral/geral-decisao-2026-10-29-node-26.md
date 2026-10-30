---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-29
substitui: 
aliases: [Node 26, Versão do Node, Node version]
---
# ✅ Node 26 fixo na imagem, no CI e no CD dos dois repositórios

- **Proposta (plano):** [[esqueleto-plano#Candidatos a registro]], dúvida "Node 24 (LTS) ou 26" de [[diario-2026-10-29-esqueleto]].
- **Decisão:** os dois repositórios usam **Node 26**: `NODE_VERSION` do `Dockerfile` do `stonebid-api`, `node-version` dos workflows de CI e CD do `stonebid-api` e do `stonebid-web`, e `engines` dos dois `package.json`. Aprovada pelo humano em 2026-10-29 23:05.
- **Alteração:** a IA perguntou entre 24 (LTS) e 26; o humano escolheu 26.
- **Motivo:** a stack já cita Node 26.13.0+ ([[geral-decisao-2026-10-28-stack-frontend]]); a imagem do backend (24) e os workflows com `lts/*` destoavam dela e do CI do web (26).
- **Consequências:** imagem, CI, CD e máquina local rodam a mesma versão; `lts/*` e `NODE_VERSION=24` saem dos repositórios num PR `chore` em cada um, depois do merge dos PRs da etapa 3.

### 🔗 Conexões
- Funcionalidade: [[esqueleto-contexto]]
- Plano: [[carteira-e-lotes-plano]]
- Decisões ligadas: [[geral-decisao-2026-10-28-stack-frontend]], [[geral-decisao-2026-10-28-stack-backend]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
