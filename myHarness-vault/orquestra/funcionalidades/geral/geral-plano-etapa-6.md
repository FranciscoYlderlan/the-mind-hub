---
tipo: plano
funcionalidade: geral
status: aprovado
criado: 2026-11-27
---
# 📋 Etapa 6 — Consumo, logs, histórico e passagem de turno: tarefas

Base comum e lacunas em [[geral-plano-etapas-4-a-7]]. O leitor de eventos (B3) e o núcleo fatiado (B1) são da base comum.

- **AC da etapa:** consumo AC-104 a 106, 146, RNF-04; logs AC-61, 108, 109, 153, 156; historico AC-45 a 47, 110, 149, 150, RNF-08; passagem-de-turno AC-32 a 35, 80, 81, 107, 124.
- **E6-T5 consumo no núcleo** — observador de `RateLimit` grava o consumo (UTC, `origem=evento`), `ConsumoAtualizado`, status novo vira `desconhecido` com ERR-50; observador de `Uso` soma `chat.tokens_usados` e emite ERR-48 no limite — `servicos/consumo.rs` — B1, B3 — AC-80, 104, 105, 146; RNF-04 de 2 s no teste.
- **E6-T6 logs no núcleo** — início e fim da ferramenta, código de saída, saída mascarada, `LogRegistrado`, `listar_logs`, `registrar_log` público para as etapas 4 e 7 — `servicos/logs.rs` — B1, B2, B3 — AC-61, 108.
- **E6-T7 histórico e retomada** — `criar_projeto` (ERR-45, 46, 47, 52), listas com a cadeia de passagens, `abrir_chat` só leitura com ERR-33, projeto ativo, `rodando` vira `interrompida` ao abrir — `servicos/historico.rs`, `servicos/retomada.rs` — B1, B2 — AC-45 a 47, 110, 149, 150, RNF-08.
- **E6-T8 passagem de turno com portas falsas** — `aceitar_passagem` (ERR-07 aguarda), `PedirOndeParei`, valida ERR-29, `LerNota`, chat anterior `encerrado` e chat novo numa transação, `continuar_no_chat` com `RegistrarContinuacao` — `servicos/passagem.rs` — B1 — AC-32 a 35, 81, 107.
- **E6-T10 CMP-01 consumo** — `src/features/consumo/` — B4 — AC-105, 106, ERR-41, ERR-50.
- **E6-T11 CMP-07 inteira** (dona da barra do chat: percentual, alerta, ERR-48 com "Passar o turno" e "Continuar", "Novo chat" e limite) — `src/features/barra-do-chat/` — B4 — AC-104, 124, 151, 152. Depois, em série: **E6-T15** passagem na tela (AC-32, 34, 35).
- **E6-T12 CMP-08 logs ao vivo** — `src/features/logs/` — B4, B2 — AC-109.
- **E6-T13 CMP-09 histórico e projeto novo** — `src/features/historico/` — B4, B2 — AC-45 a 47, 110, 149, 150; NAV-02, NAV-20, NAV-22.
- **E6-T14 destino do ERR-53 e ERR-55** — `RegistroNoLog` com `origem=nucleo`, saída de erro como reserva — `integracoes.rs`, `src-tauri/src/lib.rs` — T6 — AC-153, 156.
- **E6-T16 ligação real** — portas da T8 no executor (E4-T4), no `read` da Obsidian CLI e na escrita do RF-28 (E5-T7); observadores no executor e no despacho — T8 e os merges das etapas 4 e 5 — AC-32, 107.
- **E6-T9 pesquisador** do Claude in Chrome e do plano B de MCP de navegador (S6), para a etapa 8 — fora do teto.
- **Prioridade:** T5, T6, T8, T11, T10; depois T7, T13, T12.

### 🔗 Conexões
- Plano conjunto: [[geral-plano-etapas-4-a-7]]
- Roteiro: [[geral-plano]]
- Projeto: [[geral-contexto]]
