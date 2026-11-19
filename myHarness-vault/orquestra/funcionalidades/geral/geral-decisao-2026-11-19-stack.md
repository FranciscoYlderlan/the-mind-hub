---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-19
substitui: 
---
# ✅ Stack e forma de rodar os agentes

- **Proposta (plano):** [[geral-plano]], seção "Proposta de arquitetura e stack", com detalhe em [[geral-plano-arquitetura-e-stack]] e [[geral-plano-arquitetura-e-stack-integracoes-e-testes]].
- **Decisão:** tela em React + Vite + TypeScript, Tailwind + shadcn/ui, TanStack Query, Zustand e zod; núcleo em Rust com Tauri 2 e `tokio`; SQLite em WAL com `sqlx`; GitHub por OAuth device flow, com token no cofre de credenciais do sistema (`keyring`); checagem com `pnpm check`. Cada agente roda como `claude -p` direto (S3), com permissão em quatro camadas (ferramentas por papel, negar por padrão, portão `harness-gate` no gancho `PreToolUse`, subagente sem token do GitHub). A S3 foi confirmada pelo P1, e o Agent SDK em Node (S4) saiu do plano: [[geral-decisao-2026-11-19-agente-por-claude-p]].
- **Alteração:** nenhuma
- **Motivo:** aval do humano em 2026-11-19.
- **Consequências:** Versões: a mais recente estável ao criar o código, sem rc.

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[geral-plano-arquitetura-e-stack]]
- Ponto S3 × S4: [[geral-decisao-2026-11-19-agente-por-claude-p]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
