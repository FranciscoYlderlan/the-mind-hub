---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-19
substitui: 
---
# ✅ Gravação dupla: SQLite e cofre com o mesmo conteúdo

- **Proposta (plano):** revisão do modelo de dados pedida pelo humano em 2026-11-19 (o que o SQLite guarda que o cofre não guarda).
- **Decisão:** o modelo de dados de [[geral-decisao-2026-11-19-entidades-no-sqlite]] fica como está. O que mora nos dois lugares (plano, tarefa, relatório, achado e o aval da decisão) é gravado no SQLite e no cofre na mesma operação do núcleo, com o mesmo conteúdo. Se um lado falha, o outro é desfeito e nada é gravado (ERR-51). Uma conferência, só no teste, compara os dois lados e manda a diferença ao Log (RN-31; AC-147 e AC-148). O aval da decisão vai com a hora do registro (`registrada_em`), que a RN-03 usa.
- **Alteração:** nenhuma
- **Motivo:** o humano cogitou deixar essas entidades só no cofre. Desistiu porque o núcleo precisaria gravar o frontmatter das notas, e hoje só o orquestrador escreve no cofre. Ficou valendo a regra de não haver escritas diferentes. Aval do humano em 2026-11-19, sessões das 16h35 e 16h49.
- **Consequências:** o G1 (esquema SQLite e contrato IPC) traz uma única função de gravação por entidade dupla, com desfazer.

### 🔗 Conexões
- Projeto: [[geral-contexto]]
- Plano: [[geral-plano]]
- Decisão que completa: [[geral-decisao-2026-11-19-entidades-no-sqlite]]
- Regras: [[manual-da-orquestra]]
