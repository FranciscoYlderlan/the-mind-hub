---
aliases: [Mapa de cofres, Atualizar README do hub, Vault map, Qual memória usar]
tags: [ferramentas/obsidian, estudos/programacao]
tipo: procedimento
status: em-uso
criado: 2026-10-26
origem: README do repositório the-mind-hub
---
# 🛠️ Registrar Cofre no README

> [!tldr] Em uma linha
> Todo cofre novo ganha uma linha na tabela "Mapa de cofres" do README. Assim, eu sei qual memória abrir para cada projeto.

O README é **o mapa do shopping**, aquela placa com "você está aqui". Ele não guarda nada, só diz em que andar fica cada loja. Bato o olho, acho o projeto e sei qual cofre abrir. A estrutura do cofre vem de [[Criar um novo cofre]].

---

```
| Cofre | Projeto | Para quê | Quando abrir |
|---|---|---|---|
| `conciliador-extratos/` | [conciliador](link-do-repo) | Regras de conciliação e decisões | Antes de mexer no código do conciliador |
```

---

> [!note] Passo a passo
> 1. Abro o `README.md` na raiz do `the-mind-hub`.
> 2. Adiciono **uma linha** na tabela "Mapa de cofres".
> 3. **Cofre:** o nome da pasta. **Projeto:** o nome, com link do repositório se houver.
> 4. **Para quê:** meia frase. **Quando abrir:** a situação concreta do meu dia.
> 5. Projeto encerrado? Não apago a linha. Escrevo "(arquivado)" no fim do nome do projeto.

> [!tip] Quando abrir esta nota
> Logo depois de criar um cofre, antes do commit.
> → Commit: `:page_facing_up: docs(readme): Register nome-do-cofre vault`

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** Uma linha por cofre, sem textão. O detalhe mora na `Home` do cofre.
* **Ponto 2:** A coluna "Quando abrir" é o gatilho, igual ao `[!tip]` das notas.
* **Ponto 3:** O commit do README é separado do commit do cofre. Ver [[Commit atômico]].

### 🔗 Conexões
- Mapa: [[MOC Programação]]
- Relacionadas: [[Criar um novo cofre]], [[Commit atômico]]
- Próxima: [[Padrão de commit]]
