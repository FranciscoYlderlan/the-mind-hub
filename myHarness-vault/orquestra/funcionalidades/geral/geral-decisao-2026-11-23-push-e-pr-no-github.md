---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-23
substitui: [[geral-decisao-2026-11-20-tudo-local-sem-github]]
---
# ✅ Push e PR no GitHub, com o aval do humano em cada PR

- **Proposta (plano):** pedido do humano em 2026-11-23: subir os commits do projeto para `https://github.com/FranciscoYlderlan/MyHarness.git`, com as datas distribuídas de 2026-09-21 até 2026-11-23.
- **Decisão:** o repositório remoto é `FranciscoYlderlan/MyHarness`. O orquestrador dá o push e abre as PRs; o humano aprova ou não cada PR, e o merge na `main` é dele, pela PR. Cada tarefa sobe na sua PR, com `pnpm check` local antes do push ([[geral-decisao-2026-11-23-uma-pr-por-tarefa]]). Histórico com datas de autor e de commit de 2026-09-21 a 2026-11-27, só de segunda a sexta, em ordem ([[geral-decisao-2026-11-27-datas-no-congelamento]]); autor `franciscoylderlan`; mensagens pela tabela de Tipos e emojis de commit (no Vault).
- **Alteração:** o humano primeiro disse que ele daria o push e depois corrigiu: o orquestrador dá o push e ele aprova as PRs. O tipo `ci` (`:construction_worker:`) entrou na tabela de Tipos e emojis de commit (no Vault), por escolha do humano; os demais emojis fora da tabela foram trocados.
- **Motivo:** respostas do humano em 2026-11-23, às 15h55, 15h57 e 16h02 ("eu não realizo commits aos sábados e domingos"); a conta do GitHub voltou.
- **Consequências:** o CI do GitHub ([[geral-decisao-2026-11-19-ci-no-github]], [[geral-decisao-2026-11-19-gatilho-do-ci]]) roda em PR e em push na `main`. As branches antigas ficam em `backup/*` no `Projetos\my-harness`; `feat/setup-mascaramento-segredo` não sobe. Hashes antigos → atuais, depois do merge da #3 e do rebase das outras PRs sobre a `main` (os diários seguem com os antigos):

  | Antigo | Novo |
  |---|---|
  | `9d5d667` | `ec3c153` |
  | `5059cd6` | `b7656f8` |
  | `79c4d56` | `29850b6` |
  | `c70d8fe` | `9153294` |
  | `3202994` | `0ba9e7b` |
  | `feafd97` | `56437a5` |
  | `85dbb72` | `055aa69` |
  | `b2dde90` | `8896227` |
  | `4393810` | `70124c2` |
  | `1a0c889` | `682b679` |
  | `e57f4bf` | `cba8f60` |
  | `0cff8ad` | `07d442d` |
  | `1fad5e7` | `5d0e88c` |

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[fundacao-plano]], [[geral-plano]]
- Datas no congelamento: [[geral-decisao-2026-11-27-datas-no-congelamento]]
- Decisão substituída: [[geral-decisao-2026-11-20-tudo-local-sem-github]]
- Decisões alteradas: [[geral-decisao-2026-11-19-branches-e-pr-unica]], [[geral-decisao-2026-11-19-repositorio-e-ambiente]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]], [[padroes]]
