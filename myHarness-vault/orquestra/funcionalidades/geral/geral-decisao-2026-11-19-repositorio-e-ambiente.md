---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-19
substitui: 
---
# ✅ Repositório, ambiente e acesso do agente

- **Proposta (plano):** [[geral-contexto]], fatos "Repositório de código" e "Ambiente de desenvolvimento", que estavam em aberto.
- **Decisão:** o repositório do código fica na pasta local `C:\Users\Ylderlan\Documents\Projetos\my-harness`. O agente escreve direto nessa pasta e implementa e testa na própria máquina virtual ([[geral-decisao-2026-11-19-acesso-ao-repositorio]]). O `compose.yaml` do repositório serve para o humano rodar o projeto no WSL com Docker quando quiser.
- **Alteração:** nenhuma
- **Motivo:** resposta do humano em 2026-11-19.
- **Consequências:** o agente pode criar e testar o código livremente na máquina virtual e na pasta, sem pedir; ação irreversível segue pedindo confirmação. A máquina virtual não alcança o Docker Hub, então o agente valida o `compose.yaml` só pela sintaxe e roda os testes direto na máquina virtual, onde já há Rust, Node e pnpm. O remoto é `FranciscoYlderlan/MyHarness` no GitHub: o orquestrador dá o push e abre as PRs, e o humano aprova ou não ([[geral-decisao-2026-11-23-push-e-pr-no-github]]).

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[geral-plano]]
- Ponto alterado: [[geral-decisao-2026-11-23-push-e-pr-no-github]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]], [[padroes]]
