---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-19
substitui: 
---
# ✅ Cada agente roda como `claude -p` direto (S3)

- **Proposta (plano):** [[geral-plano-arquitetura-e-stack]], seção 4 (S3 × S4); prova em [[geral-plano-arquitetura-e-stack-integracoes-e-testes-prototipos]] (P1).
- **Decisão:** S3 confirmada: o `AgentRunner` abre cada agente como `claude -p` direto, com as quatro camadas de permissão (ferramentas por papel, `dontAsk` com lista de permitidos, `harness-gate` no gancho `PreToolUse` carregado por `--settings`, ambiente sem token do GitHub; no `PATH`, sai só a pasta com token, [[geral-decisao-2026-11-20-path-sem-a-pasta-do-token]]) e `--setting-sources ""`, com `--strict-mcp-config` em toda chamada ([[geral-decisao-2026-11-20-strict-mcp-sempre]]). O Agent SDK em Node (S4) sai do plano.
- **Alteração:** ponto S3 × S4 de [[geral-decisao-2026-11-19-stack]], que segue aprovada com a linha reescrita.
- **Motivo:** P1 em 2026-11-19, no Windows: 8 de 8 tentativas barradas pela camada esperada, efeitos no disco conferidos, gancho com mediana de 8,6 ms (56 ms com a partida do Node), nenhuma configuração pessoal carregada. Aval do humano em 2026-11-19.
- **Consequências:** o `harness-gate` cobre também a ferramenta `PowerShell`, que o agente usa no Windows. O núcleo confere o login da CLI antes de despachar: sem `/login`, o `claude -p` sai com `authentication_failed`. As tarefas-interface (G1) podem começar. Se um dia a S3 falhar, a volta à S4 é decisão nova.

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[geral-plano-arquitetura-e-stack]]
- Decisão de origem: [[geral-decisao-2026-11-19-stack]]
- Ponto alterado: [[geral-decisao-2026-11-20-strict-mcp-sempre]], [[geral-decisao-2026-11-20-path-sem-a-pasta-do-token]]
- Regras: [[manual-da-orquestra]]
