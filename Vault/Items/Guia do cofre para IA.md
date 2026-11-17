---
aliases: [CLAUDE.md do cofre, Instruções do cofre para agentes, Vault agent guide, Como a IA entende o cofre]
tags: [ferramentas/obsidian, estudos/programacao]
tipo: procedimento
status: em-uso
criado: 2026-10-27
origem: Configuração do the-mind-hub para projetos do Claude Code
---
# 🛠️ Guia do Cofre para IA

> [!tldr] Em uma linha
> Todo cofre tem um `CLAUDE.md` na raiz: o manual de bolso que o agente lê assim que o cofre entra como contexto.

É como **o crachá com instruções pendurado na porta de cada sala**. Quem entra não precisa perguntar onde fica cada coisa: lê o crachá e já trabalha. Como cada projeto conecta um grupo diferente de cofres, cada cofre carrega o próprio crachá. O conteúdo vem do [[Manual do Meu Cérebro no Obsidian|Manual]] e segue o esqueleto do `Modelo de CLAUDE do cofre`.

---

> [!note] Passo a passo
> 1. O `cofre.py criar` gera o `CLAUDE.md` a partir do [[Modelo de CLAUDE do cofre]], já com pasta, projeto, objetivo e o bloco de escopos (nome da pasta e `readme`), e gera `orquestra/padroes.md` com o bloco `padroes` (`limite-palavras: 2000`).
> 2. Mudou o modelo? `cofre.py sincronizar` regenera o `CLAUDE.md` de cada cofre de projeto, preservando projeto e objetivo.
> 3. O mesmo comando recopia modelos e manuais, convertendo os links (kebab-case, mapa `moc-orquestra`, outras notas do `Vault` viram "(no Vault)"). No perfil prático, leva também a pasta `contrato/` para `orquestra/modelos/contrato/`, sem converter: são os arquivos do [[Contrato funcional]] para `docs/contrato/` do repositório, não notas, e o `verificar` não os lê. O perfil vem da linha `- Perfil:` do `geral-contexto`; sem ela, conta como prático.
> 4. Confiro que o arquivo cita **só o próprio cofre**. Cofres vizinhos entram apenas pela regra de fronteira.
> 5. Fecho com `cofre.py verificar`: zero ERRO.

> [!warning] Armadilhas
> - Nome do arquivo em maiúsculas: `CLAUDE.md`. Outro nome o agente não lê sozinho.
> - O `CLAUDE.md` não é nota: sem frontmatter, na raiz, e é o **único índice** (sem `leia-primeiro.md`).
> - O `CLAUDE.md` é **índice, não manual**: cada regra geral fica em 1 linha imperativa (gatilho e o que fazer) com link para a nota que detalha, lida pela CLI quando a tarefa toca no assunto. Explicação, exemplo e passo a passo moram nos manuais. O `cofre.py verificar` dá ERRO se o modelo ou o `CLAUDE.md` de um cofre passar de 2500 palavras (teto, não meta).
> - Regra só do projeto (grafia, documentos-fonte, exceções de nome, repositórios e acesso) vira decisão em `orquestra/funcionalidades/geral/`, com aval do humano. O `CLAUDE.md` só aponta para lá e manda buscar pela CLI, para o consumo de tokens não crescer com o projeto.
> - O bloco `padroes` mora em `orquestra/padroes.md`, lido pelo `cofre.py verificar`. No `Vault`, que não tem `orquestra/`, ele fica no próprio `CLAUDE.md`.
> - O único bloco de projeto do modelo é `<!-- projeto:escopos -->`, na seção Commits: a lista fechada de escopos de commit, que nasce com o nome da pasta e `readme` e ganha na criação os escopos do projeto. O `sincronizar` o preserva, e o `verificar` dá ERRO se ele faltar ou estiver sem nenhum escopo.
> - Nota do `Vault` citada dentro de um cofre de projeto (no `CLAUDE.md`, numa decisão, no `geral-plano`) é escrita como texto "Nome (no Vault)", nunca como wikilink: lá ela não existe, e o link ficaria quebrado. O `cofre.py` já converte assim os links das cópias de modelos e manuais.
> - Cofre antigo ainda guarda regras em outros blocos `<!-- projeto:... -->` no `CLAUDE.md`: o `sincronizar` os preserva como estão (no fim do arquivo, se o modelo não tem lugar para eles), o `verificar` lê o `padroes` dali enquanto não houver `orquestra/padroes.md` e dá só AVISO pelo tamanho até a migração.
> - Não apago "Como buscar", "Padronização", "Etapas vitais" nem "Commits": são elas que obrigam o agente a consultar antes, seguir o padrão e verificar depois.
> - O `CLAUDE.md` só é lido depois que o agente já escolheu por onde ler. Numa sessão que entra por um projeto do claude.ai, a primeira coisa lida são as **instruções do projeto**: elas recebem o bloco do [[modelo-instrucoes-do-projeto-claude]], que manda usar a CLI (carregando as ferramentas adiadas com `ToolSearch`) e proíbe ler ou escrever o cofre pela ferramenta `Projects`.
> - "Como buscar" exige a Obsidian CLI, também para ler, antes de qualquer outra ferramenta; o aviso "Leitura: Obsidian CLI primeiro" no topo repete isso. O `cofre.py verificar` dá ERRO se faltar o aviso, a seção ou o `vault="nome-da-pasta"` certo. Se a CLI falhar, o agente reporta e analisa com [[Obsidian CLI via MCP não carrega]] antes de buscar nos `.md`.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** Um `CLAUDE.md` por cofre faz qualquer combinação de cofres funcionar num projeto.
* **Ponto 2:** O agente lê o crachá e já sabe estrutura, regras e como buscar.
* **Ponto 3:** Erro comum: escrever no `CLAUDE.md` regras de outro cofre e misturar os contextos.

### 🔗 Conexões
- Mapa: [[MOC Programação]]
- Relacionadas: [[Criar um novo cofre]], [[Atualizar a memória]], [[Manual da Orquestra]], [[Contrato funcional]]
- Próxima: [[Registrar cofre no README]]
