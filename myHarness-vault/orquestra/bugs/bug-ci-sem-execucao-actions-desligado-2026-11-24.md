---
tipo: bug
funcionalidade: geral
status: resolvido
criado: 2026-11-24
aliases: [CI sem execução, Actions desligado, Workflows aren't being run]
---
# 🐞 CI nunca rodou: Actions desligado no repositório

## Contexto
O `MyHarness` tem o workflow `CI` (`.github/workflows/ci.yml`, em `pull_request` e `push` na `main`), ativo segundo a API ([[geral-decisao-2026-11-19-ci-no-github]], [[geral-decisao-2026-11-19-gatilho-do-ci]]).

## Sintoma
- Esperado: cada push e cada PR (#1 a #7) disparam o `CI`.
- Observado (2026-11-23 e 2026-11-24): a API mostrava o workflow `active` e `total_count: 0` execuções.

## Impacto
Nenhuma PR da etapa 2 passou pelo `CI` no GitHub (Linux e Windows); só pelo `pnpm check` local dos agentes. Os testes `#[cfg(windows)]` nunca rodaram.

## Hipóteses
- Workflow com erro de sintaxe: descartada; o arquivo aparece como `active` e o GitHub lista o `CI`.
- Permissão de Actions restrita: descartada; `Settings → Actions → General` estava em "Allow all actions and reusable workflows".
- Actions desligado no próprio repositório (causa): a aba **Actions** mostrava "Workflows aren't being run on this repository — GitHub Actions is not currently enabled on this repository", com o botão "Enable Actions on this repository". Por que veio desligado [a confirmar]; a página de Settings não mostra isso.

## Linha do tempo técnica
- 2026-11-23: push da `main` e das branches; PRs #1 a #7; 0 execuções.
- 2026-11-24 07h45: pelo Chrome (Claude in Chrome), com o pedido do humano, o orquestrador abriu a aba Actions e clicou "Enable Actions on this repository"; o GitHub respondeu "Actions Enabled.".
- 2026-11-24 07h58: primeira execução, na PR #8, falhou nos dois sistemas por erros que já estavam na `main` e nunca tinham passado pelo `CI`: no Linux, o clippy do Rust estável 1.100 (local 1.97) acusa `result_large_err` no `DualWriteError`; no Windows, `dead_code` num auxiliar de teste usado só fora do Windows (`path_filtrado`). Correção numa branch própria (Tci do [[integracoes-plano]]).

## Testes feitos
- `gh api repos/.../actions/workflows`: `CI` `active`.
- `gh api .../actions/permissions`: bloqueado pelo proxy da sessão (403).
- Settings → Actions → General: "Allow all actions".
- Aba Actions: aviso de Actions desligado.

## Evidências encontradas
- O aviso só aparece na aba **Actions**, não em Settings nem na API de workflows.

## Correção aplicada
Actions ligado na aba Actions do repositório (2026-11-24, 07h45).

## Solução
Regra: repositório novo (ou que recebeu histórico por push) só conta com o `CI` depois de abrir a aba **Actions** e confirmar que não há o aviso "Workflows aren't being run"; se houver, "Enable Actions on this repository", com o aval do humano.

## Como validar que não voltou
O próximo push de branch de tarefa abre uma execução do `CI` (`actions/runs` com `total_count` maior que 0, ou a aba Checks da PR).

## Logs que deveriam existir
No diário: a primeira execução do `CI` depois da correção e o resultado em Linux e Windows.

## O que aprendi
- Com o `CI` desligado, os erros se acumulam sem ninguém ver: o `pnpm check` local não substitui o `CI`, porque roda outra versão do Rust e só o Linux.
"Workflow ativo" e "Actions permitido" não bastam: o repositório tem um interruptor próprio, visível só na aba Actions. Zero execuções depois de um push é sinal para olhar lá primeiro.

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Decisões: [[geral-decisao-2026-11-19-ci-no-github]], [[geral-decisao-2026-11-19-gatilho-do-ci]]
- Outros bugs: [[bug-github-sem-acesso-em-chat-novo-2026-11-23]]
- Diário: [[diario-2026-11-24]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
