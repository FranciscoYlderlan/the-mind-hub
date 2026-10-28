---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-19
substitui: 
---
# ✅ Plataforma final do app

- **Proposta (plano):** [[geral-contexto]], fato "Plataforma final do app", em aberto entre Windows nativo e Linux pelo WSLg depois de [[geral-decisao-2026-11-19-repositorio-e-ambiente]].
- **Decisão:** o MyHarness roda no **Windows**, como app nativo. O WSL + Docker serve só para desenvolver e testar.
- **Alteração:** nenhuma
- **Motivo:** resposta do humano em 2026-11-19.
- **Consequências:** no app final, as credenciais ficam no Gerenciador de Credenciais do Windows e os agentes formam um grupo (Job Object) do Windows. A CI checa em `windows-latest`. As medidas dos RNF valem no Windows 11, como pede a especificação. No container, o código também precisa compilar e rodar no Linux (Secret Service no lugar do Gerenciador de Credenciais).

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[geral-plano-arquitetura-e-stack]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
