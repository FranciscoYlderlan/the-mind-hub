---
tipo: padroes
status: em-uso
criado: 2026-11-19
aliases: [padroes do projeto, padronização]
---
# 📏 Padrões — MyHarness

> [!tldr] Em uma linha
> O bloco abaixo é lido pelo `cofre.py verificar`: termo fora do padrão, estado substituído (`antigo:`) e limite de palavras por nota dão ERRO.

```padroes
# termo fora do padrão => forma certa   ("re:" no início = expressão regular)
# antigo: termo do estado substituído => estado atual (nota dona)   (ERRO só fora do histórico)
re:\b[Oo] Harness\b|\bpelo Harness\b|\bdo Harness\b => o MyHarness (geral-decisao-2026-11-19-grafia-do-nome)
antigo: re:\*\*não tem acesso\*\* a essa pasta|que o agente não acessa|entrega os arquivos ao humano|A entrega ao humano é por arquivo => o agente escreve direto em Projetos\my-harness (geral-decisao-2026-11-19-acesso-ao-repositorio)
antigo: re:O Agent SDK em Node \(S4\) é o plano B|\(S4\) fica como plano B|Plano B \(S4\) => S3 confirmada pelo P1; S4 fora do plano (geral-decisao-2026-11-19-agente-por-claude-p)
antigo: re:só checagem em PR => checagem em PR e em push na main (geral-decisao-2026-11-19-gatilho-do-ci)
antigo: re:contrato da funcionalidade em `docs/contrato/`|preencher o contrato em `docs/contrato/`|`docs/contrato/` com `00-requisitos`|vai para `docs/contrato/00-requisitos.md` => contrato em Anexos/contrato/ do cofre; docs/contrato/ só na aceitação final (geral-decisao-2026-11-19-subagente-nao-altera-contrato)
antigo: re:ADIAMENTO_JA_USADO|adiamento_usado|segundo adiamento => limite do chat é aviso ERR-48 LIMITE_DO_CHAT_ATINGIDO; o Humano segue quantas vezes quiser (contrato, M-18)
antigo: re:com só o aval guardado no SQLite|no SQLite fica só o aval => aval e registrada_em no SQLite (geral-decisao-2026-11-19-gravacao-dupla)
antigo: re:valores de chave token/senha/secret/api key => mascarar só prefixos conhecidos e os segredos que o núcleo guarda, sem adivinhar (geral-decisao-2026-11-20-mascaramento-sem-adivinhar)
antigo: re:Entregar, em série|Série T1 → T5|tarefas-interface rodam em série => paralelo por padrão; série só com arquivo em comum, combinado, cadeia, recurso ou teto (geral-decisao-2026-11-20-paralelo-por-padrao)
antigo: re:merge local na `main`|sem PR, e o merge|tudo segue local, sem PR|conta sem acesso; tudo local|Enquanto o GitHub não existe => push e PR no GitHub pelo orquestrador; o humano aprova a PR e faz o merge (geral-decisao-2026-11-23-push-e-pr-no-github)
antigo: re:`concluido`(?! ×)|\bconcluido, falhou => concluído, com acento, em Execução e Relatório (contrato, M-38)
antigo: re:PR única da G1|numa PR só|uma PR só da G1|feat/setup-g1-interfaces`, `pnpm check`, push => uma PR por tarefa, mergeada pelo humano na ordem indicada (geral-decisao-2026-11-23-uma-pr-por-tarefa)
limite-palavras: 2000
```

## Como usar
- Cada linha cita a nota dona: a decisão em `orquestra/funcionalidades/geral/` que fixou a regra.
- Despadronização achada: primeiro a regra (decisão + linha aqui), depois as notas.
- Mudou um estado: o antigo entra como linha `antigo:` (varredura de impacto, etapas B2 e B6).

## A definir (cada item vira decisão em `geral/`)
- Documentos-fonte com seções próprias e como são citados. [a preencher]
- Exceções de nome de arquivo, com o motivo. [a preencher]

### 🔗 Conexões
- Índice: [[CLAUDE]]
- Decisões: [[geral-decisao-2026-11-19-grafia-do-nome]], [[geral-decisao-2026-11-19-acesso-ao-repositorio]], [[geral-decisao-2026-11-19-agente-por-claude-p]], [[geral-decisao-2026-11-19-gatilho-do-ci]], [[geral-decisao-2026-11-19-subagente-nao-altera-contrato]], [[geral-decisao-2026-11-20-mascaramento-sem-adivinhar]], [[geral-decisao-2026-11-20-paralelo-por-padrao]], [[geral-decisao-2026-11-20-tudo-local-sem-github]], [[geral-decisao-2026-11-23-push-e-pr-no-github]], [[geral-decisao-2026-11-23-uma-pr-por-tarefa]]
- Mapa: [[moc-orquestra]]
- Regras: [[manual-da-orquestra]]
