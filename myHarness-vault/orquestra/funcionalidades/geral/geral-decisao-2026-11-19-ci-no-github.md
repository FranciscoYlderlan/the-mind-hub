---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-19
substitui: 
---
# ✅ CI no GitHub Actions

- **Proposta (plano):** [[geral-plano-arquitetura-e-stack-integracoes-e-testes]], linhas "CI local" e "CI no GitHub", com a alternativa de ficar sem CI remoto.
- **Decisão:** o repositório tem **CI no GitHub Actions**: checagem em PR e em push na `main` ([[geral-decisao-2026-11-19-gatilho-do-ci]]), sem CD, em `windows-latest` e `ubuntu-latest`, rodando `pnpm check`. O gancho local (`lefthook`) segue como na proposta.
- **Alteração:** nenhuma
- **Motivo:** resposta do humano em 2026-11-19.
- **Consequências:** o `.github/workflows/ci.yml` entra no esqueleto com o escopo de commit `setup`; o workflow `CI` está ativo no GitHub desde o primeiro push, em 2026-11-23 ([[geral-decisao-2026-11-23-push-e-pr-no-github]]). O ✔ do CI aparece no PR antes do merge do humano.

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[geral-plano-arquitetura-e-stack-integracoes-e-testes]]
- Regras: [[manual-da-orquestra]]
