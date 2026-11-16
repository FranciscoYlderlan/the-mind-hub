---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-26
substitui: 
---
# ✅ Todo número e padrão do produto vira opção em Configurações

- **Proposta (plano):** pontos do humano na sessão de 2026-11-26 07h14: "tudo que for parametrizável irá virar opção, com descrição breve abaixo dos inputs, configurável em settings". O orquestrador propôs separar números e padrões (viram opção) das regras de governança (ficam no núcleo) e pôr cada parâmetro na tela pela etapa que o cria.
- **Decisão:** todo limite numérico e todo valor padrão do MyHarness vira opção na tela Configurações (TEL-06). Cada opção tem: valor de fábrica, faixa permitida (mínimo e máximo; exceção: o teto de tokens do projeto), descrição breve logo abaixo do campo dizendo o que ela controla, e "restaurar padrão" do campo. A tela tem também o botão **"Restaurar configurações padrão"**, que volta todas as opções e todos os prompts de papel ao valor de fábrica de uma vez, depois de uma confirmação; cada prompt volta como versão nova, com o histórico preservado (RF-31); cofres ligados (UC-14) e pastas em contexto (ENT-26) não são opções e não mudam. Exemplos aprovados: limite de tokens do projeto e do chat, quantidade de agentes por tipo ([[geral-decisao-2026-11-26-agentes-por-tipo]]), voltas de teste (2), devoluções do plano (2), modelo padrão por tipo, tamanho máximo do briefing (3 mil tokens) e do relatório (1,5 mil), tempo para considerar um agente caído (RNF-07), tamanho do prompt de papel (80 palavras, 150 tokens). Ficam fixas no núcleo, fora das opções: as ferramentas de cada papel (RN-27), quem implementa não testa (RN-09), nada despachado sem aval (RN-05), só o orquestrador grava no cofre (RN-01) e um orquestrador por chat.
- **Alteração:** às 07h27 o humano acrescentou o botão geral "Restaurar configurações padrão"; às 10h19 o humano confirmou que o botão volta todas as configurações ao padrão, prompts incluídos; cofres e pastas não são configurações e não mudam; às 12h21 o humano confirmou a janela de confirmação antes de restaurar. Às 12h25 o humano definiu padrão e faixa: devoluções do plano 2 (1 a 5); briefing 3 mil tokens (1 mil a 8 mil); relatório 1,5 mil tokens (500 a 4 mil); silêncio para marcar o agente parado 10 min (2 a 60 min), com a detecção de queda em 5 s fixa no núcleo (RNF-07); limite de tokens do chat 100 mil (100 mil a 400 mil). Às 12h26 o humano definiu o limite de tokens do projeto desligado de fábrica ("sem limite"), com a opção de ligar um teto; às 14h27 o humano definiu que o teto, quando ligado, não tem faixa (sem mínimo e sem máximo), a única exceção à regra da faixa.
- **Motivo:** respostas do humano em 2026-11-26 (perguntas das 07h15): "números de padrões, e gostei do exemplo que você forneceu, eles serão parametrizados"; momento: "etapa 4 + cada etapa"; às 07h27: "botão de restaurar configurações padrões em settings para retornar as configurações padrões".
- **Consequências:**
  - A etapa 4 cria a tela (campo, descrição embaixo, faixa, padrão de fábrica, restaurar do campo e o botão geral) junto dos prompts de papel; cada etapa seguinte põe ali os parâmetros que ela cria: etapa 4 (prompts e o tamanho deles, modelo padrão por tipo, limites de tokens), etapa 7 (agentes por tipo, devoluções do plano, tamanho do briefing e do relatório, tempo de queda), etapa 8 (voltas de teste). A documentação e o contrato de tela têm uma tela Configurações global só, alimentada desde a etapa 4 (humano, 10h27).
  - Proibido número fixo no código para o que é parâmetro: o núcleo lê o valor da Configuração (ENT-22), validado na faixa; valor fora da faixa não é salvo e mostra o erro do campo.
  - Contrato a preencher no início de cada etapa, com aval: ENT-22 vira a tabela de parâmetros (nome, valor, padrão, mínimo, máximo, descrição); `Papel.modelo_padrao` (ENT-15) sai do código para a Configuração; TEL-06, CMP-16 e UC-13 ganham os campos; RF novo para "editar parâmetro"; AC de faixa, de restaurar o campo e de restaurar tudo.
  - Valores de fábrica e faixas que o humano ainda não definiu ficam `[a preencher]`.

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[geral-plano]]
- Junto: [[geral-decisao-2026-11-26-agentes-por-tipo]], [[geral-decisao-2026-11-26-prompt-basico-por-tipo]]
- Regras: [[manual-da-orquestra]]
