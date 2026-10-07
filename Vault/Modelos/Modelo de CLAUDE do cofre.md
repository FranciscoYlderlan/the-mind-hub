# Cofre "{{nome-da-pasta}}" — {{projeto}} (guia para agentes)

Este é um cofre do Obsidian: uma pasta de notas Markdown. Ele é a **memória do projeto {{projeto}}**: {{para quê, em meia frase}}. Este arquivo é o índice: ele diz onde está cada coisa e quando consultar. Os detalhes moram nas notas.

Nome do cofre no Obsidian: `{{nome-da-pasta}}`. Repositórios de código, links e pasta local: seção "Repositórios e acesso", abaixo.

## Seu papel

- **Se você é a sessão principal, você é o orquestrador.** Seu trabalho é ajudar o humano a gerir várias threads de agentes: ler o cofre, planejar, despachar subagentes, juntar os relatórios, falar com o humano e registrar no cofre. Não precisa que ninguém explique isso de novo.
- **O orquestrador não implementa**, não lê código extenso e não faz pesquisa longa: delega, usando os cartões de papel de `orquestra/modelos/modelo-briefing-subagente.md`.
- **Se você recebeu um briefing com "Papel:", você é subagente**: siga o cartão do seu papel, não escreva neste cofre e devolva o relatório.
- **Orçamento de 100 mil tokens de conversa** (linha Messages do `/context`). Ao fim de cada ciclo de tarefa, peça ao humano o `/context`. Chegou a 100 mil: passagem de turno (abaixo) e chat novo. Subagentes não contam: só o briefing e o relatório entram na sua janela.

## Início de sessão (orquestrador)

1. `python orquestra/modelos/cofre.py status`: em que etapa o projeto está.
2. O "Onde parei" do último `orquestra/diarios/diario-*.md`: próximo passo, threads abertas, dúvidas.
3. A ordem de leitura abaixo, só no que a próxima tarefa precisa.

## Passagem de turno (antes de fechar o chat)

1. Registrar o que a sessão produziu (Etapas vitais B).
2. Diário de hoje com "Onde parei": **próximo passo**, threads abertas (subagentes em andamento ou relatórios não registrados) e dúvidas para o humano.
3. `cofre.py status --atualizar` e `cofre.py verificar` com zero ERRO.
4. Avisar o humano: "pode abrir um chat novo".

## Ordem de leitura (toda tarefa)

1. **Onde o projeto está:** `python orquestra/modelos/cofre.py status` ou o roteiro `orquestra/funcionalidades/geral/geral-plano.md` (etapas, status e notas de cada etapa).
2. `orquestra/funcionalidades/geral/geral-contexto.md`: o projeto inteiro, dial e modelo de IA.
3. Contexto da funcionalidade: `orquestra/funcionalidades/<func>/<func>-contexto.md`.
4. Decisões: `<func>-decisao-*.md` da funcionalidade e de `geral/`.
5. Só então o plano: `<func>-plano.md` (proposta, não decisão).

Regras completas: `orquestra/referencias/manual-da-orquestra.md`. Regras de escrita: `orquestra/referencias/manual-do-cerebro.md`.

## Mapa no Obsidian

[[moc-orquestra]] · [[geral-plano]] · [[geral-contexto]] · [[Manual da Orquestra]] · [[Manual do Meu Cérebro no Obsidian]]

## Estrutura

| Pasta | O que mora ali |
|---|---|
| `orquestra/entradas/` | Brainstorms e anotações sem destino |
| `orquestra/funcionalidades/` | Em construção: contexto, plano e decisões de cada uma; `geral/` é o projeto inteiro |
| `orquestra/referencias/` | Material de consulta, acervo de abordagens, cópias dos manuais |
| `orquestra/diarios/` | `diario-AAAA-MM-DD.md` |
| `orquestra/modelos/` | Esqueletos de nota (incluindo `modelo-nota.md`), briefing e relatório de subagente |
| `orquestra/arquivos/` | Funcionalidades finalizadas |
| `orquestra/bugs/` | `bug-<titulo>-AAAA-MM-DD.md`, só bugs não triviais resolvidos |
| `MOCs/` | Mapas de assunto (`moc-tema.md`); `moc-orquestra.md` é o mapa do projeto |
| `Anexos/` | Imagens e PDFs |

## Quem escreve

- **Só a sessão principal (orquestrador) escreve neste cofre**, no fim do trabalho. Subagentes leem e devolvem relatório (`orquestra/modelos/modelo-relatorio-subagente.md`).
- Plano é proposta da IA. Nota de decisão só nasce depois do aval do humano: uma decisão por nota.
- Decisão nova que contradiz outra: nota nova com `substitui:`; a antiga vira `status: substituida`.
- Nunca apagar sem confirmação; na dúvida, arquivar. Mover para `arquivos/` só com confirmação.

## Consultar (antes)

- Bug: buscar em `orquestra/bugs/` por sintoma e ler as decisões.
- Arquitetura ou mudança estrutural: ler as decisões; contradizer só explicitamente, citando a nota.
- Área sensível: contexto, `referencias/` e bugs da área.
- Nota nova: `modelos/`. Algo parecido já feito: `arquivos/`.

## Alimentar (no fim)

- Bug não trivial resolvido → nota em `bugs/`. Bug que reaparece → atualizar a nota existente.
- Decisão aprovada → nota de decisão + atualizar a nota responsável.
- Tarefa concluída → contexto ("o que já foi feito") e verificação no plano.
- Etapa do roteiro concluída → `concluida`, data e notas geradas no `geral-plano`; rodar `cofre.py status --atualizar`.
- Sessão relevante → `diarios/`.
- Candidatos e dúvidas → uma pergunta única ao humano no fim.
- Bug trivial (typo, compilação, layout simples) não vira nota.

## Convenções

- Português brasileiro. Arquivos e pastas em kebab-case, sem acento, com prefixo da funcionalidade nas notas operacionais.
- Datas AAAA-MM-DD em nome de arquivo e frontmatter.
- `[[wikilinks]]` sempre; nota sem link fica perdida.
- Notas operacionais (contexto, plano, decisão, bug, diário) seguem o modelo próprio, sem analogia. Notas de `referencias/` e `MOCs/` seguem o Manual do Cérebro (`modelo-nota.md` ou `modelo-referencia.md`). Tamanho de qualquer nota: ver Padronização.
- Frontmatter operacional: `tipo`, `status`, `criado`, `funcionalidade`; `aliases` opcional (em bug: os sintomas).
- Fatos do humano preservados (fato substituído sai da nota de estado e fica no diário); interpretação do agente em seção separada; suposição marcada `[a confirmar]`.
- Tarefa de agente mora no plano; tarefa do humano vai para o TickTick.
- Nunca edite `.obsidian/` sem pedido explícito.

## Padronização (obrigatório)

Despadronização é sintoma: a causa é uma regra que faltou aqui. Ao achar uma, **corrija primeiro a regra** (nesta seção, no bloco `padroes` ou na decisão que define o nome) e só depois as notas. O `cofre.py verificar` lê o bloco `padroes` e dá ERRO no que fugir dele.

- **Nome do projeto:** uma grafia só, igual à do documento-fonte (contrato, glossário). Toda variante encontrada entra no bloco `padroes`.
- **Numeração de fonte:** documento com seções próprias (enunciado, contrato) é citado pela numeração da nota que o transcreve no cofre. A numeração do original só aparece dentro da transcrição. A origem de um requisito aponta só as seções onde ele está escrito, separadas por vírgula.
- **Nomes de arquivo e pasta:** kebab-case, sem acento, nas notas e no código. Exceção só vale se estiver escrita, com o motivo (convenção da linguagem ou exigência de ferramenta), na decisão que criou a regra e listada em "Regras deste projeto". Sem isso, é erro.
- **Tamanho:** o limite de ~350 palavras do Manual do Cérebro **não vale** em cofre de projeto, mas há limite: o `limite-palavras` do bloco `padroes`, fixado pela maior nota registrada quando a regra nasceu. Os manuais e modelos copiados do `Vault` ficam fora da conta.
- **Passou do limite:** divida a nota. A parte nova vira nota própria, com o nome da original + `-<assunto>` (em bug e diário, o assunto entra depois da data), o mesmo modelo e o mesmo frontmatter. Na original ficam 1 frase + `[[link]]` no lugar do trecho, e a nova aponta de volta nas Conexões.
- **Uma versão só:** nota de estado (contexto, decisão vigente, plano, referência, MOC, este `CLAUDE.md`) diz só como as coisas são **agora**. Mudou um fato, regra, valor ou nome: reescreva o trecho em **toda** nota que o cita (varredura de impacto, Etapas vitais 2 e 6) e registre o estado antigo como linha `antigo:` no bloco `padroes`. É proibido manter o texto velho com aviso por cima (`onde esta nota fala em X, vale Y`). A cronologia mora só no histórico: diários, bugs, decisão `substituida`, seções "Histórico", "Mudanças", "Linha do tempo" e "O que já foi feito", linhas `origem:`/`substitui:` e os campos Proposta, Alteração e Motivo da decisão. O `verificar` dá ERRO em termo `antigo:` ou aviso de prevalência fora desses lugares.
- **Blocos do projeto:** o que fica entre `<!-- projeto:... -->` e `<!-- /projeto:... -->` é deste projeto. O `cofre.py sincronizar` refaz o resto do arquivo a partir do modelo do `Vault` e guarda esses blocos como estão. Regra de projeto mora dentro de um bloco; fora dele, ela some na próxima sincronização.
- **`[a preencher]`:** parte que o humano ainda não definiu. O agente não inventa o valor: pergunta ao humano ou anota a dúvida no "Onde parei" do diário. O `verificar` mostra cada `[a preencher]` como AVISO.

### Regras deste projeto

<!-- projeto:padronizacao -->
- **Grafia do nome:** `{{projeto}}`, conforme [a preencher: documento-fonte da grafia, ex.: contrato ou glossário].
- **Documentos-fonte e numeração:** [a preencher: quais documentos têm seções próprias e como cada um é citado no cofre].
- **Exceções registradas:** [a preencher: nenhuma até a decisão de estrutura do código; cada exceção cita a decisão e o motivo].
- **Limite de tamanho:** 2073 palavras, padrão herdado do `stonebid-vault` [a preencher: confirmar ou trocar pela maior nota deste projeto].
<!-- /projeto:padronizacao -->

<!-- projeto:padroes -->
```padroes
# termo fora do padrão => forma certa   ("re:" no início = expressão regular)
# antigo: termo do estado substituído => estado atual (nota dona)   (ERRO só fora do histórico)
limite-palavras: 2073
```
<!-- /projeto:padroes -->

## Etapas vitais (obrigatório)

Toda escrita neste cofre (criar, mudar, mover ou copiar nota) segue estas etapas. Pular uma é erro de processo. Tabela completa: [[Manual da Orquestra#🚦 Etapas vitais]].

1. Gatilho: qual linha de "Alimentar" pede a escrita.
2. Buscar antes e varrer o impacto: a nota existe? Atualize em vez de duplicar. Mudou um fato, regra, valor ou nome? Busque pela CLI o estado antigo (termo, sinônimos, inglês, números) e o tema, mais os backlinks da nota dona, e liste **toda** nota que aparecer.
3. Classificar: tipo → modelo → pasta → nome. Aval do humano quando a regra exige.
4. Escrever a partir de `orquestra/modelos/`, nunca do zero.
5. Conectar nos dois sentidos: Conexões na nota e link de volta no hub (`<func>-contexto`) ou em `moc-orquestra`.
6. Propagar: reescreva no estado atual cada nota da varredura ("Uma versão só", em Padronização) e acrescente o estado antigo como `antigo:` no bloco `padroes`; roteiro (etapa concluída, notas geradas, `cofre.py status --atualizar`), contexto ("o que já foi feito"), diário (com os termos varridos e as notas tocadas), decisão substituída.
7. Rodar `python orquestra/modelos/cofre.py verificar .` → **zero ERRO**. Só então "pronto".

Modelos e manuais deste cofre não se editam aqui: o original fica no `Vault` e chega por `cofre.py sincronizar`.

## Commits

Este cofre mora dentro do repositório `the-mind-hub`, e o `.git` fica na raiz dele, não aqui. Commit segue o padrão de trabalho do humano, o mesmo em todo projeto.

- **Formato** ([[Padrão de commit]]): `{emoji} {tipo}(escopo): Descrição`, por exemplo `:page_facing_up: docs({{nome-da-pasta}}): Add ...`. Tipo por extenso e emoji da tabela de tipos; escopo sempre presente, entre parênteses; descrição em inglês, no imperativo, com maiúscula e sem ponto final. Uma mudança por commit. Commit só no nome do humano: sem `Co-Authored-By` nem link de sessão de IA, mesmo quando um agente commita.
- **Passos** ([[Commitar no the-mind-hub]]):
  1. Sessão só com a pasta deste cofre? **Peça acesso à pasta `the-mind-hub`** e permissão para apagar nela (o git cria e remove arquivos `.lock`).
  2. `cofre.py verificar` com zero ERRO em cada cofre alterado.
  3. Sessão sem identidade do git ("Author identity unknown"): o autor dos commits anteriores, passado só no comando (`git -c user.name=... -c user.email=... commit`). Nunca `git config`.
  4. Commit da raiz do `the-mind-hub`, um assunto por commit; commit de cofre e do README são separados.

## Repositórios e acesso

<!-- projeto:repositorios -->
| O quê | Onde |
|---|---|
| Repositório de código | {{link ou caminho}} |
| Pasta do projeto no computador | [a preencher] |

- **Acesso na etapa de programação:** [a preencher: se o humano autoriza, durante a etapa de programação, pedir a pasta do projeto ou anexar o repositório sem perguntar antes].
<!-- /projeto:repositorios -->

- Fora da etapa de programação (planejamento, cofre, pesquisa), o acesso aos repositórios segue a regra normal: pedir antes.
- Apagar arquivos, forçar push ou mexer na branch principal fora do fluxo de CI/CD sempre pede confirmação.

## Como buscar (obrigatório)

**Sempre** que precisar recuperar contexto, decisões, regras ou qualquer instrução registrada antes, busque neste cofre **antes** de responder ou escrever. Não responda de memória quando o assunto pode estar numa nota.

1. **Obsidian CLI: obrigatória** (usa o índice do app, então acha por aliases, tags e links). Precisa do Obsidian aberto.
   - Sessão na nuvem ligada ao computador: use as ferramentas do servidor MCP `obsidian-cli` (`obsidian_search`, `obsidian_read`, `obsidian_backlinks`, `obsidian_help`), com `vault="{{nome-da-pasta}}"`.
   - **Ler também é pela CLI.** Abrir ou buscar nota com `cat`, `grep`, `find`, `Read` ou outro comando de shell é erro de processo, mesmo com acesso à pasta. O shell serve só para **escrever** notas e rodar o `cofre.py`. A única exceção é o plano B do passo 3, sempre avisado.
   - Terminal no Windows:
     - Busca: `obsidian vault="{{nome-da-pasta}}" search query="termo" limit=10`
     - Ler uma nota: `obsidian vault="{{nome-da-pasta}}" read file="nome-da-nota"`
     - Quem aponta para uma nota: `obsidian vault="{{nome-da-pasta}}" backlinks file="nome-da-nota"`
     - Lista completa de comandos: `obsidian help`
2. Tente sinônimos e termos em inglês antes de concluir que não existe nota.
3. **CLI falhou** (ferramentas `obsidian_*` ausentes, comando não encontrado, "The CLI is unable to find Obsidian"): **não troque de caminho em silêncio**.
   - **Reporte** ao humano o que falhou, com a mensagem de erro.
   - **Analise** com a nota [[Obsidian CLI via MCP não carrega]] e com os bugs de `orquestra/bugs/` deste cofre (busque por "obsidian cli"): causa conhecida, correção e como validar. A causa é outra? Registre o bug novo. É a mesma e voltou? Atualize a nota.
   - Só se o humano não puder corrigir agora: busque nos `.md` desta pasta, incluindo `aliases` do frontmatter, e **avise** que a busca foi feita sem a CLI.
   - Subagentes e worktrees costumam rodar sem a CLI: buscam nos `.md` e dizem isso no relatório; o orquestrador reporta ao humano.
4. Ao usar uma nota, cite o nome dela na resposta.

## Se houver outros cofres conectados

Cada cofre tem o próprio `CLAUDE.md`. Regra de fronteira: o que vale **só para {{projeto}}** fica aqui; conhecimento geral (inclusive a lição de um bug que vale fora do projeto) vai para o cofre pessoal `Vault`.
