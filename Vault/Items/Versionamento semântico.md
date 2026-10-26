---
aliases: [SemVer, Semantic versioning, Número de versão, O que significa v1.0.6]
tags: [estudos/programacao]
tipo: conceito
status: rascunho
criado: 2026-10-26
origem: https://semver.org/lang/pt-BR/
---
# 🔢 Versionamento Semântico

> [!tldr] Em uma linha
> Versionamento semântico (SemVer) é o número `MAIOR.MENOR.CORREÇÃO`. Cada parte conta que tipo de mudança aconteceu.

Pense nas **edições de um livro**. Uma reimpressão que só corrige erros de digitação é a correção. Um capítulo novo, que não estraga o que já existia, é a versão menor. Uma edição reescrita, em que as páginas antigas não batem mais, é a versão maior. A tag `v1.0.6` do meu projeto conciliador-extratos segue essa lógica.

---

| Parte | Exemplo | Sobe quando | Commit que costuma causar |
|---|---|---|---|
| MAIOR (major) | **2**.0.0 | Quebra compatibilidade | `BREAKING CHANGE` |
| MENOR (minor) | 1.**1**.0 | Função nova compatível | ✨ `feat` |
| CORREÇÃO (patch) | 1.0.**7** | Correção compatível | 🩹 `fix` |

---

> [!note] Como funciona
> 1. Subiu uma parte? As partes à direita voltam a zero: `1.4.2` → `1.5.0`.
> 2. Versão `0.x.y` = projeto em desenvolvimento, tudo pode mudar.
> 3. A **tag** no Git (`git tag v1.0.6`) marca o commit exato daquela versão.
> 4. `v1.0.6` = primeira versão estável com 6 correções depois do `1.0.0`.

> [!tip] Quando abrir esta nota
> Na hora de fechar uma entrega e decidir o número da próxima tag.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** Os tipos do [[Conventional Commits]] dizem qual número sobe.
* **Ponto 2:** A tag vai no último commit relevante da versão, depois das correções finais.
* **Ponto 3:** Erro comum: subir o MAIOR por "achar a mudança grande". Ele só sobe quando quebra compatibilidade.

### 🔗 Conexões
- Mapa: [[MOC Programação]]
- Relacionadas: [[Conventional Commits]], [[Commit atômico]]
- Próxima: [[Padrão de commit]]
