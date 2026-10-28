# Trecho para o CLAUDE.md do repositório de código

Colar o bloco abaixo no `CLAUDE.md` ou `AGENTS.md` do repositório do projeto, trocando os campos. Só o bloco: as Conexões ficam aqui.

```markdown
## Memória do projeto

A memória deste projeto é o cofre Obsidian `{{nome-do-cofre}}`, em `{{caminho-do-cofre}}`.

- Antes de qualquer tarefa, leia `{{caminho-do-cofre}}/CLAUDE.md` e siga a ordem de leitura dele.
- A sessão principal é o orquestrador: só ela escreve no cofre, no fim do trabalho.
- Subagentes leem o cofre, trabalham em worktree própria e devolvem relatório no formato de `orquestra/modelos/modelo-relatorio-subagente.md`.
- Comandos de prova deste repositório: teste `{{comando}}` · lint `{{comando}}` · tipos `{{comando}}`
```

### 🔗 Conexões
- Lado do cofre: o `CLAUDE.md` do cofre, gerado de `Modelo de CLAUDE do cofre`
- Formato dos subagentes: [[modelo-briefing-subagente]], [[modelo-relatorio-subagente]]
- Regras: [[Manual da Orquestra]]
