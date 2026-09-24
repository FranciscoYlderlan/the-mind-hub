---
aliases: [Meu padrão de commit, Mensagem de commit, Commit message pattern, Como escrevo commit]
tags: [estudos/programacao]
tipo: procedimento
status: em-uso
criado: 2026-10-26
origem: Meu prompt de versionamento do projeto conciliador-extratos
---
# 🛠️ Padrão de Commit

> [!tldr] Em uma linha
> Toda mensagem de commit segue um formato fixo: `emoji tipo(escopo): Descrição`, sem variações.

É como **o rótulo dos potes da despensa**. Se todo pote tem etiqueta no mesmo formato, eu acho o açúcar sem abrir nada. No histórico do Git é igual: bato o olho e sei o que cada commit fez. Esse formato vem do [[Conventional Commits]], com os emojis da minha [[Tipos e emojis de commit|tabela de tipos]].

---

```
:sparkles: feat(backend): Add bank statement upload endpoint
│          │    │          └─ Descrição: imperativo, maiúscula, sem ponto final
│          │    └─ Escopo: a área do projeto, sempre entre parênteses
│          └─ Tipo: o que a mudança é, sem abreviar
└─ Emoji: código do tipo (o GitHub mostra o desenho)
```

---

> [!note] Passo a passo
> 1. Confiro se o commit tem **uma mudança só**. Ver [[Commit atômico]].
> 2. Escolho o tipo e o emoji na [[Tipos e emojis de commit|tabela]].
> 3. Defino o escopo: a pasta ou área real (`backend`, `frontend`, `infra`, `readme`, `setup`).
> 4. Escrevo a descrição em inglês, no imperativo: `Add`, e não `Added`.
> 5. Começo com maiúscula e termino sem ponto.

> [!warning] Armadilhas
> - Escopo **sempre presente**: nunca `feat:` sozinho.
> - Escopo entre parênteses, nunca com barra: `feat(backend)`, e não `feat/backend`.
> - Tipo por extenso: `refactor`, e não `refact`.
> - `:tada:` só no **primeiro commit** do projeto.
> - Commit só no **meu nome**: sem `Co-Authored-By` nem link de sessão de IA, mesmo quando um agente faz o commit.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** Formato único: `{emoji} {tipo}(escopo): Descrição`. Esqueleto fixo, igual às minhas notas.
* **Ponto 2:** Dica do imperativo: a frase completa "If applied, this commit will ___". Exemplo: "will *Add pagination*".
* **Ponto 3:** Erro comum: juntar dois assuntos numa mensagem só.

### 🔗 Conexões
- Mapa: [[MOC Programação]]
- Relacionadas: [[Tipos e emojis de commit]], [[Commit atômico]], [[Conventional Commits]], [[Commitar no the-mind-hub]]
- Próxima: [[Tipos e emojis de commit]]
