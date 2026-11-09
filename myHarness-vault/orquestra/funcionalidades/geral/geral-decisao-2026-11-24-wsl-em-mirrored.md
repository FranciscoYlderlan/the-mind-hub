---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-24
substitui: 
---
# ✅ WSL em modo mirrored para alcançar o servidor MCP do Obsidian

- **Proposta (plano):** T2b do [[integracoes-plano]]: o servidor MCP da Obsidian CLI escuta só no `127.0.0.1` do Windows ([[geral-decisao-2026-11-24-servidor-mcp-do-obsidian]]); com o WSL em `nat`, nem o WSL nem o contêiner o alcançavam (`Connection refused`).
- **Decisão:** o WSL do humano roda com `networkingMode=mirrored` (`C:\Users\Ylderlan\.wslconfig`); o contêiner de desenvolvimento usa a rede do WSL (`--network host` / `network_mode: host`) e o app usa `OBSIDIAN_MCP_URL=http://127.0.0.1:27180/mcp`, igual no Windows e no WSL. O servidor segue só em `127.0.0.1`.
- **Alteração:** nenhuma.
- **Motivo:** recomendação do orquestrador em 2026-11-24, aplicada pelo humano às 08h32; prova às 08h33: `mirrored` e `HTTP/1.1 200` com `Mcp-Session-Id` no WSL e num contêiner com `--network host`.
- **Consequências:** a T4 confere o `compose.yaml` (rede do serviço que roda o backend) e o `.env.example` (`OBSIDIAN_MCP_URL`); abrir o servidor para fora do `127.0.0.1` fica descartado.

### 🔗 Conexões
- Funcionalidade: [[integracoes-contexto]]
- Plano: [[integracoes-plano]]
- Decisões ligadas: [[geral-decisao-2026-11-24-servidor-mcp-do-obsidian]], [[geral-decisao-2026-11-19-repositorio-e-ambiente]]
- Projeto: [[geral-contexto]]
