# Requisitos (RF, RNF, RN)

Transcrição dos requisitos do documento-fonte. Cite sempre pelo ID daqui; a numeração do original fica só na coluna Origem.

- **Documento-fonte:** "Harness — especificação funcional", sem número de versão [a confirmar], 18 de nov. de 2026, @Ylderlan (decisões D5 e D6 de 2026-11-19)
- **Preenchido em:** 2026-11-19 (rascunho do pesquisador, aguardando aval do humano)

**Fronteiras (seção "Fronteiras" da fonte):** o Obsidian lembra, o MyHarness governa, o Modelo executa e o Humano valida. A regra de como os agentes trabalham é código no núcleo Rust (Tauri), que monta o briefing de cada papel, decide ferramentas e pastas de cada processo e segura o despacho até o aval. "Backend" = núcleo Rust (Tauri), que conversa com as CLIs e o GitHub; "frontend" = interface React.

## Funcionais (RF)

A camada (backend, frontend, ambos) e a dependência vêm entre colchetes. As RN de cada RF estão em `07-rastreabilidade.md`.

| ID | Requisito | Origem | Prioridade |
|---|---|---|---|
| RF-01 | Detectar o Claude CLI instalado, verificar a autenticação e iniciar o login quando faltar. Entrada: caminho do executável (opcional). Saída: status (conectado, sem login, não instalado) e versão. [backend; depende de RF-04] | Seção 2 · Integrações; UC-01 | Essencial |
| RF-02 | Verificar se o Obsidian está aberto, se a CLI responde e se o cofre do projeto está acessível. Entrada: nome do cofre. Saída: status e número de notas indexadas. [backend; depende de RF-04] | Seção 2 · Integrações; UC-01 | Essencial |
| RF-03 | Autenticar no GitHub por OAuth e guardar o token no cofre de credenciais do sistema operacional. Entrada: consentimento no navegador. Saída: status, conta, escopos. [backend; depende de RF-04] | Seção 2 · Integrações; UC-01 | Essencial |
| RF-04 | Mostrar no canto superior direito o status das três integrações e permitir conectar cada uma. Entrada: status de RF-01 a RF-03. Saída: indicadores e ação "conectar". [frontend; depende de RF-01, RF-02, RF-03] | Seção 2 · Integrações; UC-01 | Essencial |
| RF-05 | Enviar o prompt ao orquestrador e transmitir a resposta em tempo real. Entrada: texto, chat_id, modelo do orquestrador. Saída: eventos de resposta, uso de tokens. [backend; depende de RF-30] | Seção 2 · Chat e orquestrador; UC-02 | Essencial |
| RF-06 | Mostrar uma aba para o orquestrador e uma aba por subagente, agrupadas por papel (funcionalidade, teste, adversarial). Entrada: execuções ativas. Saída: abas com a saída de cada agente. [frontend; depende de RF-11] | Seção 2 · Chat e orquestrador; UC-04 | Essencial |
| RF-07 | Abrir um chat novo do orquestrador, com o limite de contexto padrão, ligado ao projeto atual. Entrada: projeto, limite (opcional). Saída: chat novo vazio. [ambos; depende de RF-23] | Seção 2 · Chat e orquestrador; UC-02 | Essencial |
| RF-08 | Receber do orquestrador um plano estruturado de tarefas (faz, toca em, depende de, paralelo, pronto quando, prova, papel) e segurá-lo até o aval. Entrada: saída estruturada do orquestrador. Saída: PlanoDelegação em proposto. [backend; depende de RF-09] | Seção 2 · Chat e orquestrador; UC-03 | Essencial |
| RF-09 | Mostrar o plano, permitir trocar o modelo de cada tarefa, aprovar, alterar ou recusar. Entrada: PlanoDelegação. Saída: aval, modelos por tarefa, pedido de alteração. [frontend; depende de RF-08] | Seção 2 · Chat e orquestrador; UC-03 | Essencial |
| RF-10 | Iniciar um processo do Claude CLI por tarefa aprovada, com o briefing do papel, o modelo e as ferramentas permitidas ao papel. Entrada: plano aprovado. Saída: execuções em rodando ou na fila. [backend; depende de RF-06, RF-12] | Seção 2 · Chat e orquestrador; UC-04 | Essencial |
| RF-11 | Acompanhar os eventos de cada subagente e, ao fim, ler o relatório no formato fixo e entregá-lo ao orquestrador. Entrada: eventos do processo. Saída: progresso, Relatório. [backend; depende de RF-12] | Seção 2 · Chat e orquestrador; UC-04 | Essencial |
| RF-12 | Mostrar lado a lado o progresso de cada subagente e permitir trocar de tela entre eles. Entrada: progresso de RF-11. Saída: cartões com papel, tarefa, modelo, etapa, tokens. [frontend; depende de RF-11] | Seção 2 · Chat e orquestrador; UC-04 | Importante |
| RF-13 | Manter a lista de modelos disponíveis e o modelo padrão de cada papel (orquestrador, funcionalidade, teste, adversarial). Entrada: escolhas do Humano. Saída: padrões salvos. [ambos; depende de RF-09] | Seção 2 · Chat e orquestrador; UC-09 | Importante |
| RF-14 | Registrar cada pasta e arquivo lidos ou usados por agente, separando as leituras pela Obsidian CLI. Entrada: eventos de ferramenta das execuções. Saída: Leitura (caminho, origem, agente, hora). [backend; depende de RF-15] | Seção 2 · Contexto; UC-11 | Essencial |
| RF-15 | Mostrar, no topo central, três abas: pastas lidas ou usadas, pastas do Obsidian usadas e pastas em contexto. Entrada: RF-14, RF-16. Saída: listas por aba. [frontend; depende de RF-14, RF-16] | Seção 2 · Contexto; UC-11 | Essencial |
| RF-16 | Permitir adicionar e remover pastas que o orquestrador e os subagentes podem acessar. Entrada: caminho da pasta. Saída: lista de contexto atualizada. [ambos; depende de RF-15] | Seção 2 · Contexto; UC-11 | Importante |
| RF-17 | Somar os tokens de conversa de cada chat e compará-los com o limite do chat. Entrada: uso de tokens dos eventos. Saída: tokens usados, % do limite. [backend; depende de RF-19] | Seção 2 · Consumo; UC-08 | Essencial |
| RF-18 | Obter o consumo semanal e o da janela de uso com reinício periódico, com a hora do próximo reinício. Entrada: dados de uso do Claude CLI [a confirmar: fonte, S2]. Saída: % semanal, % da janela, hora do reinício. [backend; depende de RF-19] | Seção 2 · Consumo; necessidade do negócio | Essencial |
| RF-19 | Mostrar o tempo todo, no canto superior esquerdo, o consumo semanal e o da janela e, sob o prompt, a barra de progresso do chat. Entrada: RF-17, RF-18. Saída: indicadores. [frontend; depende de RF-17, RF-18] | Seção 2 · Consumo; necessidade do negócio | Essencial |
| RF-20 | Ao atingir o limite do chat, pedir ao orquestrador o registro do "Onde parei" e abrir um chat novo de continuação ligado ao anterior. Entrada: RF-17. Saída: diário gravado, chat novo. [backend; depende de RF-07, RF-28] | Seção 2 · Consumo; UC-08 | Essencial |
| RF-21 | Registrar cada comando e ferramenta executados por agente, com início, fim, resultado e saída. Entrada: eventos das execuções. Saída: Log. [backend; depende de RF-22] | Seção 2 · Logs e histórico; necessidade do negócio | Essencial |
| RF-22 | Mostrar no canto inferior esquerdo os logs em tempo real, um por linha minimizada, com a saída completa ao expandir. Entrada: RF-21. Saída: lista de logs. [frontend; depende de RF-21] | Seção 2 · Logs e histórico; necessidade do negócio | Importante |
| RF-23 | Guardar e listar, no canto inferior direito, os projetos e os chats de cada um, com a cadeia de passagens de turno. Entrada: chats e projetos. Saída: lista filtrável, reabertura. [ambos; depende de RF-07] | Seção 2 · Logs e histórico; UC-12 | Importante |
| RF-24 | Despachar um subagente de teste para cada funcionalidade entregue, com os critérios e a prova, e gravar ✔/✘ por critério. Entrada: funcionalidade entregue, critérios. Saída: resultado por critério, bugs. [backend; depende de RF-26] | Seção 2 · Teste e entrega; UC-05 | Essencial |
| RF-25 | Despachar o adversarial, sem contexto, para cumprir tarefas na aplicação pelo Claude in Chrome e relatar bugs e sugestões de UI/UX. Entrada: objetivos de tarefa, endereço, acesso de teste. Saída: Achados tipados. [backend; depende de RF-26] | Seção 2 · Teste e entrega; UC-06 | Essencial |
| RF-26 | Listar bugs e sugestões com evidência e permitir ao Humano decidir corrigir, registrar como limite ou deixar opcional. Entrada: Achados. Saída: decisões por achado. [frontend; depende de RF-24, RF-25] | Seção 2 · Teste e entrega; UC-07 | Essencial |
| RF-27 | Criar uma worktree e uma branch por subagente de funcionalidade e, ao fim, fazer push e abrir o PR no GitHub. Entrada: repositório, tarefa. Saída: caminho da worktree, branch, link do PR. [backend; depende de RF-03] | Seção 2 · Teste e entrega; UC-10 | Essencial |
| RF-28 | Permitir escrita no cofre só ao processo do orquestrador e registrar cada escrita (nota, motivo, hora). Entrada: pedido de escrita. Saída: nota gravada, log. [backend; depende de RF-02] | Seção 2 · Memória e governança; UC-04 | Essencial |
| RF-29 | Gerar, a partir das regras do harness, o CLAUDE.md do orquestrador e o briefing de cada papel, com as ferramentas permitidas a cada um. Entrada: regras ativas, papel. Saída: instruções e lista de ferramentas por papel. [backend; depende de RF-10] | Seção 2 · Memória e governança; necessidade do negócio (governança no harness, não no cofre) | Essencial |
| RF-30 | Oferecer um campo de texto que cresce com o conteúdo, botão de enviar e seletor de modelo do orquestrador. Entrada: texto, modelo. Saída: prompt enviado a RF-05. [frontend; depende de RF-05] | Seção 2 · Chat e orquestrador (listado na fonte entre RF-13 e RF-14); UC-02 | Essencial |
| RF-31 | Permitir ver, editar, salvar como versão nova e restaurar o prompt de papel de cada fluxo (orquestrador, funcionalidade, teste, adversarial, passagem de turno). Entrada: fluxo, texto. Saída: versão nova, contagem de palavras, histórico de versões. [ambos; depende de RF-32] | Seção 2 · Configurações; UC-13 | Essencial |
| RF-32 | Colocar o prompt de papel vigente do fluxo antes de cada instrução enviada à LLM e gravar qual versão foi usada. Entrada: fluxo, versão vigente. Saída: chamada com o prompt no início; Execução.prompt_versao. [backend; depende de RF-31] | Seção 2 · Configurações; necessidade do negócio | Essencial |
| RF-33 | Permitir ligar ao projeto um cofre de memória e quantos cofres de consulta o Humano quiser, e ativar ou desativar cada um. Entrada: nome do cofre, função (memoria, consulta). Saída: lista de cofres do projeto com status. [ambos; depende de RF-02] | Seção 2 · Configurações; UC-14 | Essencial |
| RF-34 | Repetir a busca e a leitura da Obsidian CLI em cada cofre ativo do projeto e juntar os resultados com o cofre de origem. Entrada: termo, cofres ativos. Saída: notas com cofre de origem. [backend; depende de RF-15, RF-33] | Seção 2 · Configurações; UC-14 | Essencial |

## Não funcionais (RNF)

| ID | Requisito | Como medir | Origem |
|---|---|---|---|
| RNF-01 | Desempenho (ambos): cada trecho de resposta de um agente aparece na tela logo que chega da CLI; até 200 ms entre o evento sair do processo e o texto aparecer, em 95% dos eventos [a confirmar, S12]. | Windows 11, 6 agentes ao mesmo tempo; marca de tempo no backend e no frontend comparada num teste automatizado | Seção 3; UC-02, TEL-01; essencial |
| RNF-02 | Desempenho (frontend): a interface responde ao clique e à digitação com vários agentes transmitindo; nenhuma tarefa da thread principal acima de 50 ms; entrada responde em até 100 ms. | 6 agentes, 1.000 linhas de log por minuto; perfil de desempenho do WebView (DevTools) em teste de carga com processos simulados | Seção 3; TEL-01; essencial |
| RNF-03 | Desempenho (ambos): o app, sem contar os processos das CLIs, ocupa até 400 MB de RAM após 8 h de uso com 6 agentes [a confirmar, S12]. | Windows 11, 16 GB de RAM; teste de longa duração com coleta pelo Gerenciador de Tarefas | Seção 3; importante |
| RNF-04 | Desempenho (ambos): consumo do chat atualizado em até 2 s após cada resposta; consumo do plano em até 60 s [a confirmar]. | Uso normal; comparar o painel com os dados da CLI em 20 amostras | Seção 3; RF-17 a RF-19; essencial |
| RNF-05 | Segurança (backend): tokens de OAuth ficam no cofre de credenciais do SO, nunca em arquivo; 0 tokens em texto puro no disco, nos logs, no SQLite e no cofre Obsidian. | Após conectar as três integrações e rodar um ciclo completo; busca automatizada pelos tokens nas pastas do app e do projeto | Seção 3; UC-01; essencial |
| RNF-06 | Segurança (backend): cada processo de agente recebe só as ferramentas e pastas do seu papel; 100% das tentativas fora do papel negadas (escrita no cofre por subagente, merge, push --force). | Suíte de tentativas proibidas por papel; teste automatizado de integração | Seção 3; RF-10, RF-29; essencial |
| RNF-07 | Confiabilidade (backend): processo de agente que encerra com erro ou para de emitir eventos é detectado e marcado; queda detectada em até 5 s; silêncio acima de 10 min marcado como parado [a confirmar: a fonte termina com "?"]. | Matar o processo durante a execução; teste automatizado de falha | Seção 3; UC-04; essencial |
| RNF-08 | Confiabilidade (ambos): fechar o app ou reiniciar a máquina não perde chats, planos, achados nem logs; 100% dos registros confirmados antes do fechamento reaparecem; execuções interrompidas aparecem como interrompida. | Encerrar o processo do app durante 3 execuções; teste automatizado com SQLite em modo WAL | Seção 3; UC-12; essencial |
| RNF-09 | Auditoria (ambos): toda ação relevante tem registro (comando de agente, escrita no cofre, aval do Humano, troca de modelo); 100% com quem, o quê, quando e de qual chat. | Um ciclo completo de funcionalidade; inspeção do log contra a lista de ações do ciclo | Seção 3; importante |
| RNF-10 | Manutenibilidade (backend): cada subagente recebe só o briefing do seu papel e busca o resto pela Obsidian CLI; briefing inicial até 3 mil tokens; relatório de volta até 1,5 mil tokens [a confirmar, S12]. | 20 despachos reais; contagem de tokens dos eventos de uso | Seção 3; RF-10, RF-29; importante |
| RNF-11 | Manutenibilidade (backend): cada integração (Claude CLI, Obsidian CLI, GitHub) fica atrás de uma interface própria no núcleo Rust; adicionar uma integração não altera arquivos das regras nem das telas existentes. | Revisão do diff ao adicionar uma integração de teste; inspeção de código | Seção 3; importante |
| RNF-12 | Acessibilidade (frontend): ações principais pelo teclado e contraste legível nos temas claro e escuro; WCAG 2.1 AA; enviar, novo chat, trocar de aba e aprovar plano com atalho. | Temas claro e escuro; auditoria com axe e roteiro manual só com teclado | Seção 3; todas as telas; desejável |
| RNF-13 | Desempenho (backend): o prompt de papel anexado a cada chamada pesa até 150 tokens por chamada [a confirmar, S14]. | Os 5 prompts de papel vigentes; contagem de tokens ao salvar, mostrada na TEL-06 | Seção 3; RF-32; essencial |
| RNF-14 | Desempenho (backend): busca em vários cofres em até 3 s para 3 cofres de até 2 mil notas cada [a confirmar]. | Obsidian aberto, Windows 11; teste cronometrado com 20 termos | Seção 3; RF-34; importante |

## Regras de negócio (RN)

Todas vêm do método da Orquestra e passam a viver no núcleo do harness. Em todas, a origem é decisão do negócio e quem altera ou valida é o Humano, dono do harness. O texto traz enunciado, violação e exceção; o aceite de cada uma está em `08-criterios-de-aceite.md`.

| ID | Regra | Entidade | Origem |
|---|---|---|---|
| RN-01 | Só o orquestrador grava, altera ou move notas no cofre do projeto, em qualquer chat. Violação: a escrita de subagente é recusada e vira log de violação (ERR-13). Exceção: o Humano escreve direto no Obsidian, fora do harness. | ENT-07, ENT-17 | Seção 1 · Memória; permissão |
| RN-02 | Todo agente lê e busca notas do cofre pela Obsidian CLI, nunca lendo os .md direto. Violação: bloqueia a leitura direta e registra aviso (ERR-18). Exceção: com a integração Obsidian desconectada e o Humano autorizando, a leitura direta é permitida e marcada "sem CLI". | ENT-11, ENT-13 | Seção 1 · Memória; restrição |
| RN-03 | Relatório de subagente e decisão aprovada são gravados no cofre antes de o orquestrador despachar a próxima tarefa. Violação: a próxima delegação fica bloqueada até o registro (ERR-15). Sem exceção. | ENT-09, ENT-18 | Seção 1 · Memória; prazo |
| RN-04 | Tokens de OAuth, chaves e senhas nunca são gravados no cofre, nos logs nem no histórico. Violação: o trecho é mascarado (••••) antes de gravar. Sem exceção. | ENT-13, ENT-12, ENT-04 | Seção 1 · Memória; restrição |
| RN-05 | O orquestrador só despacha subagentes depois que o Humano aprova o plano de delegação. Violação: bloqueia o despacho (ERR-09). Exceção: subagente só de leitura (pesquisa) [a confirmar, S10]. | ENT-05 | Seção 1 · Decisão e delegação; permissão |
| RN-06 | Um item do plano marcado "para o aval" só vira decisão registrada quando o Humano o aprova. Violação: bloqueia a criação da nota de decisão (ERR-10). Sem exceção. | ENT-18 | Seção 1 · Decisão e delegação; restrição |
| RN-07 | Toda execução de agente roda com um modelo definido: o escolhido para a tarefa ou, sem escolha, o padrão do papel. Violação: sem modelo e sem padrão, o despacho é bloqueado e pede escolha (ERR-11). Sem exceção. | ENT-06, ENT-15 | Seção 1 · Decisão e delegação; condição |
| RN-08 | Ação que depende de Claude CLI, Obsidian CLI ou GitHub só executa com a integração conectada. Violação: bloqueia e aponta qual integração falta (ERR-05, ERR-06, ERR-07). Exceção: a de RN-02, autorizada. | ENT-13 | Seção 1 · Decisão e delegação; condição |
| RN-09 | A execução que testa uma funcionalidade é sempre diferente da que a implementou. Violação: bloqueia a atribuição (ERR-19). Sem exceção. | ENT-07, ENT-06 | Seção 1 · Papéis e separação; restrição |
| RN-10 | O agente adversarial recebe só o objetivo da tarefa, o endereço da aplicação e o acesso de teste. Violação: o briefing com conversa, plano, código ou notas é recusado (ERR-23). Sem exceção. | ENT-19, ENT-07 | Seção 1 · Papéis e separação; restrição |
| RN-11 | O adversarial só roda quando todas as funcionalidades da rodada estão concluídas nos testes. Violação: bloqueia o despacho adversarial (ERR-24). Exceção: rodada adversarial avulsa pedida pelo Humano [a confirmar, S11]. | ENT-20, ENT-21 | Seção 1 · Papéis e separação; condição |
| RN-12 | Dúvida de subagente sobe no relatório; só o orquestrador fala com o Humano. Violação: a pergunta direta é convertida em dúvida do relatório. Sem exceção. | ENT-09 | Seção 1 · Papéis e separação; restrição |
| RN-13 | No máximo 5 subagentes que escrevem código rodam ao mesmo tempo. Violação: o excedente entra em fila (ERR-44). Exceção: subagentes só de leitura e de teste não contam. | ENT-22 (teto_escrita, padrão 5 [a confirmar, S8]) | Seção 1 · Paralelismo; limite |
| RN-14 | Tarefas cujo "toca em" se sobrepõe nunca rodam ao mesmo tempo. Violação: a segunda tarefa espera a primeira (ERR-12). Sem exceção. | ENT-06 | Seção 1 · Paralelismo; restrição |
| RN-15 | Um recurso exclusivo (navegador do Claude in Chrome, banco de teste) atende um agente por vez. Violação: a execução espera o recurso (ERR-25). Sem exceção. | ENT-16 | Seção 1 · Paralelismo; restrição |
| RN-16 | Cada subagente de funcionalidade trabalha na própria worktree e branch `tipo/ID-descricao`. Violação: bloqueia o despacho sem worktree (ERR-16). Sem exceção. | ENT-07 | Seção 1 · Paralelismo; restrição |
| RN-17 | O subagente termina no push e no PR aberto; o merge é sempre do Humano. Violação: bloqueia merge, push --force e push na branch principal (ERR-14). Sem exceção. | ENT-23, ENT-07 | Seção 1 · Paralelismo; permissão |
| RN-18 | Um critério só é ✔ com prova objetiva anexada (saída de teste, captura, resposta). Violação: o critério fica ✘ "sem prova" (ERR-20). Exceção: o Humano dispensa a prova; o registro diz "não verificado, presumido". | ENT-24 | Seção 1 · Verificação; restrição |
| RN-19 | Uma tarefa reprovada volta no máximo 2 vezes a um implementador novo; na 3ª reprovação, sobe ao Humano. Violação: a 3ª volta é bloqueada e vira item na caixa de aval (ERR-21). Sem exceção. | ENT-06 | Seção 1 · Verificação; limite |
| RN-20 | Uma funcionalidade só fica concluída com todos os critérios ✔ e nenhum bug aberto. Violação: bloqueia a mudança de status (ERR-22). Exceção: exceção registrada pelo Humano, com escopo fechado. | ENT-21, ENT-10 | Seção 1 · Verificação; condição |
| RN-21 | Achado adversarial em que o fluxo não se completa é bug; em que se completa com dificuldade é sugestão de UI/UX. Violação: achado sem tipo não é aceito no relatório (ERR-27). Sem exceção. | ENT-10 | Seção 1 · Verificação; condição |
| RN-22 | Toda sugestão de UI/UX recebe do Humano uma de três decisões: corrigir, registrar como limite ou deixar como opcional. Violação: a rodada fica aguardando decisão (ERR-28). Sem exceção. | ENT-10 | Seção 1 · Verificação; condição |
| RN-23 | Cada chat do orquestrador tem um limite de tokens de conversa; o padrão vale para todo chat novo. Violação: ao atingir o limite, dispara a passagem de turno (RN-24). Exceção: o Humano pode adiar uma vez por chat; o adiamento vai ao diário. | ENT-03 (limite_tokens, padrão 100 mil [a confirmar, S7]) | Seção 1 · Contexto e consumo; limite |
| RN-24 | Um chat novo de continuação só abre depois que o orquestrador grava no cofre o "Onde parei" com próximo passo. Violação: bloqueia a abertura do chat novo (ERR-29). Sem exceção. | ENT-25, ENT-03 | Seção 1 · Contexto e consumo; condição |
| RN-25 | Toda chamada à LLM (orquestrador, subagente, passagem de turno) leva, antes da instrução, o prompt de papel do fluxo que a fez. Violação: a chamada é bloqueada (ERR-36). Sem exceção. | ENT-08, ENT-07 | Seção 1 · Prompts de papel; condição |
| RN-26 | Um prompt de papel tem no máximo 80 palavras [a confirmar, S14]. Violação: bloqueia o salvamento e mostra quantas palavras passaram (ERR-34). Sem exceção. | ENT-08 | Seção 1 · Prompts de papel; limite |
| RN-27 | O prompt de papel descreve responsabilidades; ferramentas, pastas e permissões vêm só do núcleo. Violação: texto que peça algo proibido ao papel não tem efeito; o núcleo continua negando (ERR-13). Sem exceção. | ENT-15, ENT-08 | Seção 1 · Prompts de papel; restrição |
| RN-28 | Uma execução usa, do começo ao fim, a versão do prompt de papel vigente quando começou; a versão nova só vale para execuções novas. Sem violação nem exceção. | ENT-08, ENT-07 | Seção 1 · Prompts de papel; condição |
| RN-29 | Cada projeto tem exatamente um cofre de memória, o único em que o orquestrador grava; os outros cofres ligados são só de consulta. Violação: escrita num cofre de consulta é bloqueada (ERR-39). Sem exceção. | ENT-02 | Seção 1 · Várias memórias; restrição |
| RN-30 | Toda nota devolvida por uma busca ou leitura pela Obsidian CLI vem com o nome do cofre de onde saiu. Violação: resultado sem origem não é entregue ao agente (ERR-40). Sem exceção. | ENT-11, ENT-02 | Seção 1 · Várias memórias; condição |

## Decisões do humano

| ID | Pergunta | Decisão | Data |
|---|---|---|---|
| D1 | Onde mora a memória do projeto | Nos .md do cofre, lidos pela Obsidian CLI e escritos só pelo orquestrador. O app guarda só o estado das execuções (chats, agentes, logs, consumo) num SQLite local | 2026-11-18 |
| D2 | Papel do adversarial | Falha de fluxo é bug e bloqueia a conclusão; problema de UI/UX é sugestão e o Humano decide | 2026-11-18 |
| D3 | Até onde o subagente vai no GitHub | Worktree e branch próprias, push e PR aberto; o merge é do Humano | 2026-11-18 |
| D4 | Quem usa | Uma pessoa, no próprio computador; sem login no app, as permissões são entre papéis | 2026-11-18 |
| D5 | Responsabilidades de cada fluxo | Tela de configurações com prompts curtos de responsabilidade primária, anexados antes de cada instrução à LLM (RN-25 a RN-28, TEL-06) | 2026-11-19 |
| D6 | Mais de uma memória | O projeto pode ligar mais de um cofre do Obsidian como contexto de pesquisa (RN-29, RN-30, UC-14) | 2026-11-19 |

O que sai do cofre e vira núcleo do harness: os princípios e as etapas do Manual da Orquestra, o núcleo comum (N), o paralelismo (G), os papéis, os cartões de briefing e o formato do relatório viram as RN-01 a RN-30, o RF-29 e os prompts de papel da TEL-06. O que fica no cofre: contexto, roteiro, planos, decisões, bugs e diários do projeto.

## Suposições [a confirmar]

| ID | Suposição | Afeta | Como confirmar |
|---|---|---|---|
| S1 | [a confirmar] O humano citou reinício a cada 4 h; os limites de uso do plano Claude funcionam em janelas de 5 h | RF-18, CMP-01 | Conferir no /usage do Claude CLI |
| S2 | [a confirmar] A fonte do consumo semanal e da janela é o próprio Claude CLI; sem saída legível por máquina, o plano B é estimar pelos registros locais de sessão da CLI | RF-18, RNF-04 | Protótipo de leitura antes da tela |
| S3 | [a confirmar] Cada agente é um processo `claude -p` com saída em fluxo JSON, modelo, ferramentas permitidas, pastas extras e instruções de sistema passados por parâmetro | RF-05, RF-10, RF-29, RF-32, RNF-06 | Conferir os parâmetros em `claude --help` da versão instalada |
| S4 | [a confirmar] Alternativa ao S3: o Claude Agent SDK num processo Node ao lado do Rust | Arquitetura do backend | Decisão de arquitetura antes do RF-10 |
| S5 | [a confirmar] Só o GitHub usa OAuth; o Claude CLI usa o login da própria CLI e a Obsidian CLI é local e exige o Obsidian aberto | RF-01 a RF-03, TEL-02 | Teste de conexão das três |
| S6 | [a confirmar] O adversarial usa a integração do Claude CLI com o Chrome (Claude in Chrome); plano B, um servidor MCP de navegador | RF-25 | Protótipo de um agente abrindo a aplicação |
| S7 | [a confirmar] O limite padrão de contexto por chat é 100 mil tokens, herdado do método da Orquestra | RN-23 | Ajustar depois de medir |
| S8 | [a confirmar] O teto de agentes que escrevem é 5, herdado do método | RN-13 | Ajustar depois de medir |
| S9 | [a confirmar] O botão "Novo chat" fica junto da barra de progresso do chat, embaixo, e as integrações no canto superior direito | CMP-03, CMP-07 | Confirmação do layout pelo humano |
| S10 | [a confirmar] Subagente só de leitura (pesquisa) pode rodar sem aval do plano | RN-05 | Decisão do humano |
| S11 | [a confirmar] O Humano pode pedir uma rodada adversarial avulsa, fora do fim da rodada | RN-11 | Decisão do humano |
| S12 | [a confirmar] As métricas dos RNF (200 ms, 400 MB, 3 mil tokens de briefing) são pontos de partida | RNF-01, RNF-03, RNF-10 | Medir no primeiro protótipo |
| S13 | [a confirmar] Os cofres extras são só de consulta; continua havendo um único cofre onde o orquestrador grava | RN-29, CMP-17 | Confirmação do humano |
| S14 | [a confirmar] O limite do prompt de papel é 80 palavras (cerca de 150 tokens) | RN-26, RNF-13 | Medir o efeito no primeiro protótipo |
| S15 | [a confirmar] O botão Configurações fica ao lado das integrações, no canto superior direito | TEL-06 | Confirmação do layout pelo humano |
