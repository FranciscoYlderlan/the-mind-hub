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
> Toda mensagem de commit, em todo cofre (prático e estudo) e em todo repositório, segue um formato fixo: `emoji tipo(escopo): Descrição`, sem variações.

É como **o rótulo dos potes da despensa**. Se todo pote tem etiqueta no mesmo formato, eu acho o açúcar sem abrir nada. No histórico do Git é igual: bato o olho e sei o que cada commit fez. Esse formato vem do [[Conventional Commits]], com os emojis da minha [[Tipos e emojis de commit|tabela de tipos]].

---

```
:sparkles: feat(backend): Add bank statement upload endpoint
│          │    │          └─ Descrição: imperativo, maiúscula, sem ponto final
│          │    └─ Escopo: um da lista fechada do projeto, sempre entre parênteses
│          └─ Tipo: o que a mudança é, sem abreviar
└─ Emoji: código do tipo (o GitHub mostra o desenho)
```

---

> [!note] Passo a passo
> 1. Confiro se o commit tem **uma mudança só**. Ver [[Commit atômico]].
> 2. Escolho o tipo e o emoji na [[Tipos e emojis de commit|tabela]].
> 3. Escolho o escopo na **lista fechada** do projeto: o bloco `<!-- projeto:escopos -->` do `CLAUDE.md` do cofre ou do repositório. No cofre, a lista sempre começa com o nome da pasta do cofre e `readme` (commits no [[Commitar no the-mind-hub|the-mind-hub]]); a criação só acrescenta os escopos do projeto (área como `backend` e `frontend`, ID do requisito ou outro), que são os do repositório de código; no projeto prático, sempre também `contrato`, o do commit que copia o contrato para `docs/contrato/` do repositório na aceitação final. A lista só muda com aval. Um commit tem um escopo só: mudanças em cofres diferentes (ou cofre e README) viram commits diferentes.
> 4. Escrevo a descrição em inglês, no imperativo (`Add`, e não `Added`), dentro do [[ASD-STE100]] completo: só palavras aprovadas do dicionário, no sentido e na classe aprovados; nome técnico do projeto entra como *technical noun*; uma ação só; até 20 palavras.
> 5. Começo com maiúscula e termino sem ponto.

> [!warning] Armadilhas
> - Escopo **sempre presente**: nunca `feat:` sozinho.
> - Escopo entre parênteses, nunca com barra: `feat(backend)`, e não `feat/backend`.
> - Tipo por extenso: `refactor`, e não `refact`.
> - Escopo fora da lista fechada: não invento; peço para incluir na lista.
> - `:tada:` só no **primeiro commit** do projeto.
> - Verbo fora do dicionário do STE: troco pela alternativa aprovada (ex.: `Make sure`, e não `Ensure`). Sem o PDF da norma, a palavra fica `[a confirmar]`.
> - Commit só no **meu nome**: sem `Co-Authored-By` nem link de sessão de IA, mesmo quando um agente faz o commit.

> [!tip] Quando commitar
> - **Cofre:** a cada registro concluído e na passagem de turno.
> - **Código:** um commit por unidade lógica, e PR ao fim da tarefa.
> - Os dois modelos de `CLAUDE.md` (do [[Modelo de CLAUDE do cofre|cofre]] e do [[modelo-claude-do-repositorio|repositório]]) trazem a seção de commits.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** Formato único: `{emoji} {tipo}(escopo): Descrição`. Esqueleto fixo, igual às minhas notas.
* **Ponto 2:** Dica do imperativo: a frase completa "If applied, this commit will ___". Exemplo: "will *Add pagination*".
* **Ponto 3:** Erro comum: juntar dois assuntos numa mensagem só.

### 🔗 Conexões
- Mapa: [[MOC Programação]]
- Relacionadas: [[Tipos e emojis de commit]], [[Commit atômico]], [[Conventional Commits]], [[Commitar no the-mind-hub]], [[ASD-STE100]]
- Próxima: [[Tipos e emojis de commit]]
