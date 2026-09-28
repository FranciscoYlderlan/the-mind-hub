# Cofre "Vault" — minha vida (guia para agentes)

Este é um cofre do Obsidian: uma pasta de notas Markdown. Ele guarda **o que eu sei e penso sobre mim**: perfil, rotina, estudos gerais e padrões que valem para todos os projetos (ex.: padrão de commit).

Nome do cofre no Obsidian: `Vault`.

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
- Despadronização (grafia, numeração, nome, tamanho) se corrige **primeiro na regra**: no `Modelo de CLAUDE do cofre`, nos manuais ou no `cofre.py`. Só depois nas notas.

## Etapas vitais (obrigatório)

- Criar cofre de projeto: siga `Items/Criar um novo cofre.md` (etapas A). Nunca monte à mão: use `Modelos/Orquestra/cofre.py criar`.
- Escrever, mover ou copiar qualquer nota (aqui ou num cofre de projeto): siga `Items/Atualizar a memória.md` (etapas B).
- Ninguém diz "pronto" sem rodar `python Modelos/Orquestra/cofre.py verificar .` com **zero ERRO**.
- Mudou um manual ou modelo daqui? Rode `cofre.py sincronizar` em cada cofre de projeto.

## Commits

Os cofres moram dentro do repositório `the-mind-hub`, e o `.git` fica na raiz dele. Se for preciso commitar e a sessão só tiver acesso à pasta de um cofre, **peça acesso à pasta `the-mind-hub`** e permissão para apagar nela (o git cria e remove arquivos `.lock`). Passos: `Items/Commitar no the-mind-hub.md`. Formato: `Items/Padrão de commit.md`.

## Como buscar (obrigatório)

**Sempre** que precisar recuperar contexto, decisões, regras ou qualquer instrução registrada antes, busque neste cofre **antes** de responder ou escrever. Não responda de memória quando o assunto pode estar numa nota.

1. **Obsidian CLI: obrigatória** (usa o índice do app, então acha por aliases, tags e links). Precisa do Obsidian aberto.
   - Sessão na nuvem ligada ao computador: use as ferramentas do servidor MCP `obsidian-cli` (`obsidian_search`, `obsidian_read`, `obsidian_backlinks`, `obsidian_help`), com `vault="Vault"`.
   - **Ler também é pela CLI.** Abrir ou buscar nota com `cat`, `grep`, `find`, `Read` ou outro comando de shell é erro de processo, mesmo com acesso à pasta. O shell serve só para **escrever** notas e rodar o `cofre.py`. A única exceção é o plano B do passo 3, sempre avisado.
   - Terminal no Windows:
     - Busca: `obsidian vault="Vault" search query="termo" limit=10`
     - Ler uma nota: `obsidian vault="Vault" read file="Nome da nota"`
     - Quem aponta para uma nota: `obsidian vault="Vault" backlinks file="Nome da nota"`
     - Notas por tag: `obsidian vault="Vault" tags`
     - Lista completa de comandos: `obsidian help`
2. Tente sinônimos e termos em inglês antes de concluir que não existe nota (as notas têm `aliases`).
3. **CLI falhou** (ferramentas `obsidian_*` ausentes, comando não encontrado, "The CLI is unable to find Obsidian"): **não troque de caminho em silêncio**.
   - **Reporte** ao humano o que falhou, com a mensagem de erro.
   - **Analise** com a nota [[Obsidian CLI via MCP não carrega]]: causa conhecida, correção e como validar. A causa é outra? Registre o bug novo. É a mesma e voltou? Atualize a nota.
   - Só se o humano não puder corrigir agora: busque nos `.md` desta pasta, incluindo os `aliases` do frontmatter, e **avise** que a busca foi feita sem a CLI.
4. Ao usar uma nota, cite o nome dela na resposta, para eu saber de onde veio.

## Criar um cofre novo

Cofre de projeto usa a estrutura `orquestra/` do `Items/Manual da Orquestra.md`. Siga `Items/Criar um novo cofre.md` (pastas, modelos, manuais, contexto geral, trecho para o repositório de código) e `Items/Guia do cofre para IA.md` (o `CLAUDE.md` do cofre novo, a partir de `Modelos/Modelo de CLAUDE do cofre.md`). O cofre novo nasce na raiz do repositório `the-mind-hub`, ao lado deste, e precisa ser registrado no `README.md` da raiz (`Items/Registrar cofre no README.md`).

## Se houver outros cofres conectados

Cada cofre tem o próprio `CLAUDE.md`. Regra de fronteira: o que vale **para a minha vida e para todos os projetos** vem para cá; o que vale **só para um projeto** vai para o cofre daquele projeto. Não misture os dois numa mesma nota. A lição de um bug de projeto que vale para qualquer projeto sobe para cá como nota de conceito.
