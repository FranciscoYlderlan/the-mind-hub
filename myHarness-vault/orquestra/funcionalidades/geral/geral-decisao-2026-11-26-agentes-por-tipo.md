---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-26
substitui: 
---
# ✅ Quantidade de agentes por tipo, com mínimo e máximo

- **Proposta (plano):** ponto do humano em 2026-11-26 07h14: "quantidade de agentes aplicáveis, limite máximo e mínimo, para cada um dos tipos de agentes utilizáveis". O orquestrador perguntou se o mínimo e o máximo valem para o que roda ao mesmo tempo, para o que entra no plano ou para os dois.
- **Decisão:** para cada tipo de subagente (funcionalidade, teste, adversarial, pesquisa), Configurações tem duas opções, cada uma com faixa permitida (mínimo e máximo), valor de fábrica e descrição breve: (1) **simultâneos:** quantos daquele tipo rodam ao mesmo tempo, com a escolha "sem limite" disponível em todo tipo; com número, o excedente vai para a fila com `motivo_fila = teto`; (2) **por plano:** o mínimo e o máximo de tarefas daquele tipo que o orquestrador pode pôr num plano de delegação. O orquestrador não é tipo configurável: um por chat.
- **Alteração:** "ambos", a opção recomendada; depois, o humano acrescentou que pesquisa vem de fábrica "sem limite" e que todo tipo tem a escolha "sem limite" em Configurações, para poder abrir vários quando for possível.
- **Motivo:** resposta do humano em 2026-11-26, pergunta das 07h15; acréscimo às 07h26: "o de leitura/pesquisa aparece na configuração como sem limite e em configurações aparece para cada um dos agentes sem limites".
- **Consequências:**
  - O teto único `teto_escrita` (ENT-22, padrão 5, RN-13) vira o "simultâneos" do tipo funcionalidade, padrão 5; pesquisa vem de fábrica "sem limite"; teste e adversarial ganham teto próprio, com valor de fábrica e faixa `[a preencher]`. Em todo tipo, a faixa vai de um mínimo até "sem limite".
  - O adversarial continua preso ao recurso exclusivo do navegador (RN-15): mesmo com "sem limite", o que passar do número de recursos espera na fila com `motivo_fila = recurso`.
  - Plano fora do mínimo ou do máximo por tipo não chega ao humano: volta ao orquestrador como devolução (ERR-49) [a confirmar: erro próprio ou ERR-49].
  - Entra no contrato e no código na etapa 7 (plano e despacho), pela tela criada na etapa 4 ([[geral-decisao-2026-11-26-parametros-em-configuracoes]]).
  - Não muda o método manual de desenvolvimento ([[geral-decisao-2026-11-20-paralelo-por-padrao]]): isto é do produto.

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[geral-plano]]
- Junto: [[geral-decisao-2026-11-26-parametros-em-configuracoes]], [[geral-decisao-2026-11-26-prompt-basico-por-tipo]]
- Regras: [[manual-da-orquestra]]
