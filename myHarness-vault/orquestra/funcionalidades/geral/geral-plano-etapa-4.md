---
tipo: plano
funcionalidade: geral
status: aprovado
criado: 2026-11-27
---
# 📋 Etapa 4 — Conversa com o orquestrador: tarefas

Base comum e lacunas em [[geral-plano-etapas-4-a-7]]. Formato curto: tarefa — faz — toca em — depende — AC. Toda tarefa: teste leve, `check:rapido` antes do push, `pnpm check` uma vez.

- **AC da etapa:** prompts-de-papel AC-48 a 52, 82 a 85, 118, 119, 140 a 142, RNF-13; modelos AC-36 a 38, 64, 100, 134 a 136; chat-orquestrador AC-06, 09, 10, 92, 94, 117, 122 (parcial), 125, 151, 152, RNF-01.
- **E4-T2 prompts no núcleo** — listar, versões, salvar versão nova, restaurar o padrão como versão nova, contagem, ERR-34/35 pelo parâmetro, aviso FA-02, `vigente(fluxo)` — `servicos/prompts.rs` — B1, B2 — AC-49 a 52, 83, 85, 118.
- **E4-T3 parâmetros e modelos no núcleo** — catálogo único de parâmetros (as etapas 6 a 8 acrescentam linhas), salvar na faixa, restaurar campo e tudo (cofres e pastas não mudam), modelos padrão por papel, ERR-30 — `servicos/configuracoes.rs`, catálogo — B1, B2 — AC-37, 38, 64, 135.
- **E4-T4 executor do agente** — abre o processo, usa o leitor B3, converte em `EventoExecucao`, cancela, `--include-partial-messages` e `--resume` na montagem — `crates/app/src/infra/agente/`, `chamada_claude.rs`, `execucao.rs` — B1, B3 — AC-92, RNF-01 no núcleo (p95 < 200 ms). **Dono único** do executor: a etapa 7 (E7-T5) acrescenta `cwd`, ambiente limpo e vigia de queda no mesmo módulo, em série.
- **E4-T6 TEL-06** — seções Prompts (CMP-16), Modelos (CMP-14) e Limites, campos gerados de `listar_parametros`, restaurar e botão geral com confirmação, simulado — `src/features/configuracoes/` — B1, B4 — AC-51, 52, 135, 136, 140 a 142.
- **E4-T7 chat no núcleo** — `novo_chat`, `definir_limite_chat`, `enviar_prompt` (ERR-05, ERR-11, ERR-36, Execução com `prompt_versao`, Log "prompt de papel vN", mensagens com `uso_tokens`, ERR-08 pausa, ERR-42), `abrir_chat`, `listar_chats` — `servicos/chat.rs` — B1, B2 (portas falsas) — AC-06, 09, 10, 82, 94, 119, 151, 152.
- **E4-T8 tela do chat** — CMP-04 (aba do orquestrador), CMP-06 (1 a 8 linhas, atalho, seletor de modelo, ERR-05), simulado com texto em pedaços — `src/features/chat/` — B1, B4 — AC-06, 09, 10, 92, 94, 117, 125. O CMP-07 é da etapa 6 (E6-T11).
- **E4-T9 ligação real e medição** — liga os serviços no `lib.rs`, `mcp-config` do orquestrador, caminho inteiro com a `fake-claude`, mede RNF-01 e RNF-13 — `src-tauri/src/lib.rs`, `crates/app/tests/etapa4.rs` — T2, T3, T4, T7, B5 — AC-36, 48, 82, 100, 119, 134.
- **Risco:** confirmar `--include-partial-messages` e `--resume` com a CLI real antes da E4-T4.

### 🔗 Conexões
- Plano conjunto: [[geral-plano-etapas-4-a-7]]
- Roteiro: [[geral-plano]]
- Projeto: [[geral-contexto]]
