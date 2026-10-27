---
aliases: [CLAUDE.md do cofre, Instruções do cofre para agentes, Vault agent guide, Como a IA entende o cofre]
tags: [ferramentas/obsidian, estudos/programacao]
tipo: procedimento
status: em-uso
criado: 2026-10-27
origem: Configuração do the-mind-hub para projetos do Claude Code
---
# 🛠️ Guia do Cofre para IA

> [!tldr] Em uma linha
> Todo cofre tem um `CLAUDE.md` na raiz: o manual de bolso que o agente lê assim que o cofre entra como contexto.

É como **o crachá com instruções pendurado na porta de cada sala**. Quem entra não precisa perguntar onde fica cada coisa: lê o crachá e já trabalha. Como cada projeto conecta um grupo diferente de cofres, cada cofre carrega o próprio crachá. O conteúdo vem do [[Manual do Meu Cérebro no Obsidian|Manual]] e segue o esqueleto do `Modelo de CLAUDE do cofre`.

---

> [!note] Passo a passo
> 1. Copio `Vault/Modelos/Modelo de CLAUDE do cofre.md` para a raiz do cofre novo, com o nome exato `CLAUDE.md`.
> 2. Troco `{{nome-da-pasta}}` pelo nome da pasta do cofre (é o nome que a Obsidian CLI usa).
> 3. Troco `{{projeto}}` e `{{para quê}}` pelo projeto e por meia frase de objetivo.
> 4. Confiro que o arquivo cita **só o próprio cofre**. Cofres vizinhos entram apenas pela regra de fronteira.
> 5. Copio o Manual para `Items/` do cofre novo, para o `CLAUDE.md` funcionar mesmo sem o `Vault` conectado.

> [!warning] Armadilhas
> - Nome do arquivo em maiúsculas: `CLAUDE.md`. Outro nome o agente não lê sozinho.
> - O `CLAUDE.md` não é nota: sem frontmatter e fora de `Items/`.
> - Mudou uma regra do Manual? Atualizo o resumo nos `CLAUDE.md` dos cofres.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** Um `CLAUDE.md` por cofre faz qualquer combinação de cofres funcionar num projeto.
* **Ponto 2:** O agente lê o crachá e já sabe estrutura, regras e como buscar.
* **Ponto 3:** Erro comum: escrever no `CLAUDE.md` regras de outro cofre e misturar os contextos.

### 🔗 Conexões
- Mapa: [[MOC Programação]]
- Relacionadas: [[Criar um novo cofre]], [[Registrar cofre no README]]
- Próxima: [[Registrar cofre no README]]
