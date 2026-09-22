# Cofre "stonebid-vault" — projeto StoneBid (guia para agentes)

Este é um cofre do Obsidian: uma pasta de notas Markdown. Ele guarda **o que vale só para o projeto StoneBid**: regras de negócio, decisões e o que foi estudado para o projeto.

Nome do cofre no Obsidian: `stonebid-vault`.

> Estado atual: cofre recém-criado. A estrutura padrão (abaixo) e a `Items/Home.md` ainda não existem. Se for criá-las, siga o procedimento "Criar um novo cofre".

## Por onde começar

1. `Items/Home.md`: porta de entrada (descreve o projeto em uma linha e leva ao repositório de código).
2. Regras de escrita: `Items/Manual do Meu Cérebro no Obsidian.md` (cópia do Manual do cofre pessoal). Se ainda não existir aqui e o cofre `Vault` estiver conectado, use `Vault/Items/Manual do Meu Cérebro no Obsidian.md`. Se nenhum dos dois estiver disponível, siga o resumo abaixo.

## Estrutura (igual a todos os cofres)

| Pasta | O que mora ali |
|---|---|
| `00 Inbox/` | Capturas rápidas (1 linha) |
| `Items/` | Todas as notas, incluindo a Home |
| `MOCs/` | Mapas de assunto, nome começa com "MOC " |
| `Anexos/` | Imagens e PDFs (kebab-case, sem acento) |
| `Modelos/` | Esqueletos de nota |

## Regras essenciais (resumo do Manual)

- Toda nota nova nasce em `Items/`.
- Frontmatter: `aliases` (2–4) e `tags` (1–3) **sempre em lista**, mais `tipo` (conceito, memoria, procedimento, moc, manual), `status` (rascunho, em-uso, consolidada), `criado` (AAAA-MM-DD) e `origem`.
- Nome do arquivo sem emoji; o emoji fica no `# Título`.
- Uma ideia por nota; toda nota tem 2+ links de saída e aparece em pelo menos um MOC.
- Frases curtas, uma analogia do cotidiano por nota, sem tom dramático nem culpa.
- Tarefas não moram aqui: viram `→ TickTick`.
- Não invente fatos; na dúvida, marque `[a confirmar]`.
- Nunca edite `.obsidian/` sem pedido explícito.

## Como buscar

1. **Obsidian CLI** (preferido; precisa do Obsidian aberto):
   - `obsidian vault="stonebid-vault" search query="termo" limit=10`
2. **Sem CLI:** busque nos `.md` desta pasta, incluindo os `aliases` do frontmatter.

## Se houver outros cofres conectados

Cada cofre tem o próprio `CLAUDE.md`. Regra de fronteira: o que vale **só para o StoneBid** fica aqui; conhecimento geral (que vale fora do projeto) vai para o cofre pessoal `Vault`.
