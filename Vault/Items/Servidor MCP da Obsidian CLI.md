---
aliases: [obsidian-cli-mcp, Obsidian CLI MCP server, Ponte MCP do Obsidian, MCP que lê o cofre]
tags: [ferramentas/obsidian, estudos/programacao]
tipo: conceito
status: rascunho
criado: 2026-11-24
origem: T2b do integracoes-plano (myHarness-vault), 2026-11-24; arquivo Modelos/Orquestra/obsidian-cli-mcp.js
---
# 🔌 Servidor MCP da Obsidian CLI

> [!tldr] Em uma linha
> Um programa Node pequeno que repassa a Obsidian CLI do Windows para o Claude e para o MyHarness, só para ler.

É o **interfone do prédio**: o Claude na nuvem não entra no meu Windows, mas toca o interfone e o porteiro (o servidor) chama a [[Obsidian CLI via MCP não carrega|Obsidian CLI]] por ele. O arquivo mora em `Modelos/Orquestra/obsidian-cli-mcp.js`, sem dependência nenhuma. Como ligar: [[Ligar o servidor MCP da Obsidian CLI]].

> [!note] Como funciona
> 1. Cada ferramenta vira um comando `obsidian vault=X ...`, com até 30 s de espera.
> 2. Ferramentas: `obsidian_search` (`query`, `limit`, `path`, `context`), `obsidian_read` e `obsidian_backlinks` (`file` ou `path`), `obsidian_files` (`folder`, `ext`, `total`) e `obsidian_help`.
> 3. `vault` é opcional em todas; o padrão vem de `OBSIDIAN_VAULT`. O executável vem de `OBSIDIAN_BIN`.
> 4. Erro da CLI volta como `isError` com o texto dela.
> 5. Transporte padrão: stdio, o que o Claude desktop usa.
> 6. Com `--http`: HTTP do MCP só em `127.0.0.1`, `POST /mcp`, porta `--port`, `OBSIDIAN_MCP_PORT` ou 27180, sessão por `Mcp-Session-Id`; o MyHarness usa este.

> [!warning] Limites
> - Só leitura: não há ferramenta de escrita.
> - Precisa do Obsidian aberto; logo depois de abrir, `Command "read" not found` é carregamento.
> - HTTP sem TLS e só local; [a confirmar] se o container alcança o `127.0.0.1` do Windows.
> - `files ext=md total` devolve só o número (75 no `Vault` em 2026-11-24, igual à contagem dos `.md` na pasta).

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** é a ponte entre a nuvem e a CLI do Windows; o bug clássico dela está em [[Obsidian CLI via MCP não carrega]].
* **Ponto 2:** a versão 1.1.0 trouxe `obsidian_files` (total de notas) e o modo `--http`, sem mudar o stdio.
* **Ponto 3:** `--http` é um segundo processo; nunca na entrada do Claude desktop, que fala por stdio.

### 🔗 Conexões
- Mapa: [[MOC Programação]]
- Relacionadas: [[Obsidian CLI via MCP não carrega]], [[Manual da Orquestra]]
- Próxima: [[Ligar o servidor MCP da Obsidian CLI]]

## 🕓 Histórico
- 1.0.0 (2026-10-28): stdio, com search, read, backlinks e help.
- 1.1.0 (2026-11-24): `obsidian_files` e transporte HTTP local (`--http`), para o MyHarness contar as notas.
