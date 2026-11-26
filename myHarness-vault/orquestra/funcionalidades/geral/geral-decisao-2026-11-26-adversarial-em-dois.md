---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-26
substitui: 
---
# ✅ Adversarial em dois, em paralelo: API e tela

- **Proposta (plano):** resposta do orquestrador em 2026-11-26 13h03: o adversarial da `integracoes` levou cerca de 27 min, com API e tela em sequência.
- **Decisão:** ao final de cada funcionalidade com interface, o orquestrador despacha dois adversariais em paralelo: um ataca pela API (camada de comandos do núcleo) e o outro pela tela (`dev:simulado` no navegador). Os dois recebem os mesmos AC de FA e FE e a lista fixa de ataques, cada um na sua parte. Funcionalidade sem interface tem um adversarial só, pela API.
- **Alteração:** nenhuma
- **Motivo:** aval do humano em 2026-11-26, 13h04.
- **Consequências:** o adversarial da tela não compila o Rust, porque o `dev:simulado` roda só o Vite ([[geral-decisao-2026-11-19-modo-simulado]], T6); assim só um build disputa o disco. O da API usa o clone e o `target/` compartilhados ([[geral-decisao-2026-11-26-build-reaproveitado-na-validacao]]). Pronto = AC dos UC passando nos dois relatórios.

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Junto: [[geral-decisao-2026-11-26-build-reaproveitado-na-validacao]], [[geral-decisao-2026-11-19-modo-simulado]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
