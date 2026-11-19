---
tipo: plano
funcionalidade: geral
status: aprovado
criado: 2026-11-19
---
# 🏗️ Proposta de arquitetura e stack — integrações, consumo, testes e protótipos

> [!tldr] Em uma linha
> Continuação da proposta (S25), aprovada em [[geral-decisao-2026-11-19-stack]]: como o app fala com Claude CLI, Obsidian CLI e GitHub, de onde vem o consumo, como se prova cada coisa e quais protótipos decidem o que falta.

Primeira parte: [[geral-plano-arquitetura-e-stack]]. Resumo e aval: [[geral-plano]].

### 5. 🔌 Integrações

| Integração | Proposta | Por quê | Alternativa |
|---|---|---|---|
| Claude CLI | Achar o executável, ler `claude --version` e o estado do login da própria CLI; se faltar, abrir o login da CLI (RF-01) | **S5 confirmado na proposta:** o Claude CLI usa o login dele; o app não guarda essa credencial | — |
| Obsidian CLI | Cliente MCP do servidor da Obsidian CLI que roda no Windows (no container, por HTTP em `host.docker.internal`); checar se o Obsidian está aberto e quantas notas responde (RF-02). Ponto de partida: `obsidian-cli-mcp.js` (no Vault), hoje stdio e só leitura, ganha transporte HTTP e escrita só para o orquestrador | **S5:** é local e exige o Obsidian aberto; sem OAuth | — |
| GitHub: login | OAuth com **device flow**: o app mostra um código, abre `github.com/login/device`, a pessoa digita e autoriza; o app consulta até o token sair | Feito para app sem servidor: **não precisa de segredo do app** guardado no programa. Precisa ligar o device flow nas configurações do app OAuth no GitHub. O código vale 15 minutos | Fluxo com navegador e porta local (precisa de segredo); ou reaproveitar o login do `gh` |
| GitHub: chamadas | `octocrab` (biblioteca Rust da API do GitHub) para PR e para saber quando o merge aconteceu (UC-10) | Tipado, mantido | `reqwest` direto |
| Git e worktrees | Chamar o `git` instalado (`git worktree add`, branch `tipo/ID-descricao`) | Mesmo comportamento que a pessoa vê no terminal; worktree é bem suportada pelo `git` | `git2`/`gitoxide` (bibliotecas, suporte a worktree mais limitado) |
| Credenciais | Cofre de credenciais do sistema pela biblioteca `keyring` do Rust: Gerenciador de Credenciais do Windows no app final; Secret Service (gnome-keyring) no container de desenvolvimento | É o "cofre do SO" que o RNF-05 pede; nenhum token em arquivo | Plugin Stronghold do Tauri (cofre cifrado **em arquivo** com senha: não atende "nunca em arquivo"); `tauri-plugin-keyring-store` (comunitário) |
| Navegador do adversarial | **S6:** Claude in Chrome pelo parâmetro `--chrome` do `claude -p`, tratado como recurso exclusivo (RN-15) | É o caminho que a especificação já supõe e existe na CLI | Servidor MCP de navegador (ex.: Playwright MCP) por `--mcp-config` |

🧪 **S6 precisa de protótipo (P3):** um agente sem contexto abrindo um endereço e completando um objetivo. Atenção: para testar **o próprio MyHarness**, o navegador não enxerga a janela do Tauri. Caminho provável: rodar a tela no navegador (Vite) com o núcleo simulado (o Tauri tem simulador de chamadas para teste), e, para a janela real, o `tauri-driver` (WebDriver). Ver dúvida 3.

### 6. 📊 Consumo do plano (S2)

| Fonte | O que dá | Situação |
|---|---|---|
| **Evento `rate_limit_event` no JSON do `claude -p`** | Situação da janela de 5 h e da semanal: % usado (`utilization`), hora do reinício (`resetsAt`), por janela | **Escolhida** ([[geral-decisao-2026-11-19-fonte-do-consumo]]). Chega de graça em toda execução; o P2 confirmou os campos |
| Barra de status (statusline) do Claude Code | JSON com `rate_limits.five_hour` e `rate_limits.seven_day` (% e reinício) | Só existe em sessão interativa; o harness usa `-p`. Serve para conferir |
| Registros locais de sessão da CLI | Tokens por mensagem | Plano B da especificação: estimar, sem o % oficial |

**S2 decidida** ([[geral-decisao-2026-11-19-fonte-do-consumo]]): ler o `rate_limit_event` de todas as execuções e guardar a última leitura no SQLite (Consumo). Sem agente rodando, o CMP-01 mostra a última leitura com a hora dela. Se o evento não trouxer o % (ex.: login por chave de API), cair para o plano B e marcar "estimado". O consumo **do chat** (RF-17) sai do campo `usage` de cada resposta, que é confiável. O P2 comparou 20 leituras com o `/usage` (RNF-04): batem.

### 7. 🧪 Testes e ferramentas

| Peça | Proposta | Por quê | Alternativa |
|---|---|---|---|
| Testes do núcleo | `cargo test` (unitário das RN no pacote `core`, sem Tauri) | Cada RN tem o seu teste; rápido | `cargo-nextest` (mais rápido em paralelo) |
| Suíte de tentativas proibidas (RNF-06) | Teste de integração que despacha cada papel contra o `claude -p` real e tenta: escrever no cofre, `git merge`, `push --force`, ler `.md` direto | É a prova de que a governança é código, não texto. Meta: 100% negadas | — |
| CLI falsa para carga | Um programa `fake-claude` que imita a saída JSON | Testa 6 agentes e 1.000 linhas por minuto (RNF-01, RNF-02) sem gastar tokens; testa queda de processo (RNF-07) | Usar a CLI real (caro e lento) |
| Testes da tela | Vitest + Testing Library, com o núcleo simulado | Componentes e estados (vazio, carregando, erro...) | — |
| Fluxo de ponta a ponta | Sem suíte no repositório: são os agentes de verificação ao fim de cada funcionalidade (Q04 e Q05, no Vault) | Regra do perfil projeto prático | — |
| Qualidade Rust | `cargo fmt` + `cargo clippy` (avisos viram erro) | Padrão do Rust | — |
| Qualidade TS | ESLint + Prettier + `tsc --noEmit` | Igual à Referência | Biome (uma ferramenta só, mais rápida) |
| Acessibilidade | `axe` nos testes da tela (RNF-12) | Contraste e rótulos | Só roteiro manual |
| Comando único de checagem | `pnpm check` (roda tudo acima) | Mesma prova para agente e humano ("Prova" do briefing) | `just` como orquestrador de tarefas |
| CI local | Gancho de git antes do push (`lefthook`) roda `pnpm check` | Projeto não é publicado; a prova roda na máquina | Só manual |
| CI no GitHub | GitHub Actions em `windows-latest` (plataforma final) e `ubuntu-latest` (o mesmo Linux do container), só checagem em PR (sem CD) | Mostra o ✔ no PR antes do merge do humano (S03) | Sem CI remoto: descartado em [[geral-decisao-2026-11-19-ci-no-github]] |
| Gerenciador de pacotes JS | `pnpm` | Rápido e rígido com dependências | `npm` |

### 8. 📁 Estrutura de pastas do repositório

```
my-harness/
├── docs/contrato/            contrato funcional (Q01): 00-requisitos a 08-criterios-de-aceite, mudancas.md
├── src/                      tela React (seção 1)
├── crates/
│   └── core/                 regras e casos de uso, sem Tauri
│       └── src/  domain/ (RN, papéis, permissões)  application/ (casos de uso)
├── src-tauri/
│   ├── src/
│   │   ├── commands/         ponte tela → casos de uso (um arquivo por feature)
│   │   ├── infra/            claude/ obsidian/ github/ git/ db/ secrets/ process/ mcp/
│   │   └── main.rs  lib.rs
│   ├── bin/harness-gate.rs   o portão chamado pelo gancho PreToolUse
│   ├── migrations/           SQL versionado
│   ├── capabilities/         permissões do Tauri (o que a tela pode chamar)
│   └── tests/                integração, incluindo a suíte de tentativas proibidas
├── tools/fake-claude/        CLI falsa para carga e queda
├── .github/workflows/ci.yml  só checagem (sem CD)
├── compose.yaml  docker/dev.Dockerfile  ambiente de desenvolvimento no WSL + Docker (já criado)
├── lefthook.yml  package.json  Cargo.toml (workspace)  README.md (com "Limites conhecidos", S18)
```
Nomes de arquivo em inglês e kebab-case (S12) onde a linguagem permite; em Rust, `snake_case`, que é a convenção da linguagem (exceção a registrar na decisão de estrutura).

### 9. 🧪 Protótipos antes de decidir

| # | O que testar | Decide | Pronto quando |
|---|---|---|---|
| P1 | Um subagente `claude -p` com as quatro camadas tenta escrever no cofre, `git merge`, `push --force` e ler `.md` direto | S3 × S4; custo do gancho por ferramenta | 100% negado, com log, e o gancho custa pouco (medir em ms) |
| P2 | Ler `rate_limit_event` em 20 execuções e comparar com o `/usage` | S2; RF-18 | % e hora do reinício batem com o `/usage` |
| P3 | Agente sem contexto, com `--chrome`, completa um objetivo numa página de teste; e a tela do MyHarness no navegador com núcleo simulado | S6; como validar o próprio app | Objetivo cumprido com captura; plano B testado se falhar |
| P4 | 6 `fake-claude` transmitindo ao mesmo tempo | RNF-01, RNF-02, RNF-03 | 95% dos eventos na tela em até 200 ms; nenhuma tarefa da tela acima de 50 ms |
| P5 | Do container, o cliente MCP alcança o servidor da Obsidian CLI no Windows por HTTP e busca em 3 cofres | RN-02, RN-30, RNF-14 | Até 3 s, cada nota com o cofre de origem |

### 10. ✅ Resultados dos protótipos (2026-11-19, no Windows do humano)

| # | Resultado | Prova |
|---|---|---|
| P1 | **Passou:** 8 de 8 tentativas no esperado. T1 a T4 (escrita no cofre, `git merge`, `push --force`, leitura de `.md`) negadas pelo `harness-gate` (camada 3); T5 (`git push` comum) pelo `dontAsk` (camada 2); T6 (`WebFetch`) sem a ferramenta (camada 1); T7 e T8 permitidas. Disco confere: nada no cofre, sem merge, remoto intacto. Gancho: mediana 8,6 ms internos, 56 ms com a partida do Node, máximo 155 ms. Nada pessoal carregado (sem MCP, skill, comando ou `CLAUDE.md`; só plugins `@builtin` do CLI) | `prototipos/p1-permissao/resultado-p1.txt` (CLI 2.1.328, haiku) |
| P2 | **Passou:** o `rate_limit_event` veio em 20 de 20 execuções, com `unifiedWindows.five_hour` e `unifiedWindows.seven_day` (`utilization`, `resetsAt`, `status`) e `overageStatus`. Leitura: 5 h com 71% e reinício às 15:00; semana com 11% e reinício em 26/11 às 06:00. O `/usage`, logo depois, mostrou 72% e 12%, com os mesmos reinícios (diferença de 1 ponto pela hora da leitura). Confirma a janela de 5 h (S1). Login: assinatura Claude Pro | `prototipos/p2-consumo/resultado-p2.txt` |
| P5 | **Passou no Windows:** 2 cofres em paralelo em 387 ms (limite 3 s), cada nota com o cofre de origem, as 4 ferramentas expostas, porta 27180. **Falta** a chamada a partir do container (`host.docker.internal`) | `prototipos/p5-ponte-mcp/resultado-p5.txt` |

Respostas às dúvidas do preparo: no Windows o agente usa a ferramenta `PowerShell` (o gate já a cobre); os ganchos de `--settings` rodam nesta máquina; `--setting-sources ""` não entrega o `CLAUDE.md` pessoal; a Obsidian CLI aceita chamadas em paralelo. O `claude -p` exige login próprio da CLI (`/login`): sem ele, sai com `authentication_failed`, e o P1 detecta.

### 🔗 Fontes consultadas (2026-11-19)
- Parâmetros do CLI: https://code.claude.com/docs/en/CLI-reference
- Permissões do Agent SDK (ordem de avaliação, modos, regras de negação): https://code.claude.com/docs/en/agent-sdk/permissions
- Ganchos do Agent SDK: https://code.claude.com/docs/en/agent-sdk/hooks
- Campos do JSON do `claude -p` (incluindo `rate_limit_event`), fonte não oficial: https://littlebearapps.com/help/untether/claude-stream-json-cheatsheet/
- Barra de status com limites 5 h e 7 dias, fonte não oficial: https://skoula.cz/blog/2026/6/how-to-display-context-and-5h-7d-limits-in-the-claude-code-status-bar/
- Node como sidecar no Tauri 2: https://v2.tauri.app/learn/sidecar-nodejs/
- Device flow do GitHub: https://docs.github.com/en/enterprise-server@3.19/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps
- Cofre de credenciais do SO no Tauri (plugin comunitário, para comparação): https://docs.rs/crate/tauri-plugin-keyring-store/0.1.5


### 🔗 Conexões
- Primeira parte: [[geral-plano-arquitetura-e-stack]]
- Resumo e aval: [[geral-plano]]
- Decisões dos protótipos: [[geral-decisao-2026-11-19-agente-por-claude-p]], [[geral-decisao-2026-11-19-fonte-do-consumo]]
- Projeto: [[geral-contexto]]
