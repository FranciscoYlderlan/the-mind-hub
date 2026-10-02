---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-29
substitui: [[geral-decisao-2026-10-28-stack-frontend]] (só o tema no Zustand)
aliases: [next-themes, Tema claro e escuro, Theme provider]
---
# ✅ Tema claro e escuro pelo next-themes, não pelo Zustand

- **Proposta (plano):** [[esqueleto-plano#Candidatos a registro]]; já implementado na etapa 2 ([[diario-2026-10-29-esqueleto]]).
- **Decisão:** o tema claro/escuro do `stonebid-web` é controlado pelo `next-themes` (o mesmo que o guia do shadcn usa). O Zustand segue na stack só para outro estado de UI global, quando for necessário. Aprovada pelo humano em 2026-10-29 22:23.
- **Alteração:** nenhuma.
- **Motivo:** é o caminho do shadcn: troca de tema sem piscar, preferência do sistema e persistência prontas, sem escrever store.
- **Consequências:** o RNF-13 (tema escuro) usa o `ThemeProvider` do `next-themes` e o componente `theme-toggle`; é proibido guardar o tema no Zustand.

### 🔗 Conexões
- Funcionalidade: [[esqueleto-contexto]]
- Plano: [[esqueleto-plano]]
- Decisões ligadas: [[geral-decisao-2026-10-28-stack-frontend]], [[geral-decisao-2026-10-28-estrutura-frontend]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
