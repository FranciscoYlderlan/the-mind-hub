---
aliases: [Instalar o obsidian-cli-mcp, Ativar MCP do Obsidian, Setup Obsidian MCP server]
tags: [ferramentas/obsidian, estudos/programacao]
tipo: procedimento
status: rascunho
criado: 2026-11-24
origem: T2b do integracoes-plano (myHarness-vault), 2026-11-24; nota Obsidian CLI via MCP não carrega
---
# 🛠️ Ligar o servidor MCP da Obsidian CLI

> [!tldr] Em uma linha
> Uma entrada no Claude desktop para o stdio e, quando o MyHarness precisar, um segundo processo com `--http`.

Como ligar a TV e o som separados: o mesmo [[Servidor MCP da Obsidian CLI]] roda duas vezes, cada uma num cabo. O Claude usa o stdio; o MyHarness, o HTTP.

> [!note] Passo a passo
> 1. Claude desktop → Configurações → Desenvolvedor → "Editar configuração": abre o arquivo certo (em `%LOCALAPPDATA%\Claude-Data\...`, nunca o caminho da documentação).
> 2. Em `mcpServers.obsidian-cli`: `command: node`, `args: [caminho do obsidian-cli-mcp.js]`, `env.OBSIDIAN_BIN: C:\Program Files\Obsidian\Obsidian.com`. Sem `--http`.
> 3. Sair pela bandeja, abrir o app e um chat novo; validar com `obsidian_search` no `Vault`.
> 4. Para o MyHarness, no PowerShell: `$env:OBSIDIAN_BIN="C:\Program Files\Obsidian\Obsidian.com"` e `node <caminho>\obsidian-cli-mcp.js --http`.
> 5. No app: `OBSIDIAN_MCP_URL=http://127.0.0.1:27180/mcp`. No WSL, antes: `[wsl2]` + `networkingMode=mirrored` em `C:\Users\<eu>\.wslconfig` e `wsl --shutdown`; contêiner com `--network host`.
> 6. Validar o HTTP: `initialize` e depois `obsidian_files` com `ext: "md"` e `total: true` devolvem um número.

> [!tip] Quando abrir esta nota
> Quando as ferramentas `obsidian_*` sumirem do chat ou o MyHarness mostrar a Obsidian CLI desconectada.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** o arquivo de configuração certo é o que o botão abre ([[Obsidian CLI via MCP não carrega]]).
* **Ponto 2:** stdio no Claude, `--http` à parte para o MyHarness.
* **Ponto 3:** porta ocupada encerra o servidor com erro; troque com `--port`.

### 🔗 Conexões
- Mapa: [[MOC Programação]]
- Relacionadas: [[Servidor MCP da Obsidian CLI]], [[Obsidian CLI via MCP não carrega]]
