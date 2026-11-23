---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-23
substitui: 
---
# ✅ Erro interno genérico no catálogo (ERR-55)

- **Proposta (plano):** conferência da T5 do [[fundacao-plano]]: falha inesperada do próprio núcleo não tinha código no catálogo.
- **Decisão:** entra o ERR-55 `FALHA_INTERNA`, com tratamento `repetir`, mensagem "Algo deu errado no MyHarness: <motivo>. Tente de novo." e o caso no Log (ENT-12), com o motivo mascarado.
- **Alteração:** nenhuma.
- **Motivo:** resposta do humano em 2026-11-23, às 17h26: "sim".
- **Consequências:** contrato com M-43 e AC-156; o `CodigoErro` em Rust, TS e zod ganha o ERR-55; erro sem código do catálogo fica proibido na IPC.

### 🔗 Conexões
- Funcionalidade: [[fundacao-contexto]]
- Plano: [[fundacao-plano]]
- Candidatos: [[fundacao-plano-candidatos]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
