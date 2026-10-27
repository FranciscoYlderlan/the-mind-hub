# Cofre "{{nome-da-pasta}}" — {{projeto}} (guia para agentes)

Este é um cofre do Obsidian: uma pasta de notas Markdown. Ele guarda **{{para quê, em meia frase}}**.

Nome do cofre no Obsidian: `{{nome-da-pasta}}`.

## Por onde começar

1. `Items/Home.md`: porta de entrada.
2. `Items/Manual do Meu Cérebro no Obsidian.md`: **regras obrigatórias** de escrita. Leia antes de criar ou editar qualquer nota.
3. `MOCs/`: mapas de assunto.

## Estrutura

| Pasta | O que mora ali |
|---|---|
| `00 Inbox/` | Capturas rápidas (1 linha) |
| `Items/` | Todas as notas, incluindo a Home |
| `MOCs/` | Mapas de assunto, nome começa com "MOC " |
| `Anexos/` | Imagens e PDFs (kebab-case, sem acento) |
| `Modelos/` | Esqueletos de nota |

## Regras essenciais (resumo do Manual)

- Toda nota nova nasce em `Items/`.
- Frontmatter: `aliases` (2–4) e `tags` (1–3) **sempre em lista**, mais `tipo`, `status`, `criado` e `origem`.
- Nome do arquivo sem emoji; o emoji fica no `# Título`.
- Uma ideia por nota; 2+ links de saída; toda nota aparece em pelo menos um MOC.
- Tarefas não moram aqui: viram `→ TickTick`.
- Não invente fatos; na dúvida, marque `[a confirmar]`.
- Nunca edite `.obsidian/` sem pedido explícito.

## Como buscar (obrigatório)

**Sempre** que precisar recuperar contexto, decisões, regras ou qualquer instrução registrada antes, busque neste cofre **antes** de responder ou escrever. Não responda de memória quando o assunto pode estar numa nota.

1. **Obsidian CLI** (primeira opção; usa o índice do app, então acha por aliases, tags e links). Precisa do Obsidian aberto:
   - Busca: `obsidian vault="{{nome-da-pasta}}" search query="termo" limit=10`
   - Ler uma nota: `obsidian vault="{{nome-da-pasta}}" read file="Nome da nota"`
   - Quem aponta para uma nota: `obsidian vault="{{nome-da-pasta}}" backlinks file="Nome da nota"`
   - Notas por tag: `obsidian vault="{{nome-da-pasta}}" tags`
   - Lista completa de comandos: `obsidian help`
2. Tente sinônimos e termos em inglês antes de concluir que não existe nota (as notas têm `aliases`).
3. **Sem CLI** (comando não encontrado ou Obsidian fechado): busque nos `.md` desta pasta, incluindo os `aliases` do frontmatter, e **avise** que a busca foi feita sem a CLI.
4. Ao usar uma nota, cite o nome dela na resposta, para eu saber de onde veio.

## Se houver outros cofres conectados

Cada cofre tem o próprio `CLAUDE.md`. Regra de fronteira: o que vale **só para {{projeto}}** fica aqui; conhecimento geral vai para o cofre pessoal `Vault`.
