# Casos de uso (UC)

Um caso de uso por objetivo do ator. O fluxo principal vem em passos numerados (ator → sistema). Fluxo alternativo (FA) é outro caminho válido; fluxo de exceção (FE) termina num erro do catálogo (`05-erros.md`).

Os IDs FA e FE são locais a cada UC, como na fonte (cite como "UC-03 FE-01"). Os critérios de aceite de cada fluxo estão em `08-criterios-de-aceite.md`.

## UC-01 Conectar integrações

- **Ator:** ATR-01; sistemas ATR-06, ATR-07, ATR-08
- **Objetivo:** deixar Claude CLI, Obsidian CLI e GitHub prontos para uso.
- **Requisitos:** RF-01, RF-02, RF-03, RF-04, RN-04, RN-08
- **Gatilho:** o app abre, ou o Humano clica numa integração.
- **Pré-condições:** nenhuma.
- **Pós-condições:** sucesso, integração `conectado` com credencial no cofre do SO; falha, status com o motivo.
- **Telas:** TEL-02 (e CMP-03 da TEL-01)

### Fluxo principal

1. Humano abre o painel de integrações → sistema mostra o status das três.
2. Humano clica em "Conectar" numa integração → sistema abre o login ou o OAuth.
3. Humano conclui o login → sistema valida e mostra `conectado`.

### Fluxos alternativos (FA)

| ID | Passo de origem | Variação | Volta ou termina |
|---|---|---|---|
| FA-01 | 2 | A integração já está conectada → sistema mostra conta e versão | Termina |

### Fluxos de exceção (FE)

| ID | Passo de origem | Erro | Estado final |
|---|---|---|---|
| FE-01 | 1 | ERR-01 | Claude CLI em `não instalado`, com o link de instalação |
| FE-02 | 3 | ERR-02 | GitHub em `desconectado` |
| FE-03 | 1 | ERR-03 | Obsidian CLI em `desconectado`, com a ação "Abrir Obsidian" |

## UC-02 Conversar com o orquestrador

- **Ator:** ATR-01; ATR-02, ATR-06
- **Objetivo:** pedir trabalho e receber respostas.
- **Requisitos:** RF-05, RF-07, RF-30, RN-02, RN-07, RN-08, RN-23, RN-25
- **Gatilho:** Humano envia um prompt.
- **Pré-condições:** Claude CLI conectado; projeto selecionado.
- **Pós-condições:** sucesso, mensagem e resposta no histórico; falha, prompt preservado.
- **Telas:** TEL-01

### Fluxo principal

1. Humano digita e clica em enviar → sistema envia ao orquestrador com o modelo escolhido, precedido do prompt de papel do orquestrador (RN-25).
2. Orquestrador busca contexto no cofre pela CLI → sistema mostra as leituras no painel de contexto.
3. Orquestrador responde → sistema transmite a resposta na aba do orquestrador e atualiza a barra do chat.

### Fluxos alternativos (FA)

| ID | Passo de origem | Variação | Volta ou termina |
|---|---|---|---|
| FA-01 | 3 | O orquestrador decide dividir o trabalho | Segue para UC-03 |
| FA-02 | 3 | O chat chega ao limite | Segue para UC-08 |

### Fluxos de exceção (FE)

| ID | Passo de origem | Erro | Estado final |
|---|---|---|---|
| FE-01 | 1 | ERR-05 | Nada enviado; o prompt fica no campo |
| FE-02 | 3 | ERR-08 | Chat em `pausado`; a hora do reinício aparece |

## UC-03 Aprovar o plano de delegação

- **Ator:** ATR-01; ATR-02
- **Objetivo:** decidir como o trabalho é dividido antes de qualquer subagente rodar.
- **Requisitos:** RF-08, RF-09, RN-05, RN-06, RN-07, RN-08, RN-14
- **Gatilho:** orquestrador propõe um plano.
- **Pré-condições:** plano em `proposto`.
- **Pós-condições:** sucesso, plano `aprovado` e decisões no cofre; falha, plano `proposto` ou `recusado`.
- **Telas:** TEL-03

### Fluxo principal

1. Sistema mostra o plano: tarefas, papel, dependências, paralelo ou série, modelo sugerido.
2. Humano ajusta o modelo de cada tarefa, se quiser.
3. Humano clica em "Aprovar" → sistema grava o aval, o orquestrador registra as decisões no cofre e o despacho começa (UC-04).

### Fluxos alternativos (FA)

| ID | Passo de origem | Variação | Volta ou termina |
|---|---|---|---|
| FA-01 | 3 | Humano pede alteração com comentário → orquestrador propõe plano novo | Volta ao passo 1 |
| FA-02 | 3 | Humano recusa → plano vira `recusado` | Termina |

### Fluxos de exceção (FE)

| ID | Passo de origem | Erro | Estado final |
|---|---|---|---|
| FE-01 | 3 | ERR-12 | O sistema ajusta a ordem para série; volta ao passo 1 |
| FE-02 | 3 | ERR-06 | Plano segue `proposto` |

## UC-04 Executar tarefas em paralelo

- **Ator:** ATR-02; ATR-03, ATR-06, ATR-08
- **Objetivo:** construir as funcionalidades do plano com subagentes.
- **Requisitos:** RF-06, RF-10, RF-11, RF-12, RF-28, RN-01, RN-03, RN-12, RN-13, RN-14, RN-16, RN-17, RN-25
- **Gatilho:** plano aprovado.
- **Pré-condições:** plano `aprovado`; integrações necessárias conectadas.
- **Pós-condições:** sucesso, branches com push e relatórios no cofre; falha, execução `falhou` registrada.
- **Telas:** TEL-01

### Fluxo principal

1. Sistema cria worktree e branch por tarefa e inicia um subagente por tarefa, até o teto.
2. Sistema mostra cada subagente numa aba e num cartão de progresso.
3. Subagente termina, faz push e devolve o relatório.
4. Orquestrador registra o relatório no cofre e manda a tarefa para teste (UC-05).

### Fluxos alternativos (FA)

| ID | Passo de origem | Variação | Volta ou termina |
|---|---|---|---|
| FA-01 | 1 | Teto atingido → tarefas extras ficam na fila (ERR-44) e iniciam quando uma vaga abre | Volta ao passo 2 |
| FA-02 | 3 | Relatório com dúvidas → dúvidas vão para a caixa de aval do Humano | Continua no passo 4 |

### Fluxos de exceção (FE)

| ID | Passo de origem | Erro | Estado final |
|---|---|---|---|
| FE-01 | 3 | ERR-17 | Execução `falhou` com o último log; o orquestrador decide refazer com subagente novo |
| FE-02 | 3 | ERR-13 (escrita no cofre) ou ERR-14 (merge) | Ação negada, log de violação; a execução continua |

## UC-05 Testar funcionalidade

- **Ator:** ATR-04; ATR-02
- **Objetivo:** provar que a funcionalidade cumpre os critérios.
- **Requisitos:** RF-24, RN-09, RN-15, RN-18, RN-19, RN-20
- **Gatilho:** relatório de funcionalidade registrado.
- **Pré-condições:** funcionalidade `em-verificacao`; critérios definidos.
- **Pós-condições:** sucesso, funcionalidade `concluida`; falha, `em-verificacao` ou `bloqueada`.
- **Telas:** TEL-01, TEL-05

### Fluxo principal

1. Sistema despacha um subagente de teste novo com critérios e prova.
2. Subagente roda as provas e checa cada critério.
3. Sistema grava ✔/✘ com a prova.
4. Todos ✔ → funcionalidade `concluida`.

### Fluxos alternativos (FA)

| ID | Passo de origem | Variação | Volta ou termina |
|---|---|---|---|
| FA-01 | 4 | Algum ✘ → bug vai a um implementador novo (UC-04) e o teste roda de novo | Volta ao passo 1 |

### Fluxos de exceção (FE)

| ID | Passo de origem | Erro | Estado final |
|---|---|---|---|
| FE-01 | 4 | ERR-21 | Caso na caixa de aval; funcionalidade `bloqueada` |
| FE-02 | 3 | ERR-20 | Critério gravado ✘ "sem prova"; segue o FA-01 |

## UC-06 Validar fluxos com o adversarial

- **Ator:** ATR-05; ATR-02, ATR-09
- **Objetivo:** descobrir, sem contexto, se a aplicação é fácil de usar e se os fluxos se completam.
- **Requisitos:** RF-25, RN-10, RN-11, RN-15, RN-21
- **Gatilho:** todas as funcionalidades da rodada `concluida`.
- **Pré-condições:** aplicação rodando num endereço de teste; acesso de teste disponível.
- **Pós-condições:** sucesso, achados registrados; falha, rodada `falhou` com motivo.
- **Telas:** TEL-01, TEL-05

### Fluxo principal

1. Sistema despacha o adversarial só com objetivos, endereço e acesso.
2. Adversarial tenta cada objetivo pelo navegador.
3. Adversarial devolve achados tipados (bug ou sugestão) com passos e captura.
4. Sistema mostra os achados para decisão (UC-07).

### Fluxos alternativos (FA)

| ID | Passo de origem | Variação | Volta ou termina |
|---|---|---|---|
| FA-01 | 3 | Nenhum achado → rodada `aprovada` | Termina |

### Fluxos de exceção (FE)

| ID | Passo de origem | Erro | Estado final |
|---|---|---|---|
| FE-01 | 2 | ERR-25 | Adversarial aguardando recurso |
| FE-02 | 2 | ERR-26 | Rodada `falhou` |

## UC-07 Decidir sobre achados

- **Ator:** ATR-01; ATR-02
- **Objetivo:** dar a palavra final sobre bugs e sugestões.
- **Requisitos:** RF-26, RN-20, RN-21, RN-22
- **Gatilho:** achados novos.
- **Pré-condições:** rodada com achados.
- **Pós-condições:** sucesso, achados decididos e tarefas criadas; falha, rodada `aguardando decisão`.
- **Telas:** TEL-05

### Fluxo principal

1. Sistema lista os achados com evidência.
2. Humano escolhe, para cada sugestão, corrigir, registrar como limite ou deixar opcional.
3. Sistema envia as decisões ao orquestrador, que registra no cofre e cria tarefas para os "corrigir".

### Fluxos alternativos (FA)

| ID | Passo de origem | Variação | Volta ou termina |
|---|---|---|---|
| FA-01 | 2 | Achado é bug → vai direto a correção, sem pedir escolha | Continua no passo 3 |

### Fluxos de exceção (FE)

| ID | Passo de origem | Erro | Estado final |
|---|---|---|---|
| FE-01 | 3 | ERR-28 | Rodada `aguardando decisão` |

## UC-08 Passar o turno

- **Ator:** ATR-02; ATR-01, ATR-07
- **Objetivo:** continuar o trabalho num chat novo sem perder o fio.
- **Requisitos:** RF-17, RF-20, RN-23, RN-24
- **Gatilho:** chat atinge o limite de contexto, ou o Humano pede.
- **Pré-condições:** chat `ativo`.
- **Pós-condições:** sucesso, chat anterior `encerrado` e chat novo `ativo`; falha, chat anterior `ativo`.
- **Telas:** TEL-01

### Fluxo principal

1. Sistema avisa o orquestrador do limite.
2. Orquestrador registra no cofre o "Onde parei": próximo passo, threads abertas, dúvidas.
3. Sistema abre um chat novo ligado ao anterior.
4. O chat novo começa lendo o "Onde parei".

### Fluxos alternativos (FA)

| ID | Passo de origem | Variação | Volta ou termina |
|---|---|---|---|
| FA-01 | 1 | Humano adia a passagem (uma vez por chat, RN-23) → sistema registra o adiamento no diário | O chat segue |

### Fluxos de exceção (FE)

| ID | Passo de origem | Erro | Estado final |
|---|---|---|---|
| FE-01 | 2 | ERR-29 | O chat novo não abre; o orquestrador refaz o passo 2 |
| FE-02 | 2 | ERR-07 | A passagem espera a conexão |

## UC-09 Gerir modelos

- **Ator:** ATR-01
- **Objetivo:** definir o modelo padrão de cada papel.
- **Requisitos:** RF-13, RN-07
- **Gatilho:** Humano abre a gestão de modelos.
- **Pré-condições:** Claude CLI conectado.
- **Pós-condições:** sucesso, padrões salvos; falha, padrões anteriores.
- **Telas:** TEL-04

### Fluxo principal

1. Sistema lista os modelos disponíveis e o padrão de cada papel.
2. Humano troca um padrão.
3. Sistema salva; as próximas execuções usam o novo padrão.

### Fluxos alternativos (FA)

| ID | Passo de origem | Variação | Volta ou termina |
|---|---|---|---|
| FA-01 | 2 | Humano restaura os padrões de fábrica → sistema volta aos valores iniciais | Continua no passo 3 [a confirmar: a fonte não diz] |

### Fluxos de exceção (FE)

| ID | Passo de origem | Erro | Estado final |
|---|---|---|---|
| FE-01 | 3 | ERR-30 | O padrão anterior continua |

## UC-10 Integrar entrega

- **Ator:** ATR-01; ATR-08
- **Objetivo:** levar o código aprovado para a branch principal.
- **Requisitos:** RF-27, RN-08, RN-17
- **Gatilho:** funcionalidade `concluida` com PR aberto.
- **Pré-condições:** PR aberto; GitHub conectado.
- **Pós-condições:** sucesso, PR `merged` registrado; falha, PR aberto com tarefa de ajuste.
- **Telas:** TEL-01 [a confirmar: nenhum CMP da fonte lista os PRs]

### Fluxo principal

1. Sistema lista os PRs prontos, com a ordem sugerida.
2. Humano abre o PR e faz o merge no GitHub.
3. Sistema detecta o merge e avisa o orquestrador, que registra no cofre.

### Fluxos alternativos (FA)

| ID | Passo de origem | Variação | Volta ou termina |
|---|---|---|---|
| FA-01 | 2 | Humano escolhe outra ordem → sistema atualiza a fila | Continua no passo 2 |

### Fluxos de exceção (FE)

| ID | Passo de origem | Erro | Estado final |
|---|---|---|---|
| FE-01 | 2 | ERR-31 | PR aberto; o orquestrador cria uma tarefa de ajuste que mantém as duas mudanças |

## UC-11 Gerir contexto

- **Ator:** ATR-01
- **Objetivo:** ver o que os agentes leem e escolher as pastas em contexto.
- **Requisitos:** RF-14, RF-15, RF-16, RN-02, RN-30
- **Gatilho:** Humano abre o painel de contexto.
- **Pré-condições:** projeto selecionado.
- **Pós-condições:** sucesso, lista de contexto atualizada; falha, lista anterior.
- **Telas:** TEL-01

### Fluxo principal

1. Sistema mostra as três abas: lidos e usados, Obsidian usado, em contexto.
2. Humano adiciona uma pasta na aba "Em contexto".
3. Sistema confirma e as próximas execuções têm acesso a ela.

### Fluxos alternativos (FA)

| ID | Passo de origem | Variação | Volta ou termina |
|---|---|---|---|
| FA-01 | 2 | Humano remove uma pasta → sistema tira o acesso das próximas execuções | Termina [a confirmar] |

### Fluxos de exceção (FE)

| ID | Passo de origem | Erro | Estado final |
|---|---|---|---|
| FE-01 | 2 | ERR-32 | A lista não muda |

## UC-12 Retomar do histórico

- **Ator:** ATR-01
- **Objetivo:** reabrir um projeto ou chat anterior.
- **Requisitos:** RF-23, RN-02
- **Gatilho:** Humano abre o histórico.
- **Pré-condições:** existe ao menos um chat salvo.
- **Pós-condições:** sucesso, chat ou projeto ativo; falha, chat `só leitura`.
- **Telas:** TEL-01

### Fluxo principal

1. Sistema lista projetos e chats, com a cadeia de passagens de turno.
2. Humano seleciona um chat.
3. Sistema reabre o chat; se estava encerrado por passagem, oferece ir ao chat de continuação.

### Fluxos alternativos (FA)

| ID | Passo de origem | Variação | Volta ou termina |
|---|---|---|---|
| FA-01 | 2 | Humano seleciona um projeto → sistema troca o projeto ativo e abre o último chat dele | Termina |

### Fluxos de exceção (FE)

| ID | Passo de origem | Erro | Estado final |
|---|---|---|---|
| FE-01 | 3 | ERR-33 | Chat aberto só para leitura; campo de prompt desabilitado |

## UC-13 Editar prompts de papel

- **Ator:** ATR-01
- **Objetivo:** ajustar as responsabilidades primárias que cada fluxo recebe antes de toda instrução.
- **Requisitos:** RF-31, RF-32, RN-25, RN-26, RN-27, RN-28
- **Gatilho:** Humano abre Configurações → Prompts de papel.
- **Pré-condições:** nenhuma.
- **Pós-condições:** sucesso, versão nova vigente e anterior no histórico; falha, versão anterior vigente.
- **Telas:** TEL-06

### Fluxo principal

1. Sistema lista os 5 fluxos com o prompt vigente, a versão e a contagem de palavras e tokens.
2. Humano edita um prompt → a contagem atualiza enquanto digita.
3. Humano salva → sistema grava a versão nova, que vale para as próximas execuções.

### Fluxos alternativos (FA)

| ID | Passo de origem | Variação | Volta ou termina |
|---|---|---|---|
| FA-01 | 2 | Humano restaura uma versão anterior ou o padrão de fábrica → sistema carrega o texto | Continua no passo 3 |
| FA-02 | 3 | Há execuções em andamento → sistema avisa "<n> execuções seguem com a versão anterior" | Continua |

### Fluxos de exceção (FE)

| ID | Passo de origem | Erro | Estado final |
|---|---|---|---|
| FE-01 | 3 | ERR-34 | Nada é salvo |
| FE-02 | 3 | ERR-35 | Nada é salvo |

## UC-14 Ligar cofres de memória e consulta

- **Ator:** ATR-01; ATR-07
- **Objetivo:** pesquisar em mais de um cofre do Obsidian sem misturar onde se grava.
- **Requisitos:** RF-33, RF-34, RN-02, RN-08, RN-29, RN-30
- **Gatilho:** Humano abre Configurações → Cofres.
- **Pré-condições:** Obsidian aberto; projeto selecionado.
- **Pós-condições:** sucesso, lista de cofres do projeto atualizada; falha, lista anterior.
- **Telas:** TEL-06

### Fluxo principal

1. Sistema lista os cofres que a Obsidian CLI enxerga e os já ligados ao projeto.
2. Humano liga um cofre como consulta → sistema testa uma busca nele.
3. Busca ok → o cofre fica ativo e as próximas buscas dos agentes passam por ele.

### Fluxos alternativos (FA)

| ID | Passo de origem | Variação | Volta ou termina |
|---|---|---|---|
| FA-01 | 2 | Humano troca qual cofre é a memória → sistema pede confirmação e o antigo vira consulta | Continua no passo 3 |
| FA-02 | 2 | Humano desativa um cofre de consulta → ele sai das buscas, mas continua ligado | Termina |

### Fluxos de exceção (FE)

| ID | Passo de origem | Erro | Estado final |
|---|---|---|---|
| FE-01 | 2 | ERR-37 | Cofre `desconectado` |
| FE-02 | 2 | ERR-38 | Nada muda |
