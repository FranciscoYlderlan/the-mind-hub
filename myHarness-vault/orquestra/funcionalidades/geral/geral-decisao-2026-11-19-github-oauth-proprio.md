---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-19
substitui: 
---
# ✅ GitHub por app OAuth próprio

- **Proposta (plano):** [[geral-plano-arquitetura-e-stack-integracoes-e-testes]], linha "GitHub: login": device flow, com a alternativa de reaproveitar o login do `gh`.
- **Decisão:** o MyHarness entra no GitHub por um **app OAuth próprio**, com device flow ligado; não reaproveita o login do `gh`.
- **Alteração:** nenhuma
- **Motivo:** resposta do humano em 2026-11-19.
- **Consequências:** o humano cria o app OAuth na conta do GitHub (com device flow ligado) quando o GitHub existir; o `client_id` entra no `.env` do repositório, sem segredo do app no programa. Token no cofre de credenciais do sistema, como na [[geral-decisao-2026-11-19-stack]].

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[geral-plano-arquitetura-e-stack-integracoes-e-testes]]
- Regras: [[manual-da-orquestra]]
