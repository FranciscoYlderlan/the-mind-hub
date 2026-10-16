---
aliases: [Nova memória, Novo segundo cérebro, New vault, Como abro um cofre para um projeto]
tags: [ferramentas/obsidian, estudos/programacao]
tipo: procedimento
status: em-uso
criado: 2026-10-26
origem: Estrutura do repositório the-mind-hub
---
# 🛠️ Criar um Novo Cofre

> [!tldr] Em uma linha
> Cada projeto ganha a sua própria memória: um cofre novo dentro do the-mind-hub, com a estrutura `orquestra/` e as regras do Manual.

Funciona como **uma franquia**. Toda loja nova abre com a mesma planta e o mesmo manual, então eu sei onde fica cada coisa. O que muda é o que ela vende. Cada cofre novo copia a planta da [[Manual da Orquestra|orquestra]] e as regras do [[Manual do Meu Cérebro no Obsidian|Manual]], e o conteúdo é só do projeto.

---

| Onde guardar | Exemplo |
|---|---|
| `Vault/` (minha vida) | Perfil, rotina, **estudos** e o que vale para todos os projetos, como o [[Padrão de commit]] |
| Cofre do projeto | O que vale **só** para aquele projeto: regras de negócio, decisões e o que estudei para ele |

> [!warning] Estudo só ganha cofre com plano
> Eu estudo coisa nova o tempo todo. Um cofre por estudo solto viraria uma estante de cadernos com uma página só: estudo geral vai para o `Vault/`, e estudo ligado a um projeto vai para o cofre do projeto. Estudo com plano ganha cofre próprio, no [[Manual da Orquestra - Perfil estudo|perfil estudo]].

---

> [!note] Passo a passo
> 1. Leio o [[Manual da Orquestra]] e pergunto ao humano: nome, objetivo em meia frase, perfil (prático ou estudo), tempo, dial, os **escopos de commit** a acrescentar (lista fechada: área, ID do requisito ou outro; ver [[Padrão de commit]]) e o que o perfil pedir (no prático, o repositório e se o projeto será publicado ou só local, em WSL ou Docker). O que faltar vira `[a confirmar]`.
> 2. Na raiz do `the-mind-hub`: `python Vault/Modelos/Orquestra/cofre.py criar nome-do-cofre --projeto "Nome" --para-que "meia frase" --perfil pratico|estudo` (padrão: `pratico`). No prático, também `--publicado sim|nao` e `--repo LINK`; o que o humano não respondeu fica `[a preencher]` e o verificar avisa. No estudo, `--publicado` e `--repo` dão erro. **Nunca monto à mão.** O `CLAUDE.md` nasce com a seção `## Commits` ([[Padrão de commit]] e [[Commitar no the-mind-hub]]) e o bloco de escopos já com o nome da pasta e `readme`: sem a seção, sem o bloco ou com o bloco vazio, o verificar dá ERRO. Nascem também `orquestra/padroes.md` (bloco `padroes`, `limite-palavras: 2000`) e, no `geral-contexto`, o perfil como fato (no prático, também publicado ou local e o repositório); onde fica o repositório e o acesso viram decisão em `funcionalidades/geral/`.
> 3. Preencho o `geral-contexto` com os fatos do passo 1, seguindo [[Atualizar a memória]], e **proponho as etapas do roteiro** no `geral-plano`. Com o aval do humano: nota `geral-decisao-AAAA-MM-DD-roteiro`, roteiro com as etapas aprovadas (`status: aprovado`), etapa 1 `concluida` com a data e a decisão em Notas geradas, e `cofre.py status --atualizar` (A4 do [[Manual da Orquestra]]).
> 4. Aplico o perfil e **acrescento** os escopos do passo 1 ao bloco `projeto:escopos` do `CLAUDE.md`, depois do nome da pasta e de `readme`, que estão em todo cofre e não saem. No [[Manual da Orquestra - Perfil projeto prático|projeto prático]], colo no repositório de código o trecho do [[modelo-claude-do-repositorio]], com os escopos acrescentados (o nome da pasta e `readme` são do `the-mind-hub`), copio `orquestra/modelos/contrato/` para `docs/contrato/` do repositório e preencho o `00-requisitos.md` a partir do documento-fonte ([[Contrato funcional]], Q01); no roteiro, cada funcionalidade com interface começa preenchendo os blocos dela (Q03), termina com o verificador de fluxo principal, o adversarial e os fluxos de teste registrados, e a última etapa entrega o roteiro do humano (Q06). Se for software, o [[Padrão de projeto de software]] passa a valer (S01 a S27; o bloco "só com deploy", S04 a S08 e S24, só se o projeto for publicado). Também **proponho a arquitetura (frontend e backend) e as tecnologias** a partir da [[Referência de arquitetura e stack]], em linguagem leiga, na seção "Proposta de arquitetura e stack" do `geral-plano`; o humano ajusta, e o aval vira as decisões de estrutura e stack em `funcionalidades/geral/`, que citam essa seção no campo Proposta (S25 do [[Padrão de projeto de software]]: "para que eu posso propor sugestões de mudança em cima delas e não precisar partir do absoluto 0"). Nota do `Vault` citada dentro do cofre de projeto (a Referência, o Padrão, os perfis) é escrita como texto "Nome (no Vault)", nunca como wikilink: lá ela não existe e o link ficaria quebrado.
> 5. Rodo `python Vault/Modelos/Orquestra/cofre.py verificar nome-do-cofre`. Só sigo com **zero ERRO**.
> 6. Abro o cofre no Obsidian (o nome no app é o da pasta), aponto Modelos para `orquestra/modelos` e **valido a CLI**: `obsidian_search` com `vault="nome-do-cofre"` devolve notas. Sem isso, nenhum agente consegue ler o cofre pela CLI; se falhar, ver [[Obsidian CLI via MCP não carrega]].
> 7. Se o projeto tiver um projeto no claude.ai, colo no campo **Instruções** dele o bloco do [[modelo-instrucoes-do-projeto-claude]] (no cofre: `orquestra/modelos/`), com o nome do cofre. Sem isso, a sessão que entra pelo projeto lê a cópia dos documentos, que envelhece, e pula a CLI.
> 8. Registro no README. Ver [[Registrar cofre no README]].

> [!tip] Quando abrir esta nota
> Quando eu começar um projeto novo e quiser um lugar para pensar sobre ele.
> → Commit: `:wrench: chore(nome-do-cofre): Add initial vault structure`

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** Só existem dois tipos de cofre: a minha vida (`Vault/`) e um por projeto.
* **Ponto 2:** Conhecimento geral fica no `Vault/`. Conhecimento do projeto fica no cofre dele, na `orquestra/`, nunca nas 5 pastas do `Vault`.
* **Ponto 3:** Erro comum: montar à mão, pular o verificar ou deixar o projeto do claude.ai sem instruções. Foi assim que nasceram modelos sem conexões, cópias com links quebrados e sessões que leram a cópia velha em vez do cofre.

### 🔗 Conexões
- Mapa: [[MOC Programação]]
- Relacionadas: [[Manual da Orquestra]], [[Referência de arquitetura e stack]], [[Contrato funcional]], [[modelo-instrucoes-do-projeto-claude]], [[Atualizar a memória]], [[Guia do cofre para IA]], [[Registrar cofre no README]], [[Commitar no the-mind-hub]]
- Próxima: [[Registrar cofre no README]]
