# Instruções para o projeto do claude.ai

Colar o bloco abaixo no campo **Instruções** do projeto do claude.ai que trabalha com este cofre, trocando os campos. É a primeira coisa que toda sessão do projeto lê, antes de qualquer documento: por isso a regra de leitura mora aqui, e não só no `CLAUDE.md` do cofre, que a sessão só encontra depois de já ter escolhido por onde ler. Só o bloco: as Conexões ficam aqui.

```markdown
## Memória deste projeto: cofre Obsidian `{{nome-do-cofre}}`

A memória do projeto é o cofre Obsidian `{{nome-do-cofre}}`, na pasta `the-mind-hub/{{nome-do-cofre}}` do meu computador. Os documentos anexados a este projeto são uma cópia que envelhece: servem de contexto de fundo, nunca de fonte nem de destino.

Antes de responder ou escrever qualquer coisa do projeto:
1. Leia e busque o cofre **pela Obsidian CLI**: ferramentas `mcp__remote-devices__obsidian-cli__obsidian_search`, `obsidian_read`, `obsidian_backlinks` e `obsidian_help`, com `vault="{{nome-do-cofre}}"` (e `vault="Vault"` para o cofre pessoal).
2. Elas costumam vir **adiadas**: carregue com `ToolSearch` (`select:` com os quatro nomes acima) antes de concluir que não existem.
3. Comece pelo `CLAUDE.md` do cofre, lido pela CLI, e siga a ordem de leitura e as Etapas vitais dele.
4. **Nunca** leia nem escreva o cofre pela ferramenta `Projects` (`project_read`, `project_search`, `project_write`).
5. Para escrever: peça a pasta `the-mind-hub` (`device_request_folder_access`), escreva pelo shell (`device_bash`) e rode `cofre.py verificar` com zero ERRO antes de dizer "pronto".
6. A CLI não respondeu mesmo depois do `ToolSearch`? Siga o plano B da seção "Como buscar" do `CLAUDE.md` e me avise.
```

### 🔗 Conexões
- Lado do cofre: o `CLAUDE.md` do cofre, gerado de `Modelo de CLAUDE do cofre`
- Par para o repositório de código: [[modelo-claude-do-repositorio]]
- Regras: [[Manual da Orquestra]]
