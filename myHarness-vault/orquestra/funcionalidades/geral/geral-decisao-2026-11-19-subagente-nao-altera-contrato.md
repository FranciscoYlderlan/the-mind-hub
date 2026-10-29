---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-19
substitui: 
---
# ✅ Só o orquestrador altera o contrato e as notas

- **Proposta (plano):** ciclo da etapa 2 do [[geral-plano]], em que um subagente atualizaria o rascunho do contrato.
- **Decisão:** **subagente não altera o contrato** (`Anexos/contrato/` deste cofre, e a cópia em `docs/contrato/` do repositório na aceitação final) **nem nenhuma nota do Obsidian** (este cofre e o `Vault`). Só o orquestrador faz essas alterações.
- **Alteração:** a proposta deixava o subagente reescrever o rascunho do contrato; passou a ser só leitura.
- **Motivo:** resposta do humano em 2026-11-19: "Subagentes não alteram contrato, nem documentos do obsidian, apenas o orquestrador pode realizar essas alterações".
- **Consequências:** subagente que trabalha sobre o contrato devolve no relatório as mudanças propostas (arquivo, trecho atual, trecho novo, motivo), e o orquestrador aplica. O contrato mora em `Anexos/contrato/` deste cofre e só ali é editado; o subagente o lê pela Obsidian CLI. No briefing, `Anexos/contrato/` nunca entra em "Pode tocar em"; implementador que achar regra faltando anota no relatório. O `harness-gate` do MyHarness deve negar escrita de subagente em `docs/contrato/` do repositório e nos cofres (entra na etapa 7, RN-01).

### 🔗 Conexões
- Projeto: [[geral-contexto]]
- Plano: [[geral-plano]]
- Regras: [[manual-da-orquestra]]
