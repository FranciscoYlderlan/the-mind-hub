---
tipo: bug
funcionalidade: geral
status: resolvido
criado: 2026-10-28
aliases: [Ferramentas obsidian_ não aparecem, Nenhum servidor adicionado no Claude Desktop, Busca sem a Obsidian CLI, The CLI is unable to find Obsidian]
---
# 🐞 Obsidian CLI via MCP não carrega

> [!tldr] Em uma linha
> As sessões do StoneBid buscavam sem a Obsidian CLI porque o Claude Desktop lia a config MCP num caminho diferente do esperado. A lição geral está na nota "Obsidian CLI via MCP não carrega" (no Vault).

## Contexto
- O `CLAUDE.md` deste cofre manda buscar **pela Obsidian CLI** (`obsidian vault="stonebid-vault" ...`).
- O orquestrador roda na nuvem, ligado ao Windows do humano. O shell da sessão é uma VM Linux que só monta as pastas conectadas: não alcança o app do Obsidian.
- A CLI chega à sessão pelo servidor MCP local `obsidian-cli` (`Vault/Modelos/Orquestra/obsidian-cli-mcp.js`), configurado no Claude Desktop e repassado pela ponte. Ferramentas: `obsidian_search`, `obsidian_read`, `obsidian_backlinks`, `obsidian_help`.

## Sintoma
- Esperado: ferramentas `obsidian_*` na sessão.
- Observado: nenhuma ferramenta do Obsidian, `obsidian` inexistente no shell e "Nenhum servidor adicionado" em Configurações → Desenvolvedor do Claude Desktop.

## Impacto
- As buscas do [[diario-2026-10-28]] foram feitas direto nos `.md`, sem o índice de aliases e backlinks do app. Risco: perder decisões ou bugs que só seriam achados por alias.

## Hipóteses
(as descartadas ficam, com o motivo)
1. ❌ O shell da sessão roda a CLI: VM Linux, sem acesso a executáveis do Windows.
2. ❌ CLI desativada no Obsidian: estava ligada (Configurações → Sobre → Avançado), Obsidian 1.14.5.
3. ⚠️ Obsidian fechado: real ("The CLI is unable to find Obsidian"), mas secundário.
4. ❌ Servidor quebrado: o teste por stdio respondeu `initialize`, `tools/list`, busca e backlinks.
5. ❌ Config em `%APPDATA%\Claude`: o app não leu.
6. ❌ Config na pasta do pacote da Microsoft Store (`Packages\Claude_pzs8sxrjxfjjc`): abandonada pelo app (marcador `.user-data-left`).
7. ✅ O app lê `%LOCALAPPDATA%\Claude-Data\claude_pzs8sxrjxfjjc\claude_desktop_config.json`.

## Linha do tempo técnica
(2026-10-28)
- 21:57: sessão sem MCP do Obsidian e sem CLI no shell.
- 22:07–22:18: setup por script; Obsidian aberto e CLI OK no Windows.
- 22:20: servidor testado por stdio: OK.
- 22:22: tela Desenvolvedor vazia.
- 22:24: "Editar configuração" revela o caminho `Claude-Data`.
- 22:26: `obsidian-cli` "Em execução" e ferramentas disponíveis na sessão.

## Pseudocódigo do problema
```
app.iniciar():    servidores = ler(Claude-Data\claude_<id>\claude_desktop_config.json)   # sem obsidian-cli
sessão.iniciar(): ferramentas += ponte.repassar(servidores)                               # nenhuma obsidian_*
orquestrador:     sem CLI -> busca nos .md deste cofre, sem índice
```

## Testes feitos
- `which obsidian` no shell da sessão: vazio.
- PowerShell no Windows: `obsidian version` e `obsidian vault="stonebid-vault" search query="lance"`.
- Teste do `obsidian-cli-mcp.js` por stdio (JSON-RPC).
- Tela Configurações → Desenvolvedor após cada mudança.

## Evidências encontradas
- "Editar configuração" abriu `C:\Users\Ylderlan\AppData\Local\Claude-Data\claude_pzs8sxrjxfjjc`.
- Gravada a entrada ali e reiniciado o app pela bandeja: `obsidian-cli` "Em execução".
- `obsidian_search` com `vault="stonebid-vault"` e `query="lance"` devolveu [[manual-da-orquestra]] e [[geral-contexto]].

## Correção aplicada
- Entrada `obsidian-cli` (`node` + caminho do `obsidian-cli-mcp.js`, `OBSIDIAN_BIN` = `C:\Program Files\Obsidian\Obsidian.com`) gravada no arquivo real, com backup e sem BOM. JSON completo na nota do Vault.

## Solução
- Achar a config **sempre** por Configurações → Desenvolvedor → "Editar configuração".
- Reiniciar o Claude Desktop saindo pela bandeja, com o Obsidian aberto, e abrir um chat novo.
- Regra de busca reforçada no `CLAUDE.md` (via `Modelo de CLAUDE do cofre` e `cofre.py sincronizar`): CLI obrigatória; falhou, reportar ao humano e analisar com esta nota antes de buscar nos `.md`.

## Como validar que não voltou
- Início de sessão: `obsidian_search` com `vault="stonebid-vault"` devolve notas.
- Tela Desenvolvedor: `obsidian-cli` "Em execução".

## Logs que deveriam existir
- "Ver registros" do `obsidian-cli` na tela Desenvolvedor.
- Linha de início no stderr do servidor com `OBSIDIAN_BIN` e a versão da CLI (melhoria sugerida) [a confirmar].

## O que aprendi
- O arquivo de config certo é o que o app abre, não o da documentação.
- Busca sem CLI tem que ser avisada e, antes, investigada: ela esconde um problema de ambiente.

> [!tip] Teste de utilidade
> Sem abrir o código, dá para entender: esperado vs. observado, hipóteses descartadas, o que provou a causa raiz, a correção e como validar? Diagramas `mermaid` são bem-vindos.

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Decisões: (nenhuma)
- Outros bugs: (nenhum)
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
- Sessão: [[diario-2026-10-28]]
- Lição geral: "Obsidian CLI via MCP não carrega" (no Vault)
