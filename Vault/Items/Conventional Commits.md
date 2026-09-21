---
aliases: [Commits convencionais, Conventional Commits, Especificação de commits, Padrão tipo escopo descrição]
tags: [estudos/programacao]
tipo: conceito
status: rascunho
criado: 2026-10-26
origem: https://www.conventionalcommits.org/pt-br/v1.0.0/
---
# 📮 Conventional Commits

> [!tldr] Em uma linha
> Conventional Commits é uma especificação aberta para mensagens de commit no formato `tipo(escopo): descrição`. É a base do meu padrão.

É como **o endereço numa carta**. Rua, número, CEP: sempre na mesma ordem, então até a máquina dos Correios consegue ler. Com o commit é igual: num formato fixo, pessoas **e ferramentas** entendem o histórico. Meu [[Padrão de commit]] usa esse formato e acrescenta um emoji na frente.

---

```
tipo(escopo opcional): descrição

corpo opcional (o porquê da mudança)

rodapé opcional (ex.: BREAKING CHANGE: ...)
```

---

> [!note] Como funciona
> 1. **Tipo** diz o que mudou. A especificação define `feat` e `fix`. Outros (`docs`, `test`, `chore`...) são convenção comum.
> 2. **Escopo** diz onde mudou. Na especificação é opcional; no meu padrão é **obrigatório**.
> 3. **Descrição**: resumo curto logo depois dos dois-pontos.
> 4. **BREAKING CHANGE** no rodapé (ou `!` depois do tipo) avisa que a mudança quebra compatibilidade.

> [!tip] Por que ferramentas gostam disso
> Com o formato fixo, dá para gerar o CHANGELOG sozinho e calcular a próxima versão: `fix` → patch, `feat` → minor, breaking → major. Ver [[Versionamento semântico]].

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** Meu padrão = Conventional Commits + emoji + escopo obrigatório.
* **Ponto 2:** O tipo da mensagem conversa direto com o número da versão.
* **Ponto 3:** Limite: a especificação não fala de emoji. O emoji é uma camada minha, inspirada no gitmoji.

### 🔗 Conexões
- Mapa: [[MOC Programação]]
- Relacionadas: [[Padrão de commit]], [[Tipos e emojis de commit]]
- Próxima: [[Versionamento semântico]]
