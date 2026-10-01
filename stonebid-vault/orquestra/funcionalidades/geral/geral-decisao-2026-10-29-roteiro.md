---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-29
substitui: 
aliases: [Roteiro aprovado, Etapas do projeto, Fluxo de tarefas, Project roadmap]
---
# ✅ Roteiro do projeto: 8 etapas, uma por incremento

- **Proposta (plano):** [[geral-plano]], proposta da IA em 2026-10-29 14:04: etapas 2 a 7 seguem os incrementos I0 a I5 de [[contrato-processo-e-plano]], e a etapa 8 é revisão e entrega.
- **Decisão:** o humano aprovou o roteiro (texto do humano: "esse roteiro foi aprovado").
  1. Definir o roteiro
  2. Esqueleto no ar (I0)
  3. Carteira e lotes (I1)
  4. Lances (I2)
  5. Sala ao vivo e liquidação (I3)
  6. Auditoria pública (I4)
  7. Opcionais (I5)
  8. Revisão e entrega
- **Alteração:** nenhuma.
- **Motivo:** fluxo simples que cobre a aplicação inteira; o detalhe de cada etapa já está no contrato.
- **Consequências:** toda etapa de código segue o ciclo branch → CI verde → `staging` → `main`, com MCP atualizada, Playwright nas telas e teste T-xx junto com a regra. Mudar a lista de etapas exige nova decisão.

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[geral-plano]]
- Projeto: [[geral-contexto]]
- Relacionadas: [[contrato-processo-e-plano]]
- Regras: [[manual-da-orquestra]]
