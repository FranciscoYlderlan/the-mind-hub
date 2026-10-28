---
tipo: plano
funcionalidade: geral
status: aprovado
criado: 2026-11-19
---
# 🏗️ Proposta de arquitetura e stack — tela, núcleo, banco e agentes

> [!tldr] Em uma linha
> Proposta da IA (S25), aprovada em [[geral-decisao-2026-11-19-stack]]: a tela React só mostra e pede; o núcleo Rust decide tudo; cada agente é um `claude -p` aberto pelo núcleo com as permissões do papel.

Resumo e campos de aval: seção "Proposta de arquitetura e stack" do [[geral-plano]]. Integrações, consumo, testes, pastas e protótipos: [[geral-plano-arquitetura-e-stack-integracoes-e-testes]].

> [!info] Como ler
> Cada escolha diz **o quê**, **por quê** e **alternativa**. O que está marcado 🧪 **protótipo** só vira decisão depois de um teste curto (lista no fim). Já decidido na especificação: app desktop Tauri + Rust + React, SQLite local em modo WAL, memória nos `.md` do Obsidian lida pela Obsidian CLI. Projeto local (não publicado), uma pessoa, desenvolvido no WSL + Docker, com o app final rodando no Windows: S04 a S08 e S24 não se aplicam.

**Ideia geral, numa frase:** a tela (React) só mostra e pede; o núcleo (Rust) decide tudo, inclusive o que cada agente pode fazer; cada agente é um processo do Claude CLI que o núcleo abre já "de mãos amarradas" para o seu papel.


### 1. 🖥️ Frontend (a tela)

| Peça | Proposta | Por quê | Alternativa |
|---|---|---|---|
| Base | React + Vite + TypeScript | Já decidido; é o padrão do `create-tauri-app` e da Referência | — |
| Estilo e componentes | Tailwind + shadcn/ui (só pela CLI, S11) | Igual à Referência; tema claro e escuro prontos ajudam no contraste do RNF-12 | Mantine ou Radix puro |
| Rotas | **Nenhuma no começo** | É uma janela só (TEL-01) com painéis e diálogos por cima; rota de URL não ajuda aqui | TanStack Router, se as telas crescerem |
| Falar com o núcleo | Comandos do Tauri (`invoke`) envolvidos em TanStack Query | Guarda em cache e recarrega sozinho; mesma ideia da Referência | Chamar `invoke` direto |
| Saída ao vivo dos agentes | Canais (`Channel`) do Tauri, um por execução | Entregam os eventos em ordem e rápido (RNF-01: até 200 ms) | Eventos globais do Tauri (mais simples, menos controle) |
| Terminal com abas | Lista virtualizada (TanStack Virtual) que desenha só as linhas visíveis | A saída chega como JSON já separado, não como terminal cru; desenhar só o visível mantém a tela fluida com 6 agentes (RNF-02) | xterm.js (terminal "de verdade", mais pesado e sem estrutura) |
| Estado de tela | Zustand | Aba ativa, painel aberto, filtros. Nunca guarda dado do núcleo | Só React Context |
| Validação | zod em todo campo (S26) e nos eventos que chegam do núcleo | Campo de prompt de papel (80 palavras, RN-26), limite do chat, pasta de contexto | — |
| Tipos iguais nos dois lados | Tipos TypeScript gerados a partir do Rust (`tauri-specta`) | Se o núcleo muda um campo, a tela não compila; evita erro silencioso | Escrever os tipos à mão |
| Atalhos de teclado | Biblioteca pequena de atalhos (ex.: `react-hotkeys-hook`) | RNF-12: enviar, novo chat, trocar aba, aprovar plano | Código próprio |

Pastas (`src/`), na mesma lógica da Referência:
```
src/
├── app/          providers (queryClient, tema) e a janela TEL-01
├── features/<f>/ chat, plano, agentes, contexto, consumo, logs, historico,
│                 integracoes, modelos, configuracoes, achados
│                 (cada uma: api, components, hooks, schemas, types; acesso só pelo index.ts)
├── components/   ui/ (só shadcn), layout/, common/
├── bindings/     tipos gerados do Rust (nunca editar à mão)
├── hooks/  lib/  stores/  styles/
```
Direção: `app → features → components / hooks / lib`; uma feature não importa outra (S13).

### 2. ⚙️ Backend (o núcleo em Rust)

| Peça | Proposta | Por quê | Alternativa |
|---|---|---|---|
| Base | Tauri 2 + Rust + `tokio` | Já decidido; `tokio` cuida de muitos processos e fluxos ao mesmo tempo | — |
| Organização | Dois pacotes Rust: `core` (regras e casos de uso, **sem** Tauri) e `src-tauri` (a ponte com a tela e as integrações) | As 30 RN ficam testáveis sem abrir janela; o núcleo "impõe" as regras num lugar só | Um pacote só, com pastas |
| Camadas | `domain` (RN, papéis, permissões por papel) → `application` (despachar, aprovar plano, passagem de turno) → `infra` (Claude, Obsidian, GitHub, git, banco, segredos) | Mesma ideia da Clean Architecture da Referência; a regra não conhece a ferramenta | — |
| Integrações | Uma interface (`trait`) por integração: `AgentRunner`, `VaultCli`, `GitHost`, `SecretStore` | RNF-11: integração nova sem mexer em regra nem tela; permite trocar S3 por S4 sem reescrever o resto | — |
| Erros | Erro com código próprio (`thiserror`), igual ao S15 | A tela mostra a mensagem certa; o teste confere o código | `anyhow` (mais solto) |
| Processos dos agentes | `tokio::process` + grupo de processos do sistema (Job Object no Windows, grupo de processos no Linux) | Fechar o app derruba todos os agentes juntos; nenhum fica órfão; queda detectada em até 5 s (RNF-07) | Matar um por um |
| Máscara de segredo | Um único "gravador" de texto que mascara tokens antes de ir ao banco, ao log ou ao cofre | RN-04 e RNF-05 num ponto só | Mascarar em cada lugar (fácil esquecer) |

### 3. 🗄️ Banco

| Peça | Proposta | Por quê | Alternativa |
|---|---|---|---|
| Banco | SQLite em modo WAL (já decidido) | Um arquivo local; WAL não perde o que já foi confirmado se o app cair (RNF-08) | — |
| Acesso | `sqlx` com migrações versionadas no repositório | Confere as consultas na compilação; migração roda sozinha ao abrir | `rusqlite` + `refinery` (mais simples, síncrono) |
| Quem acessa | **Só o núcleo Rust**. A tela nunca fala com o banco | Se a tela gravasse direto, a regra poderia ser pulada | `tauri-plugin-sql` (deixa a tela acessar: não recomendado aqui) |
| Ao reabrir | Execução que estava "rodando" vira "interrompida" | Pedido do RNF-08 | — |

### 4. 🤖 Como cada agente roda (S3 × S4)

**O que é cada opção:**
- **S3, `claude -p` direto:** o núcleo Rust abre um processo do Claude CLI por agente e lê a saída em JSON linha a linha (`--output-format stream-json`). Tudo que o papel pode fazer vai por parâmetro: modelo (`--model`), ferramentas (`--tools`, `--allowedTools`, `--disallowedTools`), pastas extras (`--add-dir`), prompt de papel (`--append-system-prompt`), modo de permissão (`--permission-mode`), servidores MCP (`--mcp-config` com `--strict-mcp-config`) e ganchos (hooks) por `--settings`.
- **S4, Agent SDK num processo Node:** um programa Node, empacotado como "sidecar" do Tauri, usa a biblioteca do Claude Code. As regras de permissão viram funções em código (`PreToolUse`, `canUseTool`) rodando dentro do mesmo processo. O Rust conversa com esse Node por entrada e saída padrão.

**Comparação para impor permissão por papel (RNF-06):**

| Critério | S3 `claude -p` | S4 Agent SDK (Node) |
|---|---|---|
| Regra de "não pode" | Regra de negação (`--disallowedTools`) vale em todo modo, até no mais solto; nome sozinho (ex.: `Edit`) some da lista do agente | Igual (as mesmas regras), mais funções em código |
| Regra fina (caminho, comando) | Gancho `PreToolUse` que roda um programa pequeno nosso (`harness-gate`), que pergunta ao núcleo e responde "nega" com motivo | Função em código, no mesmo processo: mais rápida e mais fácil de testar |
| Onde a regra mora | No Rust, como a especificação pede ("o núcleo Rust impõe") | Parte da regra passa para o Node: dois lugares para manter |
| Peças a mais | Nenhuma além do Claude CLI | Node empacotado (arquivo maior), ponte Rust ↔ Node, segunda linguagem |
| Ler a saída | Nós lemos o JSON linha a linha | Mensagens já com tipo |
| Risco | Gancho por programa externo custa um pouco a cada ferramenta usada; precisa medir | Mais uma camada que pode cair; versão do SDK e do CLI precisam andar juntas |

**Recomendação: S3**, com permissão em quatro camadas, para que nenhuma dependa só do texto do prompt (RN-27):
1. **Ferramentas por papel:** o núcleo monta a lista de cada papel. O que o papel não pode, nem aparece para ele (`--disallowedTools` com nome sozinho).
2. **Negar por padrão:** `--permission-mode dontAsk` com só as permissões do papel em `--allowedTools`. O que não está na lista é negado, sem perguntar a ninguém (RN-12: subagente não pergunta).
3. **Portão por gancho:** `PreToolUse` chama o `harness-gate`, que confere com o núcleo, pela execução, o papel e o caminho: escrita em `orquestra/` ou em qualquer cofre (RN-01, RN-29), `git merge`, `push --force`, push na `main` (RN-17). Cada negação vira log "escrita negada: papel sem permissão".
4. **Sem a chave, sem o estrago:** o subagente **não recebe o token do GitHub**. Quem faz push e abre o PR é o núcleo (RF-27), com o token do cofre de credenciais do sistema. Mesmo que um comando escape, não há credencial para fazer merge. Somar a proteção da `main` no próprio GitHub (merge só por PR).

Detalhes que completam:
- **Prompt de papel antes de tudo (RN-25):** vai em `--append-system-prompt`, com a versão gravada na execução (RN-28).
- **Configuração pessoal não vaza para o papel:** carregar só as fontes de configuração que o núcleo escolher (`--setting-sources`) e só os MCP dele (`--strict-mcp-config`). O P1 confirmou `--setting-sources ""` com `--settings` do papel: nada pessoal carregado.
- **Leitura do cofre pela CLI (RN-02):** o núcleo fala com o Obsidian, que roda no Windows, só via MCP (servidor da Obsidian CLI). No container de desenvolvimento, o transporte é HTTP em `OBSIDIAN_MCP_URL`; no app final no Windows, o mesmo cliente MCP, local [a confirmar: HTTP ou stdio]. Para os agentes, o núcleo oferece um servidor MCP próprio (`obsidian_search`, `obsidian_read`; `obsidian_write` só para o orquestrador). Ele repete a busca em todos os cofres ativos e marca a origem (RN-30, RF-34) e já registra a leitura para a aba "Obsidian usado" (RF-14). Ler `.md` do cofre direto fica negado por regra de caminho.
- **S4 fora do plano:** o P1 aprovou a S3 ([[geral-decisao-2026-11-19-agente-por-claude-p]]). O `AgentRunner` segue atrás de uma interface, então uma troca futura não mexe nas regras nem nas telas.

✅ **Protótipo P1** decidiu S3 × S4: S3.


### 🔗 Conexões
- Resumo e aval: [[geral-plano]]
- Continuação: [[geral-plano-arquitetura-e-stack-integracoes-e-testes]]
- Projeto: [[geral-contexto]]
