---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-26
substitui: 
---
# ✅ Validação em modo de desenvolvimento e build só no fim da etapa

- **Proposta (plano):** resposta do orquestrador em 2026-11-26, 13h43, a partir da sugestão do humano de testar em modo de desenvolvimento.
- **Decisão:** o verificador de fluxo principal e os adversariais testam a tela pelo `pnpm dev:simulado` (só o Vite, sem compilar Rust) e a API pelos testes do núcleo, com o build já aquecido. O build do app instalado (`tauri build`) roda uma vez só, ao fechar a etapa.
- **Alteração:** nenhuma
- **Motivo:** aval do humano em 2026-11-26, 13h45.
- **Consequências:** o `dev:simulado` da T6 ([[geral-decisao-2026-11-19-modo-simulado]]) é a base do teste de tela. A janela real com o GitHub real e o `/login` real segue no teste manual do humano. Junto: [[geral-decisao-2026-11-26-teste-leve-na-tarefa]], [[geral-decisao-2026-11-26-adversarial-em-dois]].

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[integracoes-plano]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
