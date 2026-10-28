---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-19
substitui: 
---
# ✅ Agentes não herdam configurações pessoais

- **Proposta (plano):** dúvida do [[diario-2026-11-19]]: quais configurações pessoais do humano os agentes herdam (proposta: nenhuma).
- **Decisão:** os agentes despachados pelo MyHarness **não herdam nenhuma** configuração pessoal do Claude CLI do humano.
- **Alteração:** nenhuma
- **Motivo:** resposta do humano em 2026-11-19.
- **Consequências:** cada `claude -p` roda só com a configuração que o MyHarness monta para o papel (ferramentas, permissões e ganchos da [[geral-decisao-2026-11-19-stack]]); o protótipo P1 confirma que nada do perfil pessoal vaza para o agente.

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[geral-plano-arquitetura-e-stack]]
- Regras: [[manual-da-orquestra]]
