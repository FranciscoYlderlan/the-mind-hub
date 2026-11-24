---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-24
substitui: 
---
# ✅ Falha inesperada vai ao registro do núcleo até a etapa 6

- **Proposta (plano):** verificação da T4 do [[integracoes-plano]]: o contrato mandava ERR-53 e ERR-55 ao Log (ENT-12), que exige `execucao`; o Log sem execução foi recusado ([[geral-decisao-2026-11-24-estado-da-integracao-com-notas-e-erro]]).
- **Decisão:** ERR-53 e ERR-55 vão ao registro do núcleo (saída de erro, `RegistroNoTerminal`), com o motivo mascarado, até a etapa 6 do [[geral-plano]] (`logs`), que define o destino final.
- **Alteração:** nenhuma.
- **Motivo:** resposta do humano em 2026-11-24, às 16h: "Terminal por enquanto".
- **Consequências:** contrato com M-48 (05 e AC-156); a etapa 6 revê o destino. Na mesma resposta, o ERR-02 ganhou o motivo na mensagem (M-47).

### 🔗 Conexões
- Funcionalidade: [[integracoes-contexto]]
- Plano: [[integracoes-plano]], [[geral-plano]]
- Decisões ligadas: [[geral-decisao-2026-11-24-erro-generico-por-fronteira]]
- Projeto: [[geral-contexto]]
