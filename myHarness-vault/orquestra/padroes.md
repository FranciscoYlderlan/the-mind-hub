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
- Decisões: [[geral-decisao-2026-11-19-grafia-do-nome]]
- Mapa: [[moc-orquestra]]
- Regras: [[manual-da-orquestra]]
