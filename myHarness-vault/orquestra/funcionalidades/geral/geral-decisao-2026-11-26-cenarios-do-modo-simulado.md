---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-26
substitui: 
---
# ✅ Cenários do modo simulado por URL

- **Proposta (plano):** dúvida do implementador da T6 ([[integracoes-plano-verificacoes-t6-t7#T6]]): cenários do modo simulado escolhidos pela URL (ex.: `?cenario=erro`), para os verificadores.
- **Decisão:** o `dev:simulado` aceita um cenário pela URL (`?cenario=<nome>`). Cada cenário põe o núcleo simulado num estado do contrato: as integrações sem login, não instaladas ou com cada erro do catálogo que a tela mostra. Sem o parâmetro, vale o cenário de hoje. Só no modo de desenvolvimento, fora do app instalado.
- **Alteração:** nenhuma
- **Motivo:** resposta do humano em 2026-11-26, 14h27 ("Sim").
- **Consequências:** tarefa T9 do [[integracoes-plano]]. O verificador de fluxo principal e o adversarial da tela abrem cada FA e FE direto pela URL, sem harness externo. A lista de cenários acompanha o contrato: erro novo na tela ganha cenário novo, como manda a [[geral-decisao-2026-11-19-modo-simulado]].

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[integracoes-plano]]
- Junto: [[geral-decisao-2026-11-19-modo-simulado]], [[geral-decisao-2026-11-26-validacao-em-modo-dev]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
