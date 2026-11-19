---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-19
substitui: 
---
# ✅ Repositório, ambiente e acesso do agente

- **Proposta (plano):** [[geral-contexto]], fatos "Repositório de código" e "Ambiente de desenvolvimento", que estavam em aberto.
- **Decisão:** o repositório do código fica na pasta local `C:\Users\Ylderlan\Documents\Projetos\my-harness`. O desenvolvimento roda no WSL com Docker, pelo `compose.yaml` do próprio repositório. O agente **não tem acesso** a essa pasta: ele implementa e testa na própria máquina virtual e entrega os arquivos ao humano, que os coloca na pasta e sobe o ambiente no WSL para testar.
- **Alteração:** nenhuma
- **Motivo:** resposta do humano em 2026-11-19.
- **Consequências:** o agente pode criar e testar o código livremente na máquina virtual, sem pedir. A entrega ao humano é por arquivo. Escrever em `Projetos\my-harness` ou pedir acesso a ela depende de novo aval. A máquina virtual não alcança o Docker Hub, então o agente valida o `compose.yaml` só pela sintaxe e roda os testes direto na máquina virtual, onde já há Rust, Node e pnpm. O GitHub ainda não existe e fica [a preencher].

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[geral-plano]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]], [[padroes]]
