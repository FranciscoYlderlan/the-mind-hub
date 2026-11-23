---
tipo: plano
funcionalidade: fundacao
status: aprovado
criado: 2026-11-20
---
# 📋 Candidatos a registro — fundação (G1)

> [!warning] Proposta da IA
> Parte de [[fundacao-plano]]. Nada aqui é decisão: cada item vira nota, decisão ou pergunta ao humano quando chegar a vez.

- Teste `mensagens_seguem_o_catalogo` não cobre ERR-04 a ERR-06 (observação do verificador da T1).
- `a_partir_do_erro` leva ERR-05 a ERR-07 a desconectado mesmo vindo de sem login ou não instalado; sem efeito na T1, revisar na etapa 3.
- Link de instalação do ERR-01: tela ou núcleo, decidir na etapa 3.
- Para o `AgentRunner` (etapa 3): portão inexistente sai com 127, que a CLI não trata como bloqueio (a ferramenta roda sem o portão); passar `stdin` nulo (sem ele, a CLI espera 3 s); limite de cerca de 32 mil caracteres da linha de comando no Windows.
- Rodar os testes da T3 no Windows (`cargo test` com `#[cfg(windows)]`) e conferir o caso `"` no `PATH`; ajustar o comentário de `execucao.rs` se preciso.
- Regra "contém" da camada 4 tira variáveis legítimas além do `PATH` (`PWD`, `LS_COLORS`, `PS1`, palavras como `weighs_more`); revisar se o agente precisar delas.
- Pontos do contrato levantados na T4, para o humano: ligações que faltam (`Tarefa.plano`, `Relatório.execucao`, `Achado.execucao`, `Escrita.cofre`); tarefa incompleta do ERR-49 sem forma de gravar; regras que dependem do papel fora do banco; `concluído` × `concluido` entre Relatório e Execução; ERR-51 diz "nada foi gravado" mesmo quando o desfazer do cofre falha; falta o campo que liga linha a nota (AC-148).
- Pontos do contrato levantados na T5, para o humano: erro interno genérico fora do catálogo (proposta ERR `FALHA_INTERNA`; o ERR-54 já vai para o desfazer que falha, M-40); ENT-20 Rodada sem `id` nem `chat`; ENT-04 Mensagem sem data e hora; percentuais da ENT-14 como inteiros; nomes ASCII para ✔, ✘ e "não verificado, presumido" da ENT-24; CMP-12 sem marca de tarefa incompleta no DTO (resolvido pelo campo `incompleta` do M-39). IDs vão como texto no IPC; converter na fronteira se a T4 usar INTEGER. `src/dev/nucleo-simulado.ts` da decisão do modo simulado ainda não existe. Os bindings importam `@tauri-apps/api/mocks`: conferir no build. `cargo test` passa a exigir `pnpm install` (o gerador usa o Prettier do projeto).
- Lição de SQLite: CHECK com `=` passa quando a expressão dá NULL; usar `IS`.
- Escolhas da T3 a revisar na tarefa do `harness-gate`: `--tools` só com nomes internos; gancho sem o papel.
- Ambiente: `cargo clippy --workspace` exige GTK e WebKitGTK (`libwebkit2gtk-4.1-dev`, `libgtk-3-dev`, `libayatana-appindicator3-dev`, `librsvg2-dev`).

## Verificação da T4 (2026-11-20)
- Ambiguidades do contrato que o esquema aceita hoje: `projeto.nome` único sem regra de caixa e espaços (NBSP e espaço de largura zero passam como não vazios); `toca_em` pode sair do repositório (`../fora`, `~/x`) e repetir item; sem unicidade em `integracao.tipo`, `(chat, versao)` do plano e `pasta_contexto (projeto, caminho)`; dependência em ciclo aceita; ciclo de vida sem trava no banco (aprovado volta a recusado, encerrado volta a ativo); `branch` frouxa, `worktree` relativa, `motivo_fila` com `rodando`; prompts de fábrica (ENT-08) sem dono definido; apagar o único cofre de memória é aceito (ERR-38 é do núcleo).
- Emoji de commit: resolvido em 2026-11-23 ([[geral-decisao-2026-11-23-push-e-pr-no-github]]): mensagens reescritas pela tabela de Tipos e emojis de commit (no Vault), que ganhou o tipo `ci`.

## Verificação da T5 (2026-11-23)
- Formato de data entre camadas: o banco da T4 aceita 0 ou 3 casas de fração; o `DataHoraUtc` aceita de 1 a 9 e o zod, qualquer número. Normalizar ao ligar o núcleo ao banco [a confirmar onde].
- Valores dos enums: o banco guarda o texto do contrato (`só leitura`, `na fila`, `não instalado`); a IPC usa ASCII (`so_leitura`, `na_fila`, `nao_instalado`). Falta definir onde fica o mapeamento.
- O teste `bindings_estao_em_dia` precisa do Prettier em `node_modules`: o `cargo test` falha sem `pnpm install` antes (a CI já instala).

## Correção da T4 (2026-11-23)
- Propostas de contrato (`02-entidades`), aguardam o humano: ENT-07 `comandos` vira "comandos executados pelo agente; push, merge e push --force nunca entram (o núcleo os nega antes, ERR-14)"; ENT-09 `criterios` obrigatório quando o papel é teste vira regra do núcleo (o banco não consegue exigir linha filha).
- Lição de SQLite (candidata ao Vault): `OR REPLACE` apaga a linha sem disparar trigger de `DELETE`; usar trigger `BEFORE INSERT` que confere cada chave única, inclusive índice único parcial.
- Refazer tabela no sqlx: `-- no-transaction`, `PRAGMA foreign_keys=OFF`, `BEGIN`/`COMMIT` próprios e conferência do `pragma_foreign_key_check` antes do `COMMIT`.
- O filtro de `comandos` olha só o subcomando logo após o programa (`git -C x push` passa); a barreira real é o portão (RN-27).

## Ajuste da T5 (2026-11-23)
- Propostas de contrato, aguardam o humano: ENT-24 Critério ganha `descricao` (texto do critério do "Pronto quando"); ENT-24 registra `passou`, `falhou` e `nao_verificado_presumido` como nomes ASCII de ✔, ✘ e "não verificado, presumido".
- Enum da IPC sempre em ASCII snake_case; o texto do contrato com acento fica só na tela e no banco (ver o mapeamento acima).
- Tipo sem comando nem evento precisa de `.typ::<T>()` no construtor para sair nos bindings.
- ENT-17 Escrita sem DTO na IPC (nenhum comando a usa).

## Segunda verificação da T5 (2026-11-23)
- Quando surgir o comando de relatório, o zod de `Relatorio` entra no fluxo de validação; a Escrita (ENT-17) ganha DTO quando surgir o comando dela.

### 🔗 Conexões
- Plano: [[fundacao-plano]]
- Funcionalidade: [[fundacao-contexto]]
- Regras: [[manual-da-orquestra]]
