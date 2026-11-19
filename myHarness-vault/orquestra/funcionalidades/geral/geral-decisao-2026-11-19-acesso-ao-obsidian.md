---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-19
substitui: 
---
# ✅ Acesso ao Obsidian via MCP

- **Proposta (plano):** [[geral-plano-arquitetura-e-stack-integracoes-e-testes]], linha "Obsidian CLI": o container de desenvolvimento não alcança a Obsidian CLI do Windows sem uma ponte.
- **Decisão:** o Obsidian roda no Windows, e o MyHarness o acessa **via MCP**.
- **Alteração:** nenhuma
- **Motivo:** resposta do humano em 2026-11-19.
- **Consequências:** a integração do Obsidian no núcleo é um cliente MCP, nunca a leitura direta dos `.md` (RN-02). No container, o servidor MCP da Obsidian CLI roda no Windows com transporte HTTP, alcançado em `OBSIDIAN_MCP_URL` (`host.docker.internal`). Faltam definir: a porta, o transporte no app final (HTTP ou stdio) e a ferramenta de escrita, só para o orquestrador (RN-01), que hoje não existe no `obsidian-cli-mcp.js` (no Vault, só leitura). O protótipo P5 prova a ponte.

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[geral-plano-arquitetura-e-stack]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
