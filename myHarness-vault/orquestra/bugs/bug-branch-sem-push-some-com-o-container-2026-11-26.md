---
tipo: bug
funcionalidade: geral
status: resolvido
criado: 2026-11-26
aliases: [Branch perdida, Commit sem push, Trabalho preso no container]
---
# 🐞 Branch sem push só existe no container de um chat

## Contexto
Cada chat do orquestrador roda num container próprio, com o clone do `MyHarness` e as worktrees dos implementadores em `/home/claude/`. O push das branches de tarefa só era feito depois da verificação ([[geral-decisao-2026-11-23-uma-pr-por-tarefa]]).

## Sintoma
- Esperado: um chat novo acha no GitHub o trabalho do chat anterior.
- Observado (2026-11-26, 07h45): num chat novo, a branch `feat/integracoes-painel` (T5 `f3004ae`) não estava no GitHub nem na pasta `my-harness` do humano; o relatório da T4b também não. A branch só existia no container do chat de 2026-11-24, que por acaso ainda estava vivo.

## Impacto
Trabalho entregue e verificado pode sumir com o container; a T5 teria de ser refeita do zero, guiada só pelas notas de [[integracoes-plano-verificacoes]].

## Hipóteses
- Branch apagada no GitHub: descartada; ela nunca recebeu push.
- Container descartado (causa): o container de um chat não é visto por outro e pode ser apagado a qualquer hora; branch sem push vive só nele.

## Linha do tempo técnica
- 2026-11-24 13h: T5 entregue em `f3004ae`, sem push (push só depois da verificação).
- 2026-11-24 16h: verificação da T5 com correções; T4b despachada; parou no limite semanal de uso.
- 2026-11-26 07h45: outro chat não achou a branch; o chat de 2026-11-24 ainda a tinha e deu push (`f3004ae` no GitHub).

## Testes feitos
- `git ls-remote origin feat/integracoes-painel` antes: vazio; depois do push: `f3004ae6409372aa41588396e254111ef62522d3`.

## Evidências encontradas
- `git branch -a` no container de 2026-11-24 listava `feat/integracoes-painel` sem `remotes/origin/...`.

## Correção aplicada
Push imediato da `feat/integracoes-painel` (2026-11-26, 07h47). A T4b foi parada antes de qualquer commit e recomeça num chat novo, a partir das branches do GitHub, com push depois de cada commit.

## Solução
Regra de processo: todo commit de implementador recebe push logo em seguida, na branch da tarefa (push sem `--force`), antes da verificação. A PR só abre depois da verificação. Todo briefing de implementador traz o comando de push.

## Como validar que não voltou
Ao fim de cada relatório de implementador, `git ls-remote origin <branch>` mostra o hash do último commit.

## Logs que deveriam existir
No diário: hash e branch de cada entrega, com "push feito".

## O que aprendi
O container é rascunho, o GitHub é o arquivo: o que não recebeu push não existe para o próximo chat.

### 🔗 Conexões
- Funcionalidade: [[integracoes-contexto]]
- Decisões: [[geral-decisao-2026-11-23-uma-pr-por-tarefa]], [[geral-decisao-2026-11-23-push-e-pr-no-github]]
- Outros bugs: [[bug-github-sem-acesso-em-chat-novo-2026-11-23]]
- Diário: [[diario-2026-11-26]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
