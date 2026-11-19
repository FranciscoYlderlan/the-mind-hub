---
tipo: plano
funcionalidade: geral
status: aprovado
criado: 2026-11-19
---
# ✅ Resultados dos protótipos P1 a P5

Parte de [[geral-plano-arquitetura-e-stack-integracoes-e-testes]] (seção 9 lista os protótipos). Resumo e aval: [[geral-plano]].

## Resultados (2026-11-19; no Windows do humano, salvo indicação)

| # | Resultado | Prova |
|---|---|---|
| P1 | **Passou:** 8 de 8 tentativas no esperado. T1 a T4 (escrita no cofre, `git merge`, `push --force`, leitura de `.md`) negadas pelo `harness-gate` (camada 3); T5 (`git push` comum) pelo `dontAsk` (camada 2); T6 (`WebFetch`) sem a ferramenta (camada 1); T7 e T8 permitidas. Disco confere: nada no cofre, sem merge, remoto intacto. Gancho: mediana 8,6 ms internos, 56 ms com a partida do Node, máximo 155 ms. Nada pessoal carregado (sem MCP, skill, comando ou `CLAUDE.md`; só plugins `@builtin` do CLI) | `prototipos/p1-permissao/resultado-p1.txt` (CLI 2.1.328, haiku) |
| P2 | **Passou:** o `rate_limit_event` veio em 20 de 20 execuções, com `unifiedWindows.five_hour` e `unifiedWindows.seven_day` (`utilization`, `resetsAt`, `status`) e `overageStatus`. Leitura: 5 h com 71% e reinício às 15:00; semana com 11% e reinício em 26/11 às 06:00. O `/usage`, logo depois, mostrou 72% e 12%, com os mesmos reinícios (diferença de 1 ponto pela hora da leitura). Confirma a janela de 5 h (S1). Login: assinatura Claude Pro | `prototipos/p2-consumo/resultado-p2.txt` |
| P3 (Chrome) | **Passou:** com `--chrome` e `--strict-mcp-config`, um agente sem contexto (sonnet) preencheu e enviou o formulário da página local, leu "Enviado: Maria Teste", e o servidor recebeu o envio; 11 turnos, 25 s, US$ 0,075. O `--strict-mcp-config` **não** tira o Chrome: o servidor `claude-in-chrome` entra como `dynamic`, com 20 ferramentas. | `prototipos/p3-chrome/resultado-p3.txt` |
| P3 (tela) | **Passou na máquina virtual (Linux):** (a) Vite com o próprio `vite.config.ts` e o simulador oficial `@tauri-apps/api/mocks` injetado, Playwright headless: 14 de 14, primeiro elemento em 455 a 929 ms; (b) binário de debug (build de 166 s) pelo `tauri-driver` 2.1.0 e `WebKitWebDriver` sob `xvfb-run`: 9 de 9, app aberto em cerca de 0,7 s, núcleo real respondeu `plugin:app|version` = `0.1.0`. Armadilhas: WebdriverIO pede BiDi (usar `wdio:enforceWebDriverClassic`) e não tem `executeAsync`. Uso: (a) é o padrão dos dois verificadores (o adversarial troca as respostas do mock); (b) só para o que a janela real mostra (comandos e eventos reais, capabilities, CSP, smoke final). **No Windows (2026-11-19, 16h03):** (a) passou, 14 de 14 com o Chrome do sistema (Vite em 840 ms, primeiro elemento em 1757 ms); (b) passou, 9 de 9, com `msedgedriver` 157.0.4341.60 (a versão do WebView2): driver em 364 ms, app aberto em 2558 ms, núcleo real `0.1.0`. No Windows a tela vem de `http://tauri.localhost/` (no Linux, `tauri://localhost`); o verificador deve aceitar os dois. O driver precisa da mesma versão do WebView2 (pasta `C:\Program Files (x86)\Microsoft\EdgeWebView\Application\`) e muda quando o WebView2 se atualiza | `prototipos/p3-tela/resultado-a.txt`, `resultado-b.txt` e `evidencia/` |
| P5 | **Passou no Windows:** 2 cofres em paralelo em 387 ms (limite 3 s), cada nota com o cofre de origem, as 4 ferramentas expostas, porta 27180. **Falta** a chamada a partir do container (`host.docker.internal`) | `prototipos/p5-ponte-mcp/resultado-p5.txt` |

Respostas às dúvidas do preparo: no Windows o agente usa a ferramenta `PowerShell` (o gate já a cobre); os ganchos de `--settings` rodam nesta máquina; `--setting-sources ""` não entrega o `CLAUDE.md` pessoal; a Obsidian CLI aceita chamadas em paralelo. O `claude -p` exige login próprio da CLI (`/login`): sem ele, sai com `authentication_failed`, e o P1 detecta.


### 🔗 Conexões
- Proposta: [[geral-plano-arquitetura-e-stack-integracoes-e-testes]]
- Decisões que saíram daqui: [[geral-decisao-2026-11-19-agente-por-claude-p]], [[geral-decisao-2026-11-19-fonte-do-consumo]], [[geral-decisao-2026-11-19-teste-da-tela]]
- Projeto: [[geral-contexto]]
- Plano: [[geral-plano]]
