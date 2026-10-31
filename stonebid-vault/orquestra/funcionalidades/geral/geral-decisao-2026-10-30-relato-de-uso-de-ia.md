---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-30
aliases: [Relato de uso de IA, Uso de IA no projeto, E6 uso de IA, AI usage report]
---
# ✅ Relato do uso de IA (E6)

- **Proposta (plano):** rascunho do pesquisador (2026-10-30 17:2x), montado só a partir do cofre.
- **Decisão:** humano definiu em 2026-10-30 17:44 e 17:4x:
  1. **Onde fica:** um `.md` próprio com o relato, citado nos READMEs do `stonebid-web` e do `stonebid-api`; o link desse arquivo vai no formulário de envio.
  2. **Sem citar o modelo de IA.**
  3. **Conteúdo (fatos do humano):**
     - Desafio pessoal: aplicar técnicas que a comunidade adotou há pouco, pela primeira vez, para ganhar conhecimento de causa.
     - Harness próprio para orquestrar subagentes e gerenciar modelos, ações e a quantidade de subagentes, com pontos de benchmarking.
     - Agentes em várias threads e graph engineering, "dividir para conquistar": o problema vira problemas menores, em paralelo.
     - **Representação visual:** o orquestrador acessa a memória "Obsidian graph", divide a tarefa entre vários subagentes em paralelo; o resultado volta ao orquestrador, que registra na memória o resultado e o status das tarefas.
     - MCP do Obsidian para a máquina Linux usar a Obsidian CLI; spec-driven na memória, lida pela CLI, para gastar menos contexto, já que o código nem sempre deixa explícitos padrões e estrutura.
     - A memória guarda padrões do projeto, o workflow (etapas, quem faz o quê e como orquestrador e subagentes trabalham, do plano ao teste em staging), o andamento do desenvolvimento (roteiro com o status de cada etapa e o "onde parei" de cada sessão nos diários), planos (sugestões da IA), decisões (o que o desenvolvedor escolheu) e bugs (humano, 2026-10-31 17:32, para workflow e andamento); bug recorrente fica no histórico com o que ocorreu, por quê, suposições e como foi resolvido, para não voltar.
     - Orquestrador gerencia e escreve na memória; subagentes desenvolvem e testam com Playwright. Quem cria não é quem testa; por padrão, ao fim, os testes rodam em staging.
     - Corrigir a causa, não o sintoma: o código é sintoma de um processo mal estruturado ou ambíguo; o harness guarda padrões e decisões históricas para o mínimo de erro e de código fora do padrão.
     - Pontos a aprimorar: primeira vez com essas técnicas; gostou do resultado, aprendeu muito e agradece a oportunidade do teste técnico.
  4. **Tabela "Definiu / Aplicou / Refinou"**, 🧠 para IA e 👤 para desenvolvedor (emoji, sem cor própria):

| Tópico | Definiu | Aplicou | Refinou |
|---|---|---|---|
| Definição dos requisitos | 👤 | 🧠 | 🧠 |
| Modelagem da estrutura do Obsidian | 👤 | 👤 🧠 | 👤 🧠 |
| Modelagem do harness | 👤 | 🧠 | 👤 |
| Tecnologias do frontend | 👤 | 🧠 | 👤 |
| Tecnologias do backend | 👤 | 🧠 | 👤 |
| Padrões e arquitetura do frontend | 👤 | 🧠 | 👤 |
| Padrões e arquitetura do backend | 👤 | 🧠 | 👤 |
| Configuração no GCP | 👤 | 🧠 👤 | 🧠 |
| Escrita de código | 👤 | 🧠 | 👤 |
| Testes | 🧠 | 🧠 | 🧠 |

- **Alteração:** o rascunho da IA citava o modelo e não tinha harness, graph engineering, benchmarking, a tabela nem o workflow e o andamento entre o que a memória guarda; o humano trouxe esse conteúdo e tirou o modelo.
- **Motivo:** o E6 pede onde e como a IA foi usada e o que foi revisado; a IA não tinha o histórico da modelagem do harness, feita pelo humano.
- **Consequências:** tarefas R3 e TF-E em [[revisao-e-entrega-plano]]; `docs/uso-de-ia.md` do web.

### 🔗 Conexões
- Funcionalidade: [[revisao-e-entrega-contexto]]
- Fonte: [[enunciado-teste-tecnico]]
- Relacionadas: [[contrato-trabalho-com-a-ia]], [[geral-decisao-2026-10-29-modo-de-implementacao]]
- Regras: [[manual-da-orquestra]]
