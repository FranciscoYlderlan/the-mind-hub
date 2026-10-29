# Cofre "Vault" — minha vida (guia para agentes)

Este é um cofre do Obsidian: uma pasta de notas Markdown. Ele guarda **o que eu sei e penso sobre mim**: perfil, rotina, estudos gerais e padrões que valem para todos os projetos (ex.: padrão de commit).

Nome do cofre no Obsidian: `Vault`.

> **Leitura: Obsidian CLI primeiro.** Antes de qualquer outra ferramenta (`cat`, `grep`, `find`, `Read`, busca de subagente, documentos do projeto do claude.ai), leia e busque este cofre pela Obsidian CLI, com `vault="Vault"`. Ferramentas `obsidian_*` fora da lista podem estar só adiadas: carregue com `ToolSearch` antes de concluir que a CLI falhou. Regras, comandos e plano B: seção "Como buscar".

## Por onde começar

1. `Items/Home.md`: porta de entrada; daqui se chega em tudo.
2. `Items/Manual do Meu Cérebro no Obsidian.md`: **regras obrigatórias** de escrita e organização. Leia antes de criar ou editar qualquer nota.
3. `MOCs/`: mapas de assunto (`MOC Perfil`, `MOC Programação`).
4. `Items/Manual da Orquestra.md`: como vários agentes trabalham em paralelo num projeto usando um cofre como memória. Leia antes de orquestrar subagentes ou de criar um cofre de projeto.

## Estrutura

| Pasta | O que mora ali |
|---|---|
| `00 Inbox/` | Capturas rápidas (1 linha) |
| `Items/` | Todas as notas, incluindo a Home |
| `MOCs/` | Mapas de assunto, nome começa com "MOC " |
| `Anexos/` | Imagens e PDFs (kebab-case, sem acento) |
| `Modelos/` | Esqueletos; o padrão é `Modelos/Modelo de nota.md`. `Modelos/Orquestra/` guarda os modelos dos cofres de projeto |

## Regras essenciais (resumo do Manual)

- Toda nota nova nasce em `Items/` com o esqueleto do Modelo de nota.
- Frontmatter: `aliases` (2–4) e `tags` (1–3, da taxonomia fechada do Manual) **sempre em lista**, mais `tipo`, `status`, `criado` e `origem` (opcional).
- Nome do arquivo sem emoji; o emoji fica no `# Título`.
- Toda nota tem 2+ links de saída e aparece em pelo menos um MOC.
- Tarefas não moram aqui: viram `→ TickTick`.
- Não invente fatos; na dúvida, marque `[a confirmar]`.
- Nunca edite `.obsidian/` sem pedido explícito.
- **Uma versão só:** mudou um fato, regra ou decisão? Varra o impacto (busque o estado antigo pela CLI, com sinônimos) e reescreva no estado atual **toda** nota que o cita; nada de aviso "vale o novo" por cima de texto velho. O estado antigo vira linha `antigo:` no bloco `padroes` (abaixo), e o `verificar` dá ERRO se ele aparecer fora do histórico (seções "Histórico", diários, bugs).
- Despadronização (grafia, numeração, nome, tamanho) se corrige **primeiro na regra**: no `Modelo de CLAUDE do cofre`, nos manuais ou no `cofre.py`. Só depois nas notas.

## Etapas vitais (obrigatório)

- Criar cofre de projeto: siga `Items/Criar um novo cofre.md` (etapas A). Nunca monte à mão: use `Modelos/Orquestra/cofre.py criar`.
- Escrever, mover ou copiar qualquer nota (aqui ou num cofre de projeto): siga `Items/Atualizar a memória.md` (etapas B), com a varredura de impacto quando a escrita muda um estado.
- Ninguém diz "pronto" sem rodar `python Modelos/Orquestra/cofre.py verificar .` com **zero ERRO**.
- Mudou um manual ou modelo daqui? Rode `cofre.py sincronizar` em cada cofre de projeto.

## Padrões deste cofre

Lido pelo `cofre.py verificar`. Sintaxe: `termo => forma certa`; `antigo: termo => estado atual (nota dona)` dá ERRO só fora do histórico.

```padroes
# termo fora do padrão => forma certa   ("re:" no início = expressão regular)
# antigo: termo do estado substituído => estado atual (nota dona)
antigo: re:40% a 50% => orçamento de 100 mil tokens na linha Messages do /context (Manual da Orquestra)
antigo: re:bloco `padroes` do `CLAUDE.md`|Padronização \+ bloco `padroes`|2073 palavras no `stonebid-vault` => regra de projeto em decisão de funcionalidades/geral/ e padroes em orquestra/padroes.md; CLAUDE.md é índice (Manual da Orquestra)
antigo: re:Estudo não ganha cofre|Feedback determinístico \(testes|cada um na sua git worktree|Constrói \*\*uma\*\* tarefa, na própria worktree => Manual neutro; o lado de software (worktree, diff, testes) e o estudo com plano em perfis (Manual da Orquestra - Perfil projeto prático, Criar um novo cofre)
antigo: re:Não há regra geral: a lista é escolhida na criação => lista de escopos do cofre começa com o nome da pasta e readme; a criação só acrescenta (Padrão de commit)
antigo: re:commitado ao fim de cada ciclo|commito o cofre \(a cada ciclo|commita o cofre a cada ciclo|Defino o escopo: a pasta ou área real => commit do cofre a cada registro concluído e na passagem de turno; escopo da lista fechada do bloco projeto:escopos (Padrão de commit)
antigo: re:Registrar no fim, não no meio|Orquestrador, no fim da sessão|Alimentar \(no fim do trabalho\)|escreve no cofre, no fim do trabalho|alimentar no fim => registrar relatório e decisão aprovada assim que chegam (Manual da Orquestra, princípio 8)
antigo: re:mora num hub com uma nota por seção vigente|nota .-mudancas. com os itens M-xx => contrato funcional e itens M-xx em Anexos/contrato/ do cofre do projeto, ao lado das decisões e do diário (Manual da Orquestra - Perfil projeto prático, P01 e Q01)
antigo: re:Playwright, por um agente verificador => verificador de fluxo principal e adversarial, agentes ao final de cada funcionalidade, sem suíte de E2E de interface no repositório (Manual da Orquestra - Perfil projeto prático, Q04 e Q05)
antigo: re:Formulários, search params e env => todo campo de entrada com schema zod tirado do ENT do contrato e mensagem por violação (Padrão de projeto de software, S26)
antigo: re:S01 a S25 \((branches|só projeto)|S01 a S24;|P01 a P16 \(só projeto prático\) => P01 a P16 e Q01 a Q06; S01 a S27 (Manual da Orquestra - Perfil projeto prático, Padrão de projeto de software)
antigo: re:poucos fluxos que cobrem o máximo|depois do roteiro do humano \(Q06\): verificadores => roteiro curto e didático que passa por todas as funcionalidades; o aceite do humano fecha a aceitação final (Manual da Orquestra - Perfil projeto prático, Q06 e P07)
```

## Commits

Os cofres moram dentro do repositório `the-mind-hub`, e o `.git` fica na raiz dele. Se for preciso commitar e a sessão só tiver acesso à pasta de um cofre, **peça acesso à pasta `the-mind-hub`** e permissão para apagar nela (o git cria e remove arquivos `.lock`). Passos: `Items/Commitar no the-mind-hub.md`. Formato: `Items/Padrão de commit.md`, que vale em todo cofre e repositório. Quando: a cada registro concluído e na passagem de turno.

<!-- projeto:escopos -->
- **Escopos do `the-mind-hub`** (lista fechada): `Vault` (este cofre), `readme` (README da raiz, commit separado) e, para cada cofre de projeto, o nome da pasta dele.
<!-- /projeto:escopos -->

## Como buscar (obrigatório)

**Sempre** que precisar recuperar contexto, decisões, regras ou qualquer instrução registrada antes, busque neste cofre **antes** de responder ou escrever. Não responda de memória quando o assunto pode estar numa nota.

1. **Obsidian CLI: obrigatória** (usa o índice do app, então acha por aliases, tags e links). Precisa do Obsidian aberto.
   - Sessão na nuvem ligada ao computador: use as ferramentas do servidor MCP `obsidian-cli` (`obsidian_search`, `obsidian_read`, `obsidian_backlinks`, `obsidian_help`), com `vault="Vault"`.
   - **Ferramenta adiada não é CLI falhando.** Se as `obsidian_*` não estão na lista de ferramentas, carregue-as com `ToolSearch` (`select:mcp__remote-devices__obsidian-cli__obsidian_search,mcp__remote-devices__obsidian-cli__obsidian_read,mcp__remote-devices__obsidian-cli__obsidian_backlinks,mcp__remote-devices__obsidian-cli__obsidian_help`). Só se não vierem depois disso vale o passo 3.
   - **Projeto do claude.ai não é o cofre.** Os documentos de um projeto do claude.ai (ferramenta `Projects`: `project_info`, `project_read`, `project_search`, `project_write`) são uma cópia que envelhece. Nunca leia nem escreva o cofre por eles. A fonte da verdade é a pasta no computador: ler pela CLI; escrever pelo shell (`device_bash`), com a pasta `the-mind-hub` conectada (`device_request_folder_access`). Para a sessão já entrar sabendo disso, as instruções do projeto do claude.ai recebem o bloco do [[modelo-instrucoes-do-projeto-claude]].
   - **Ler também é pela CLI.** Abrir ou buscar nota com `cat`, `grep`, `find`, `Read` ou outro comando de shell é erro de processo, mesmo com acesso à pasta. O shell serve só para **escrever** notas e rodar o `cofre.py`. A única exceção é o plano B do passo 3, sempre avisado.
   - Terminal no Windows:
     - Busca: `obsidian vault="Vault" search query="termo" limit=10`
     - Ler uma nota: `obsidian vault="Vault" read file="Nome da nota"`
     - Quem aponta para uma nota: `obsidian vault="Vault" backlinks file="Nome da nota"`
     - Notas por tag: `obsidian vault="Vault" tags`
     - Lista completa de comandos: `obsidian help`
2. Tente sinônimos e termos em inglês antes de concluir que não existe nota (as notas têm `aliases`).
3. **CLI falhou** (ferramentas `obsidian_*` ausentes, comando não encontrado, "The CLI is unable to find Obsidian"): **não troque de caminho em silêncio**.
   - **Obsidian recém-aberto:** `Command "read" not found` (ou outro comando) logo depois de abrir o app não é falha da CLI: ele ainda está carregando. Espere alguns segundos e repita a mesma chamada antes do resto deste passo.
   - **Reporte** ao humano o que falhou, com a mensagem de erro.
   - **Analise** com a nota [[Obsidian CLI via MCP não carrega]]: causa conhecida, correção e como validar. A causa é outra? Registre o bug novo. É a mesma e voltou? Atualize a nota.
   - Só se o humano não puder corrigir agora: busque nos `.md` desta pasta, incluindo os `aliases` do frontmatter, e **avise** que a busca foi feita sem a CLI.
4. Ao usar uma nota, cite o nome dela na resposta, para eu saber de onde veio.

## Criar um cofre novo

Cofre de projeto usa a estrutura `orquestra/` do `Items/Manual da Orquestra.md`. Siga `Items/Criar um novo cofre.md` (pastas, modelos, manuais, contexto geral, trecho para o repositório de código) e `Items/Guia do cofre para IA.md` (o `CLAUDE.md` do cofre novo, a partir de `Modelos/Modelo de CLAUDE do cofre.md`). O cofre novo nasce na raiz do repositório `the-mind-hub`, ao lado deste, e precisa ser registrado no `README.md` da raiz (`Items/Registrar cofre no README.md`).

**Regra herdada por todo cofre novo: leitura pela Obsidian CLI.** O `cofre.py criar` gera o `CLAUDE.md` do cofre a partir do `Modelos/Modelo de CLAUDE do cofre.md`, que já traz o aviso "Obsidian CLI primeiro" e a seção "Como buscar" completa: CLI também para ler, ferramentas adiadas carregadas com `ToolSearch`, documentos do projeto do claude.ai proibidos como fonte ou destino, escrita pelo shell. O `cofre.py verificar` dá ERRO se algum desses trechos faltar, e o `cofre.py sincronizar` leva qualquer mudança do modelo aos cofres que já existem. Como o `CLAUDE.md` só é lido depois que a sessão já escolheu por onde ler, o passo 7 de `Items/Criar um novo cofre.md` cola o bloco do [[modelo-instrucoes-do-projeto-claude]] nas instruções do projeto do claude.ai. Mudar esta regra é mudar o modelo, nunca o `CLAUDE.md` de um cofre só.

## Se houver outros cofres conectados

Cada cofre tem o próprio `CLAUDE.md`. Regra de fronteira: o que vale **para a minha vida e para todos os projetos** vem para cá; o que vale **só para um projeto** vai para o cofre daquele projeto. Não misture os dois numa mesma nota. A lição de um bug de projeto que vale para qualquer projeto sobe para cá como nota de conceito.
