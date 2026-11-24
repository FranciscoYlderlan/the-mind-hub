---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-24
substitui: 
---
# ✅ "Desconectar" o Claude CLI vale só no MyHarness

- **Proposta (plano):** dúvida da T1 do [[integracoes-plano]]: fazer logout da CLI tiraria o login do Humano também fora do app.
- **Decisão:** "Desconectar" do Claude CLI marca a integração como `desconectado` no MyHarness e não faz logout da CLI.
- **Alteração:** nenhuma.
- **Motivo:** resposta do humano em 2026-11-24: "Só no MyHarness".
- **Consequências:** a T4 guarda o estado de desconectado do núcleo; o login da CLI fora do app segue valendo.

### 🔗 Conexões
- Funcionalidade: [[integracoes-contexto]]
- Plano: [[integracoes-plano]]
- Projeto: [[geral-contexto]]
