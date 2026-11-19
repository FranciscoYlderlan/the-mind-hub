# Estados e navegação (NAV)

Só para funcionalidade com interface. Cada transição diz de onde, com que evento, sob que condição e para onde. Os estados são lógicos; o mapa para telas vem depois, na última coluna.

App desktop de um só usuário (D4): não há URL nem login. A coluna Tela traz a tela prevista na fonte (TEL-xx, seção 5), ainda não implementada.

| ID | Origem | Evento | Condição | Destino | Tela (preencher depois) |
|---|---|---|---|---|---|
| NAV-01 | app-fechado | abriu o app | há projeto selecionado | area-de-trabalho | TEL-01 (prevista) |
| NAV-02 | app-fechado | abriu o app | nenhum projeto selecionado | historico | TEL-01, CMP-09 (prevista) |
| NAV-03 | area-de-trabalho | clicou no indicador de integrações (CMP-03) | — | integracoes | TEL-02 (prevista) |
| NAV-04 | integracoes | fechou o painel | — | area-de-trabalho, com o CMP-03 atualizado | TEL-01 (prevista) |
| NAV-05 | area-de-trabalho | clicou em "Revisar" no CMP-10 | há plano em `proposto` | revisao-do-plano | TEL-03 (prevista) |
| NAV-06 | revisao-do-plano | clicou em "Aprovar" (UC-03 passo 3) | integrações exigidas conectadas (RN-08) | area-de-trabalho, com o despacho começando | TEL-01 (prevista) |
| NAV-07 | revisao-do-plano | clicou em "Pedir alteração" com comentário (UC-03 FA-01) | — | revisao-do-plano, com a versão nova do plano | TEL-03 (prevista) |
| NAV-08 | revisao-do-plano | clicou em "Recusar" (UC-03 FA-02) | — | area-de-trabalho | TEL-01 (prevista) |
| NAV-09 | revisao-do-plano | clicou no link da mensagem de ERR-06 | integração exigida desconectada | integracoes | TEL-02 (prevista) |
| NAV-10 | area-de-trabalho | usou o seletor de modelo do CMP-06 | Claude CLI conectado | gestao-de-modelos [a confirmar: o seletor escolhe o modelo do orquestrador ou abre a TEL-04?] | TEL-04 (prevista) |
| NAV-11 | gestao-de-modelos | salvou ou fechou | — | area-de-trabalho | TEL-01 (prevista) |
| NAV-12 | area-de-trabalho | clicou em "Revisar" no CMP-10 | há achados ou 3ª reprovação pendentes | revisao-de-achados | TEL-05 (prevista) |
| NAV-13 | revisao-de-achados | clicou em "Confirmar" (UC-07 passo 3) | toda sugestão tem decisão (RN-22) | area-de-trabalho | TEL-01 (prevista) |
| NAV-14 | revisao-de-achados | fechou | — | area-de-trabalho, com a rodada `aguardando decisão` se faltar decisão [a confirmar] | TEL-01 (prevista) |
| NAV-15 | area-de-trabalho | clicou no botão Configurações | — | configuracoes | TEL-06 (prevista; posição do botão [a confirmar, S15]) |
| NAV-16 | configuracoes | fechou | — | area-de-trabalho | TEL-01 (prevista) |
| NAV-17 | area-de-trabalho (chat ativo) | o chat atingiu o limite ou o Humano pediu a passagem (UC-08) | "Onde parei" com próximo passo gravado (RN-24) | area-de-trabalho, no chat de continuação | TEL-01 (prevista) |
| NAV-18 | area-de-trabalho | clicou em "Novo chat" (CMP-07) | — | area-de-trabalho, num chat vazio com o limite padrão | TEL-01 (prevista) |
| NAV-19 | historico | selecionou um chat (UC-12 passo 2) | o cofre do projeto existe | area-de-trabalho, com o chat reaberto | TEL-01 (prevista) |
| NAV-20 | historico | selecionou um chat encerrado por passagem | — | area-de-trabalho, com a oferta de ir ao chat de continuação | TEL-01 (prevista) |
| NAV-21 | historico | selecionou um projeto (UC-12 FA-01) | — | area-de-trabalho, no último chat do projeto | TEL-01 (prevista) |
| NAV-22 | historico | selecionou um chat | cofre do projeto não encontrado (ERR-33) | area-de-trabalho em só leitura | TEL-01 (prevista) |
| NAV-23 | area-de-trabalho | clicou num cartão do CMP-05 (TEL-01 FA-01) | — | area-de-trabalho, com a aba daquele subagente ativa no CMP-04 | TEL-01 (prevista) |

## Estado inicial

Sem URL: o "estado inicial" é o que cada estado mostra ao ser aberto, sem clique prévio.

| Estado | Mostra ao abrir |
|---|---|
| area-de-trabalho | CMP-01 (consumo), CMP-02 (contexto), CMP-03 (integrações), CMP-04 só com a aba do orquestrador, CMP-06 no estado `vazio`, CMP-07, CMP-08 e CMP-09; CMP-10 oculto sem pendência |
| historico | CMP-09 com projetos e chats e a cadeia de passagens, ou "nenhum chat salvo" |
| integracoes | um CMP-11 por integração, já com o status checado |
| revisao-do-plano | CMP-12 com as tarefas do plano em `proposto` e CMP-13; "Aprovar" desabilitado se faltar integração |
| gestao-de-modelos | CMP-14 com os modelos lidos da CLI e o padrão de cada papel; "Salvar" desabilitado |
| revisao-de-achados | CMP-15 com os achados da rodada; bugs já em "corrigir" |
| configuracoes | CMP-16 com o fluxo [a confirmar: qual fluxo vem primeiro] e CMP-17 com os cofres do projeto |
