---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-28
substitui: 
aliases: [Como criar componentes, Regras de componentes, shadcn first, Component guidelines]
---
# ✅ Criação de componentes no frontend

- **Proposta (plano):** nenhuma. A definição veio direto do humano, como base do projeto.
- **Decisão:** componente novo no `stonebid-web` passa por este roteiro, nesta ordem:
  1. **Já existe, ou existe algo parecido?** Consultar o [[registro-de-componentes]] neste cofre e o código. Existindo, reutilizar. Parecido, adaptar a peça existente para receber a variação (props, `children` ou slot), em vez de criar outra.
  2. **Vai ser reutilizado?** Avaliar se o componente pode ser usado em outras telas.
  3. **Está no shadcn/ui?** Checar o catálogo e o comando de instalação, e **instalar sempre pela CLI** (`npx shadcn@latest add <componente>`). Componente do shadcn **nunca é escrito à mão** nem copiado da documentação: o código dele só entra no projeto pelo comando.
  4. **Só então criar**, se nada acima resolver: em `components/common/` quando compartilhado, em `features/<feature>/components/` quando é do domínio.
  5. **Registrar** o componente no [[registro-de-componentes]].
- **Regras de escrita:**
  - Evitar elementos HTML nativos quando o shadcn/ui tem equivalente pronto (`Button`, `Input`, `Select`, `Dialog`...).
  - Nada de telas ou componentes muito grandes. Código limpo, sem repetição; o que pede refatoração vira componentes menores.
  - Para padrões que se repetem, usar templates de estruturação, evitando reescrita de código e mutações desnecessárias.
  - Componente próprio nunca vai para `components/ui/` (reservado ao shadcn).
  - Tudo em `components/ui/` nasce do comando `npx shadcn@latest add`; nenhum arquivo dessa pasta é criado manualmente.
- **Reuso como padrão do projeto (humano, 2026-10-29):** vale para toda tela e todo componente do `stonebid-web`, não só para um caso. Reuso de componentes bem arquitetados é princípio de código limpo e de boa arquitetura.
  - **Por quê: DRY (Don't Repeat Yourself).** É o princípio mais citado sobre o tema, de Andy Hunt e Dave Thomas em *The Pragmatic Programmer*. A definição formal: **cada pedaço de conhecimento deve ter uma representação única, inequívoca e autoritativa no sistema**. Criar um segundo componente quase igual ao primeiro, só com algo a mais, duplica conhecimento: a próxima mudança precisa ser feita nos dois lugares, e o dia em que um deles for esquecido as telas passam a divergir.
  - **DRY trata de conhecimento, não de texto parecido.** Os próprios autores reforçam isso: dois trechos que se parecem por coincidência, mas mudam por motivos diferentes, não são o mesmo conhecimento e não precisam virar um só. A pergunta é "se esta regra mudar, as duas peças mudam juntas?". Se sim, é uma peça só.
  - **Compor antes de criar:** tela ou componente parecido com outro é a mesma peça, com a parte que muda recebida de fora (props, `children` ou um slot nomeado, como `bidSlot`). Nada de copiar a tela e trocar um trecho.
  - **A variação vem de fora, não de uma condição interna:** o componente não pergunta quem está logado nem em que rota está; quem decide é a rota ou o componente pai. Variação visual usa as variantes do próprio shadcn (`variant`, `size`).
  - **Detectar ao escrever:** o mesmo trecho de UI ou de lógica apareceu pela segunda vez, extrair na hora: para `components/common/` se não tem regra de negócio, para `features/<feature>/components/` se é do domínio, para um hook se é lógica de estado.
  - **Pequeno e com uma responsabilidade:** componente que faz duas coisas vira dois, para cada parte poder ser reaproveitada.
  - **Revisão:** trecho copiado entre telas, ou componente novo que repete um existente, é erro de revisão, como componente do shadcn escrito à mão.
- **Alteração:** 2026-10-29: o humano deixou explícito que os componentes do shadcn/ui não são escritos, e sim instalados pelos comandos da CLI (o passo 3 dizia só "evitar criar do zero"). 2026-10-29: reuso e detecção de componentes reutilizáveis passaram a ser padrão de todo o projeto: o passo 1 inclui "algo parecido" e entrou a seção "Reuso como padrão do projeto" (humano). 2026-10-29: motivação pelo DRY (Hunt e Thomas, *The Pragmatic Programmer*) acrescentada à seção, com o limite de que DRY trata de conhecimento, não de texto parecido (humano; o limite foi acrescentado pela IA).
- **Motivo:** evitar duplicação e retrabalho, aproveitando o que o shadcn/ui já entrega. Reuso de componentes bem arquitetados é princípio de código limpo e de boa arquitetura, e o DRY pede uma representação única de cada conhecimento (humano, 2026-10-29).
- **Consequências:**
  - Proibido: escrever ou colar à mão o código de um componente do shadcn/ui, ou criar arquivo manualmente em `components/ui/`. O implementador informa no relatório o comando `npx shadcn@latest add ...` que rodou.
  - Toda tarefa de frontend que cria ou instala componente termina com o registro atualizado. Como só o orquestrador escreve no cofre, o implementador lista os componentes novos no relatório e o orquestrador registra.
  - O briefing de implementador do frontend aponta para o [[registro-de-componentes]] e para esta nota.
  - O relatório do implementador lista, além dos componentes novos e dos comandos do shadcn, os **componentes reaproveitados** e os **candidatos a extração** que encontrou; o orquestrador registra no [[registro-de-componentes]].
  - Exemplo aplicado: a sala do lote em duas rotas (`/lots/$id` e `/bidding/$id`) que compõem a mesma `LotRoom` pelo `bidSlot` ([[geral-decisao-2026-10-28-estrutura-frontend]]).
  - Estrutura das pastas: [[geral-decisao-2026-10-28-estrutura-frontend]].

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[geral-plano]]
- Projeto: [[geral-contexto]]
- Relacionadas: [[registro-de-componentes]], [[geral-decisao-2026-10-28-stack-frontend]]
- Regras: [[manual-da-orquestra]]
