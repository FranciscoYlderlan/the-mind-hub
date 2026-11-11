---
tipo: bug
funcionalidade: integracoes
status: aberto
criado: 2026-11-26
aliases: [Tempo esgotado do MCP no Windows, Teste do servidor fora do ar no CI do Windows, MCP timeout on Windows]
---
# 🐞 Testes do MCP com tempo esgotado no Windows do CI

## Contexto
O cliente MCP da T2 fala com o servidor da Obsidian CLI por HTTP ([[integracoes-plano]], T2). Dois testes simulam o servidor fora do ar e esperam um erro de rede.

## Sintoma
- Esperado: com o servidor fora do ar, o teste recebe o erro de rede (ERR-53) logo.
- Observado no job Windows do `CI`: `TempoEsgotado(2000)` nos dois testes; no Linux, passam.
- `infra::mcp::tests::servidor_fora_do_ar_e_rede` (`src-tauri\src\infra\mcp\mod.rs:310`).
- `infra::obsidian::tests::servidor_fora_do_ar_da_err_53_e_conectar_de_novo_funciona` (`src-tauri\src\infra\obsidian\tests.rs:140`).

## Impacto
O Windows fica vermelho na PR #12 (T2) e na #13 (T4 com T1), que recebe os testes pelo merge da #12.

## Hipóteses
- `[a confirmar]`: no Windows, conectar numa porta fechada de `127.0.0.1` não recusa na hora; o TCP tenta de novo por cerca de 2 s, e o tempo limite de 2000 ms chega antes do erro de rede.
- Descartada: falta das correções da #9; as falhas seguem depois do merge da `main` (`e26e145`).

## Linha do tempo técnica
- 2026-11-26 07h51: a #13 falha no Windows com os 2 testes; atribuído na hora à falta da #9.
- 2026-11-26 08h50: depois do merge da `main` nas 5 PRs, #8, #10 e #11 passam; #12 (job 139888782844) e #13 (job 139889300687) falham nos mesmos 2 testes.

## Pseudocódigo do problema
`[a preencher]`

## Testes feitos
- `CI` Linux e Windows nas 5 PRs depois do merge da `main`.

## Evidências encontradas
- #12: `43 passed; 2 failed; 1 ignored`; #13: `100 passed; 2 failed; 1 ignored`.

## Correção aplicada
`[a preencher]`

## Solução
`[a preencher]`

## Como validar que não voltou
Job Windows do `CI` verde na #12 e na #13.

## Logs que deveriam existir
`[a preencher]`

## O que aprendi
`[a preencher]`

### 🔗 Conexões
- Funcionalidade: [[integracoes-contexto]]
- Plano: [[integracoes-plano-verificacoes]]
- Outros bugs: [[bug-ci-sem-execucao-actions-desligado-2026-11-24]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
