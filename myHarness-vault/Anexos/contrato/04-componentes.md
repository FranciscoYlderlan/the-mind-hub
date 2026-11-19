# Componentes lógicos (CMP)

Só para funcionalidade com interface. Descreve o papel do componente, não a aparência. A tela escolhe o visual; o comportamento vem daqui.

Fonte: seção 5 "Contrato das telas". Todas as telas são acessadas só pelo Humano (ATR-01), com permissão total (uso local, pessoa única, D4). Os estados seguem a ordem vazio · carregando · preenchido · erro · sucesso · desabilitado; "não se aplica" é da fonte.

## Telas previstas (TEL)

| ID | Tela | Objetivo | Pré-condições | CMP | UC |
|---|---|---|---|---|---|
| TEL-01 | Área de trabalho (janela principal, sempre aberta) | Conversar com o orquestrador e acompanhar ao vivo agentes, contexto, consumo e logs | App aberto; projeto selecionado (senão, abre o histórico) | CMP-01 a CMP-10 | UC-02, UC-04, UC-05, UC-06, UC-08, UC-10, UC-11, UC-12 |
| TEL-02 | Integrações | Conectar e conferir Claude CLI, Obsidian CLI e GitHub | Nenhuma | CMP-11 | UC-01 |
| TEL-03 | Revisão do plano de delegação | Aprovar, ajustar ou recusar a divisão do trabalho antes do despacho | Plano em `proposto` | CMP-12, CMP-13 | UC-03 |
| TEL-04 | Gestão de modelos | Definir o modelo padrão de cada papel | Claude CLI conectado | CMP-14 | UC-09 |
| TEL-05 | Revisão de achados | Ver bugs e sugestões de UI/UX com evidência e decidir cada um | Rodada de teste ou adversarial com achados | CMP-15 | UC-05, UC-06, UC-07 |
| TEL-06 | Configurações | Ajustar os prompts de papel de cada fluxo e os cofres ligados ao projeto | Nenhuma | CMP-16, CMP-17 | UC-13, UC-14 |

As TEL-02 a TEL-06 abrem sobre a TEL-01 como painéis ou diálogos. Navegação em `06-navegacao.md`.

## CMP-01 Consumo do plano (TEL-01, canto superior esquerdo)

- **Papel:** mostrar o consumo semanal e o da janela de uso com reinício.
- **Entradas:** RF-18 (ENT-14).
- **Saídas:** nada.
- **Eventos:** `passou-o-mouse` (mostra a hora do próximo reinício).
- **Atende:** RF-18, RF-19 (necessidade do negócio, sem UC); UC-02 FE-02 [a confirmar].
- **Valida:** — (só leitura de ENT-14).
- **Regras:** fica visível em todas as telas. Janela de 4 h ou 5 h [a confirmar, S1].

### Estados obrigatórios

| Estado | O que o usuário vê | Ações possíveis |
|---|---|---|
| vazio | sem dados ainda | nenhuma |
| carregando | primeira leitura | nenhuma |
| preenchido | dois percentuais (semanal e janela) | passar o mouse para ver o reinício |
| erro | "consumo indisponível" (ERR-41) | nenhuma [a confirmar: tentar de novo?] |
| sucesso | não se aplica | — |
| desabilitado | Claude CLI desconectado | conectar pela TEL-02 [a confirmar] |

## CMP-02 Painel de contexto (TEL-01, topo, centro)

- **Papel:** mostrar o que os agentes leem e as pastas em contexto.
- **Entradas:** RF-14 (ENT-11), RF-16; resultados de RF-34.
- **Saídas:** pasta adicionada ou removida.
- **Eventos:** `trocou-de-aba` (Lidos e usados, Obsidian usado, Em contexto), `adicionou-pasta`, `removeu-pasta`, `filtrou-por-agente`.
- **Atende:** UC-11 (passos 1 a 3, FA-01, FE-01); UC-02 passo 2; UC-14 (resultados por cofre).
- **Valida:** caminho da pasta (existente e com permissão; violação: ERR-32).
- **Regras:** RN-02 (leitura sem CLI aparece marcada "sem CLI"); RN-30 (a aba "Obsidian usado" agrupa as notas por cofre).

### Estados obrigatórios

| Estado | O que o usuário vê | Ações possíveis |
|---|---|---|
| vazio | "nenhuma leitura neste chat" | trocar de aba, adicionar pasta |
| carregando | indicação de carga | nenhuma [a confirmar] |
| preenchido | lista com caminho, agente, hora | trocar de aba, filtrar, adicionar ou remover pasta |
| erro | pasta inacessível (ERR-32) | corrigir o caminho |
| sucesso | pasta adicionada | continuar |
| desabilitado | sem projeto | escolher projeto no histórico |

## CMP-03 Indicador de integrações (TEL-01, canto superior direito)

- **Papel:** mostrar se Claude CLI, Obsidian CLI e GitHub estão conectados.
- **Entradas:** RF-01 a RF-03 (ENT-13).
- **Saídas:** abrir TEL-02.
- **Eventos:** `clicou` (abre TEL-02).
- **Atende:** UC-01 passo 1, FE-01, FE-03; RF-04; TEL-01 FE-01.
- **Valida:** —
- **Regras:** RN-08. Posição no canto superior direito [a confirmar, S9].

### Estados obrigatórios

| Estado | O que o usuário vê | Ações possíveis |
|---|---|---|
| vazio | não se aplica | — |
| carregando | checando | nenhuma |
| preenchido | um sinal por integração | abrir TEL-02 |
| erro | integração desconectada, em destaque | abrir TEL-02 |
| sucesso | todas conectadas | abrir TEL-02 |
| desabilitado | não se aplica | — |

## CMP-04 Terminal com abas por agente (TEL-01, centro, parte inferior)

- **Papel:** mostrar a conversa com o orquestrador e a saída de cada subagente.
- **Entradas:** RF-05, RF-11 (eventos de ENT-07).
- **Saídas:** aba selecionada.
- **Eventos:** `trocou-de-aba`, `fechou-aba` (de agente concluído), `rolou`.
- **Atende:** UC-02 passo 3; UC-04 passo 2, FE-01; UC-08 (abre o chat novo); RF-06.
- **Valida:** —
- **Regras:** abas agrupadas por papel: orquestrador, funcionalidade, teste, adversarial (RN-09, RN-10). As abas de subagente são só leitura (RN-12).

### Estados obrigatórios

| Estado | O que o usuário vê | Ações possíveis |
|---|---|---|
| vazio | chat novo, só a aba do orquestrador | digitar no CMP-06 |
| carregando | resposta chegando | rolar, trocar de aba |
| preenchido | conversa e saídas | trocar de aba, rolar, fechar aba concluída |
| erro | agente falhou, aba em destaque (ERR-17) | ver o último log |
| sucesso | agente `concluido` | fechar a aba |
| desabilitado | chat encerrado por passagem | ir ao chat de continuação [a confirmar] |

## CMP-05 Progresso dos subagentes (TEL-01)

- **Papel:** mostrar lado a lado o andamento de cada subagente e trocar de tela entre eles.
- **Entradas:** RF-11.
- **Saídas:** subagente selecionado (abre a aba no CMP-04).
- **Eventos:** `clicou-cartao`, `alternou-visao` (grade ou foco).
- **Atende:** UC-04 passo 2, FA-01, FE-01; RF-12; TEL-01 FA-01, FE-02.
- **Valida:** —
- **Regras:** RN-13 (mostra a fila e o contador "x de 5 que escrevem"). Posição na tela não dada pela fonte [a confirmar].

### Estados obrigatórios

| Estado | O que o usuário vê | Ações possíveis |
|---|---|---|
| vazio | "nenhum subagente" | nenhuma |
| carregando | despachando | nenhuma |
| preenchido | cartões com papel, tarefa, modelo, etapa, tokens | clicar num cartão, alternar visão |
| erro | cartão falhou (ERR-17) | clicar para ver a aba |
| sucesso | cartão `concluido` | clicar para ver a aba |
| desabilitado | não se aplica | — |

## CMP-06 Campo de prompt (TEL-01, abaixo do terminal)

- **Papel:** receber o pedido do Humano.
- **Entradas:** modelo do orquestrador.
- **Saídas:** prompt e modelo para RF-05.
- **Eventos:** `digitou`, `enviou` (botão ou atalho, RNF-12), `escolheu-modelo` (abre TEL-04 [a confirmar: o seletor escolhe o modelo ou abre a TEL-04?]).
- **Atende:** UC-02 passo 1, FE-01; RF-30; TEL-01 FE-01; UC-12 FE-01.
- **Valida:** texto do prompt [a confirmar: tamanho máximo, vazio]; modelo (RN-07).
- **Regras:** altura mínima de 1 linha, cresce até 8 linhas e depois rola [a confirmar]; RN-07, RN-08.

### Estados obrigatórios

| Estado | O que o usuário vê | Ações possíveis |
|---|---|---|
| vazio | placeholder | digitar, escolher modelo |
| carregando | enviando | nenhuma |
| preenchido | texto digitado | enviar, escolher modelo |
| erro | falha no envio, texto preservado (ERR-42) | enviar de novo |
| sucesso | campo limpo | digitar |
| desabilitado | Claude CLI desconectado (ERR-05), chat encerrado, cofre não encontrado (ERR-33) ou passagem em andamento | nenhuma; o texto digitado é mantido |

## CMP-07 Barra do chat e novo chat (TEL-01, abaixo do prompt)

- **Papel:** mostrar os tokens usados contra o limite do chat e iniciar chat novo.
- **Entradas:** RF-17 (ENT-03).
- **Saídas:** pedido de chat novo, novo limite.
- **Eventos:** `clicou-novo-chat`, `trocou-limite`.
- **Atende:** RF-07, RF-17, RF-19; UC-02 passo 3, FA-02; UC-08.
- **Valida:** `limite_tokens` de ENT-03 [a confirmar: faixa].
- **Regras:** RN-23; a partir de 80% a barra muda para alerta [a confirmar]. Posição do "Novo chat" [a confirmar, S9].

### Estados obrigatórios

| Estado | O que o usuário vê | Ações possíveis |
|---|---|---|
| vazio | 0% | novo chat, trocar limite |
| carregando | não se aplica | — |
| preenchido | percentual e tokens | novo chat, trocar limite |
| erro | não se aplica | — |
| sucesso | passagem concluída | — |
| desabilitado | não se aplica | — |

## CMP-08 Logs ao vivo (TEL-01, canto inferior esquerdo)

- **Papel:** mostrar cada comando executado, minimizado, com a saída ao expandir.
- **Entradas:** RF-21 (ENT-12).
- **Saídas:** nada.
- **Eventos:** `expandiu-painel`, `recolheu-painel`, `expandiu-log`, `filtrou-por-agente`.
- **Atende:** RF-21, RF-22 (necessidade do negócio, sem UC); UC-04 FE-02 (log de violação); RF-32 (log "prompt de papel vN").
- **Valida:** —
- **Regras:** RN-04 (segredos mascarados).

### Estados obrigatórios

| Estado | O que o usuário vê | Ações possíveis |
|---|---|---|
| vazio | "nenhum comando ainda" | nenhuma |
| carregando | comando rodando, com cronômetro | expandir |
| preenchido | lista de logs minimizados | expandir, filtrar |
| erro | comando com saída diferente de zero | expandir |
| sucesso | comando ok | expandir |
| desabilitado | não se aplica | — |

## CMP-09 Histórico (TEL-01, canto inferior direito)

- **Papel:** listar projetos e chats e reabrir um deles.
- **Entradas:** RF-23 (ENT-01, ENT-03).
- **Saídas:** chat ou projeto selecionado.
- **Eventos:** `buscou`, `selecionou-chat`, `selecionou-projeto`.
- **Atende:** UC-12 (passos 1 a 3, FA-01, FE-01).
- **Valida:** —
- **Regras:** nenhuma.

### Estados obrigatórios

| Estado | O que o usuário vê | Ações possíveis |
|---|---|---|
| vazio | "nenhum chat salvo" | nenhuma |
| carregando | indicação de carga | nenhuma |
| preenchido | lista com cadeia de passagens | buscar, selecionar |
| erro | cofre do projeto não encontrado (ERR-33) | abrir o chat só para leitura |
| sucesso | não se aplica | — |
| desabilitado | não se aplica | — |

## CMP-10 Cartão de plano e caixa de aval (TEL-01, no terminal do orquestrador)

- **Papel:** avisar que há algo esperando o Humano: plano proposto, dúvidas de subagente, 3ª reprovação, achados.
- **Entradas:** RF-08, RF-11, RF-24, RF-25.
- **Saídas:** abrir TEL-03 ou TEL-05.
- **Eventos:** `clicou-revisar`.
- **Atende:** UC-02 FA-01; UC-03 (gatilho); UC-04 FA-02; UC-05 FE-01; UC-06 passo 4; UC-07 (gatilho).
- **Valida:** —
- **Regras:** RN-05, RN-12, RN-19, RN-22. Onde aparecem as dúvidas de subagente para leitura [a confirmar: TEL-03, TEL-05 ou outro].

### Estados obrigatórios

| Estado | O que o usuário vê | Ações possíveis |
|---|---|---|
| vazio | oculto | — |
| carregando | não se aplica | — |
| preenchido | contador de pendências | "Revisar" |
| erro | não se aplica | — |
| sucesso | pendência resolvida | — |
| desabilitado | não se aplica | — |

## CMP-11 Cartão de integração (TEL-02, um por integração)

- **Papel:** mostrar status, conta ou versão e permitir conectar ou desconectar.
- **Entradas:** RF-01 a RF-03 (ENT-13).
- **Saídas:** pedido de conexão ou desconexão.
- **Eventos:** `conectar`, `desconectar`, `testar-conexao`.
- **Atende:** UC-01 (passos 1 a 3, FA-01, FE-01 a FE-03).
- **Valida:** caminho do executável do Claude CLI (opcional, RF-01) [a confirmar].
- **Regras:** RN-04, RN-08.

### Estados obrigatórios

| Estado | O que o usuário vê | Ações possíveis |
|---|---|---|
| vazio | não se aplica | — |
| carregando | login em andamento | nenhuma [a confirmar: cancelar?] |
| preenchido | conta e versão | testar, desconectar |
| erro | motivo da falha (ERR-01, ERR-02, ERR-03, ERR-04) | conectar de novo |
| sucesso | conectado | testar, desconectar |
| desabilitado | "Desconectar" durante execução que depende da integração | testar |

## CMP-12 Lista de tarefas do plano (TEL-03)

- **Papel:** mostrar cada tarefa com papel, "toca em", dependências, paralelo ou série e modelo.
- **Entradas:** RF-08 (ENT-05, ENT-06).
- **Saídas:** modelo por tarefa.
- **Eventos:** `trocou-modelo`, `expandiu-detalhes`.
- **Atende:** UC-03 passos 1 e 2, FE-01.
- **Valida:** `modelo` e `toca_em` de ENT-06.
- **Regras:** RN-07, RN-14.

### Estados obrigatórios

| Estado | O que o usuário vê | Ações possíveis |
|---|---|---|
| vazio | não se aplica | — |
| carregando | indicação de carga | nenhuma |
| preenchido | tarefas do plano | trocar modelo, expandir |
| erro | conflito de "toca em" destacado (ERR-12) | revisar |
| sucesso | não se aplica | — |
| desabilitado | depois do aval | só ver |

## CMP-13 Ações do aval (TEL-03)

- **Papel:** registrar a decisão do Humano.
- **Entradas:** estado do plano (ENT-05).
- **Saídas:** aprovar, pedir alteração (com comentário), recusar.
- **Eventos:** `aprovar`, `pedir-alteracao`, `recusar`.
- **Atende:** UC-03 passo 3, FA-01, FA-02, FE-02.
- **Valida:** comentário do pedido de alteração [a confirmar: obrigatório? tamanho?].
- **Regras:** RN-05, RN-06, RN-08.

### Estados obrigatórios

| Estado | O que o usuário vê | Ações possíveis |
|---|---|---|
| vazio | não se aplica | — |
| carregando | gravando | nenhuma (duplo clique não reenvia [a confirmar]) |
| preenchido | comentário digitado | pedir alteração |
| erro | integração exigida desconectada (ERR-06) | ir à TEL-02 pelo link |
| sucesso | plano aprovado | voltar à TEL-01 |
| desabilitado | "Aprovar" enquanto houver integração exigida desconectada, com o motivo | pedir alteração, recusar |

## CMP-14 Tabela de papéis e modelos (TEL-04)

- **Papel:** mostrar e editar o padrão de orquestrador, funcionalidade, teste e adversarial.
- **Entradas:** RF-13 (ENT-15).
- **Saídas:** padrões novos.
- **Eventos:** `trocou-modelo`, `salvar`, `restaurar-padroes`.
- **Atende:** UC-09 (passos 1 a 3, FA-01, FE-01).
- **Valida:** `modelo_padrao` de ENT-15 (modelo disponível na CLI; violação: ERR-30).
- **Regras:** RN-07.

### Estados obrigatórios

| Estado | O que o usuário vê | Ações possíveis |
|---|---|---|
| vazio | não se aplica | — |
| carregando | lendo modelos da CLI | nenhuma |
| preenchido | papéis com o modelo padrão | trocar, salvar, restaurar |
| erro | modelo indisponível (ERR-30) | escolher outro |
| sucesso | salvo | — |
| desabilitado | "Salvar" sem mudança | trocar, restaurar |

## CMP-15 Lista de achados (TEL-05)

- **Papel:** mostrar cada achado com tipo, passos, esperado, obtido e captura.
- **Entradas:** RF-24, RF-25 (ENT-10).
- **Saídas:** decisão por achado.
- **Eventos:** `abriu-captura`, `decidiu` (corrigir, limite, opcional), `filtrou-por-tipo`, `confirmar`.
- **Atende:** UC-07 (passos 1 a 3, FA-01, FE-01); RF-26.
- **Valida:** `decisao` de ENT-10 (faltando: ERR-28).
- **Regras:** RN-20, RN-21, RN-22.

### Estados obrigatórios

| Estado | O que o usuário vê | Ações possíveis |
|---|---|---|
| vazio | "nenhum achado" | voltar |
| carregando | indicação de carga | nenhuma |
| preenchido | achados com evidência | decidir, filtrar, abrir captura |
| erro | captura indisponível (ERR-43) | continuar decidindo |
| sucesso | todas as decisões dadas | confirmar |
| desabilitado | bug: decisão fixa em "corrigir" | ler |

## CMP-16 Editor de prompts de papel (TEL-06)

- **Papel:** mostrar e editar o prompt curto de cada fluxo, com versão e custo.
- **Entradas:** RF-31 (ENT-08).
- **Saídas:** texto salvo, versão restaurada.
- **Eventos:** `escolheu-fluxo`, `editou`, `salvar`, `ver-versoes`, `restaurar-padrao`.
- **Atende:** UC-13 (passos 1 a 3, FA-01, FA-02, FE-01, FE-02).
- **Valida:** `texto` de ENT-08 (vazio: ERR-35; acima de 80 palavras: ERR-34).
- **Regras:** RN-26, RN-27, RN-28; o contador fica vermelho acima de 80 palavras.

### Estados obrigatórios

| Estado | O que o usuário vê | Ações possíveis |
|---|---|---|
| vazio | não se aplica: todo fluxo nasce com o padrão | — |
| carregando | indicação de carga | nenhuma |
| preenchido | texto, versão, palavras e tokens | editar, salvar, ver versões, restaurar |
| erro | acima do limite (ERR-34) ou vazio (ERR-35) | corrigir |
| sucesso | versão nova salva | — |
| desabilitado | "Salvar" sem mudança | editar, ver versões, restaurar |

## CMP-17 Cofres do projeto (TEL-06)

- **Papel:** ligar, desligar, ativar e definir a função de cada cofre.
- **Entradas:** RF-33 (ENT-02); lista de cofres da Obsidian CLI.
- **Saídas:** cofre ligado, função, ativo.
- **Eventos:** `ligar-cofre`, `trocou-funcao` (memoria, consulta), `ativou`, `desativou`, `testar-busca`.
- **Atende:** UC-14 (passos 1 a 3, FA-01, FA-02, FE-01, FE-02); RF-34.
- **Valida:** `funcao` e `nome` de ENT-02 (ERR-37, ERR-38).
- **Regras:** RN-29 (um só memoria, marcado com destaque), RN-30. "Desligar" não tem fluxo na fonte [a confirmar].

### Estados obrigatórios

| Estado | O que o usuário vê | Ações possíveis |
|---|---|---|
| vazio | "nenhum cofre ligado" | ligar cofre |
| carregando | testando busca | nenhuma |
| preenchido | lista com função e status | ligar, trocar função, ativar, desativar, testar |
| erro | cofre não responde (ERR-37) | testar de novo |
| sucesso | cofre ligado | — |
| desabilitado | Obsidian desconectado (ERR-07) | conectar pela TEL-02 [a confirmar] |
