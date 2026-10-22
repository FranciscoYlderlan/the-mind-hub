# Cofre "PrepBTG-vault" — PrepBTG (guia para agentes)

Cofre do Obsidian: a **memória do projeto PrepBTG**: Preparar o estudo de caso de Analista de Compliance Engineering no BTG Pactual, treinando em um banco de dados mocado com Python e SQL. Este arquivo é índice: cada regra em 1 linha, com link para o detalhe (ler pela CLI quando a tarefa tocar no assunto).

Nome do cofre no Obsidian: `PrepBTG-vault`.

> **Leitura: Obsidian CLI primeiro.** Antes de qualquer outra ferramenta (`cat`, `grep`, `Read`, subagente, documentos do projeto do claude.ai), leia e busque pela Obsidian CLI, com `vault="PrepBTG-vault"`. Ferramenta `obsidian_*` ausente pode estar só adiada: `ToolSearch`. Ver "Como buscar".

## Seu papel

- **Sessão principal = orquestrador:** lê o cofre, planeja, despacha subagentes, junta relatórios, fala com o humano e registra. **Não implementa** nem faz leitura ou pesquisa longa: delega com os cartões de `orquestra/modelos/modelo-briefing-subagente.md`.
- **Briefing com "Papel:" = subagente:** siga o cartão do papel, não escreva neste cofre e devolva o relatório.
- **Orçamento: 100 mil tokens** (linha Messages do `/context`): peça o `/context` ao humano a cada ciclo; chegou lá, passagem de turno e chat novo. Subagentes não contam.
- Detalhe: [[manual-da-orquestra#4. 🎭 Papéis]] (ler pela CLI).

## Início de sessão (orquestrador)

1. `python orquestra/modelos/cofre.py status`: em que etapa o projeto está.
2. O "Onde parei" do último diário (`orquestra/diarios/`; se o dia tem partes, a parte mais recente).
3. Só o que a tarefa precisa: [[geral-contexto]] → contexto da funcionalidade → decisões → plano (proposta).

## Passagem de turno (antes de fechar o chat)

1. Registrar o que a sessão produziu (Etapas vitais).
2. Diário de hoje com "Onde parei": **próximo passo**, threads abertas, dúvidas.
3. `cofre.py status --atualizar`, `verificar` com zero ERRO e commit do cofre.
4. Avisar: "pode abrir um chat novo".

Detalhe: [[manual-da-orquestra#🔄 Passagem de turno]] (ler pela CLI).

## Regras e decisões do projeto

Moram em `orquestra/funcionalidades/geral/`, uma decisão por nota (grafia, documentos-fonte, exceções de nome, repositórios, acesso). **Busque lá pela CLI** (`obsidian_search` com `path="orquestra/funcionalidades/geral"`) antes de agir. Regra nova de projeto vira decisão ali, com aval do humano, nunca texto neste arquivo.

## Estrutura

`orquestra/`: `entradas/` (sem destino), `funcionalidades/` (contexto, plano e decisões; `geral/` é o projeto), `referencias/` (consulta e manuais), `diarios/`, `modelos/` (esqueletos e `cofre.py`), `arquivos/` (finalizadas), `bugs/` e `padroes` (bloco no fim deste arquivo, formato antigo). Fora dela: `MOCs/` ([[moc-orquestra]] é o mapa) e `Anexos/`. Regras completas: [[manual-da-orquestra]] e [[manual-do-cerebro]].

## Quem escreve

- **Só o orquestrador escreve neste cofre**; subagente lê e devolve relatório (`orquestra/modelos/modelo-relatorio-subagente.md`).
- **Plano é proposta; decisão só com aval do humano**, uma por nota.
- **Decisão muda:** campo Alteração reescrito no estado atual (cronologia no diário); ainda não aplicada → muda na própria nota + 1 linha no diário; já aplicada → nota nova com `substitui:`, a antiga vira `substituida`; só um ponto muda → nota nova só dele, a antiga segue `aprovada` com a linha reescrita + link.
- **Nunca apagar sem confirmação**; na dúvida, arquivar. Mover para `arquivos/` só com confirmação.
- Detalhe: [[manual-da-orquestra#3. ✍️ Quem escreve o quê]] (ler pela CLI).

## Consultar antes e alimentar assim que chega

- **Antes:** bug → `bugs/` por sintoma e decisões; mudança estrutural → decisões (contradizer só citando a nota); área sensível → contexto, `referencias/`, bugs; nota nova → `modelos/`; algo parecido → `arquivos/`.
- **Assim que chega** (sem esperar o fim da sessão): relatório de subagente → registrar; bug não trivial → nota em `bugs/` (reapareceu: atualizar); decisão aprovada → nota de decisão + nota responsável; tarefa concluída → contexto e plano; etapa concluída → roteiro e `status --atualizar`; sessão relevante → diário; dúvidas → uma pergunta única ao humano. Bug trivial não vira nota.
- Detalhe: [[manual-da-orquestra#6. 🔎 Quando consultar e quando alimentar]] (ler pela CLI).

## Convenções

- Português brasileiro; arquivos e pastas em kebab-case, sem acento, com prefixo da funcionalidade; datas AAAA-MM-DD; `[[wikilinks]]` sempre; nota do `Vault` é citada como texto `Nome (no Vault)`, nunca como wikilink.
- Nota operacional: modelo próprio, frontmatter `tipo`, `status`, `criado`, `funcionalidade`; `referencias/` e `MOCs/`: Manual do Cérebro.
- Fato do humano preservado; interpretação do agente separada; suposição `[a confirmar]`. Tarefa do humano vai para o TickTick. Nunca editar `.obsidian/` sem pedido.
- Detalhe: [[manual-da-orquestra#7. 📏 Convenções do cofre de projeto]] (ler pela CLI).

## Padronização (obrigatório)

- **Despadronização:** corrija primeiro a regra (decisão em `geral/` e `padroes` (bloco no fim deste arquivo, formato antigo)), depois as notas. O `cofre.py verificar` lê o bloco `padroes` e dá ERRO no que fugir dele.
- **Nome do projeto:** uma grafia só, a do documento-fonte; variante encontrada entra no `padroes`.
- **Numeração de fonte:** cite pela numeração da nota que transcreve o documento; a do original só dentro da transcrição.
- **Nomes:** kebab-case sem acento; exceção só registrada em decisão, com o motivo.
- **Tamanho:** passou do `limite-palavras` do `padroes` (bloco no fim deste arquivo, formato antigo) → divida: nota nova `<original>-<assunto>`, 1 frase + link na original, links nos dois sentidos.
- **Uma versão só:** mudou fato, regra, valor ou nome → reescreva toda nota que o cita (sem aviso por cima de texto velho) e registre `antigo:` no `padroes`; cronologia só no histórico.
- **`[a preencher]`:** o humano ainda não definiu; pergunte ou anote no "Onde parei", nunca invente.
- Detalhe: [[manual-da-orquestra#7. 📏 Convenções do cofre de projeto]] (ler pela CLI).

## Etapas vitais (obrigatório)

Toda escrita neste cofre (criar, mudar, mover ou copiar nota):

1. **Gatilho:** qual linha de "alimentar" pede a escrita.
2. **Buscar e varrer o impacto:** nota existe? atualize. Mudou um estado? busque o antigo pela CLI (sinônimos, inglês, backlinks) e liste toda nota.
3. **Classificar:** tipo → modelo → pasta → nome; aval do humano quando a regra exige.
4. **Escrever** a partir de `orquestra/modelos/`, nunca do zero.
5. **Conectar** nos dois sentidos: Conexões e hub (`<func>-contexto` ou `moc-orquestra`).
6. **Propagar:** reescreva cada nota da varredura, `antigo:` no `padroes`, roteiro, contexto, diário, decisão substituída.
7. **Verificar:** `python orquestra/modelos/cofre.py verificar .` com **zero ERRO**; só então "pronto".

Detalhe: [[manual-da-orquestra#🚦 Etapas vitais]] (ler pela CLI). Modelos e manuais daqui não se editam: o original fica no `Vault` e chega por `cofre.py sincronizar`.

## Commits

- **Vale neste cofre e em todo repositório do projeto.** Formato: `{emoji} {tipo}(escopo): Descrição`, em inglês, imperativo; escopo só da lista abaixo; uma mudança por commit; só no nome do humano, sem `Co-Authored-By` nem link de sessão.
- **Quando:** a cada registro concluído e na passagem de turno.
- **Passos:** `.git` na raiz do `the-mind-hub` (peça a pasta e permissão para apagar); `verificar` zero ERRO; sem identidade, `git -c user.name=... -c user.email=...`, nunca `git config`; cofre e README em commits separados.
- Detalhe: Padrão de commit (no Vault) e Commitar no the-mind-hub (no Vault) (ler pela CLI).

<!-- projeto:escopos -->
- **Escopos deste cofre** (lista fechada; muda só com aval): `PrepBTG-vault` (notas deste cofre), `readme` (README da raiz do `the-mind-hub`, commit separado).
<!-- /projeto:escopos -->

## Acesso e ações irreversíveis

- Onde fica cada coisa e o que o agente pode sem perguntar: decisão em `funcionalidades/geral/` (busque "acesso" e "repositório"). Sem decisão, pedir antes.
- Apagar ou sobrescrever o que não se recupera: sempre pedir confirmação. No projeto prático (repositório, `--force`, branch principal): Manual da Orquestra - Perfil projeto prático (no Vault) (ler pela CLI).

## Como buscar (obrigatório)

Busque **antes** de responder ou escrever; não responda de memória.

1. **Obsidian CLI: obrigatória** (índice do app; precisa do Obsidian aberto). MCP `obsidian-cli`: `obsidian_search`, `obsidian_read`, `obsidian_backlinks`, `obsidian_help`, com `vault="PrepBTG-vault"`. No terminal: `obsidian vault="PrepBTG-vault" search query="termo"`.
   - **Ferramenta adiada não é CLI falhando:** carregue com `ToolSearch` (`select:mcp__remote-devices__obsidian-cli__obsidian_search,mcp__remote-devices__obsidian-cli__obsidian_read,mcp__remote-devices__obsidian-cli__obsidian_backlinks,mcp__remote-devices__obsidian-cli__obsidian_help`).
   - **Projeto do claude.ai não é o cofre:** os documentos dele (`project_read` e afins) são cópia que envelhece; nunca leia nem escreva o cofre por eles. Escrita é pelo shell (`device_bash`), com a pasta `the-mind-hub` conectada. Bloco para as instruções do projeto: [[modelo-instrucoes-do-projeto-claude]].
   - **Ler também é pela CLI:** `cat`, `grep`, `find` ou `Read` em nota é erro de processo. O shell só escreve notas e roda o `cofre.py`.
2. Tente sinônimos e termos em inglês antes de concluir que não existe nota.
3. **CLI falhou:** não troque de caminho em silêncio.
   - **Obsidian recém-aberto:** `Command "read" not found` logo depois de abrir o app é carregamento: espere alguns segundos e repita.
   - **Reporte** ao humano, com a mensagem de erro, e **analise** com Obsidian CLI via MCP não carrega (no Vault) e os bugs de `orquestra/bugs/` (busque "obsidian cli").
   - Só se o humano não puder corrigir agora: busque nos `.md` (com `aliases`) e **avise** que foi sem a CLI. Subagente ou worktree sem CLI: o mesmo, dito no relatório.
4. Ao usar uma nota, cite o nome dela na resposta.

## Se houver outros cofres conectados

Cada cofre tem o próprio `CLAUDE.md`. O que vale **só para PrepBTG** fica aqui; conhecimento geral (inclusive lição de bug que vale fora daqui) vai para o `Vault`.

## Blocos do projeto (formato antigo)

Regras deste projeto ainda no formato antigo. Migrar cada uma para decisão em `orquestra/funcionalidades/geral/` e o bloco `padroes` para `orquestra/padroes.md`; o `cofre.py sincronizar` preserva estes blocos até lá.

<!-- projeto:padronizacao -->
- **Grafia do nome:** `PrepBTG`, conforme o nome do cofre (`PrepBTG-vault`) definido pelo humano em 2026-11-05.
- **Documentos-fonte e numeração:** [a preencher: quais documentos têm seções próprias e como cada um é citado no cofre].
- **Exceções registradas:** [a preencher: nenhuma até a decisão de estrutura do código; cada exceção cita a decisão e o motivo].
- **Limite de tamanho:** 2073 palavras, padrão herdado do `stonebid-vault` [a preencher: confirmar ou trocar pela maior nota deste projeto].
<!-- /projeto:padronizacao -->

<!-- projeto:padroes -->
```padroes
# termo fora do padrão => forma certa   ("re:" no início = expressão regular)
# antigo: termo do estado substituído => estado atual (nota dona)   (ERRO só fora do histórico)
limite-palavras: 2073
antigo: 5 blocos => 6 passos (geral-decisao-2026-11-05-esqueleto-de-6-passos)
antigo: Python só quando o SQL fica difícil => SQL extrai, Python analisa (geral-decisao-2026-11-05-trilha-sql-e-python)
antigo: 44 questões => 51 questões (questoes-por-cenario)
antigo: 15 minutos com esta tabela => cenário concreto do C8 (geral-decisao-2026-11-05-treino-por-cenarios-concretos)
antigo: T8 diagnóstico + T9 D2 e D3 => T8 começa pela trilha didática de SQL (geral-decisao-2026-11-06-trilha-didatica-antes-dos-drills)
antigo: diagnóstico com S2, S3, S8 e S13 => trilha didática de SQL antes dos drills (geral-decisao-2026-11-06-trilha-didatica-antes-dos-drills)
antigo: T8 fase A: M0 de => T8 fase A: M1, no sábado de manhã (banco-mocado-plano)
antigo: M0 e M1 (leves => M0 feito na sexta; M1 no sábado de manhã (banco-mocado-plano)
antigo: 📊 M1: 3 de 7 => barra de progresso visual (geral-decisao-2026-11-06-progresso-a-cada-questao)
antigo: ▓▓▓▓░░░░░░  3/7 => `▰▰▰▰▱▱` 4 de 6 (geral-decisao-2026-11-06-progresso-a-cada-questao)
antigo: M1 de [[trilha-sql-didatica]] no sábado de manhã, depois M2 => T8 fase A: M3 no sábado à tarde (banco-mocado-plano)
antigo: M2 de [[trilha-sql-didatica]] no sábado, depois M3 => T8 fase A: M3 no sábado à tarde (banco-mocado-plano)
antigo: M3 de [[trilha-sql-didatica]] no sábado à tarde => T8 fase A: M4 no domingo de manhã (banco-mocado-plano)
antigo: T8 trilha: M5 a M7 => T8 trilha: M4 e M5 no domingo de manhã (banco-mocado-plano-agenda)
antigo: depois O7.6 e O7.3 => depois o acumulado da O7.3 e os empates da O7.2 (trilha-sql-didatica-avancado)
antigo: acumulado da O7.4 => acumulado da O7.3 (trilha-sql-didatica-avancado)
antigo: até 6 questões por módulo => 5 questões por módulo e uma bônus (geral-decisao-2026-11-08-cinco-questoes-e-bonus)
antigo: até 6 questões cada => 5 questões e 1 bônus cada (banco-mocado-plano-agenda)
antigo: T8 fase A: M4 de => T8 fase A: M7 de (banco-mocado-plano)
antigo: T8 fase A: M5 de => T8 fase A: M7 de (banco-mocado-plano)
antigo: M4 ✅ e M5, 5 questões => M4 ✅ e M5 ✅ (banco-mocado-plano-agenda)
antigo: variante de O5.5 => variante de O5.4 (trilha-sql-didatica-extras)
antigo: variante de O7.4 => variante de O7.3 (trilha-sql-didatica-extras)
antigo: variante de O8.5 => variante de O8.4 (trilha-sql-didatica-extras)
antigo: variante de O3.6 => variante de O3.5 (trilha-sql-didatica-extras)
antigo: T8 fase A: avaliador do M5 => T8 fase A: M7 de (banco-mocado-plano)
antigo: agente avaliador do M5 | => avaliador do M5 ✅ (banco-mocado-plano-agenda)
antigo: T8 trilha: M6 e M7 => M6 pausado em 2 de 5 e M7 antes do simulado das 15h (banco-mocado-plano-agenda)
antigo: razão volume ÷ renda => razão créditos ÷ renda anual (trilha-sql-didatica-avancado)
antigo: Próximo: avaliador do M5 => avaliador do M5 rodado (banco-mocado-contexto)
antigo: M7 antes do simulado das 15h => M7 pausado em 2 de 5 (banco-mocado-plano-agenda)
antigo: antes do simulado com um amigo às 15h de domingo => M7 pausado em 2 de 5 (banco-mocado-plano)
antigo: pergunta curta de checagem a cada ideia => 2 checagens por módulo e exercícios cobrindo todos os conceitos (geral-decisao-2026-11-09-revisao-leve-do-dia-do-teste)
antigo: vale também para as questões do M5 e do M7 => M5 e M7 com exercícios próprios (geral-decisao-2026-11-09-revisao-leve-do-dia-do-teste)
antigo: pausado em 2 de 5 (faltam O7.3 => revisão didática leve de M0 a M8 (banco-mocado-plano)
antigo: re:2026-11-09( \(segunda\))?, 13h => teste em 2026-11-09, 15h (processo-seletivo-btg)
antigo: 13h teste => 15h teste (banco-mocado-plano-agenda)
antigo: **1 extra opcional** => 1 questão só por módulo (geral-decisao-2026-11-09-revisao-leve-do-dia-do-teste)
antigo: as 2 questões por módulo da revisão => a questão única por módulo da revisão (geral-decisao-2026-11-09-revisao-leve-do-dia-do-teste)
antigo: (6 no total: M0, M1, M2, M3, M4 e M6) => 8 no total, com M5 e M7 por último (geral-decisao-2026-11-09-revisao-leve-do-dia-do-teste)
antigo: Agora é o estudo de caso => conversa com o head do time em 2026-11-11, 14h (processo-seletivo-btg)
antigo: o estudo de caso é o atual => a conversa com o head é a atual (processo-seletivo-btg)
antigo: etapa final conhecida do processo => conversa com o head do time (processo-seletivo-btg)
antigo: referência técnica → liderar → sócio pelo resultado => aprender → entregar → preparar quem me substitui → liderar (roteiro-conversa-com-o-head)
antigo: entregar → liderar → sócio pelo resultado => ciclo da casa com o sucessor (geral-decisao-2026-11-11-modulos-da-conversa-com-o-head)
antigo: entregar, liderar, virar sócio pelo mérito => aprender, entregar, formar o sucessor, liderar (roteiro-conversa-com-o-head)
antigo: os 6 pilares têm prova => os 7 pilares têm prova (roteiro-conversa-com-o-head)
antigo: re:2026-11-11(,| \(quarta\),) 14h => conversa com o head em 2026-11-11, 18h, com 30 min (processo-seletivo-btg)
antigo: ler às 13h30 => ler às 17h30 (roteiro-conversa-com-o-head-cartao)
antigo: viram decisão segura => processo bem definido e dado bem estruturado geram decisão confiável (roteiro-conversa-com-o-head)
```
<!-- /projeto:padroes -->

<!-- projeto:repositorios -->
| O quê | Onde |
|---|---|
| Repositório de código | [a confirmar] |
| Pasta do projeto no computador | [a preencher] |
| Cofre | `C:\Users\Ylderlan\Documents\Projetos\the-mind-hub\PrepBTG-vault`, ligado ao chat como pasta real (o projeto do claude.ai fica vazio) |
| Banco de treino | `\\wsl.localhost\Ubuntu\home\ylderlan\docker\containers\mysql-estudos` (container `mysql-compliance`) |
| Cópia do banco para a IA | `C:\Users\Ylderlan\Documents\Projetos\mysql-estudos-dump` ([[esquema-do-banco-compliance]]) |

- **Acesso na etapa de programação:** [a preencher: se o humano autoriza, durante a etapa de programação, pedir a pasta do projeto ou anexar o repositório sem perguntar antes].
<!-- /projeto:repositorios -->
