# 🧠 The Mind Hub

> Um lugar para guardar o que eu sei e penso, dividido em vários segundos cérebros.

Pense numa **estante com vários cadernos**. Só existem dois tipos de caderno: o da minha vida e um para cada projeto. A estante é este repositório. Os cadernos são os cofres do [Obsidian](https://obsidian.md).

## 🗺️ Mapa de cofres

Qual memória abrir para cada projeto:

| Cofre | Projeto | Para quê | Quando abrir |
|---|---|---|---|
| `Vault/` | Minha vida | Quem eu sou, como eu funciono, meus estudos e padrões que valem para todos os projetos | Rotina, perfil, estudos, padrão de commit |
| `stonebid-vault/` | StoneBid | Regras de negócio, decisões e estudos do projeto | Antes de trabalhar no StoneBid |

> Regra: cofre novo só para **projeto novo**. Estudo não ganha cofre: estudo geral fica no `Vault/`, e estudo de um projeto fica no cofre dele.

## ➕ Novo cofre

1. Na raiz: `python Vault/Modelos/Orquestra/cofre.py criar nome-do-cofre --projeto "Nome" --para-que "meia frase" --repo LINK`. O script monta a estrutura `orquestra/`, o `CLAUDE.md`, o mapa e o contexto geral.
2. Preencho o contexto geral e rodo `python Vault/Modelos/Orquestra/cofre.py verificar nome-do-cofre` até dar zero ERRO.
3. Adiciono **uma linha** no Mapa de cofres acima.
4. Faço dois commits: um para o cofre e outro para este README.

O passo a passo completo está nas notas **Criar um novo cofre**, **Atualizar a memória** e **Registrar cofre no README**, dentro do `Vault/`.

## 🧭 Como cada cofre funciona

- Cada cofre tem um `CLAUDE.md` na raiz: o índice que os agentes de IA leem primeiro, com as etapas vitais.
- O `Vault/` guarda as notas em `Items/` e os mapas em `MOCs/`, e começa pela nota **Home**.
- Cofres de projeto usam a estrutura `orquestra/` (contexto, plano, decisões, bugs e diários) e começam por `MOCs/moc-orquestra.md`. As regras estão no **Manual da Orquestra**.
- As regras de escrita estão no **Manual do Meu Cérebro no Obsidian**.
- Toda escrita num cofre termina com `cofre.py verificar` com zero ERRO.
- Minhas tarefas não moram aqui: ficam no TickTick. Tarefas de agente ficam no plano de cada funcionalidade.

## 🌿 Commits

Formato único: `{emoji} {tipo}(escopo): Descrição`. A regra completa está na nota **Padrão de commit**, dentro do `Vault/`.

Os cofres não têm `.git` próprio: os commits são feitos da raiz deste repositório. Ver **Commitar no the-mind-hub**.
