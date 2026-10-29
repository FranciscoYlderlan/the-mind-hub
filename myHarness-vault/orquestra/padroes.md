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
- Decisões: [[geral-decisao-2026-11-19-grafia-do-nome]], [[geral-decisao-2026-11-19-acesso-ao-repositorio]], [[geral-decisao-2026-11-19-agente-por-claude-p]], [[geral-decisao-2026-11-19-gatilho-do-ci]], [[geral-decisao-2026-11-19-subagente-nao-altera-contrato]]
- Mapa: [[moc-orquestra]]
- Regras: [[manual-da-orquestra]]
