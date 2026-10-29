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
- **Decisão:** o repositório `stonebid-web` usa estas tecnologias e versões. Nenhuma versão é travada: vale a versão citada ou mais recente.

| Tecnologia | Versão | Observação |
|---|---|---|
| Node | 26.13.0 ou mais recente | |
| npm | latest | |
| React | 19.3 ou mais recente | |
| Vite | 8.3.4 ou mais recente | |
| Tailwind CSS | v4.3 ou mais recente | |
| TanStack Router | v1 ou mais recente | **Só a gestão de rotas**, não o framework (TanStack Start fica de fora) |
| TanStack Query | v5 ou mais recente | Dados do servidor |
| Zustand | latest | Só estado de UI global (sidebar, tema, preferências), quando realmente necessário |
| zod | 4.6 ou mais recente | Validações e env |
| shadcn/ui | — | Projeto iniciado pelo guia oficial para Vite: https://ui.shadcn.com/docs/installation/vite |
| ESLint | latest | Lint |
| Prettier | latest | Configuração e padrão do Prettier |
| Playwright | latest | Usado pelas subthreads de teste para validar cada funcionalidade |
| GitHub Actions | — | CI/CD integrado ao GitHub: lint, formatação, checagem de tipos e build em todo push/PR; deploy automático depois do CI verde |

- **Alteração:** 2026-10-28: lint definido como ESLint (com Prettier) e Playwright acrescentado para os testes de funcionalidade ([[geral-decisao-2026-10-28-testes-frontend-playwright]]). Sem testes unitários e de componente no frontend. Zustand (latest) acrescentado. 2026-10-28: CI/CD com GitHub Actions acrescentado, igual ao backend. 2026-10-29: destino do CD definido: Vercel ([[geral-decisao-2026-10-29-hospedagem]]). Versões sem trava: Node 26.13.0, React 19.3, Vite 8.3.4, Tailwind CSS v4.3, TanStack Router v1, TanStack Query v5 e zod 4.6 valem a citada ou mais recente.
- **Motivo:** definição base do projeto informada pelo humano: escolha do humano (resposta de 2026-10-29).
- **Consequências:**
  - A criação do projeto segue o passo a passo do shadcn para Vite, não um template próprio.
  - Rotas file-based com o plugin do TanStack Router no Vite; sem adotar TanStack Start nem outro framework full-stack.
  - Estado do servidor no TanStack Query; Zustand nunca guarda dado vindo da API; validação de formulários, search params e env com zod.
  - Versões sem trava: no `package.json`, faixa que aceita a citada ou mais recente (não a versão exata).
  - Trocar ou acrescentar biblioteca de base (roteador, validação, UI, estilos, lint, testes) exige nova decisão.
  - Sem testes unitários e de componente (sem Vitest, Testing Library ou MSW no frontend).
  - CI no GitHub Actions roda ESLint, Prettier (checagem), checagem de tipos do TypeScript e build em todo push/PR; PR com CI vermelho não entra. O Playwright não roda no CI: a validação é feita pelas subthreads de teste ([[geral-decisao-2026-10-28-testes-frontend-playwright]]).
  - CD no GitHub Actions faz o deploy automático do `stonebid-web` quando o CI passa na branch principal. Destino do deploy: Vercel, pela [[geral-decisao-2026-10-29-hospedagem]]; branch principal `main`, pela [[geral-decisao-2026-10-29-padrao-de-branches]].
  - Variáveis e segredos do deploy ficam nos *secrets* do GitHub, nunca no repositório.
  - Funcionalidade do frontend só está pronta depois de validada no Playwright: [[geral-decisao-2026-10-28-testes-frontend-playwright]].
  - Estrutura de pastas: [[geral-decisao-2026-10-28-estrutura-frontend]]. Regras de componentes: [[geral-decisao-2026-10-28-criacao-de-componentes]].

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[geral-plano]]
- Projeto: [[geral-contexto]]
- Relacionadas: [[geral-decisao-2026-10-28-stack-backend]], [[geral-decisao-2026-10-28-testes-frontend-playwright]], [[geral-decisao-2026-10-29-hospedagem]]
- Regras: [[manual-da-orquestra]]
