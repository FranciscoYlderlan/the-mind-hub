---
aliases: [Tabela de commits, Emojis de commit, Commit types, Qual emoji eu uso]
tags: [estudos/programacao]
tipo: conceito
status: em-uso
criado: 2026-10-26
origem: Meu prompt de versionamento do projeto conciliador-extratos; https://gitmoji.dev
---
# 🏷️ Tipos e Emojis de Commit

> [!tldr] Em uma linha
> Cada tipo de mudança tem um emoji fixo: o desenho diz o que o commit fez antes mesmo de eu ler.

Funciona como **as placas de trânsito**. Eu reconheço a placa de "pare" pela cor e pela forma, sem ler a palavra. No histórico, ✨ já diz "coisa nova" e 🩹 já diz "conserto". O formato completo está no [[Padrão de commit]].

---

| Código | Emoji | Tipo | Quando usar |
|---|---|---|---|
| `:sparkles:` | ✨ | `feat` | Nova funcionalidade |
| `:adhesive_bandage:` | 🩹 | `fix` | Correção simples de bug |
| `:zap:` | ⚡ | `refactor` | Melhorar a estrutura sem mudar o comportamento |
| `:art:` | 🎨 | `style` | Formatação, espaçamento, layout visual |
| `:package:` | 📦 | `chore` | Manutenção: remover arquivo, dependências |
| `:wrench:` | 🔧 | `chore` | Configuração e variáveis de ambiente |
| `:page_facing_up:` | 📄 | `docs` | Documentação e imagens do README |
| `:white_check_mark:` | ✅ | `test` | Testes |
| `:tada:` | 🎉 | `chore` | **Só** o primeiro commit do projeto |

---

> [!example] Exemplos no meu padrão
> - `:tada: chore(setup): Initial project setup`
> - `:zap: refactor(backend): Add pagination dto to GetFoodItems return`
> - `:adhesive_bandage: fix(frontend): Use handler env variables`
> - `:wrench: chore(frontend): Adjust example environment variables`
> - `:art: style(frontend): Adjust spacing of layout and table`

> [!warning] Meu padrão x gitmoji oficial
> Minha tabela é minha convenção. O [gitmoji](https://gitmoji.dev) oficial usa ♻️ para refactor (⚡ lá é desempenho), 📝 para docs (📄 lá é licença) e 🩹 só para correções simples. Vale a minha tabela, mas é bom saber a diferença ao ler projetos de outras pessoas.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** Escrevo o **código** (`:sparkles:`) na mensagem, e o GitHub mostra o desenho.
* **Ponto 2:** `chore` tem dois emojis: 📦 para manutenção, 🔧 para configuração.
* **Ponto 3:** Na dúvida entre `feat` e `refactor`: o usuário percebe a mudança? Se sim, é `feat`.

### 🔗 Conexões
- Mapa: [[MOC Programação]]
- Relacionadas: [[Padrão de commit]], [[Conventional Commits]]
- Próxima: [[Commit atômico]]
