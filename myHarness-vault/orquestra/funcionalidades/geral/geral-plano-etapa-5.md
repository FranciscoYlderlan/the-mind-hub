---
tipo: plano
funcionalidade: geral
status: aprovado
criado: 2026-11-27
---
# 📋 Etapa 5 — Memória, contexto e vários cofres: tarefas

Base comum e lacunas em [[geral-plano-etapas-4-a-7]]; cofre do app em [[geral-decisao-2026-11-27-cofre-do-app]].

- **AC da etapa:** memoria AC-16 (parte), 58, 84 (parte), 86, 115, 147, 148, 155, ERR-13, 15, 39; contexto-de-leitura AC-42 a 44, 59, 87, 101 a 103, ERR-18, 32, 40; cofres-do-projeto AC-53 a 57, 120, 121, 143, ERR-37, 38, 40, RNF-14; criar e anexar cofre: AC novos da B0.
- **Já existe:** tabelas `cofre`, `leitura`, `pasta_contexto`, `escrita` (gatilho do ERR-39); trait `VaultSide` sem implementação real; `ObsidianCli::checar` num cofre só, por `MYHARNESS_OBSIDIAN_COFRE` (sai nesta etapa); `--add-dir` e `--mcp-config` na montagem.
- **E5-T1 regras de memória e leitura** — `decidir_escrita` (ERR-13 também para `Anexos/contrato/` e `docs/contrato/`, ERR-39) e `decidir_leitura` (ERR-18, sem CLI) — `crates/core/src/domain/memoria.rs` — nenhuma — AC-58, 59, 84, 86. Junto: **E5-T5** leituras a partir do `tool_use` (`domain/leitura.rs`, aviso ERR-18).
- **E5-T2 cofres do projeto** — listar, **criar** e **anexar**, ligar testando uma busca (ERR-37), primeiro vira memória, trocar função numa transação (ERR-38), ativar, desativar, testar; a integração Obsidian checa o cofre de memória do projeto; conectar o MCP da Obsidian CLI — `servicos/cofres/`, `integracoes.rs` (só o cofre), `.env.example` — B1 — AC-54 a 57, 120, 143.
- **E5-T3 ferramentas novas no `obsidian-cli-mcp.js`** (no `Vault`) — `obsidian_vaults`, `obsidian_create`, `obsidian_append` — o implementador devolve a mudança e o orquestrador aplica e roda `cofre.py sincronizar` — nenhuma.
- **E5-T4 pastas em contexto e leituras** — adicionar e remover pasta (ERR-32), `pastas_para_execucao`, `registrar_leitura` com `LeituraRegistrada`, `listar_leituras` — `servicos/contexto/` — B1 — AC-42 a 44, 101, 103.
- **E5-T6 busca em vários cofres** — busca e leitura em paralelo nos cofres ativos, com tempo limite e origem; sem origem vai ao log (ERR-40) — `servicos/cofres/busca.rs`, `servidor_falso.rs` — nenhuma — AC-53, 55, 87, 121, RNF-14 com o falso.
- **E5-T7 escrita no cofre de memória** — `GravadorDeNotas` implementa o `VaultSide` por `obsidian_create`, com desfazer; passa por `decidir_escrita` e grava o ENT-17 — `servicos/memoria/` — B1, T1, formato da T3 — AC-86, 115, 147.
- **E5-T11 criar cofre no núcleo** — roda `cofre.py criar` e `verificar`, saída mascarada, ERR novos — `servicos/cofres/criar.rs`, `tools/fake-cofre-py/` — B1, B0.
- **E5-T8 proxy MCP do MyHarness** — servidor local por execução com busca e leitura (T6), registro de leitura (T4), escrita só para o orquestrador (T7); gera o `mcp_config` — `crates/app/src/infra/mcp_proxy/` — T4, T6, T7 — AC-59, 86, 102.
- **E5-T9 CMP-02 painel de contexto** e **E5-T10 CMP-17 cofres na TEL-06** (criar, anexar, conectar MCP) — `src/features/contexto/`, `src/features/cofres/` — B4 — AC-44, 87, 101, 102; AC-54 a 57, 120, 143.
- **Riscos:** cofre recém-criado só aparece na CLI depois de aberto no Obsidian (ERR-37 logo depois) `[a confirmar]`; a CLI por processo pode passar dos 3 s do RNF-14.

### 🔗 Conexões
- Plano conjunto: [[geral-plano-etapas-4-a-7]]
- Roteiro: [[geral-plano]]
- Projeto: [[geral-contexto]]
