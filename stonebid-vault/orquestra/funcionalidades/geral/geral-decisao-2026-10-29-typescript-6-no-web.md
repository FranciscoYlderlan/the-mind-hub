---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-29
substitui: 
aliases: [TypeScript 6, Versão do TypeScript no web]
---
# ✅ TypeScript 6 no stonebid-web

- **Proposta (plano):** [[esqueleto-plano#Candidatos a registro]]; já implementado na etapa 2 ([[diario-2026-10-29-esqueleto]]).
- **Decisão:** o `stonebid-web` usa **TypeScript 6** (6.0.3 ou mais recente da linha 6). Aprovada pelo humano em 2026-10-29 22:23.
- **Alteração:** nenhuma.
- **Motivo:** o `typescript-eslint` ainda não suporta o TypeScript 7.
- **Consequências:** a checagem de tipos do CI roda com o TypeScript 6; subir para o 7 só quando o `typescript-eslint` suportar, com decisão nova.

### 🔗 Conexões
- Funcionalidade: [[esqueleto-contexto]]
- Plano: [[esqueleto-plano]]
- Decisões ligadas: [[geral-decisao-2026-10-28-stack-frontend]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
