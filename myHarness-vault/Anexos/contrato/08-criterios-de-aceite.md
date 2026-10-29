# Critérios de aceite (AC)

Um critério por fluxo (principal, alternativo e exceção), no formato dado / quando / então. Ao final de cada funcionalidade, o verificador de fluxo principal executa os AC dos fluxos principais e, depois, o adversarial executa os dos FA e FE: no backend pela API e, se a funcionalidade tem interface, também no frontend.

No MyHarness, "API" é a camada de comandos do núcleo Rust (Tauri) [a confirmar: como o verificador chama o backend sem a tela]. Todos os textos vêm dos "Aceite" da fonte. Ordem: AC-01 a AC-57 por fluxo de UC; AC-58 a AC-87, uma por RN; AC-88 a AC-121, uma por RF; AC-122 a AC-143, por fluxo de tela.

## Por fluxo de caso de uso

| ID | UC | Fluxo | Dado | Quando | Então |
|---|---|---|---|---|---|
| AC-01 | UC-01 | principal | o GitHub desconectado | o OAuth conclui | o indicador fica verde com o nome da conta |
| AC-02 | UC-01 | FA-01 | o Claude CLI logado | o painel abre | mostra a versão sem pedir login |
| AC-03 | UC-01 | FE-01 | o Claude CLI ausente | o app abre | o indicador fica em erro com o link (ERR-01) |
| AC-04 | UC-01 | FE-02 | o OAuth cancelado | o navegador fecha | o status continua desconectado (ERR-02) |
| AC-05 | UC-01 | FE-03 | o Obsidian fechado | o status é checado | aparece "Abrir Obsidian" (ERR-03) |
| AC-06 | UC-02 | principal | um chat aberto | o Humano envia | a resposta aparece em tempo real |
| AC-07 | UC-02 | FA-01 | um pedido com 3 partes | o orquestrador decide dividir | aparece o plano para aval |
| AC-08 | UC-02 | FA-02 | o chat no limite | a resposta termina | começa a passagem de turno |
| AC-09 | UC-02 | FE-01 | o Claude CLI desconectado | o Humano envia | o texto continua no campo (ERR-05) |
| AC-10 | UC-02 | FE-02 | o limite do plano atingido | o Humano envia | aparece a hora do reinício (ERR-08) |
| AC-11 | UC-03 | principal | um plano proposto | o Humano aprova | os subagentes iniciam |
| AC-12 | UC-03 | FA-01 | um comentário de alteração | é enviado | chega uma versão nova do plano |
| AC-13 | UC-03 | FA-02 | um plano recusado | o Humano volta ao chat | nenhum subagente rodou |
| AC-14 | UC-03 | FE-01 | duas tarefas sobre src/auth | o plano é aprovado | elas rodam em série (ERR-12) |
| AC-15 | UC-03 | FE-02 | o GitHub desconectado | o Humano aprova | o app pede a conexão (ERR-06) |
| AC-16 | UC-04 | principal | um plano com 2 tarefas paralelas | é aprovado | 2 abas aparecem e cada relatório chega ao cofre |
| AC-17 | UC-04 | FA-01 | 6 implementadores | são despachados | o 6º fica na fila (ERR-44) |
| AC-18 | UC-04 | FA-02 | um relatório com dúvida | chega | a dúvida aparece na caixa de aval |
| AC-19 | UC-04 | FE-01 | um processo morto | passam 5 s | a aba mostra falhou (ERR-17) |
| AC-20 | UC-04 | FE-02 | uma tentativa de merge | ocorre | o log mostra a negação (ERR-14) |
| AC-21 | UC-05 | principal | 3 critérios ✔ com prova | o teste termina | a funcionalidade fica concluida |
| AC-22 | UC-05 | FA-01 | um ✘ | o teste termina | um implementador novo recebe o bug |
| AC-23 | UC-05 | FE-01 | a 3ª reprovação | ocorre | o Humano recebe o caso (ERR-21) |
| AC-24 | UC-05 | FE-02 | um ✔ sem prova | é gravado | vira ✘ "sem prova" (ERR-20) |
| AC-25 | UC-06 | principal | a rodada concluída | o adversarial termina | cada achado tem tipo e captura |
| AC-26 | UC-06 | FA-01 | nenhum achado | o adversarial termina | a rodada fica aprovada |
| AC-27 | UC-06 | FE-01 | o navegador ocupado | o adversarial inicia | aguarda (ERR-25) |
| AC-28 | UC-06 | FE-02 | o endereço fora do ar | o adversarial tenta abrir | a rodada falha com a mensagem (ERR-26) |
| AC-29 | UC-07 | principal | 2 sugestões decididas | o Humano confirma | o cofre registra as 2 decisões |
| AC-30 | UC-07 | FA-01 | um bug | a lista abre | ele já aparece como "corrigir" |
| AC-31 | UC-07 | FE-01 | uma sugestão sem decisão | o Humano fecha | o app aponta qual falta (ERR-28) |
| AC-32 | UC-08 | principal | o limite atingido | o registro termina | um chat novo abre com o "Onde parei" |
| AC-33 | UC-08 | FA-01 | o adiamento | o Humano confirma | o diário contém o adiamento |
| AC-34 | UC-08 | FE-01 | o registro sem próximo passo | a passagem continua | o chat novo não abre (ERR-29) |
| AC-35 | UC-08 | FE-02 | o Obsidian fechado | a passagem começa | ela espera a conexão (ERR-07) |
| AC-36 | UC-09 | principal | o padrão do teste trocado | um teste é despachado | usa o novo |
| AC-37 | UC-09 | FA-01 | um reset | é confirmado | os padrões voltam aos de fábrica |
| AC-38 | UC-09 | FE-01 | um modelo removido | é salvo | aparece a mensagem e nada muda (ERR-30) |
| AC-39 | UC-10 | principal | um PR aprovado | o Humano faz o merge | o cofre registra a integração |
| AC-40 | UC-10 | FA-01 | uma ordem nova | é salva | a fila muda |
| AC-41 | UC-10 | FE-01 | um conflito | é detectado | aparece uma tarefa de ajuste (ERR-31) |
| AC-42 | UC-11 | principal | uma pasta adicionada | o próximo agente inicia | pode ler nela |
| AC-43 | UC-11 | FA-01 | uma pasta removida | o próximo agente inicia | não a acessa |
| AC-44 | UC-11 | FE-01 | uma pasta sem permissão | é adicionada | aparece a mensagem (ERR-32) |
| AC-45 | UC-12 | principal | um chat de ontem | é selecionado | reabre com as mensagens |
| AC-46 | UC-12 | FA-01 | outro projeto | é selecionado | o painel de contexto muda para ele |
| AC-47 | UC-12 | FE-01 | o cofre ausente | o chat abre | o campo de prompt fica desabilitado com a mensagem (ERR-33) |
| AC-48 | UC-13 | principal | o prompt de Teste editado | é salvo | o próximo teste começa com o texto novo |
| AC-49 | UC-13 | FA-01 | a versão 1 restaurada | é salva | vira a versão vigente |
| AC-50 | UC-13 | FA-02 | 2 execuções rodando | o Humano salva | o aviso aparece e elas mantêm a versão anterior |
| AC-51 | UC-13 | FE-01 | um texto de 95 palavras | é salvo | aparece o excesso (ERR-34) |
| AC-52 | UC-13 | FE-02 | o campo vazio | é salvo | aparece a mensagem (ERR-35) |
| AC-53 | UC-14 | principal | o Vault ligado como consulta | um agente busca | há resultados dele marcados "Vault" |
| AC-54 | UC-14 | FA-01 | a troca de memória | é confirmada | só o novo cofre aceita gravação |
| AC-55 | UC-14 | FA-02 | um cofre desativado | um agente busca | ele não aparece |
| AC-56 | UC-14 | FE-01 | um cofre que não responde | é ligado | aparece a mensagem (ERR-37) |
| AC-57 | UC-14 | FE-02 | um só cofre de memória | o Humano tenta removê-lo | o app recusa (ERR-38) |

## Por regra de negócio

| ID | UC | Fluxo | Dado | Quando | Então |
|---|---|---|---|---|---|
| AC-58 | UC-04 | regra RN-01 | um subagente de funcionalidade em execução | ele tenta escrever em orquestra/ | a escrita é bloqueada e o log mostra "escrita negada: papel sem permissão" |
| AC-59 | UC-02 | regra RN-02 | o Obsidian conectado | um agente pede uma nota | a leitura sai pela CLI e aparece na aba "Obsidian usado" |
| AC-60 | UC-04 | regra RN-03 | um relatório recebido e ainda não registrado | o orquestrador tenta delegar | a delegação espera e o log mostra "aguardando registro" |
| AC-61 | UC-01 | regra RN-04 | um log que contém um token do GitHub | ele é gravado | o token aparece como •••• |
| AC-62 | UC-03 | regra RN-05 | um plano em proposto | nenhum aval foi dado | nenhum subagente inicia |
| AC-63 | UC-03 | regra RN-06 | um ponto do plano sem aval | o orquestrador tenta registrar a decisão | a gravação é recusada |
| AC-64 | UC-03, UC-09 | regra RN-07 | o padrão do papel teste = Sonnet | uma tarefa de teste não tem modelo escolhido | ela roda com Sonnet |
| AC-65 | UC-01 | regra RN-08 | o GitHub desconectado | um plano com PR é aprovado | o despacho para e pede "conectar GitHub" |
| AC-66 | UC-05 | regra RN-09 | a funcionalidade F feita pela execução E1 | o teste de F é despachado | ele roda numa execução nova E2 |
| AC-67 | UC-06 | regra RN-10 | um briefing adversarial que cita o plano | o despacho valida | ele é recusado |
| AC-68 | UC-06 | regra RN-11 | uma funcionalidade ainda em teste | a rodada adversarial é pedida | ela fica bloqueada |
| AC-69 | UC-04 | regra RN-12 | um subagente com dúvida | ele termina | a dúvida aparece no relatório e na caixa de aval do Humano |
| AC-70 | UC-04 | regra RN-13 | 5 implementadores rodando | um 6º é despachado | ele fica na fila |
| AC-71 | UC-03 | regra RN-14 | T1 e T2 que tocam src/auth | o plano é despachado | T2 só inicia após T1 |
| AC-72 | UC-06 | regra RN-15 | o navegador em uso pelo adversarial A1 | A2 o pede | A2 fica aguardando recurso |
| AC-73 | UC-04 | regra RN-16 | dois implementadores | os dois iniciam | cada um tem worktree e branch próprias |
| AC-74 | UC-10 | regra RN-17 | um subagente com PR aberto | ele tenta git merge na main | o comando é negado |
| AC-75 | UC-05 | regra RN-18 | um critério marcado ✔ sem prova | o relatório chega | ele é gravado como ✘ "sem prova" |
| AC-76 | UC-05 | regra RN-19 | uma tarefa com 2 voltas | ela reprova de novo | nenhum implementador é despachado e o Humano recebe o caso |
| AC-77 | UC-05, UC-07 | regra RN-20 | uma funcionalidade com um bug aberto | o orquestrador tenta concluir | o status continua em-verificacao |
| AC-78 | UC-06 | regra RN-21 | que o adversarial não consegue salvar o formulário | ele relata | o achado é gravado como bug |
| AC-79 | UC-07 | regra RN-22 | 3 sugestões sem decisão | o Humano tenta fechar a rodada | o app pede as 3 decisões |
| AC-80 | UC-08 | regra RN-23 | um chat com limite de 100 mil tokens | ele chega a 100 mil | a passagem de turno começa |
| AC-81 | UC-08 | regra RN-24 | um diário sem "Próximo passo" | a passagem tenta abrir o chat novo | ele não abre |
| AC-82 | UC-02, UC-04 | regra RN-25 | um despacho de teste | a chamada sai | o início dela é o prompt de papel "Teste" vigente |
| AC-83 | UC-13 | regra RN-26 | um prompt com 95 palavras | o Humano salva | o app recusa e mostra "15 palavras acima do limite" |
| AC-84 | UC-13 | regra RN-27 | o prompt de Funcionalidade editado para "pode escrever no cofre" | o subagente tenta escrever | a escrita continua negada |
| AC-85 | UC-13 | regra RN-28 | um teste rodando com a versão 3 | o Humano salva a versão 4 | esse teste termina com a 3 e o próximo usa a 4 |
| AC-86 | UC-14 | regra RN-29 | o cofre Vault ligado como consulta | o orquestrador tenta gravar nele | a escrita é negada |
| AC-87 | UC-11, UC-14 | regra RN-30 | uma busca que acha notas em dois cofres | o resultado volta | cada nota traz o nome do cofre e a aba "Obsidian usado" agrupa por cofre |

## Por requisito funcional

| ID | UC | Fluxo | Dado | Quando | Então |
|---|---|---|---|---|---|
| AC-88 | UC-01 | requisito RF-01 | o CLI instalado e sem login | o app abre | o status é sem login e o login pode ser iniciado |
| AC-89 | UC-01 | requisito RF-02 | o Obsidian fechado | o status é checado | aparece desconectado com a mensagem da CLI |
| AC-90 | UC-01 | requisito RF-03 | o OAuth concluído | o status é checado | aparece conectado com o nome da conta |
| AC-91 | UC-01 | requisito RF-04 | o GitHub desconectado | o painel é aberto | o GitHub aparece em estado de erro com o botão "Conectar" |
| AC-92 | UC-02 | requisito RF-05 | um chat aberto | o Humano envia um prompt | a resposta começa a aparecer antes de terminar |
| AC-93 | UC-04 | requisito RF-06 | 3 subagentes despachados | o despacho termina | aparecem 3 abas novas com o papel de cada um |
| AC-94 | UC-02 | requisito RF-07 | o limite padrão de 100 mil | o Humano clica em "Novo chat" | o chat abre com esse limite |
| AC-95 | UC-03 | requisito RF-08 | um pedido grande | o orquestrador decide dividir | o plano aparece para aval e nada é despachado |
| AC-96 | UC-03 | requisito RF-09 | um plano com 3 tarefas | o Humano troca o modelo de T2 e aprova | T2 é despachada com o modelo escolhido |
| AC-97 | UC-04 | requisito RF-10 | um plano com T1 e T2 paralelas | é aprovado | as duas iniciam ao mesmo tempo |
| AC-98 | UC-04 | requisito RF-11 | um subagente que termina | o relatório chega | o orquestrador o recebe e a aba mostra concluído |
| AC-99 | UC-04 | requisito RF-12 | 4 subagentes rodando | o Humano abre o painel | vê 4 cartões atualizando |
| AC-100 | UC-09 | requisito RF-13 | o padrão do teste trocado para Haiku | um teste é despachado sem escolha | roda com Haiku |
| AC-101 | UC-11 | requisito RF-14 | um agente que lê src/app.ts | a leitura acontece | ela aparece na aba "Lidos e usados" |
| AC-102 | UC-11 | requisito RF-15 | uma busca no cofre | ela termina | a aba "Obsidian usado" lista as notas devolvidas |
| AC-103 | UC-11 | requisito RF-16 | uma pasta adicionada | o próximo agente inicia | ele tem acesso a ela |
| AC-104 | UC-08 | requisito RF-17 | um chat com limite de 100 mil e 50 mil usados | a barra é lida | mostra 50% |
| AC-105 | — (necessidade do negócio) | requisito RF-18 | o uso da janela em 70% | o painel atualiza | mostra 70% e a hora do reinício |
| AC-106 | — (necessidade do negócio) | requisito RF-19 | qualquer tela aberta | o Humano olha o canto superior esquerdo | vê os dois consumos |
| AC-107 | UC-08 | requisito RF-20 | um chat que atinge o limite | o registro termina | um chat novo abre já com o "Onde parei" como primeira leitura |
| AC-108 | — (necessidade do negócio) | requisito RF-21 | um npm test rodado por um subagente | termina | o log tem o comando, a duração e o código de saída |
| AC-109 | — (necessidade do negócio) | requisito RF-22 | um log minimizado | o Humano o expande | vê a saída completa do comando |
| AC-110 | UC-12 | requisito RF-23 | um chat fechado ontem | o Humano o seleciona no histórico | ele reabre com as mensagens |
| AC-111 | UC-05 | requisito RF-24 | uma funcionalidade entregue | o teste termina | cada critério tem ✔ ou ✘ com a prova |
| AC-112 | UC-06 | requisito RF-25 | a rodada concluída | o adversarial termina | cada achado tem tipo, passos e evidência |
| AC-113 | UC-07 | requisito RF-26 | uma sugestão | o Humano escolhe "corrigir" | o orquestrador recebe uma tarefa nova para o plano |
| AC-114 | UC-10 | requisito RF-27 | uma tarefa concluída | o subagente termina | existe um PR aberto da branch dela |
| AC-115 | UC-04 | requisito RF-28 | um relatório recebido | o orquestrador registra | a nota aparece no cofre e no log |
| AC-116 | — (necessidade do negócio) | requisito RF-29 | a regra RN-01 ativa | um subagente é despachado | a ferramenta de escrita no cofre não está entre as dele |
| AC-117 | UC-02 | requisito RF-30 | um texto de 10 linhas | o Humano digita | o campo cresce até a altura máxima e depois rola |
| AC-118 | UC-13 | requisito RF-31 | o prompt de Teste na versão 2 | o Humano edita e salva | surge a versão 3 e a 2 fica no histórico |
| AC-119 | — (necessidade do negócio) | requisito RF-32 | o prompt de Funcionalidade na versão 4 | um implementador é despachado | o log da execução mostra "prompt de papel v4" |
| AC-120 | UC-14 | requisito RF-33 | o projeto com o cofre de memória | o Humano liga o Vault como consulta | ele aparece na lista como consulta e ativo |
| AC-121 | UC-14 | requisito RF-34 | dois cofres ativos | um agente busca "padrão de commit" | o resultado traz as notas dos dois com o nome de cada cofre |

## Por fluxo de tela

| ID | UC | Fluxo | Dado | Quando | Então |
|---|---|---|---|---|---|
| AC-122 | UC-02 | TEL-01 principal | um projeto aberto | o Humano envia um prompt | a resposta e as leituras aparecem ao vivo |
| AC-123 | UC-04 | TEL-01 FA-01 | 3 cartões | o Humano clica no 2º | a aba dele fica ativa |
| AC-124 | UC-08 | TEL-01 FA-02 | a barra no limite | a resposta termina | abre o chat de continuação |
| AC-125 | UC-02 | TEL-01 FE-01 | o CLI caído | o Humano tenta enviar | o campo está desabilitado com a mensagem (ERR-05) |
| AC-126 | UC-04 | TEL-01 FE-02 | um subagente que falha | a falha é detectada | o cartão fica em erro em até 5 s (ERR-17) |
| AC-127 | UC-01 | TEL-02 principal | o GitHub desconectado | o OAuth conclui | o cartão mostra a conta |
| AC-128 | UC-01 | TEL-02 FA-01 | o Obsidian aberto | o Humano testa | aparece o número de notas indexadas |
| AC-129 | UC-01 | TEL-02 FE-01 | o OAuth recusado | o navegador fecha | o cartão mostra o motivo (ERR-02) |
| AC-130 | UC-03 | TEL-03 principal | um plano | é aprovado | as tarefas iniciam com os modelos escolhidos |
| AC-131 | UC-03 | TEL-03 FA-01 | um comentário | é enviado | chega a versão 2 do plano |
| AC-132 | UC-03 | TEL-03 FA-02 | um plano recusado | a tela fecha | nenhum subagente iniciou |
| AC-133 | UC-03 | TEL-03 FE-01 | o GitHub desconectado | a tela abre | "Aprovar" está desabilitado com o motivo (ERR-06) |
| AC-134 | UC-09 | TEL-04 principal | o teste trocado para Haiku | é salvo | o próximo teste roda com Haiku |
| AC-135 | UC-09 | TEL-04 FA-01 | o reset | é confirmado | os valores voltam aos de fábrica |
| AC-136 | UC-09 | TEL-04 FE-01 | um modelo removido | é salvo | aparece a mensagem (ERR-30) |
| AC-137 | UC-07 | TEL-05 principal | 3 sugestões decididas | são confirmadas | o cofre registra 3 decisões |
| AC-138 | UC-07 | TEL-05 FA-01 | o filtro "bug" | é aplicado | só bugs aparecem |
| AC-139 | UC-07 | TEL-05 FE-01 | uma sugestão sem decisão | o Humano confirma | ela fica destacada (ERR-28) |
| AC-140 | UC-13 | TEL-06 principal | um prompt editado | é salvo | a próxima execução daquele fluxo começa com ele |
| AC-141 | UC-13 | TEL-06 FA-01 | "Restaurar padrão" | é confirmado | o editor mostra o texto de fábrica |
| AC-142 | UC-13 | TEL-06 FE-01 | um texto longo | é salvo | aparece o excesso (ERR-34) |
| AC-143 | UC-14 | TEL-06 FE-02 | um cofre inexistente | é ligado | aparece a mensagem (ERR-37) |
