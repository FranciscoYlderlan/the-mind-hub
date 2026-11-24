---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-24
substitui: 
---
# ✅ O MyHarness usa o servidor MCP da Obsidian CLI, melhorado

- **Proposta (plano):** dúvida da T2 do [[integracoes-plano]]: o `obsidian-cli-mcp.js` (no `Vault`, `Modelos/Orquestra/`) só expõe `obsidian_search`, `obsidian_read`, `obsidian_backlinks` e `obsidian_help` e não aceita conexão pela rede local; sem isso o número de notas indexadas (AC-128) não sai.
- **Decisão:** o app segue falando com a Obsidian CLI pelo servidor MCP ([[geral-decisao-2026-11-19-acesso-ao-obsidian]]); o servidor ganha uma ferramenta de listar arquivos com total (como `obsidian files ext=md total`) e transporte HTTP local, em que o cliente da T2 se conecta (`OBSIDIAN_MCP_URL`).
- **Alteração:** nenhuma.
- **Motivo:** resposta do humano em 2026-11-24: "Melhorar o servidor MCP".
- **Consequências:** tarefa nova T2b no [[integracoes-plano]]; o servidor mora no `Vault` e chega aos cofres por `cofre.py sincronizar`; a T2 só é verificada contra o servidor real depois da T2b.

### 🔗 Conexões
- Funcionalidade: [[integracoes-contexto]]
- Plano: [[integracoes-plano]]
- Decisão de origem: [[geral-decisao-2026-11-19-acesso-ao-obsidian]]
- Projeto: [[geral-contexto]]
