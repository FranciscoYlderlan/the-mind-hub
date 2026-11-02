---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-20
substitui: 
---
# ✅ `--strict-mcp-config` em toda chamada ao `claude -p`

- **Proposta (plano):** relatório do implementador da T3 do [[fundacao-plano]] (commit `70124c2`): o `--strict-mcp-config` ia só quando o papel tinha `mcp_config`; o orquestrador sugeriu mandá-lo sempre.
- **Decisão:** toda chamada montada pelo núcleo leva `--strict-mcp-config`, com ou sem `--mcp-config`. Sem MCP do papel, o agente não carrega nenhum servidor MCP de projeto ou de usuário.
- **Alteração:** um ponto de [[geral-decisao-2026-11-19-agente-por-claude-p]], que segue aprovada com a linha reescrita.
- **Motivo:** aval do humano em 2026-11-20, sessão das 08h57 (resposta das 09h13): "Sempre mandar".
- **Consequências:** a T3 volta para um implementador novo, só neste ponto (junto do que o verificador achar). O P3 mostrou que o `--strict-mcp-config` não tira o servidor `claude-in-chrome` quando o `--chrome` vai junto; o papel que usa o navegador continua pedindo `--chrome` de propósito.

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[fundacao-plano]]
- Decisão de origem: [[geral-decisao-2026-11-19-agente-por-claude-p]]
- Regras: [[manual-da-orquestra]]
