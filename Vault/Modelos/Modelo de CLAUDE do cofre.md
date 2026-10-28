# Cofre "{{nome-da-pasta}}" — {{projeto}} (guia para agentes)

Este é um cofre do Obsidian: uma pasta de notas Markdown. Ele é a **memória do projeto {{projeto}}**: {{para quê, em meia frase}}. Este arquivo é o índice: ele diz onde está cada coisa e quando consultar. Os detalhes moram nas notas.

Nome do cofre no Obsidian: `{{nome-da-pasta}}`. Repositório de código: {{link ou caminho}}.

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
- Notas operacionais (contexto, plano, decisão, bug, diário) seguem o modelo próprio, sem analogia nem limite de tamanho. Notas de `referencias/` e `MOCs/` seguem o Manual do Cérebro (`modelo-nota.md` ou `modelo-referencia.md`).
- Frontmatter operacional: `tipo`, `status`, `criado`, `funcionalidade`; `aliases` opcional (em bug: os sintomas).
- Fatos do humano preservados; interpretação do agente em seção separada; suposição marcada `[a confirmar]`.
- Tarefa de agente mora no plano; tarefa do humano vai para o TickTick.
- Nunca edite `.obsidian/` sem pedido explícito.

## Etapas vitais (obrigatório)

Toda escrita neste cofre (criar, mudar, mover ou copiar nota) segue estas etapas. Pular uma é erro de processo. Tabela completa: [[Manual da Orquestra#🚦 Etapas vitais]].

1. Gatilho: qual linha de "Alimentar" pede a escrita.
2. Buscar antes: a nota existe? Atualize em vez de duplicar.
3. Classificar: tipo → modelo → pasta → nome. Aval do humano quando a regra exige.
4. Escrever a partir de `orquestra/modelos/`, nunca do zero.
5. Conectar nos dois sentidos: Conexões na nota e link de volta no hub (`<func>-contexto`) ou em `moc-orquestra`.
6. Propagar: roteiro (etapa concluída, notas geradas, `cofre.py status --atualizar`), contexto ("o que já foi feito"), diário, decisão substituída.
7. Rodar `python orquestra/modelos/cofre.py verificar .` → **zero ERRO**. Só então "pronto".

Modelos e manuais deste cofre não se editam aqui: o original fica no `Vault` e chega por `cofre.py sincronizar`.

## Commits

Este cofre mora dentro do repositório `the-mind-hub`, e o `.git` fica na raiz dele, não aqui. Se for preciso commitar e a sessão só tiver acesso a esta pasta, **peça acesso à pasta `the-mind-hub`** e permissão para apagar nela (o git cria e remove arquivos `.lock`). Passos e formato: notas "Commitar no the-mind-hub" e "Padrão de commit" do cofre pessoal `Vault`. Antes do commit: `cofre.py verificar` com zero ERRO.

## Como buscar (obrigatório)

**Sempre** que precisar recuperar contexto, decisões, regras ou qualquer instrução registrada antes, busque neste cofre **antes** de responder ou escrever. Não responda de memória quando o assunto pode estar numa nota.

1. **Obsidian CLI** (primeira opção; usa o índice do app, então acha por aliases, tags e links). Precisa do Obsidian aberto:
   - Busca: `obsidian vault="{{nome-da-pasta}}" search query="termo" limit=10`
   - Ler uma nota: `obsidian vault="{{nome-da-pasta}}" read file="nome-da-nota"`
   - Quem aponta para uma nota: `obsidian vault="{{nome-da-pasta}}" backlinks file="nome-da-nota"`
   - Lista completa de comandos: `obsidian help`
2. Tente sinônimos e termos em inglês antes de concluir que não existe nota.
3. **Sem CLI** (comando não encontrado ou Obsidian fechado, comum em subagentes e worktrees): busque nos `.md` desta pasta, incluindo `aliases` do frontmatter, e **avise** que a busca foi feita sem a CLI.
4. Ao usar uma nota, cite o nome dela na resposta.

## Se houver outros cofres conectados

Cada cofre tem o próprio `CLAUDE.md`. Regra de fronteira: o que vale **só para {{projeto}}** fica aqui; conhecimento geral (inclusive a lição de um bug que vale fora do projeto) vai para o cofre pessoal `Vault`.
