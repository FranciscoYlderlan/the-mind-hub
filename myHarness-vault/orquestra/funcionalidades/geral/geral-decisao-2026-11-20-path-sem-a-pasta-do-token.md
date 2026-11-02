---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-20
substitui: 
---
# ✅ No `PATH`, sai só a pasta com token do GitHub

- **Proposta (plano):** correção da T3 do [[fundacao-plano]] (commit `1a0c889`): a camada 4 tira do ambiente do agente toda variável cujo valor contém um token com prefixo do GitHub. O implementador apontou que isso também tira o `PATH` quando uma pasta tem um nome como `ghp_tools`.
- **Decisão:** no `PATH`, o núcleo tira só as pastas que contêm um token com prefixo do GitHub e mantém as outras. As demais variáveis seguem a regra da camada 4: o valor contém token, a variável sai inteira.
- **Alteração:** um ponto da camada 4 de [[geral-decisao-2026-11-19-agente-por-claude-p]], que segue aprovada.
- **Motivo:** resposta do humano em 2026-11-20, às 09h24: "Opção B" (tirar só a pasta e manter o resto, para o agente não parar).
- **Consequências:** o agente acha os programas mesmo com uma pasta assim no `PATH`. O separador das pastas é `;` no Windows e `:` no Linux. A T3 volta para um implementador novo, só neste ponto (junto do que a segunda verificação achar).

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[fundacao-plano]]
- Decisão de origem: [[geral-decisao-2026-11-19-agente-por-claude-p]]
- Mascaramento: [[geral-decisao-2026-11-20-mascaramento-sem-adivinhar]]
- Regras: [[manual-da-orquestra]]
