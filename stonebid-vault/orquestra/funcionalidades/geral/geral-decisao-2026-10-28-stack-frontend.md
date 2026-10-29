---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-28
substitui: 
aliases: [Tecnologias do frontend, Stack do stonebid-web, Frontend stack]
---
# ✅ Stack do frontend (stonebid-web)

- **Proposta (plano):** nenhuma. A definição veio direto do humano, como base do projeto, sem proposta da IA antes.
- **Decisão:** o repositório `stonebid-web` usa estas tecnologias e versões:

| Tecnologia | Versão | Observação |
|---|---|---|
| Node | 26.13.0 | |
| npm | latest | |
| React | 19.3 | |
| Vite | 8.3.4 | |
| Tailwind CSS | v4.3 | |
| TanStack Router | v1 | **Só a gestão de rotas**, não o framework (TanStack Start fica de fora) |
| TanStack Query | v5 | Dados do servidor |
| Zustand | latest | Só estado de UI global (sidebar, tema, preferências), quando realmente necessário |
| zod | 4.6 | Validações e env |
| shadcn/ui | — | Projeto iniciado pelo guia oficial para Vite: https://ui.shadcn.com/docs/installation/vite |
| ESLint | latest | Lint |
| Prettier | latest | Configuração e padrão do Prettier |
| Playwright | latest | Usado pelas subthreads de teste para validar cada funcionalidade |

- **Alteração:** 2026-10-28: lint definido como ESLint (com Prettier) e Playwright acrescentado para os testes de funcionalidade ([[geral-decisao-2026-10-28-testes-frontend-playwright]]). Sem testes unitários e de componente no frontend. Zustand (latest) acrescentado.
- **Motivo:** definição base do projeto informada pelo humano; motivo de cada escolha não registrado [a confirmar].
- **Consequências:**
  - A criação do projeto segue o passo a passo do shadcn para Vite, não um template próprio.
  - Rotas file-based com o plugin do TanStack Router no Vite; sem adotar TanStack Start nem outro framework full-stack.
  - Estado do servidor no TanStack Query; Zustand nunca guarda dado vindo da API; validação de formulários, search params e env com zod.
  - Trocar ou acrescentar biblioteca de base (roteador, validação, UI, estilos, lint, testes) exige nova decisão.
  - Sem testes unitários e de componente (sem Vitest, Testing Library ou MSW no frontend).
  - Funcionalidade do frontend só está pronta depois de validada no Playwright: [[geral-decisao-2026-10-28-testes-frontend-playwright]].
  - Estrutura de pastas: [[geral-decisao-2026-10-28-estrutura-frontend]]. Regras de componentes: [[geral-decisao-2026-10-28-criacao-de-componentes]].

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[geral-plano]]
- Projeto: [[geral-contexto]]
- Relacionadas: [[geral-decisao-2026-10-28-stack-backend]], [[geral-decisao-2026-10-28-testes-frontend-playwright]]
- Regras: [[manual-da-orquestra]]
