---
tipo: plano
funcionalidade: geral
status: aprovado
criado: 2026-11-27
---
# 📋 Etapas 4 a 7 — plano conjunto

Proposta montada pelo orquestrador a partir de quatro pesquisadores (2026-11-27, 07h50 a 08h10), sobre a `main` `26923aa`. Etapas juntas e teto de 8 ([[geral-decisao-2026-11-27-etapas-4-a-7-juntas]]). Tarefas de cada etapa: [[geral-plano-etapa-4]], [[geral-plano-etapa-5]], [[geral-plano-etapa-6]], [[geral-plano-etapa-7]].

## Fatos do código (os quatro concordam)
- O trait `Nucleo` (`crates/app/src/nucleo.rs:41-151`), os comandos Tauri, os DTO e os eventos das etapas 4 a 7 já existem; o corpo devolve ERR-55 (`nao_implementado`).
- O `Database` é aberto em `src-tauri/src/lib.rs:21`, mas não entra no `NucleoMyHarness`.
- Não existe leitor de `stream-json`, executor do agente, `harness-gate` (o portão é obrigatório na montagem da chamada) nem `infra/git`.
- A tela só tem a TEL-02 e o cabeçalho; o núcleo simulado só cobre as integrações.
- Regerar os bindings compila o Tauri: só a base comum faz isso.

## Onda 0: base comum (G1), um dono por arquivo quente
Arquivos quentes: `nucleo.rs`, `dto.rs`, `erro.rs`, `src-tauri/src/{lib.rs,commands/}`, `src/bindings/`, `src/lib/ipc/esquemas.ts`, `main-window.tsx`, `src/dev/nucleo-simulado.ts`, `src/dev/cenarios.ts`, `Cargo.toml` da raiz e a numeração das migrações. Depois da onda 0, cada tarefa toca só a própria pasta.
- **B0 (orquestrador):** aplicar no contrato as lacunas aprovadas (M-52 em diante), antes do código.
- **B1 núcleo fatiado e IPC:** o núcleo recebe o `Database`; cada grupo do trait delega a um serviço em arquivo próprio (`crates/app/src/servicos/<area>.rs`, em stub); projeto atual provisório **sem cofre fixo** ([[geral-decisao-2026-11-27-cofre-do-app]]); todo DTO, comando, evento, ERR novo e zod das etapas 4 a 7 (`FluxoPrompt::Pesquisa`, `Parametro` e os 4 comandos de parâmetro, `PR`, `listar_prs`, `reordenar_prs`, `criar_cofre`, `anexar_cofre`, `EventoExecucao::Progresso`, `ComAvisos` no `salvar_prompt_papel`); bindings regenerados uma vez.
- **B2 migração única `0004`:** `prompt_papel` com `pesquisa` e sem o CHECK de 80 palavras; tabela `parametro` (nome, valor, padrão, mín, máx, ligado) no lugar de `configuracao`; `chat.sessao_cli`, `chat.criado_em`, `mensagem.criada_em`; `log.execucao` opcional, `origem`, `codigo_erro`; `pr` com execução, branch, número, url e ordem; `briefing.execucao`; `execucao.tokens_usados` e `etapa`; `tarefa.rotulo`; `ultimo_projeto`; 6 prompts de fábrica v1.
- **B3 leitor de eventos da CLI:** `crates/core/src/domain/evento_cli.rs` (Init, Texto em pedaços, FerramentaInicio, FerramentaFim, RateLimit, Uso, Resultado); trait `ObservadorExecucao`; `fake-claude` com cenários (normal, pedaços com atraso, morre, trava, tenta_push, relatório, rate limit).
- **B4 tela em espaços:** `main-window` em grade com um espaço por CMP (01, 02, 03, 04, 06, 07, 08, 09) e botão Configurações; TEL-06 vazia com seções; núcleo simulado e cenários compostos por um arquivo por funcionalidade.
- **B5 `harness-gate`:** `tools/harness-gate/` e a política por papel em `crates/core/src/domain/politica.rs`; nega por padrão; suíte RNF-06 por tabela papel × tentativa.
- Paralelo: B1+B2 num implementador só (mesmos arquivos); B3, B4 e B5 em paralelo com ele.

## Regra para todo briefing de código
No app, **todos os agentes leem** o Obsidian pela Obsidian CLI via MCP e **só o orquestrador escreve** ([[geral-decisao-2026-11-27-cofre-do-app]]). Vale para B5 (política por papel), E5-T7, E5-T8 e E7-T10.

## Lacunas aprovadas pelo humano (2026-11-27, cerca de 07h50)
Aprovadas em bloco, menos o projeto provisório com o `myHarness-vault`, trocado pela [[geral-decisao-2026-11-27-cofre-do-app]]. Ainda não aplicadas no contrato (B0).
- **Etapa 4:** 6 fluxos de prompt com `pesquisa`; ENT-22 vira tabela de parâmetros, RF e ERR novos de faixa; limite do chat de 100 mil a 400 mil, padrão 100 mil, mesma faixa no CMP-07 (AC-151 e AC-152 reescritos); CMP-14 vira seção da TEL-06 e o seletor do CMP-06 não navega; modelos padrão `opus` no orquestrador e `sonnet` nos demais; palavras 80 (20 a 150, por espaço); tokens 150 (50 a 300, só aviso, caracteres ÷ 4); lista fixa de modelos `opus`, `sonnet`, `haiku` como parâmetro; `sessao_cli` com `--resume`; prompt de papel por `--append-system-prompt`; AC-122 parcial até a etapa 5; textos dos ERR redigidos pelo orquestrador.
- **Etapa 5:** `obsidian_vaults`, `obsidian_create` e `obsidian_append` no `obsidian-cli-mcp.js`, escrita só para o orquestrador; agentes leem o Obsidian só pelo proxy MCP do MyHarness; contrato do "Criar novo cofre" e do anexar (RF-35, UC-15, ERR e AC novos); caminho do `Vault` e do `python` como parâmetros; RN-02 com regra e aviso na etapa 5 e bloqueio no portão da etapa 7; textos do ERR-18 e do ERR-39; RNF-14 real no teste do humano.
- **Etapa 6:** `log.execucao` opcional com `origem` e `codigo_erro` (destino do ERR-53 e ERR-55); `chat.criado_em` e rótulo por data e primeira mensagem; "Onde parei" em bloco estruturado validado pelo núcleo; a linha de continuação gravada pelo núcleo como Escrita (exceção ao RN-01); refazer depois do ERR-29: 2 (1 a 5); RNF-04 com 3 pontos de tolerância; plano B "estimado" como limite registrado; alerta do CMP-07 a 80% (50 a 95); código de saída por "Exit code N" ou `is_error`; `ultimo_projeto`; CMP-01 sem botão no erro.
- **Etapa 7:** plano em bloco ```` ```plano-myharness ```` com JSON e relatório em ```` ```relatorio-myharness ````, formato no CLAUDE.md gerado; CMP-18 "Entregas" na TEL-01, merge consultado a cada 60 s (parâmetro); por plano, mínimo 0 e máximo sem limite, mínimo de teste só com tarefa de funcionalidade; ERR novo de plano fora da faixa por tipo; RN-13, ENT-07, ENT-22 e ERR-44 reescritos para os tipos; "parado" depois do silêncio segue `rodando` com aviso; RNF-10 com estimativa e 3 despachos reais no teste do humano.

## Ordem e prioridade
1. B0 e a onda 0 (B1+B2, B3, B4, B5).
2. Onda 1: tarefas de núcleo e de tela das quatro etapas, até 8 ao mesmo tempo, na prioridade: etapa 4 e etapa 7 (exigidas completas) → etapa 6 essenciais → etapa 5.
3. Onda 2: ligações reais e medições; verificadores de fluxo principal e adversariais por funcionalidade.

### 🔗 Conexões
- Decisões: [[geral-decisao-2026-11-27-etapas-4-a-7-juntas]], [[geral-decisao-2026-11-27-cofre-do-app]]
- Etapas: [[geral-plano-etapa-4]], [[geral-plano-etapa-5]], [[geral-plano-etapa-6]], [[geral-plano-etapa-7]]
- Roteiro: [[geral-plano]]
- Projeto: [[geral-contexto]]
