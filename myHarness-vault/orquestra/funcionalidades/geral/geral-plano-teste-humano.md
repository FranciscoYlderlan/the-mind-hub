---
tipo: plano
funcionalidade: geral
status: em-uso
criado: 2026-11-26
---
# 🧪 Fluxos de teste e roteiro do humano

> [!tldr] Em uma linha
> Registro acumulado dos fluxos de teste de cada funcionalidade, que o humano pode usar a qualquer momento, e o roteiro final, curto e didático, que passa por todas as funcionalidades e é entregue só no fim do projeto.

> [!warning] Quem escreve e quando
> - **A cada funcionalidade** que passou no verificador de fluxo principal e no adversarial: o orquestrador acrescenta a seção dela em "Fluxos registrados". Nada é entregue ao humano nessa hora.
> - **Na etapa final**, com todas as funcionalidades passando nos dois agentes: o orquestrador monta o "Roteiro final" a partir dos fluxos registrados e o entrega ao humano depois dos verificadores e do avaliador independente da aceitação final. O aceite do humano fecha a aceitação (Q06 e P07 do Manual da Orquestra - Perfil projeto prático (no Vault)).
> - Passou do limite de palavras: a seção de uma funcionalidade vira `geral-plano-teste-humano-<funcionalidade>.md`, com link nos dois sentidos.

## Fluxos registrados

Uma seção por funcionalidade, na ordem em que passaram. Passos: faça → clique em → esperado, cada um ligado ao AC de `Anexos/contrato/08-criterios-de-aceite.md` que ele prova.

### integracoes (2026-11-26)
- **Contexto:** [[integracoes-contexto]] · **UC:** UC-01, TEL-02 · **Acesso:** GitHub pelo app OAuth do projeto, no repositório de testes `FranciscoYlderlan/myharness-teste` ([[geral-decisao-2026-11-23-github-real-na-etapa-3]]); nenhuma senha aqui.
- **Sem o app instalado:** os passos 1 a 9 também rodam no `pnpm dev:simulado`, com o cenário da coluna AC (`?cenario=<nome>`, [[geral-decisao-2026-11-26-cenarios-do-modo-simulado]]).

| # | AC | Faça | Clique em | Esperado |
|---|---|---|---|---|
| 1 | AC-91 | Abra o app sem o GitHub conectado | o indicador de integrações | O painel abre com as três integrações; o GitHub com ponto vermelho e "Conectar" |
| 2 | AC-02 | Com o Claude CLI já logado, olhe o cartão dele | — | "conectado" e a versão, sem botão "Conectar" |
| 3 | AC-88 | Com o Claude CLI sem login (`claude-sem-login`) | "Conectar" do Claude CLI | O `/login` abre; ao concluir, o cartão mostra "conectado" e a versão |
| 4 | AC-01, AC-127 | No cartão do GitHub | "Conectar" | Aparece um código e o endereço `github.com/login/device`; depois de autorizar no navegador, "conectado" e a sua conta |
| 5 | AC-157 | Durante o código do passo 4, feche e abra o painel | "Fechar", depois o indicador | O mesmo código continua; nenhum código novo |
| 6 | AC-04, AC-129 | Comece o "Conectar" do GitHub e recuse no navegador | "Cancel" no GitHub | "recusada no GitHub", status desconectado e o botão "Conectar" de volta |
| 7 | AC-128 | Com o Obsidian aberto | "Conectar", depois "Testar" do Obsidian CLI | "conectado" e o número de notas indexadas |
| 8 | AC-05, AC-89 | Feche o Obsidian (`obsidian-err-03`) | "Testar" do Obsidian CLI | A mensagem da CLI, o botão "Abrir Obsidian" e o status desconectado |
| 9 | AC-153 | Com o GitHub conectado, tire a rede (`github-err-53`) | "Testar" do GitHub | "Falha inesperada com GitHub", com "Repetir" e "Conectar"; com a rede de volta, "Conectar" funciona |
| 10 | AC-90 | Com o GitHub conectado | "Testar" do GitHub | "conectado", a conta e os botões "Testar" e "Desconectar" |
| 11 | AC-03 | Tire o `claude` do `PATH` (`claude-nao-instalado`) e abra o painel | — | "Claude CLI não encontrado" e o link de instalação |

## Roteiro final

Gerado só na etapa final. Versão testada: commit ou endereço `[a preencher]` · Data: `[a preencher]`.

### Parte 1: tarefas sem ajuda (descoberta)
Só o objetivo, sem dizer onde clicar. O humano anota onde travou, o que procurou e quanto tempo levou.

| # | Tarefa | UC | ✔/✘ | Onde travou | Observação |
|---|---|---|---|---|---|

### Parte 2: fluxos guiados
Tirados dos fluxos registrados. Cada fluxo pode atravessar vários UC, com FA e FE no caminho; juntos, passam por todas as funcionalidades.

| Fluxo | Passo | AC | Faça | Clique em | Esperado | ✔/✘ | Observação |
|---|---|---|---|---|---|---|---|

### Cobertura por funcionalidade
Toda funcionalidade do roteiro do projeto aparece em ao menos uma tarefa ou fluxo. Linha sem tarefa nem fluxo é lacuna: o roteiro não é entregue assim.

| Funcionalidade | Tarefa (parte 1) | Fluxo (parte 2) |
|---|---|---|

### Aceite do humano
A palavra final da aceitação (P07).
- **Aceite:** `[a preencher]` · **Data:** `[a preencher]` · **Observação:** 

## Achados
Cada achado vai ao humano como opções (P06): corrigir, registrar como limite ou deixar como opcional.

| # | Parte e linha | O que aconteceu | Opção escolhida | Nota gerada |
|---|---|---|---|---|

### 🔗 Conexões
- Projeto: [[geral-contexto]] · Roteiro: [[geral-plano]]
- Funcionalidades registradas: [[integracoes-contexto]]
- Quem prova antes: cartões "Verificador de fluxo principal" e "Adversarial" do [[modelo-briefing-subagente]]
- Modelo: [[modelo-roteiro-teste-humano]]
- Contrato: Contrato funcional (no Vault)
- Regras: Manual da Orquestra - Perfil projeto prático (no Vault) (Q06)
