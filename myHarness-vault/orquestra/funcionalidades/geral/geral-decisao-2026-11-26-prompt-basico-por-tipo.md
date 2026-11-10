---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-26
substitui: 
---
# ✅ Prompt básico próprio para cada tipo de agente

- **Proposta (plano):** ponto do humano em 2026-11-26 07h14: "prompt inicial básico para todos os tipos de agentes". O orquestrador perguntou entre um prompt comum a todos mais um por tipo, ou só um por tipo; hoje o papel pesquisa não tem prompt (ENT-08).
- **Decisão:** cada tipo de agente tem o seu prompt básico, sem texto comum entre eles: orquestrador, funcionalidade, teste, adversarial e pesquisa (novo), mais o de passagem de turno. É básico porque o núcleo o concatena antes do que o orquestrador pede para aquele agente em cada tarefa (o briefing), como no RF-32. Todos editáveis em Configurações, com versões e restaurar padrão (RF-31).
- **Alteração:** o humano escolheu "só um por tipo" e explicou o motivo: o prompt é básico porque é concatenado com o pedido de cada tarefa.
- **Motivo:** resposta do humano em 2026-11-26, pergunta das 07h15.
- **Consequências:**
  - ENT-08 ganha o fluxo `pesquisa`; RF-31 passa a listar seis fluxos. Texto de fábrica do pesquisa, proposto pelo orquestrador [a confirmar]: "Você pesquisa e só lê: não altera arquivos, cofres nem o repositório. Busque primeiro na memória pela Obsidian CLI e cite a fonte de cada fato. Separe o que encontrou do que supõe, marcando a suposição como [a confirmar]. Devolva o relatório no formato pedido, com dúvidas e o que notou fora da pergunta."
  - Ordem da chamada: prompt básico do tipo → briefing da tarefa; o texto continua sem mudar permissões (RN-27).
  - Entra no contrato e no código na etapa 4 (`prompts-de-papel`), com o tamanho máximo do prompt como parâmetro ([[geral-decisao-2026-11-26-parametros-em-configuracoes]]).

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[geral-plano]]
- Junto: [[geral-decisao-2026-11-26-parametros-em-configuracoes]], [[geral-decisao-2026-11-26-agentes-por-tipo]]
- Regras: [[manual-da-orquestra]]
