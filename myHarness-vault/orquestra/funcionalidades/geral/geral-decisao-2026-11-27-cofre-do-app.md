---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-27
---
# ✅ O app cria ou anexa o cofre; o myHarness-vault não é o cofre do app

- **Proposta (plano):** o pesquisador da etapa 5 propôs um projeto provisório com o `myHarness-vault` como cofre de memória, até a etapa 6.
- **Decisão:** o `myHarness-vault` é o cofre usado para **construir** o MyHarness; ele não é o cofre de referência do aplicativo. No app, deve ser possível:
  - criar um cofre do zero ("Criar novo cofre", pelo `cofre.py criar`, [[geral-decisao-2026-11-26-criar-cofre-pelo-myharness]]);
  - anexar um cofre que já existe;
  - conectar o MCP para usar a Obsidian CLI.
- **Acesso dos agentes no app:** **todos** os agentes (orquestrador e subagentes de todo papel) podem **ler** o Obsidian pela Obsidian CLI, via MCP. **Só o orquestrador escreve.** A ferramenta de escrita não chega ao subagente, e o portão nega escrita em cofre.
- **Alteração:** nenhuma
- **Motivo:** respostas do humano em 2026-11-27: às 07h50, o `myHarness-vault` "não será o cofre utilizado como referência para o aplicativo"; às 07h55, "todos os agentes tem permissão de ler o obsidian via cli via mcp ... mas apenas o orquestrador tem permissão de escrever".
- **Consequências:** o projeto provisório da base comum nasce **sem cofre fixo**; o cofre vem de criar ou anexar. Os testes usam cofre temporário e o servidor MCP falso. As demais lacunas propostas pelos pesquisadores foram aprovadas em bloco ([[geral-plano-etapas-4-a-7]], seção Lacunas).

### 🔗 Conexões
- Plano: [[geral-plano-etapas-4-a-7]]
- Relacionada: [[geral-decisao-2026-11-26-criar-cofre-pelo-myharness]], [[geral-decisao-2026-11-19-acesso-ao-obsidian]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
