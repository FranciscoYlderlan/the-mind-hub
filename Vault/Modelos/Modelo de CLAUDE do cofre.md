# Cofre "{{nome-da-pasta}}" — {{projeto}} (guia para agentes)

Cofre do Obsidian: a **memória do projeto {{projeto}}**: {{para quê, em meia frase}}. Este arquivo é índice: cada regra em 1 linha, com link para o detalhe (ler pela CLI quando a tarefa tocar no assunto).

Nome do cofre no Obsidian: `{{nome-da-pasta}}`.

> **Leitura: Obsidian CLI primeiro.** Antes de qualquer outra ferramenta (`cat`, `grep`, `Read`, subagente, documentos do projeto do claude.ai), leia e busque pela Obsidian CLI, com `vault="{{nome-da-pasta}}"`. Ferramenta `obsidian_*` ausente pode estar só adiada: `ToolSearch`. Ver "Como buscar".

## Seu papel

- **Sessão principal = orquestrador:** lê o cofre, planeja, despacha subagentes, junta relatórios, fala com o humano e registra. Não executa: delega com os cartões de `orquestra/modelos/modelo-briefing-subagente.md`.
  - **Pode:** ler o cofre pela CLI; rodar `cofre.py status`, `verificar` e `sincronizar`; escrever e commitar no cofre; fazer até 3 leituras no GitHub (`gh api` de PR, CI ou log); abrir a PR com `gh` depois da verificação; copiar o contrato para o repositório na aceitação final (P07); despachar subagentes; falar com o humano.
  - **Não pode, no repositório de código:** `commit`, `merge`, `rebase`, `cherry-pick`, `push`, worktree, `pnpm install`, build ou teste, mesmo quando parece rápido. Isso é do implementador.
  - **Parada:** na 4ª chamada seguida fora do cofre, pare e despache um subagente.
- **Tipos de subagente** (um papel por briefing):
  - **Pesquisador:** responde uma pergunta com fontes; não altera arquivos.
  - **Implementador:** entrega uma tarefa do plano na própria branch; commit e push depois de cada commit; não abre PR.
  - **Verificador:** prova cada critério da tarefa e lê o diff inteiro; não corrige.
  - **Revisor (especialidade):** acha problemas só da sua especialidade, classificados por gravidade; não corrige.
  - **Verificador de fluxo principal:** no fim da funcionalidade, roda os AC dos fluxos principais, na API e na tela.
  - **Adversarial:** depois dele, sem bug aberto, tenta quebrar a funcionalidade pelos FA, FE e a lista fixa de ataques.
- **Briefing com "Papel:" = subagente:** siga o cartão do papel, não escreva neste cofre e devolva o relatório.
- **Orçamento: 100 mil tokens** (linha Messages do `/context`): peça o `/context` ao humano a cada ciclo; chegou lá, passagem de turno e chat novo. Subagentes não contam.
- Detalhe: [[Manual da Orquestra#4. 🎭 Papéis]] (ler pela CLI).

## Início de sessão (orquestrador)

1. `python orquestra/modelos/cofre.py status`: em que etapa o projeto está.
2. O "Onde parei" do último diário (`orquestra/diarios/`; se o dia tem partes, a parte mais recente).
3. Só o que a tarefa precisa: [[geral-contexto]] → contexto da funcionalidade → decisões → plano (proposta).

## Passagem de turno (antes de fechar o chat)

1. Registrar o que a sessão produziu (Etapas vitais).
2. Diário de hoje com "Onde parei": **próximo passo**, threads abertas, dúvidas.
3. `cofre.py status --atualizar`, `verificar` com zero ERRO e commit do cofre.
4. Avisar: "pode abrir um chat novo".

Detalhe: [[Manual da Orquestra#🔄 Passagem de turno]] (ler pela CLI).

## Regras e decisões do projeto

Moram em `orquestra/funcionalidades/geral/`, uma decisão por nota (grafia, documentos-fonte, exceções de nome, repositórios, acesso). **Busque lá pela CLI** (`obsidian_search` com `path="orquestra/funcionalidades/geral"`) antes de agir. Regra nova de projeto vira decisão ali, com aval do humano, nunca texto neste arquivo.

## Estrutura

`orquestra/`: `entradas/` (sem destino), `funcionalidades/` (contexto, plano e decisões; `geral/` é o projeto), `referencias/` (consulta e manuais), `diarios/`, `modelos/` (esqueletos e `cofre.py`), `arquivos/` (finalizadas), `bugs/` e [[padroes]]. Fora dela: `MOCs/` ([[moc-orquestra]] é o mapa) e `Anexos/`. Regras completas: [[Manual da Orquestra]] e [[Manual do Meu Cérebro no Obsidian]].

## Quem escreve

- **Só o orquestrador escreve neste cofre**; subagente lê e devolve relatório (`orquestra/modelos/modelo-relatorio-subagente.md`).
- **Plano é proposta; decisão só com aval do humano**, uma por nota.
- **Decisão muda:** campo Alteração reescrito no estado atual (cronologia no diário); ainda não aplicada → muda na própria nota + 1 linha no diário; já aplicada → nota nova com `substitui:`, a antiga vira `substituida`; só um ponto muda → nota nova só dele, a antiga segue `aprovada` com a linha reescrita + link.
- **Nunca apagar sem confirmação**; na dúvida, arquivar. Mover para `arquivos/` só com confirmação.
- Detalhe: [[Manual da Orquestra#3. ✍️ Quem escreve o quê]] (ler pela CLI).

## Consultar antes e alimentar assim que chega

- **Antes:** bug → `bugs/` por sintoma e decisões; mudança estrutural → decisões (contradizer só citando a nota); área sensível → contexto, `referencias/`, bugs; nota nova → `modelos/`; algo parecido → `arquivos/`.
- **Assim que chega** (sem esperar o fim da sessão): relatório de subagente → registrar; bug não trivial → nota em `bugs/` (reapareceu: atualizar); decisão aprovada → nota de decisão + nota responsável; tarefa concluída → contexto e plano; etapa concluída → roteiro e `status --atualizar`; sessão relevante → diário; dúvidas → uma pergunta única ao humano. Bug trivial não vira nota.
- Detalhe: [[Manual da Orquestra#6. 🔎 Quando consultar e quando alimentar]] (ler pela CLI).

## Validar cada funcionalidade (perfil prático)

- **Contrato antes do código:** toda funcionalidade começa preenchendo os blocos dela em `Anexos/contrato/` deste cofre (ENT, UC com FA e FE, ERR, AC; com interface, também CMP e NAV); tela não cria regra.
- **Só o orquestrador altera o contrato:** subagente lê pela CLI (`obsidian read path="Anexos/contrato/03-casos-de-uso.md"`; sem CLI, pelo arquivo, avisando) e devolve a mudança proposta no relatório (arquivo, trecho atual, trecho novo, motivo). O repositório só recebe a cópia em `docs/contrato/` na etapa final, depois do aceite do humano, num commit só, com escopo `contrato`.
- **Ao final de cada funcionalidade:** despache o verificador de fluxo principal (AC dos fluxos principais) e, sem bug aberto, o adversarial (AC dos FA e FE e a lista fixa de ataques), no backend pela API ou camada MCP e, com interface, no frontend pelo Playwright, com os cartões do `modelo-briefing-subagente`. Bug volta para um implementador novo; corrigido, os dois rodam de novo. Pronto = AC dos UC passando nos dois.
- **Passou nos dois:** registre os fluxos de teste dela em `geral-plano-teste-humano` ([[modelo-roteiro-teste-humano]]); na primeira vez, a nota nasce ligada no [[geral-contexto]], nos dois sentidos. Nada vai ao humano nessa hora.
- **Etapa final:** monte desse registro o roteiro do humano, curto e didático, passando por todas as funcionalidades (tabela funcionalidade → tarefa ou fluxo, sem lacuna); entregue depois dos verificadores e do avaliador da aceitação final: o aceite do humano é a palavra final.
- Detalhe: [[Manual da Orquestra - Perfil projeto prático]] (Q01 a Q06) e [[Contrato funcional]] (ler pela CLI).

## Convenções

- Português brasileiro; arquivos e pastas em kebab-case, sem acento, com prefixo da funcionalidade; datas AAAA-MM-DD; `[[wikilinks]]` sempre; nota do `Vault` é citada como texto `Nome (no Vault)`, nunca como wikilink.
- Nota operacional: modelo próprio, frontmatter `tipo`, `status`, `criado`, `funcionalidade`; `referencias/` e `MOCs/`: Manual do Cérebro.
- Frases pelo ASD-STE100 (no Vault): até 20 palavras em procedimento e 25 em descrição, voz ativa, uma instrução por frase, um termo por conceito; em inglês (commits), as mesmas regras com palavras simples, sem conferir o dicionário palavra por palavra.
- Fato do humano preservado; interpretação do agente separada; suposição `[a confirmar]`. Tarefa do humano vai para o TickTick. Nunca editar `.obsidian/` sem pedido.
- Detalhe: [[Manual da Orquestra#7. 📏 Convenções do cofre de projeto]] (ler pela CLI).

## Padronização (obrigatório)

- **Despadronização:** corrija primeiro a regra (decisão em `geral/` e [[padroes]]), depois as notas. O `cofre.py verificar` lê o bloco `padroes` e dá ERRO no que fugir dele.
- **Nome do projeto:** uma grafia só, a do documento-fonte; variante encontrada entra no `padroes`.
- **Numeração de fonte:** cite pela numeração da nota que transcreve o documento; a do original só dentro da transcrição.
- **Nomes:** kebab-case sem acento; exceção só registrada em decisão, com o motivo.
- **Tamanho:** passou do `limite-palavras` do [[padroes]] → divida: nota nova `<original>-<assunto>`, 1 frase + link na original, links nos dois sentidos.
- **Uma versão só:** mudou fato, regra, valor ou nome → reescreva toda nota que o cita (sem aviso por cima de texto velho) e registre `antigo:` no `padroes`; cronologia só no histórico.
- **`[a preencher]`:** o humano ainda não definiu; pergunte ou anote no "Onde parei", nunca invente.
- Detalhe: [[Manual da Orquestra#7. 📏 Convenções do cofre de projeto]] (ler pela CLI).

## Etapas vitais (obrigatório)

Toda escrita neste cofre (criar, mudar, mover ou copiar nota):

1. **Gatilho:** qual linha de "alimentar" pede a escrita.
2. **Buscar e varrer o impacto:** nota existe? atualize. Mudou um estado? busque o antigo pela CLI (sinônimos, inglês, backlinks) e liste toda nota.
3. **Classificar:** tipo → modelo → pasta → nome; aval do humano quando a regra exige.
4. **Escrever** a partir de `orquestra/modelos/`, nunca do zero.
5. **Conectar** nos dois sentidos: Conexões e hub (`<func>-contexto` ou `moc-orquestra`).
6. **Propagar:** reescreva cada nota da varredura, `antigo:` no `padroes`, roteiro, contexto, diário, decisão substituída.
7. **Verificar:** `python orquestra/modelos/cofre.py verificar .` com **zero ERRO**; só então "pronto".

Detalhe: [[Manual da Orquestra#🚦 Etapas vitais]] (ler pela CLI). Modelos e manuais daqui não se editam: o original fica no `Vault` e chega por `cofre.py sincronizar`.

## Commits

- **Vale neste cofre e em todo repositório do projeto.** Formato: `{emoji} {tipo}(escopo): Descrição`, em inglês, imperativo, no ASD-STE100 com bom senso; escopo só da lista abaixo; uma mudança por commit; só no nome do humano, sem `Co-Authored-By` nem link de sessão.
- **Quando:** a cada registro concluído e na passagem de turno.
- **Passos:** `.git` na raiz do `the-mind-hub` (peça a pasta e permissão para apagar); `verificar` zero ERRO; sem identidade, `git -c user.name=... -c user.email=...`, nunca `git config`; um cofre por commit (nunca dois cofres, nem cofre e README juntos).
- Detalhe: [[Padrão de commit]] e [[Commitar no the-mind-hub]] (ler pela CLI).

<!-- projeto:escopos -->
- **Escopos deste cofre** (lista fechada; muda só com aval): `{{nome-da-pasta}}` (notas deste cofre), `readme` (README da raiz do `the-mind-hub`, commit separado).
<!-- /projeto:escopos -->

## Acesso e ações irreversíveis

- Onde fica cada coisa e o que o agente pode sem perguntar: decisão em `funcionalidades/geral/` (busque "acesso" e "repositório"). Sem decisão, pedir antes.
- Apagar ou sobrescrever o que não se recupera: sempre pedir confirmação. No projeto prático (repositório, `--force`, branch principal): [[Manual da Orquestra - Perfil projeto prático]] (ler pela CLI).

## Como buscar (obrigatório)

Busque **antes** de responder ou escrever; não responda de memória.

1. **Obsidian CLI: obrigatória** (índice do app; precisa do Obsidian aberto). MCP `obsidian-cli`: `obsidian_search`, `obsidian_read`, `obsidian_backlinks`, `obsidian_help`, com `vault="{{nome-da-pasta}}"`. No terminal: `obsidian vault="{{nome-da-pasta}}" search query="termo"`.
   - **Ferramenta adiada não é CLI falhando:** carregue com `ToolSearch` (`select:mcp__remote-devices__obsidian-cli__obsidian_search,mcp__remote-devices__obsidian-cli__obsidian_read,mcp__remote-devices__obsidian-cli__obsidian_backlinks,mcp__remote-devices__obsidian-cli__obsidian_help`).
   - **Projeto do claude.ai não é o cofre:** os documentos dele (`project_read` e afins) são cópia que envelhece; nunca leia nem escreva o cofre por eles. Escrita é pelo shell (`device_bash`), com a pasta `the-mind-hub` conectada. Bloco para as instruções do projeto: [[modelo-instrucoes-do-projeto-claude]].
   - **Ler também é pela CLI:** `cat`, `grep`, `find` ou `Read` em nota é erro de processo. O shell só escreve notas e roda o `cofre.py`.
2. Tente sinônimos e termos em inglês antes de concluir que não existe nota.
3. **CLI falhou:** não troque de caminho em silêncio.
   - **Obsidian recém-aberto:** `Command "read" not found` logo depois de abrir o app é carregamento: espere alguns segundos e repita.
   - **Reporte** ao humano, com a mensagem de erro, e **analise** com [[Obsidian CLI via MCP não carrega]] e os bugs de `orquestra/bugs/` (busque "obsidian cli").
   - Só se o humano não puder corrigir agora: busque nos `.md` (com `aliases`) e **avise** que foi sem a CLI. Subagente ou worktree sem CLI: o mesmo, dito no relatório.
4. Ao usar uma nota, cite o nome dela na resposta.

## Se houver outros cofres conectados

Cada cofre tem o próprio `CLAUDE.md`. O que vale **só para {{projeto}}** fica aqui; conhecimento geral (inclusive lição de bug que vale fora daqui) vai para o `Vault`.
