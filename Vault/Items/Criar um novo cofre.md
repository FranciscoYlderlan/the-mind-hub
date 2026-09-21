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
> Cada projeto ganha a sua própria memória: um cofre novo dentro do the-mind-hub, com a mesma estrutura do `Vault/`.

Funciona como **uma franquia**. Toda loja nova abre com a mesma planta e o mesmo manual, então eu sei onde fica cada coisa. O que muda é o que ela vende. Cada cofre novo copia a estrutura e as regras do [[Manual do Meu Cérebro no Obsidian|Manual]], e o conteúdo é só do projeto.

---

| Onde guardar | Exemplo |
|---|---|
| `Vault/` (pessoal) | O que vale para **todos** os projetos: perfil, rotina, [[Padrão de commit]] |
| Cofre do projeto | O que vale **só** para aquele projeto: regras de negócio, decisões, aprendizados |

---

> [!note] Passo a passo
> 1. Crio a pasta do cofre na raiz do `the-mind-hub`, com o nome do projeto em kebab-case. Exemplo: `conciliador-extratos/`.
> 2. Copio a estrutura: `00 Inbox/` (com `.gitkeep`), `Items/`, `MOCs/`, `Anexos/` e `Modelos/`.
> 3. Copio o Manual e o Modelo de nota. Do `.obsidian/`, copio só `app.json` e `core-plugins.json`.
> 4. No Obsidian: "Abrir pasta como cofre" e escolho a pasta nova.
> 5. Crio a `Home` dizendo, em uma linha, qual é o projeto e o link do repositório de código.
> 6. Registro o cofre no README. Ver [[Registrar cofre no README]].

> [!tip] Quando abrir esta nota
> Quando eu começar um projeto novo e quiser um lugar para pensar sobre ele.
> → Commit: `:wrench: chore(nome-do-cofre): Add initial vault structure`

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** Um projeto = um cofre. A estrutura é sempre a mesma.
* **Ponto 2:** Conhecimento geral fica no `Vault/`. Conhecimento do projeto fica no cofre dele.
* **Ponto 3:** Erro comum: esquecer o README. Um cofre que não está no mapa vira um cofre perdido.

### 🔗 Conexões
- Mapa: [[MOC Programação]]
- Relacionadas: [[Registrar cofre no README]], [[Padrão de commit]]
- Próxima: [[Registrar cofre no README]]
