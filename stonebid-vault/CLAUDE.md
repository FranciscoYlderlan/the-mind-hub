# Cofre "stonebid-vault" — Stonebid (guia para agentes)

Cofre do Obsidian: a **memória do projeto Stonebid**: regras de negócio, decisões, bugs e o que foi estudado para o projeto. Este arquivo é índice: cada regra em 1 linha, com link para o detalhe (ler pela CLI quando a tarefa tocar no assunto).

Nome do cofre no Obsidian: `stonebid-vault`.

> **Leitura: Obsidian CLI primeiro.** Antes de qualquer outra ferramenta (`cat`, `grep`, `Read`, subagente, documentos do projeto do claude.ai), leia e busque pela Obsidian CLI, com `vault="stonebid-vault"`. Ferramenta `obsidian_*` ausente pode estar só adiada: `ToolSearch`. Ver "Como buscar".

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
3. `cofre.py status --atualizar` e `verificar` com zero ERRO.
4. Avisar: "pode abrir um chat novo".

Detalhe: [[manual-da-orquestra#🔄 Passagem de turno]] (ler pela CLI).

## Regras e decisões do projeto

Moram em `orquestra/funcionalidades/geral/`, uma decisão por nota (grafia, documentos-fonte, exceções de nome, repositórios, acesso). **Busque lá pela CLI** (`obsidian_search` com `path="orquestra/funcionalidades/geral"`) antes de agir. Regra nova de projeto vira decisão ali, com aval do humano, nunca texto neste arquivo.

## Estrutura

`orquestra/`: `entradas/` (sem destino), `funcionalidades/` (contexto, plano e decisões; `geral/` é o projeto), `referencias/` (consulta e manuais), `diarios/`, `modelos/` (esqueletos e `cofre.py`), `arquivos/` (finalizadas), `bugs/` e [[padroes]]. Fora dela: `MOCs/` ([[moc-orquestra]] é o mapa) e `Anexos/`. Regras completas: [[manual-da-orquestra]] e [[manual-do-cerebro]].

## Quem escreve

- **Só o orquestrador escreve neste cofre**; subagente lê e devolve relatório (`orquestra/modelos/modelo-relatorio-subagente.md`).
- **Plano é proposta; decisão só com aval do humano**, uma por nota. Decisão que contradiz outra: nota nova com `substitui:`, a antiga vira `substituida`.
- **Nunca apagar sem confirmação**; na dúvida, arquivar. Mover para `arquivos/` só com confirmação.
- Detalhe: [[manual-da-orquestra#3. ✍️ Quem escreve o quê]] (ler pela CLI).

## Consultar antes e alimentar no fim

- **Antes:** bug → `bugs/` por sintoma e decisões; mudança estrutural → decisões (contradizer só citando a nota); área sensível → contexto, `referencias/`, bugs; nota nova → `modelos/`; algo parecido → `arquivos/`.
- **No fim:** bug não trivial → nota em `bugs/` (reapareceu: atualizar); decisão aprovada → nota de decisão + nota responsável; tarefa concluída → contexto e plano; etapa concluída → roteiro e `status --atualizar`; sessão relevante → diário; dúvidas → uma pergunta única ao humano. Bug trivial não vira nota.
- Detalhe: [[manual-da-orquestra#6. 🔎 Quando consultar e quando alimentar]] (ler pela CLI).

## Convenções

- Português brasileiro; arquivos e pastas em kebab-case, sem acento, com prefixo da funcionalidade; datas AAAA-MM-DD; `[[wikilinks]]` sempre.
- Nota operacional: modelo próprio, frontmatter `tipo`, `status`, `criado`, `funcionalidade`; `referencias/` e `MOCs/`: Manual do Cérebro.
- Fato do humano preservado; interpretação do agente separada; suposição `[a confirmar]`. Tarefa do humano vai para o TickTick. Nunca editar `.obsidian/` sem pedido.
- Detalhe: [[manual-da-orquestra#7. 📏 Convenções do cofre de projeto]] (ler pela CLI).

## Padronização (obrigatório)

- **Despadronização:** corrija primeiro a regra (decisão em `geral/` e [[padroes]]), depois as notas. O `cofre.py verificar` lê o bloco `padroes` e dá ERRO no que fugir dele.
- **Nome do projeto:** uma grafia só, a do documento-fonte; variante encontrada entra no `padroes`.
- **Numeração de fonte:** cite pela numeração da nota que transcreve o documento; a do original só dentro da transcrição.
- **Nomes:** kebab-case sem acento; exceção só registrada em decisão, com o motivo.
- **Tamanho:** passou do `limite-palavras` do [[padroes]] → divida: nota nova `<original>-<assunto>`, 1 frase + link na original, links nos dois sentidos.
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

- **Formato:** `{emoji} {tipo}(stonebid-vault): Descrição`, em inglês, imperativo; uma mudança por commit; só no nome do humano, sem `Co-Authored-By` nem link de sessão.
- **Passos:** `.git` na raiz do `the-mind-hub` (peça a pasta e permissão para apagar); `verificar` zero ERRO; sem identidade, `git -c user.name=... -c user.email=...`, nunca `git config`; cofre e README em commits separados.
- Detalhe: Padrão de commit (no Vault) e Commitar no the-mind-hub (no Vault) (ler pela CLI).

## Repositórios e acesso

- Onde ficam e o que o agente pode sem perguntar: decisão em `funcionalidades/geral/` (busque "repositório"). Sem decisão, pedir antes.
- Apagar arquivos, forçar push ou mexer na branch principal fora do CI/CD: sempre pedir confirmação.

## Como buscar (obrigatório)

Busque **antes** de responder ou escrever; não responda de memória.

1. **Obsidian CLI: obrigatória** (índice do app; precisa do Obsidian aberto). MCP `obsidian-cli`: `obsidian_search`, `obsidian_read`, `obsidian_backlinks`, `obsidian_help`, com `vault="stonebid-vault"`. No terminal: `obsidian vault="stonebid-vault" search query="termo"`.
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

Cada cofre tem o próprio `CLAUDE.md`. O que vale **só para Stonebid** fica aqui; conhecimento geral (inclusive lição de bug que vale fora daqui) vai para o `Vault`.
