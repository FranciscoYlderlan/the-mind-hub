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

> [!warning] Estudo não ganha cofre
> Eu estudo coisa nova o tempo todo. Um cofre por estudo viraria uma estante de cadernos com uma página só. Estudo geral vai para o `Vault/`; estudo ligado a um projeto vai para o cofre do projeto.

---

> [!note] Passo a passo
> 1. Leio o [[Manual da Orquestra]] e pergunto ao humano: nome, objetivo em meia frase, repositório, tempo e dial. O que faltar vira `[a confirmar]`.
> 2. Na raiz do `the-mind-hub`: `python Vault/Modelos/Orquestra/cofre.py criar nome-do-cofre --projeto "Nome" --para-que "meia frase" --repo LINK`. **Nunca monto à mão.** O `CLAUDE.md` nasce com a seção `## Commits` ([[Padrão de commit]] e [[Commitar no the-mind-hub]]): obrigatória, sem ela o verificar dá ERRO.
> 3. Preencho o `geral-contexto` com os fatos do passo 1, seguindo [[Atualizar a memória]].
> 4. No repositório de código, colo o trecho do [[modelo-claude-do-repositorio]].
> 5. Rodo `python Vault/Modelos/Orquestra/cofre.py verificar nome-do-cofre`. Só sigo com **zero ERRO**.
> 6. Abro o cofre no Obsidian, aponto Modelos para `orquestra/modelos` e registro no README. Ver [[Registrar cofre no README]].

> [!tip] Quando abrir esta nota
> Quando eu começar um projeto novo e quiser um lugar para pensar sobre ele.
> → Commit: `:wrench: chore(nome-do-cofre): Add initial vault structure`

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** Só existem dois tipos de cofre: a minha vida (`Vault/`) e um por projeto.
* **Ponto 2:** Conhecimento geral fica no `Vault/`. Conhecimento do projeto fica no cofre dele, na `orquestra/`, nunca nas 5 pastas do `Vault`.
* **Ponto 3:** Erro comum: montar à mão ou pular o verificar. Foi assim que nasceram modelos sem conexões e cópias com links quebrados.

### 🔗 Conexões
- Mapa: [[MOC Programação]]
- Relacionadas: [[Manual da Orquestra]], [[Atualizar a memória]], [[Guia do cofre para IA]], [[Registrar cofre no README]], [[Commitar no the-mind-hub]]
- Próxima: [[Registrar cofre no README]]
