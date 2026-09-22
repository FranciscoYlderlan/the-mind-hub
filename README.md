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

1. Crio a pasta do projeto na raiz, em kebab-case, copiando a estrutura do `Vault/`.
2. Crio o `CLAUDE.md` na raiz do cofre, a partir de `Vault/Modelos/Modelo de CLAUDE do cofre.md`.
3. Adiciono **uma linha** no Mapa de cofres acima.
4. Faço dois commits: um para o cofre e outro para este README.

O passo a passo completo está nas notas **Criar um novo cofre** e **Registrar cofre no README**, dentro do `Vault/`.

## 🧭 Como cada cofre funciona

- Cada cofre começa pela nota **Home**.
- Cada cofre tem um `CLAUDE.md` na raiz: o guia que os agentes de IA leem quando o cofre entra como contexto.
- As regras de escrita estão no **Manual do Meu Cérebro no Obsidian**.
- As notas ficam em `Items/`, e os mapas de assunto ficam em `MOCs/`.
- Tarefas não moram aqui. O Obsidian guarda o que eu **sei**, e o TickTick guarda o que eu **faço**.

## 🌿 Commits

Formato único: `{emoji} {tipo}(escopo): Descrição`. A regra completa está na nota **Padrão de commit**, dentro do `Vault/`.
