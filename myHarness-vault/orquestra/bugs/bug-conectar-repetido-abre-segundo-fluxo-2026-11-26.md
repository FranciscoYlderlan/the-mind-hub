---
tipo: bug
funcionalidade: integracoes
status: resolvido
criado: 2026-11-26
aliases: [Conectar repetido no núcleo, Fluxo órfão desfaz o conectado, Duplicate connect opens a second flow]
---
# 🐞 Conectar repetido abre um segundo fluxo e o órfão desfaz o conectado

## Contexto
Adversarial da `integracoes` em 2026-11-26, na `main` `fc7e540` ([[integracoes-plano-verificacoes#T5]]). A guarda de operação em andamento da T4b existe só na tela; o núcleo não tem guarda.

## Sintoma
- Passos (API): dois `conectar_integracao(github)` ao mesmo tempo. Na tela: recarregar no meio do device flow e clicar "Conectar" de novo. Depois, o humano conclui um dos fluxos.
- Esperado: um device flow só, ou o segundo recusado; o estado fica `conectado`.
- Observado: dois pedidos de código; o segundo conecta (`octocat`); o fluxo órfão expira (4 s no falso, 15 min no GitHub real) e emite `integracao-mudou` com GitHub `desconectado` e ERR-02 `expired_token`, com o token guardado. A tela mostra desconectado até uma checagem nova.
- O Claude CLI tem o mesmo problema: dois `claude auth login` ao mesmo tempo.
- Viola o ENT-13 (`status` e `erro` só quando o status vem de uma falha) e o estado final do ERR-02.

## Impacto
Estado falso de desconectado depois de uma conexão certa; RN-08 bloquearia ações com a integração conectada.

## Hipóteses
- Provável: `conectar` no `Nucleo` não registra a operação em andamento por integração; cada chamada abre um fluxo novo, e o fim de qualquer fluxo grava o estado.

## Linha do tempo técnica
- 2026-11-26 13h05: achado B1 do adversarial (deve corrigir).
- 2026-11-26 13h10: o humano escolheu reaproveitar; contrato M-50.
- 2026-11-26 14h12: T7 mergeada (PR #16).
- 2026-11-26 18h00: adversariais de novo na `main` `26923aa`: API ✔ nos ataques 3 e 4 (três `conectar` geram 1 código e 1 `/login`; sem fluxo órfão depois de 2000 s no relógio simulado); tela ✔ no AC-157 na mesma página ([[integracoes-plano-verificacoes-t6-t7#Validação final]]).

## Pseudocódigo do problema
`conectar(github)` ×2 → fluxo A e fluxo B; B conclui → `conectado`; A expira → grava `desconectado` + ERR-02 por cima.

## Testes feitos
- API pelo trait `Nucleo` com `GitHubFalso` e `fake-claude`; tela no Vite 1420 com o núcleo simulado (prints 11, 12 e 14 do adversarial).

## Evidências encontradas
- Relatório do adversarial de 2026-11-26, resumido em [[integracoes-plano-verificacoes#T5]].

## Correção aplicada
T7, PR #16: guarda de conexão em andamento por integração no `NucleoMyHarness`; `ClaudeCli::cancelar()` no "Desconectar"; registro "reaproveita" e "cancela" no log do núcleo. Os dois adversariais de 2026-11-26 18h00 passaram.

## Solução
O núcleo reaproveita a operação em andamento ([[geral-decisao-2026-11-26-conectar-repetido-reaproveita]]; contrato M-50, UC-01 FA-02, AC-157); aplicação na T7 do [[integracoes-plano]].

## Como validar que não voltou
Teste no núcleo com dois `conectar` ao mesmo tempo para o GitHub e o Claude CLI; adversarial de novo (ataques 3, 4 e 8).

## Logs que deveriam existir
Registro do núcleo quando uma operação repetida é recusada ou reaproveitada.

## O que aprendi
Guarda de operação só na tela não basta: recarregar a tela zera a guarda, e o núcleo precisa da sua. Candidato a nota de conceito no `Vault`.

### 🔗 Conexões
- Funcionalidade: [[integracoes-contexto]]
- Plano: [[integracoes-plano-verificacoes]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
