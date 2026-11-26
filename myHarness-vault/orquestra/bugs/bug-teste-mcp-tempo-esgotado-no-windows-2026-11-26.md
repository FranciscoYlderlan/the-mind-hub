---
tipo: bug
funcionalidade: integracoes
status: resolvido
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
- Confirmada: no Windows, conectar numa porta fechada de `127.0.0.1` não recusa na hora; depois do RST, o TCP reenvia o SYN (`TcpMaxConnectRetransmissions`) e a recusa chega em cerca de 2 s, depois do tempo limite de 2000 ms do teste.
- Descartada: erro no cliente MCP; o código está certo, a recusa é que chega tarde.
- Descartada como correção: `SIO_TCP_INITIAL_RTO` sem reenvio de SYN (como curl, Chrome e JDK) exige `unsafe`, proibido no workspace (`unsafe_code = "forbid"`), e a dependência `windows-sys`.
- Descartada: falta das correções da #9; as falhas seguem depois do merge da `main` (`e26e145`).

## Linha do tempo técnica
- 2026-11-26 07h51: a #13 falha no Windows com os 2 testes; atribuído na hora à falta da #9.
- 2026-11-26 08h50: depois do merge da `main` nas 5 PRs, #8, #10 e #11 passam; #12 (job 139888782844) e #13 (job 139889300687) falham nos mesmos 2 testes.

## Pseudocódigo do problema
`conectar(127.0.0.1:porta_fechada)` com limite de 2000 ms: Linux recusa em milissegundos (`Rede`); Windows reenvia o SYN e recusa em ~2 s, então o limite vence antes (`TempoEsgotado(2000)`).

## Testes feitos
- `CI` Linux e Windows nas 5 PRs depois do merge da `main`.

## Evidências encontradas
- #12: `43 passed; 2 failed; 1 ignored`; #13: `100 passed; 2 failed; 1 ignored`.
- No job 139888782844, o teste falha ~2 s depois dos outros testes rápidos do MCP.
- Com o limite maior, os dois passam no Windows (suíte em ~10 s; no Linux, 2,4 s).

## Correção aplicada
`ef8e957` na `feat/integracoes-obsidian-cli`: `ServidorFalso::LIMITE_FORA_DO_AR = 10 s` (`servidor_falso.rs`, com comentário do caso do Windows), usado pelos dois testes; o teste do MCP mostra o tempo gasto quando falha.

## Solução
Só o teste muda. O produto usa `tempo_limite` padrão de 5 s, então no Windows já devolve ERR-53 em ~2 s; o contrato não muda. Recusa rápida no loopback do Windows fica como proposta, com aval, se o atraso incomodar na TEL-02.

## Como validar que não voltou
Job Windows do `CI` verde na #12 (`43ea5a0`), na #13 (`c1b5d69`) e na #14 (`bd41b95`), conferido em 2026-11-26.

## Logs que deveriam existir
O tempo gasto até o erro, na mensagem de falha do teste (já existe no teste do MCP).

## O que aprendi
No Windows, porta fechada de localhost demora ~2 s para recusar. Teste de servidor fora do ar precisa de limite bem acima de 2 s. Candidato a nota de conceito no `Vault`.

### 🔗 Conexões
- Funcionalidade: [[integracoes-contexto]]
- Plano: [[integracoes-plano-verificacoes]]
- Outros bugs: [[bug-ci-sem-execucao-actions-desligado-2026-11-24]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
