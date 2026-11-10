---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-26
substitui: 
---
# ✅ Quantidade de agentes por tipo, com mínimo e máximo

- **Proposta (plano):** ponto do humano em 2026-11-26 07h14: "quantidade de agentes aplicáveis, limite máximo e mínimo, para cada um dos tipos de agentes utilizáveis". O orquestrador perguntou se o mínimo e o máximo valem para o que roda ao mesmo tempo, para o que entra no plano ou para os dois.
- **Decisão:** para cada tipo de subagente (funcionalidade, teste, adversarial, pesquisa), Configurações tem duas opções, cada uma com faixa permitida (mínimo e máximo), valor de fábrica e descrição breve: (1) **simultâneos:** quantos daquele tipo rodam ao mesmo tempo; o excedente vai para a fila com `motivo_fila = teto`; (2) **por plano:** o mínimo e o máximo de tarefas daquele tipo que o orquestrador pode pôr num plano de delegação. O orquestrador não é tipo configurável: um por chat.
- **Alteração:** nenhuma ("ambos", a opção recomendada).
- **Motivo:** resposta do humano em 2026-11-26, pergunta das 07h15.
- **Consequências:**
  - O teto único `teto_escrita` (ENT-22, padrão 5, RN-13) vira o "simultâneos" do tipo funcionalidade, padrão 5; teste, adversarial e pesquisa passam a ter teto próprio (hoje sem limite). Valores de fábrica e faixas dos outros tipos: `[a preencher]`.
  - O adversarial continua preso ao recurso exclusivo do navegador (RN-15): o teto dele não passa o número de recursos.
  - Plano fora do mínimo ou do máximo por tipo não chega ao humano: volta ao orquestrador como devolução (ERR-49) [a confirmar: erro próprio ou ERR-49].
  - Entra no contrato e no código na etapa 7 (plano e despacho), pela tela criada na etapa 4 ([[geral-decisao-2026-11-26-parametros-em-configuracoes]]).
  - Não muda o método manual de desenvolvimento ([[geral-decisao-2026-11-20-paralelo-por-padrao]]): isto é do produto.

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[geral-plano]]
- Junto: [[geral-decisao-2026-11-26-parametros-em-configuracoes]], [[geral-decisao-2026-11-26-prompt-basico-por-tipo]]
- Regras: [[manual-da-orquestra]]
