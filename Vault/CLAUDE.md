# Cofre "Vault" — minha vida (guia para agentes)

Este é um cofre do Obsidian: uma pasta de notas Markdown. Ele guarda **o que eu sei e penso sobre mim**: perfil, rotina, estudos gerais e padrões que valem para todos os projetos (ex.: padrão de commit).

Nome do cofre no Obsidian: `Vault`.

## Por onde começar

1. `Items/Home.md`: porta de entrada; daqui se chega em tudo.
2. `Items/Manual do Meu Cérebro no Obsidian.md`: **regras obrigatórias** de escrita e organização. Leia antes de criar ou editar qualquer nota.
3. `MOCs/`: mapas de assunto (`MOC Perfil`, `MOC Programação`).

## Estrutura

| Pasta | O que mora ali |
|---|---|
| `00 Inbox/` | Capturas rápidas (1 linha) |
| `Items/` | Todas as notas, incluindo a Home |
| `MOCs/` | Mapas de assunto, nome começa com "MOC " |
| `Anexos/` | Imagens e PDFs (kebab-case, sem acento) |
| `Modelos/` | Esqueletos; o padrão é `Modelos/Modelo de nota.md` |

## Regras essenciais (resumo do Manual)

- Toda nota nova nasce em `Items/` com o esqueleto do Modelo de nota.
- Frontmatter: `aliases` (2–4) e `tags` (1–3, da taxonomia fechada do Manual) **sempre em lista**, mais `tipo`, `status` e `criado`.
- Nome do arquivo sem emoji; o emoji fica no `# Título`.
- Toda nota tem 2+ links de saída e aparece em pelo menos um MOC.
- Tarefas não moram aqui: viram `→ TickTick`.
- Não invente fatos; na dúvida, marque `[a confirmar]`.
- Nunca edite `.obsidian/` sem pedido explícito.

## Como buscar (obrigatório)

**Sempre** que precisar recuperar contexto, decisões, regras ou qualquer instrução registrada antes, busque neste cofre **antes** de responder ou escrever. Não responda de memória quando o assunto pode estar numa nota.

1. **Obsidian CLI** (primeira opção; usa o índice do app, então acha por aliases, tags e links). Precisa do Obsidian aberto:
   - Busca: `obsidian vault="Vault" search query="termo" limit=10`
   - Ler uma nota: `obsidian vault="Vault" read file="Nome da nota"`
   - Quem aponta para uma nota: `obsidian vault="Vault" backlinks file="Nome da nota"`
   - Notas por tag: `obsidian vault="Vault" tags`
   - Lista completa de comandos: `obsidian help`
2. Tente sinônimos e termos em inglês antes de concluir que não existe nota (as notas têm `aliases`).
3. **Sem CLI** (comando não encontrado ou Obsidian fechado): busque nos `.md` desta pasta, incluindo os `aliases` do frontmatter, e **avise** que a busca foi feita sem a CLI.
4. Ao usar uma nota, cite o nome dela na resposta, para eu saber de onde veio.

## Criar um cofre novo

Siga `Items/Criar um novo cofre.md` (estrutura de pastas, Manual, Home) e `Items/Guia do cofre para IA.md` (o `CLAUDE.md` do cofre novo, a partir de `Modelos/Modelo de CLAUDE do cofre.md`). O cofre novo nasce na raiz do repositório `the-mind-hub`, ao lado deste, e precisa ser registrado no `README.md` da raiz (`Items/Registrar cofre no README.md`).

## Se houver outros cofres conectados

Cada cofre tem o próprio `CLAUDE.md`. Regra de fronteira: o que vale **para a minha vida e para todos os projetos** vem para cá; o que vale **só para um projeto** vai para o cofre daquele projeto. Não misture os dois numa mesma nota.
