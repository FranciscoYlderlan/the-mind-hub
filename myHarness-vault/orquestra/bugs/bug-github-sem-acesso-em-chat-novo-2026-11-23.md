---
tipo: bug
funcionalidade: geral
status: resolvido
criado: 2026-11-23
aliases: [GitHub sem acesso em chat novo, add_repo negado, Repositório não ligado ao chat]
---
# 🐞 GitHub "sem acesso" em chat novo

## Contexto
O código do MyHarness mora em `FranciscoYlderlan/MyHarness` ([[geral-decisao-2026-11-23-push-e-pr-no-github]]). Cada chat novo do orquestrador roda num container limpo e precisa ligar o repositório ao chat com a ferramenta `add_repo` (acesso `push`) antes de usar a API do GitHub (`gh api`) ou dar push.

## Sintoma
- Esperado: o chat novo liga o repositório e usa a API e o push, como nos chats anteriores.
- Observado (2026-11-23, chat das 17h22): o `add_repo` voltou com `Permission ... denied by the Claude Code auto mode classifier. Reason: [Unauthorized Access]`, e o `gh api` voltou `GitHub access to this repository is not enabled for this session` (HTTP 403). O orquestrador concluiu que não havia acesso e pediu ao humano para liberar o GitHub.

## Impacto
Sem o repositório ligado, o chat fica sem API (PRs, `CI`) e sem push; os implementadores não podem ser despachados. O humano recebe um pedido de algo que ele já tinha liberado.

## Hipóteses
- **Humano tirou a permissão no GitHub:** descartada. O humano não mudou nada, e a segunda chamada do `add_repo`, minutos depois, passou sem prompt.
- **Acesso dado num chat vale nos seguintes:** descartada. O acesso vale por chat; todo chat novo precisa chamar o `add_repo`.
- **Recusa da aprovação automática do app (causa raiz):** o classificador revisa as ações do agente e recusou o `add_repo` feito logo no início do chat, antes de o humano falar em GitHub. No chat das 17h22 a segunda chamada passou depois de o humano citar o acesso ao GitHub; no das 17h38, com só o aviso do orquestrador, a segunda também foi negada. Confirmado às 17h47: a chamada passa quando o humano autoriza o GitHub na conversa.

## Linha do tempo técnica
- 17h22: `add_repo` (push) negado pelo classificador; `gh api` com 403. A `git ls-remote` e o `git clone` do repositório público funcionaram, só para leitura.
- 17h26: o orquestrador pediu ao humano para "liberar o acesso".
- 17h30: o humano disse que o acesso sempre foi dado; segundo `add_repo` aceito, clone feito e `register_repo_root` chamado; `gh api` passou a responder.
- 17h38 (chat novo, reapareceu): primeiro `add_repo` (push) negado pelo classificador com `[Unauthorized Access]`; o humano foi avisado em 1 linha e a segunda chamada também foi negada, agora com `[Undermining Oversight]`. O `git clone` público funcionou, só leitura. 17h47: o humano escreveu no chat que libera o acesso ao GitHub; a terceira chamada do `add_repo` foi aceita, clone feito e `register_repo_root` chamado; `gh api` respondeu.

## Pseudocódigo do problema
```text
chat novo:
  add_repo(push)  -> negado pelo classificador (não é o GitHub, não é o humano)
  agente conclui "sem acesso"        # erro: a recusa não foi testada de novo
correto:
  add_repo(push)  -> negado? avisar o humano em 1 linha e chamar de novo
  aceito -> git clone --depth 1 ... -> register_repo_root
```

## Testes feitos
- `gh api repos/FranciscoYlderlan/MyHarness/pulls` antes do `add_repo`: 403 da sessão.
- `git ls-remote` e `git clone --filter=blob:none` do repositório público: funcionam sem `add_repo`, só leitura.
- Segundo `add_repo` (push): `status: appended`; `gh api .../actions/runs` respondeu.

## Evidências encontradas
- O texto da recusa cita o classificador do modo automático, não o GitHub nem uma escolha do humano.
- A mesma chamada, sem nenhuma ação do humano, passou na segunda vez.

## Correção aplicada
Processo do orquestrador: no início do chat, chamar o `add_repo` (push); se vier a recusa do classificador, dizer ao humano em 1 linha e chamar de novo uma vez, sem pedir que ele libere nada. Regra do humano (17h47): no início de todo chat novo, o orquestrador abre ao humano um pedido de autorização para usar o GitHub neste chat, antes de chamar o `add_repo`; com a resposta dele na conversa, chama o `add_repo`. "Onde parei" do [[diario-2026-11-23]] atualizado com isso.

## Solução
1. Início do chat: abrir ao humano um pedido de autorização para usar o GitHub neste chat (pergunta com opções, "libero" ou "não agora") e esperar a resposta.
2. Com a autorização na conversa: `add_repo(owner="FranciscoYlderlan", repo="MyHarness", access="push")`; recusa do classificador: avisar o humano em 1 linha e repetir uma vez.
3. Aceito: `git clone --depth 1 https://github.com/FranciscoYlderlan/myharness /home/claude/myharness` (tempo longo) e `register_repo_root`.
4. Recusado de novo: reportar ao humano, com a mensagem de erro; enquanto isso, ler pelo `git clone` público e trabalhar nas branches locais.

## Como validar que não voltou
Num chat novo, o pedido de autorização aparece antes do `add_repo` e `gh api repos/FranciscoYlderlan/MyHarness/actions/runs --jq .total_count` responde um número depois do passo 3; nenhum pedido de "liberar o GitHub" ao humano sem a segunda tentativa.

## Logs que deveriam existir
No diário do dia: hora da chamada do `add_repo`, se foi negada e por quem (classificador, GitHub ou humano) e o resultado da segunda chamada.

## O que aprendi
Recusa de ferramenta não é falta de permissão: ler quem recusou antes de concluir. Recusa do classificador do modo automático não vem do humano nem do serviço, e pode passar numa nova tentativa com o motivo claro na conversa.

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Decisões: [[geral-decisao-2026-11-23-push-e-pr-no-github]]
- Outros bugs: (nenhum)
- Diário: [[diario-2026-11-23]]
- Funcionalidade afetada: [[integracoes-contexto]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
