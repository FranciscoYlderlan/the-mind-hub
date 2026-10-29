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
> 1. O `cofre.py criar` gera o `CLAUDE.md` a partir do [[Modelo de CLAUDE do cofre]], já com pasta, projeto, objetivo e repositório.
> 2. Mudou o modelo? `cofre.py sincronizar` regenera o `CLAUDE.md` de cada cofre de projeto, preservando projeto, objetivo e repositório.
> 3. O mesmo comando recopia modelos e manuais, convertendo os links (kebab-case, mapa `moc-orquestra`, outras notas do `Vault` viram "(no Vault)").
> 4. Confiro que o arquivo cita **só o próprio cofre**. Cofres vizinhos entram apenas pela regra de fronteira.
> 5. Fecho com `cofre.py verificar`: zero ERRO.

> [!warning] Armadilhas
> - Nome do arquivo em maiúsculas: `CLAUDE.md`. Outro nome o agente não lê sozinho.
> - O `CLAUDE.md` não é nota: sem frontmatter, na raiz, e é o **único índice** (sem `leia-primeiro.md`).
> - Regra só do projeto **não** vai no `CLAUDE.md`, porque o sincronizar o regenera. Ela vira decisão em `funcionalidades/geral/`.
> - Não apago "Como buscar", "Padronização" nem "Etapas vitais": são elas que obrigam o agente a consultar antes, seguir o padrão e verificar depois.
> - Em cofre de projeto, o que é só do projeto (regras de padronização, bloco `padroes`, repositórios e acesso) fica entre `<!-- projeto:... -->` e `<!-- /projeto:... -->`. O `cofre.py sincronizar` refaz o resto pelo modelo e guarda esses blocos; o que ainda não foi definido nasce `[a preencher]`.
> - "Como buscar" exige a Obsidian CLI, também para ler. Se ela falhar, o agente reporta e analisa com [[Obsidian CLI via MCP não carrega]] antes de buscar nos `.md`.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** Um `CLAUDE.md` por cofre faz qualquer combinação de cofres funcionar num projeto.
* **Ponto 2:** O agente lê o crachá e já sabe estrutura, regras e como buscar.
* **Ponto 3:** Erro comum: escrever no `CLAUDE.md` regras de outro cofre e misturar os contextos.

### 🔗 Conexões
- Mapa: [[MOC Programação]]
- Relacionadas: [[Criar um novo cofre]], [[Atualizar a memória]], [[Manual da Orquestra]]
- Próxima: [[Registrar cofre no README]]
