---
aliases: [Onde fica o git dos cofres, Commit nos cofres, Commit in the vault hub, Como commito as notas]
tags: [estudos/programacao, ferramentas/obsidian]
tipo: procedimento
status: em-uso
criado: 2026-10-28
origem: Sessão de 2026-10-28: commit bloqueado porque a sessão só tinha acesso às pastas dos cofres
---
# 🛠️ Commitar no the-mind-hub

> [!tldr] Em uma linha
> Os cofres moram dentro do repositório `the-mind-hub`: para commitar, a sessão precisa da pasta `the-mind-hub`, não só da pasta do cofre.

É como **a chave do apartamento e a portaria do prédio**. Com a chave do apartamento eu entro no cofre e mexo nas notas. Mas o registro de quem entrou e saiu (o `.git`) fica na portaria, no térreo. O formato da mensagem continua o do [[Padrão de commit]].

---

> [!note] Passo a passo
> 1. Confiro onde está o `.git`: `git rev-parse --show-toplevel` dentro da pasta do cofre.
> 2. A sessão só tem a pasta do cofre (`Vault/`, `stonebid-vault/`...)? **Peço acesso à pasta `the-mind-hub`.**
> 3. Peço também permissão para apagar no `the-mind-hub`: o git cria e remove arquivos `.lock` a cada commit.
> 4. Rodo `cofre.py verificar` nos cofres alterados: zero ERRO. Ver [[Atualizar a memória]].
> 5. Confiro a identidade do git: `git log -3 --format='%an <%ae>'`. Se a sessão não tiver nome e e-mail configurados (erro "Author identity unknown"), uso o mesmo autor dos commits anteriores **só no comando**: `git -c user.name=franciscoylderlan -c user.email=ylderlan@nca.ufma.br commit ...`.
> 6. Commito da raiz do `the-mind-hub`, um assunto por commit. Ver [[Commit atômico]].

> [!warning] Armadilhas
> - Sem a pasta raiz, o commit falha com "not a git repository".
> - Sem permissão de apagar, o git deixa `.lock` para trás e os próximos comandos falham com "File exists".
> - Commit de cofre e commit do README são separados.
> - Sessão na nuvem (shell ligado ao computador) costuma rodar sem identidade do git e o commit falha com "Author identity unknown". Nunca rode `git config` (nem `--global`, nem no repositório) para resolver: passe `-c user.name=... -c user.email=...` no próprio comando, com o autor `franciscoylderlan <ylderlan@nca.ufma.br>`. Nunca invente autor nem use a identidade da sessão.

> [!tip] Quando abrir esta nota
> Sempre que for commitar mudanças em qualquer cofre do `the-mind-hub`.
> → Commit: `:page_facing_up: docs(vault): Add ...`

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** O `.git` mora na raiz do `the-mind-hub`, não dentro de cada cofre.
* **Ponto 2:** Pasta do cofre basta para escrever; para commitar, precisa da raiz e de permissão de apagar.
* **Ponto 3:** Erro comum: tentar commitar só com a pasta do cofre e concluir que "não tem git".
* **Ponto 4:** Sem identidade do git na sessão, o autor é sempre `franciscoylderlan <ylderlan@nca.ufma.br>`, passado com `-c` só no commit, sem mexer na configuração.

### 🔗 Conexões
- Mapa: [[MOC Programação]]
- Relacionadas: [[Padrão de commit]], [[Commit atômico]], [[Registrar cofre no README]]
- Próxima: [[Padrão de commit]]
