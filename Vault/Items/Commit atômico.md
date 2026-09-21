---
aliases: [Um commit uma mudança, Atomic commit, Como fatiar commits, Commit pequeno]
tags: [estudos/programacao]
tipo: conceito
status: rascunho
criado: 2026-10-26
origem: Meu prompt de versionamento do projeto conciliador-extratos; https://cbea.ms/git-commit/
---
# ⚛️ Commit Atômico

> [!tldr] Em uma linha
> Um commit guarda uma única mudança coesa. Dois assuntos viram dois commits.

É como **as caixas de uma mudança de casa**. Uma caixa escrita "cozinha" só tem coisas da cozinha. Se eu misturar panela com toalha, na hora de desfazer a caixa eu me perco. Commit também: se algo quebrar, eu desfaço só aquela caixa. Combina com a minha [[Atenção em túnel]]: um assunto por vez, no código e nas notas.

---

| ❌ Commit misturado | ✅ Commits atômicos |
|---|---|
| `feat(backend): Add upload and fix layout and update readme` | `:sparkles: feat(backend): Add upload endpoint` |
| | `:art: style(frontend): Adjust table layout` |
| | `:page_facing_up: docs(readme): Update usage section` |

---

> [!note] Ordem natural de um projeto
> 1. 🎉 Setup do projeto.
> 2. ✨ Estrutura do backend, depois integrações e regras de negócio.
> 3. ✨ Frontend.
> 4. ✅ Testes.
> 5. 🎨 Ajustes de estilo e 📄 documentação.
> 6. 🩹 Correções finais e a tag da versão. Ver [[Versionamento semântico]].

> [!tip] Quando abrir esta nota
> Quando eu for escrever a mensagem e precisar da palavra "and". O "and" avisa que ali cabem dois commits.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** Uma mudança = um commit = uma mensagem no [[Padrão de commit]].
* **Ponto 2:** Commits pequenos facilitam revisar, desfazer (`git revert`) e achar onde o erro entrou.
* **Ponto 3:** Erro comum: fazer um commit gigante no fim do dia com "tudo que mudei".

### 🔗 Conexões
- Mapa: [[MOC Programação]]
- Relacionadas: [[Padrão de commit]], [[Atenção em túnel]], [[Versionamento semântico]]
- Próxima: [[Conventional Commits]]
