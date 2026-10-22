---
tipo: plano
funcionalidade: geral
status: em-uso
criado: {{date}}
---
# 🧪 Fluxos de teste e roteiro do humano

> [!tldr] Em uma linha
> Registro acumulado dos fluxos de teste de cada funcionalidade, que o humano pode usar a qualquer momento, e o roteiro final, sucinto, entregue só no fim do projeto.

> [!warning] Quem escreve e quando
> - **A cada funcionalidade** que passou no verificador de fluxo principal e no adversarial: o orquestrador acrescenta a seção dela em "Fluxos registrados". Nada é entregue ao humano nessa hora.
> - **Na etapa final**, com todas as funcionalidades passando nos dois agentes: o orquestrador monta o "Roteiro final" a partir dos fluxos registrados e o entrega ao humano, antes da aceitação final (Q06 e P07 do Manual da Orquestra - Perfil projeto prático (no Vault)).
> - Nota única do projeto: `funcionalidades/geral/geral-plano-teste-humano.md`. Nasce com a primeira funcionalidade que passa nos dois agentes, já ligada nos dois sentidos: o [[geral-contexto]] ganha o link para ela nas Conexões, e ela aponta de volta nas Conexões abaixo; a última etapa do [[geral-plano]] também a cita. Passou do limite de palavras: a seção de uma funcionalidade vira `geral-plano-teste-humano-<funcionalidade>.md`, com link nos dois sentidos.

Fala do humano (2026-11-17): "o objetivo é eu conseguir testar o máximo de coisa possível em poucos fluxos ... mas no obsidian esses fluxos são registrados para caso eu quero realizar um teste a qualquer momento".

## Fluxos registrados

Uma seção por funcionalidade, na ordem em que passaram. Passos didáticos e sucintos: faça → clique em → esperado, cada um ligado ao AC de `docs/contrato/08-criterios-de-aceite.md` que ele prova.

### nome-da-funcionalidade (AAAA-MM-DD)
- **Contexto:** [[nome-da-func-contexto]] · **UC:** UC-01 · **Acesso:** nota de acesso de teste (P08), nunca a senha aqui

| # | AC | Faça | Clique em | Esperado |
|---|---|---|---|---|
| 1 | AC-01 | Entre como cliente | "Nova reserva" | O formulário abre com as salas ativas |
| 2 | AC-03 | Escolha uma sala já reservada nesse horário | "Confirmar" | A mensagem de ERR-01 aparece e nada é gravado |

## Roteiro final

Gerado só na etapa final. Versão testada: commit ou endereço `[a preencher]` · Data: AAAA-MM-DD.

### Parte 1: tarefas sem ajuda (descoberta)
Só o objetivo, sem dizer onde clicar. O humano anota onde travou, o que procurou e quanto tempo levou.

| # | Tarefa | UC | ✔/✘ | Onde travou | Observação |
|---|---|---|---|---|---|
| 1 | Crie uma reserva que comece amanhã. | UC-01 | | | |

### Parte 2: poucos fluxos guiados
Poucos fluxos que cobrem o máximo de AC: cada fluxo atravessa vários UC, com alguns FA e FE no caminho. Tirados dos fluxos registrados.

| Fluxo | Passo | AC | Faça | Clique em | Esperado | ✔/✘ | Observação |
|---|---|---|---|---|---|---|---|
| A | 1 | AC-01 | Entre como cliente | "Nova reserva" | O formulário abre com as salas ativas | | |
| A | 2 | AC-04 | Digite "dez" em pessoas | — | O campo não aceita letras | | |

- **Cobertura:** AC cobertos / AC do contrato (os que ficaram de fora, listados aqui).

## Achados
Cada achado vai ao humano como opções (P06): corrigir, registrar como limite ou deixar como opcional.

| # | Parte e linha | O que aconteceu | Opção escolhida | Nota gerada |
|---|---|---|---|---|

### 🔗 Conexões
- Projeto: [[geral-contexto]] · Roteiro: [[geral-plano]]
- Quem prova antes: cartões "Verificador de fluxo principal" e "Adversarial" do [[modelo-briefing-subagente]]
- Contrato: Contrato funcional (no Vault)
- Regras: Manual da Orquestra - Perfil projeto prático (no Vault) (Q06)
