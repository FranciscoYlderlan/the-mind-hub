---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-29
substitui: [[geral-decisao-2026-10-28-stack-backend]] (só a linha do Prisma)
aliases: [Prisma 7, Prisma 7.10.1, Versão do Prisma, ORM version]
---
# ✅ Prisma 7.10.1 ou mais recente da linha 7, no lugar da 8

- **Proposta (plano):** [[esqueleto-plano#Candidatos a registro]]; já implementado na etapa 2 ([[diario-2026-10-29-esqueleto]]).
- **Decisão:** o ORM é o Prisma **7.10.1 ou mais recente da linha 7**. Substitui a linha do Prisma de [[geral-decisao-2026-10-28-stack-backend]]; o resto daquela decisão segue valendo. Aprovada pelo humano em 2026-10-29 22:23.
- **Alteração:** nenhuma.
- **Motivo:** na implementação, o Prisma 8 só existia em versão rc e é outro produto, sem `migrate`.
- **Consequências:** `prisma migrate deploy` e o seed seguem no CD ([[geral-decisao-2026-10-29-hospedagem]]); o Prisma 7 recusa `migrate reset` vindo de agente, então resets de banco local ficam com o humano ou com comando explícito.

### 🔗 Conexões
- Funcionalidade: [[esqueleto-contexto]]
- Plano: [[esqueleto-plano]]
- Decisões ligadas: [[geral-decisao-2026-10-28-stack-backend]], [[geral-decisao-2026-10-29-hospedagem]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
