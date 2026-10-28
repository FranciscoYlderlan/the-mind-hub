---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-19
substitui: 
---
# ✅ Como os agentes testam a tela do MyHarness

- **Proposta (plano):** [[geral-plano-arquitetura-e-stack-integracoes-e-testes]], seção 5 (S6 e P3), e a dúvida do pesquisador do roteiro sobre como verificar um app desktop.
- **Decisão:** o verificador de fluxo principal e o adversarial testam a tela no navegador (Vite, porta 1420 do container), com o núcleo simulado, e a janela real do app pelo `tauri-driver` (WebDriver). O backend é testado pela camada de comandos do núcleo, sem a tela.
- **Alteração:** nenhuma
- **Motivo:** aval do humano em 2026-11-19.
- **Consequências:** no MyHarness, o Playwright do Q04 e o navegador do adversarial atuam sobre a tela no navegador; o `tauri-driver` cobre o que só a janela real mostra. O protótipo P3 da etapa 2 prova os dois caminhos.

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[geral-plano-arquitetura-e-stack-integracoes-e-testes]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
