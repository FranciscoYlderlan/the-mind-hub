# Gera trocas.json (lista de {arquivo, atual, novo, motivo}).
import json, os
AV = "[a confirmar: suposição de 2026-11-19, aguarda aval]"
T = []
def t(arquivo, atual, novo, motivo):
    T.append({"arquivo": arquivo, "atual": atual, "novo": novo, "motivo": motivo})

# ---------- 05-erros.md ----------
t("05-erros.md", "# Catálogo de erros (ERR)", "# Catálogo de erros e avisos (ERR)", "Decisão 1: o catálogo passa a ter erros e avisos")
t("05-erros.md",
  "Um erro por condição. O código do ERR é o código de erro que o servidor devolve; o frontend mostra a mensagem daqui.",
  "Um item por condição. O catálogo separa dois tipos: **erro** (dado inválido: nada é salvo) e **aviso** (limite de boa prática: o sistema sinaliza e recomenda, e o Humano decide; tratamento `avisar`). O código do ERR é o código que o servidor devolve; o frontend mostra a mensagem daqui.",
  "Decisão 1: introdução separa erro de aviso")
t("05-erros.md",
  "Mensagem entre aspas é texto da fonte;",
  "Mensagem entre aspas é texto da fonte ou aprovado pelo Humano (`mudancas.md`);",
  "Decisões 2 a 5: as mensagens novas vêm do aval do Humano, não da fonte")
t("05-erros.md",
  "| ERR-45 | `PROJETO_NOME_INVALIDO` | nome do projeto vazio, com mais de 80 caracteres ou igual ao de outro projeto (ENT-01) | voltar | [a confirmar] | projeto não salvo |",
  "| ERR-45 | `PROJETO_NOME_INVALIDO` | nome do projeto vazio, com mais de 80 caracteres ou igual ao de outro projeto (ENT-01) | voltar | vazio: \"Dê um nome ao projeto.\"; longo: \"O nome passa de 80 caracteres.\"; repetido: \"Já existe um projeto com esse nome.\" | projeto não salvo |",
  "Decisão 2: ERR-45 é erro, com uma mensagem por violação")
t("05-erros.md",
  "| ERR-46 | `REPOSITORIO_INVALIDO` | repositório do projeto que não é caminho absoluto de uma pasta com `.git` (ENT-01) | voltar | [a confirmar] | projeto não salvo |",
  "| ERR-46 | `REPOSITORIO_INVALIDO` | repositório do projeto que não é caminho absoluto de uma pasta com `.git` (ENT-01) | voltar | \"Escolha a pasta de um repositório git (com `.git`).\" | projeto não salvo |",
  "Decisão 2: ERR-46 é erro, com mensagem")
t("05-erros.md",
  "| ERR-47 | `LIMITE_DE_CONTEXTO_FORA_DA_FAIXA` | limite de contexto do projeto ou do chat fora de 10 mil a 1 milhão de tokens (ENT-01, ENT-03; CMP-07) | voltar | [a confirmar] | limite anterior mantido |",
  "| ERR-47 | `LIMITE_DE_CONTEXTO_FORA_DA_FAIXA` | limite de contexto do projeto ou do chat fora da faixa recomendada de 10 mil a 1 milhão de tokens (ENT-01, ENT-03; CMP-07) | avisar | \"Fora da faixa recomendada: 10 mil a 1 milhão de tokens.\" | valor novo salvo |",
  "Decisão 3: ERR-47 vira aviso; o valor é aceito")
t("05-erros.md",
  "| ERR-48 | `ADIAMENTO_JA_USADO` | segundo pedido de adiamento da passagem de turno no mesmo chat (RN-23; ENT-03) | bloquear | [a confirmar] | a passagem de turno segue |",
  "| ERR-48 | `LIMITE_DO_CHAT_ATINGIDO` | os tokens do chat atingem o `limite_tokens` (RN-23; ENT-03; UC-02 FA-02; UC-08 passo 1; CMP-07) | avisar | \"Este chat passou do limite de <limite> tokens. Recomendado: passar o turno e abrir um chat novo.\" | chat segue `ativo` |",
  "Decisão 4: ERR-48 reaproveitado como aviso de limite do chat; sai o adiamento")
t("05-erros.md",
  "| ERR-49 | `TAREFA_INCOMPLETA` | tarefa do plano com `faz` vazio ou acima de 500 caracteres, ou com `pronto_quando` ou `prova` vazios (ENT-06) (agente) | bloquear | [a confirmar] | [a confirmar] |",
  "| ERR-49 | `TAREFA_INCOMPLETA` | tarefa do plano com `faz` vazio ou acima de 500 caracteres, ou com `pronto_quando` ou `prova` vazios (ENT-05, ENT-06; UC-03 FA-03, FA-04) (agente) | voltar [a confirmar: a decisão não dá o tratamento] | \"Tarefa incompleta: preencha `faz` (até 500 caracteres), `pronto_quando` e `prova`.\" | plano devolvido ao orquestrador (devolução <n> de 2); na 3ª, chega ao Humano com as tarefas marcadas |",
  "Decisão 5: ERR-49 com teto de 2 devoluções ao orquestrador")
t("05-erros.md",
  "- **aguardar:** a ação fica em espera e segue sozinha quando a condição some (vaga no teto, recurso livre, registro feito, integração conectada).",
  "- **aguardar:** a ação fica em espera e segue sozinha quando a condição some (vaga no teto, recurso livre, registro feito, integração conectada).\n- **avisar:** aviso, não erro: um limite de boa prática foi passado; o sistema sinaliza e recomenda, o valor é salvo ou a ação segue, e o Humano decide (limite fora da faixa recomendada, chat acima do limite).",
  "Decisão 1: novo tratamento avisar")

# ---------- 00-requisitos.md ----------
t("00-requisitos.md",
  "| RF-20 | Ao atingir o limite do chat, pedir ao orquestrador o registro do \"Onde parei\" e abrir um chat novo de continuação ligado ao anterior. Entrada: RF-17. Saída: diário gravado, chat novo.",
  "| RF-20 | Ao atingir o limite do chat, avisar o Humano e recomendar a passagem de turno e um chat novo (RN-23); com o aceite do Humano, pedir ao orquestrador o registro do \"Onde parei\" e abrir um chat novo de continuação ligado ao anterior. Entrada: RF-17, resposta do Humano ao aviso. Saída: aviso, diário gravado, chat novo.",
  "Decisão 4: a passagem só começa com o aceite do Humano")
t("00-requisitos.md",
  "| RN-23 | Cada chat do orquestrador tem um limite de tokens de conversa; o padrão vale para todo chat novo. Violação: ao atingir o limite, dispara a passagem de turno (RN-24). Exceção: o Humano pode adiar uma vez por chat; o adiamento vai ao diário, e um segundo adiamento é recusado (ERR-48). | ENT-03 (limite_tokens, padrão 100 mil [a confirmar, S7]) |",
  "| RN-23 | Cada chat do orquestrador tem um limite de tokens de conversa; o padrão vale para todo chat novo. Violação: ao atingir o limite, o sistema avisa e recomenda a passagem de turno (RN-24) e um chat novo (ERR-48); a passagem só começa quando o Humano aceita a recomendação. Exceção: o Humano pode continuar no mesmo chat quantas vezes quiser; cada continuação vai ao diário. | ENT-03 (limite_tokens, padrão 100 mil [a confirmar, S7]; continuacoes), ENT-25 |",
  "Decisão 4: limite do chat vira aviso, sem adiamento")

# ---------- 01-atores.md ----------
t("01-atores.md",
  "adiar a passagem de turno uma vez por chat;",
  "seguir no chat depois do aviso de limite, quantas vezes quiser (RN-23);",
  "Decisão 4: sai o adiamento único")

# ---------- 02-entidades.md ----------
t("02-entidades.md",
  "| limite_contexto_padrao | inteiro (tokens) | 10 mil a 1 milhão | sim | só algarismos | padrão 100 mil (S7) | fora da faixa: ERR-47 |",
  "| limite_contexto_padrao | inteiro (tokens) | recomendado: 10 mil a 1 milhão | sim | só algarismos | padrão 100 mil (S7) | fora da faixa recomendada: aviso ERR-47, valor salvo |",
  "Decisão 3: fora da faixa é aceito com aviso")
t("02-entidades.md",
  "| limite_tokens | inteiro | 10 mil a 1 milhão | sim | só algarismos | padrão: o do projeto (100 mil, S7) | fora da faixa: ERR-47 |",
  "| limite_tokens | inteiro | recomendado: 10 mil a 1 milhão | sim | só algarismos | padrão: o do projeto (100 mil, S7) | fora da faixa recomendada: aviso ERR-47, valor salvo; atingido: aviso ERR-48 |",
  "Decisões 3 e 4: limite fora da faixa e limite atingido são avisos")
t("02-entidades.md",
  "| adiamento_usado | booleano (RN-23) | — | sim | — | sim, não | segundo adiamento: ERR-48 |",
  "| continuacoes | inteiro (RN-23) | ≥ 0 | sim | — | conta as vezes que o Humano seguiu no chat depois do aviso de limite | — |",
  "Decisão 4: adiamento_usado sai; entra continuacoes")
t("02-entidades.md",
  "- Ao atingir `limite_tokens`, começa a passagem de turno (RN-23), salvo adiamento único (RN-23).",
  "- Ao atingir `limite_tokens`, o sistema avisa e recomenda a passagem de turno e um chat novo (RN-23; ERR-48); a passagem só começa quando o Humano aceita, e cada vez que ele segue no chat `continuacoes` sobe 1.",
  "Decisão 4: invariante no estado novo")
t("02-entidades.md",
  "| aprovado_em | data e hora | — | só se aprovado | ISO 8601 UTC | — | — |",
  "| aprovado_em | data e hora | — | só se aprovado | ISO 8601 UTC | — | — |\n| devolucoes | inteiro | 0 a 2 | sim | — | sobe 1 a cada devolução do plano ao orquestrador por tarefa incompleta | tarefa incompleta: ERR-49 |",
  "Decisão 5: ENT-05 ganha devolucoes")
t("02-entidades.md",
  "- \"Aprovar\" só com as integrações exigidas pelo plano conectadas (RN-08; violação: ERR-06).",
  "- \"Aprovar\" só com as integrações exigidas pelo plano conectadas (RN-08; violação: ERR-06).\n- Plano com tarefa incompleta volta ao orquestrador até 2 vezes (`devolucoes`); na 3ª, chega ao Humano com as tarefas incompletas marcadas, e o Humano pede o preenchimento por \"Pedir alteração\" (ERR-49) [a confirmar: \"Aprovar\" fica bloqueado enquanto houver tarefa marcada?].",
  "Decisão 5: invariante do teto de devolução")
t("02-entidades.md",
  "| janela_status | enumeração | — | sim | — | [a confirmar: valores do `rate_limit_event`] | — |\n| semanal_status | enumeração | — | sim | — | [a confirmar: valores do `rate_limit_event`] | — |\n| excedente | [a confirmar: tipo] | — | não | — | [a confirmar] | — |",
  f"| janela_status | enumeração | — | sim | — | valores do campo `status` do `rate_limit_event` (prováveis `allowed`, `allowed_warning`, `rejected`, a conferir no resultado do P2) e `desconhecido` para valor novo {AV} | — |\n| semanal_status | enumeração | — | sim | — | valores do campo `status` do `rate_limit_event` (prováveis `allowed`, `allowed_warning`, `rejected`, a conferir no resultado do P2) e `desconhecido` para valor novo {AV} | — |\n| excedente | texto {AV} | — | não | — | o `overageStatus` do `rate_limit_event`; fora da tela por ora {AV} | — |",
  "Decisão 6: suposição de trabalho para ENT-14, sem aval")
t("02-entidades.md",
  "| adiamento | texto | — | não | — | um por chat (RN-23) | — |",
  "| continuacao | texto | uma linha por continuação | não | — | uma linha a cada vez que o Humano segue no chat depois do aviso de limite (RN-23) [a confirmar: o que a linha traz] | — |",
  "Decisão 4: campo adiamento vira registro de continuação")
t("02-entidades.md",
  "| caminho | caminho | — | sim | caminho de pasta no disco [a confirmar: absoluto?] | pasta existente e com permissão | inacessível: ERR-32 |",
  f"| caminho | caminho | — | sim | caminho absoluto de pasta no disco {AV} | pasta existente e com permissão | inacessível: ERR-32 |",
  "Decisão 6: suposição de trabalho para ENT-26, sem aval")

# ---------- 03-casos-de-uso.md ----------
t("03-casos-de-uso.md",
  "| FA-02 | 3 | O chat chega ao limite | Segue para UC-08 |",
  "| FA-02 | 3 | O chat chega ao limite → sistema avisa e recomenda passar o turno e abrir um chat novo (ERR-48) | Segue para UC-08 |",
  "Decisão 4: no limite, aviso com recomendação")
t("03-casos-de-uso.md",
  "| FA-02 | 3 | Humano recusa → plano vira `recusado` | Termina |",
  "| FA-02 | 3 | Humano recusa → plano vira `recusado` | Termina |\n| FA-03 | 1 | Plano com tarefa incompleta e `devolucoes` abaixo de 2 → núcleo devolve o plano ao orquestrador (ERR-49) e soma 1 em `devolucoes`; o Humano não o vê | Volta ao passo 1 com o plano completado |\n| FA-04 | 1 | Plano com tarefa incompleta pela 3ª vez (`devolucoes` = 2) → o plano chega ao Humano com as tarefas incompletas marcadas (ERR-49); o Humano pede o preenchimento por \"Pedir alteração\" [a confirmar: \"Aprovar\" fica bloqueado enquanto houver tarefa marcada?] | Segue o FA-01 |",
  "Decisão 5: FA do teto de devolução")
t("03-casos-de-uso.md",
  "1. Sistema avisa o orquestrador do limite.\n2. Orquestrador registra no cofre o \"Onde parei\": próximo passo, threads abertas, dúvidas.\n3. Sistema abre um chat novo ligado ao anterior.\n4. O chat novo começa lendo o \"Onde parei\".",
  "1. Chat atinge o limite → sistema avisa o Humano e recomenda passar o turno e abrir um chat novo (ERR-48).\n2. Humano aceita a recomendação, ou pede a passagem → sistema avisa o orquestrador.\n3. Orquestrador registra no cofre o \"Onde parei\": próximo passo, threads abertas, dúvidas.\n4. Sistema abre um chat novo ligado ao anterior.\n5. O chat novo começa lendo o \"Onde parei\".",
  "Decisão 4: a passagem só começa com o aceite do Humano")
t("03-casos-de-uso.md",
  "| FA-01 | 1 | Humano adia a passagem (uma vez por chat, RN-23) → sistema registra o adiamento no diário | O chat segue |",
  "| FA-01 | 2 | Humano segue no chat em vez de passar o turno (quantas vezes quiser, RN-23) → sistema soma 1 em `continuacoes` e registra a continuação no diário | O chat segue `ativo` [a confirmar: o aviso volta a cada resposta acima do limite?] |",
  "Decisão 4: continuação sem teto no lugar do adiamento")
t("03-casos-de-uso.md",
  "| FE-01 | 2 | ERR-29 | O chat novo não abre; o orquestrador refaz o passo 2 |\n| FE-02 | 2 | ERR-07 | A passagem espera a conexão |",
  "| FE-01 | 3 | ERR-29 | O chat novo não abre; o orquestrador refaz o passo 3 |\n| FE-02 | 3 | ERR-07 | A passagem espera a conexão |",
  "Decisão 4: renumeração dos passos do UC-08")

# ---------- 04-componentes.md ----------
t("04-componentes.md",
  "- **Saídas:** pedido de chat novo, novo limite.\n- **Eventos:** `clicou-novo-chat`, `trocou-limite`.\n- **Atende:** RF-07, RF-17, RF-19; UC-02 passo 3, FA-02; UC-08.\n- **Valida:** `limite_tokens` de ENT-03 (10 mil a 1 milhão; violação: ERR-47).\n- **Regras:** RN-23; a partir de 80% a barra muda para alerta [a confirmar].",
  "- **Saídas:** pedido de chat novo, novo limite, aceite da passagem de turno ou continuação no chat.\n- **Eventos:** `clicou-novo-chat`, `trocou-limite`, `aceitou-passagem`, `continuou-no-chat`.\n- **Atende:** RF-07, RF-17, RF-19, RF-20; UC-02 passo 3, FA-02; UC-08 passos 1 e 2, FA-01.\n- **Valida:** `limite_tokens` de ENT-03 (fora de 10 mil a 1 milhão: aviso ERR-47, valor salvo).\n- **Regras:** RN-23: no limite, mostra o aviso ERR-48 com as ações de passar o turno e de continuar no chat [a confirmar: rótulos]; a passagem só começa quando o Humano aceita. A partir de 80% a barra muda para alerta [a confirmar].",
  "Decisões 3 e 4: CMP-07 no estado novo")
t("04-componentes.md",
  "| preenchido | percentual e tokens | novo chat, trocar limite |",
  "| preenchido | percentual e tokens; no limite, o aviso ERR-48; com limite fora da faixa, o aviso ERR-47 | novo chat, trocar limite; no aviso de limite, passar o turno ou continuar no chat |",
  "Decisões 3 e 4: avisos visíveis no CMP-07")
t("04-componentes.md",
  "- **Atende:** UC-03 passos 1 e 2, FE-01.\n- **Valida:** `modelo` e `toca_em` de ENT-06.",
  "- **Atende:** UC-03 passos 1 e 2, FA-04, FE-01.\n- **Valida:** `modelo` e `toca_em` de ENT-06; `faz`, `pronto_quando` e `prova` de ENT-06 (tarefa incompleta marcada: ERR-49).",
  "Decisão 5: tarefas incompletas marcadas na TEL-03")
t("04-componentes.md",
  "| erro | conflito de \"toca em\" destacado (ERR-12) | revisar |",
  "| erro | conflito de \"toca em\" (ERR-12) ou tarefa incompleta (ERR-49) destacados | revisar; pedir o preenchimento por \"Pedir alteração\" |",
  "Decisão 5: estado de erro do CMP-12")
t("04-componentes.md",
  "- **Atende:** UC-03 passo 3, FA-01, FA-02, FE-02.",
  "- **Atende:** UC-03 passo 3, FA-01, FA-02, FA-04, FE-02.",
  "Decisão 5: CMP-13 atende o FA-04")
t("04-componentes.md",
  "- **Regras:** RN-05, RN-06, RN-08.",
  "- **Regras:** RN-05, RN-06, RN-08. Com tarefa incompleta marcada (ERR-49), o Humano pede o preenchimento por \"Pedir alteração\" [a confirmar: \"Aprovar\" fica bloqueado enquanto houver tarefa marcada?].",
  "Decisão 5: ponto em aberto do Aprovar")

# ---------- 06-navegacao.md ----------
t("06-navegacao.md",
  "| NAV-17 | area-de-trabalho (chat ativo) | o chat atingiu o limite ou o Humano pediu a passagem (UC-08) |",
  "| NAV-17 | area-de-trabalho (chat ativo) | o Humano aceitou a recomendação de passagem dada no limite (RN-23) ou pediu a passagem (UC-08) |",
  "Decisão 4: a passagem só começa com o aceite do Humano")

# ---------- 07-rastreabilidade.md ----------
t("07-rastreabilidade.md",
  "| RF-08 | UC-03 | principal, FE-01 | CMP-10, CMP-12 | ENT-05, ENT-06 | ERR-09, ERR-12, ERR-49 | TEL-01, TEL-03 (previstas) | AC-07, AC-14, AC-95 |",
  "| RF-08 | UC-03 | principal, FA-03, FA-04, FE-01 | CMP-10, CMP-12, CMP-13 | ENT-05, ENT-06 | ERR-09, ERR-12, ERR-49 | TEL-01, TEL-03 (previstas) | AC-07, AC-14, AC-95, AC-144, AC-145 |",
  "Decisão 5: rastreabilidade dos FA e AC novos")
t("07-rastreabilidade.md",
  "| RN-23 | UC-02, UC-08 | UC-02 FA-02; UC-08 principal, FA-01 | CMP-07 | ENT-03 | ERR-48 (segundo adiamento); dispara a passagem | TEL-01 (prevista) | AC-08, AC-33, AC-80 |",
  "| RN-23 | UC-02, UC-08 | UC-02 FA-02; UC-08 principal, FA-01 | CMP-07 | ENT-03, ENT-25 | ERR-48 (aviso de limite); a passagem só com o aceite do Humano | TEL-01 (prevista) | AC-08, AC-32, AC-33, AC-80 |",
  "Decisão 4: RN-23 no estado novo")

# ---------- 08-criterios-de-aceite.md ----------
t("08-criterios-de-aceite.md",
  "Todos os textos vêm dos \"Aceite\" da fonte. Ordem: AC-01 a AC-57 por fluxo de UC; AC-58 a AC-87, uma por RN; AC-88 a AC-121, uma por RF; AC-122 a AC-143, por fluxo de tela.",
  "Os textos vêm dos \"Aceite\" da fonte, salvo os escritos por mudança aprovada (`mudancas.md`). Ordem: AC-01 a AC-57 por fluxo de UC; AC-58 a AC-87, uma por RN; AC-88 a AC-121, uma por RF; AC-122 a AC-143, por fluxo de tela; AC-144 e AC-145, por fluxo de UC criado depois (na tabela, junto do UC dele).",
  "Decisões 4 e 5: AC novos e reescritos fora da fonte")
t("08-criterios-de-aceite.md",
  "| AC-08 | UC-02 | FA-02 | o chat no limite | a resposta termina | começa a passagem de turno |",
  "| AC-08 | UC-02 | FA-02 | o chat no limite | a resposta termina | aparece o aviso com a recomendação de passar o turno e abrir um chat novo (ERR-48), e o chat segue ativo |",
  "Decisão 4: no limite, aviso, não passagem automática")
t("08-criterios-de-aceite.md",
  "| AC-15 | UC-03 | FE-02 | o GitHub desconectado | o Humano aprova | o app pede a conexão (ERR-06) |",
  "| AC-15 | UC-03 | FE-02 | o GitHub desconectado | o Humano aprova | o app pede a conexão (ERR-06) |\n| AC-144 | UC-03 | FA-03 | um plano com uma tarefa sem `prova` e `devolucoes` = 0 | o orquestrador o propõe | o núcleo o devolve ao orquestrador com \"Tarefa incompleta: preencha `faz` (até 500 caracteres), `pronto_quando` e `prova`.\" (ERR-49), `devolucoes` fica em 1 e nada chega ao Humano |\n| AC-145 | UC-03 | FA-04 | um plano com `devolucoes` = 2 e uma tarefa com `faz` de 501 caracteres | o orquestrador o propõe de novo | o plano chega ao Humano com essa tarefa marcada como incompleta (ERR-49) |",
  "Decisão 5: AC novos para o UC-03 FA-03 e FA-04")
t("08-criterios-de-aceite.md",
  "| AC-32 | UC-08 | principal | o limite atingido | o registro termina |",
  "| AC-32 | UC-08 | principal | o limite atingido e a recomendação de passagem aceita pelo Humano | o registro termina |",
  "Decisão 4: a passagem só começa com o aceite")
t("08-criterios-de-aceite.md",
  "| AC-33 | UC-08 | FA-01 | o adiamento | o Humano confirma | o diário contém o adiamento |",
  "| AC-33 | UC-08 | FA-01 | um chat em que o Humano já seguiu uma vez depois do aviso de limite | o Humano escolhe seguir no chat de novo | o chat segue ativo, `continuacoes` fica em 2 e o diário contém as duas continuações |",
  "Decisão 4: continuação sem teto no lugar do adiamento")
t("08-criterios-de-aceite.md",
  "| AC-80 | UC-08 | regra RN-23 | um chat com limite de 100 mil tokens | ele chega a 100 mil | a passagem de turno começa |",
  "| AC-80 | UC-08 | regra RN-23 | um chat com limite de 100 mil tokens | ele chega a 100 mil | aparece \"Este chat passou do limite de 100 mil tokens. Recomendado: passar o turno e abrir um chat novo.\" (ERR-48), o chat segue ativo e a passagem só começa se o Humano aceitar |",
  "Decisão 4: RN-23 no estado novo")
t("08-criterios-de-aceite.md",
  "| AC-107 | UC-08 | requisito RF-20 | um chat que atinge o limite | o registro termina |",
  "| AC-107 | UC-08 | requisito RF-20 | um chat que atinge o limite, com a recomendação de passagem aceita pelo Humano | o registro termina |",
  "Decisão 4: RF-20 no estado novo")
t("08-criterios-de-aceite.md",
  "| AC-124 | UC-08 | TEL-01 FA-02 | a barra no limite | a resposta termina | abre o chat de continuação |",
  "| AC-124 | UC-08 | TEL-01 FA-02 | a barra no limite | a resposta termina | aparece a recomendação de passar o turno (ERR-48); o chat de continuação só abre depois que o Humano aceita |",
  "Decisão 4: sem abertura automática do chat de continuação")

# ---------- README.md ----------
t("README.md",
  "| `05-erros.md` | Catálogo de erros | ERR-01 a ERR-49 |",
  "| `05-erros.md` | Catálogo de erros e avisos | ERR-01 a ERR-49 |",
  "Decisão 1: o catálogo tem erros e avisos")
t("README.md",
  "| `08-criterios-de-aceite.md` | Critérios de aceite | AC-01 a AC-143 |",
  "| `08-criterios-de-aceite.md` | Critérios de aceite | AC-01 a AC-145 |",
  "Decisão 5: AC-144 e AC-145 novos")
t("README.md",
  "Mensagem de erro vem do ERR: uma por condição.",
  "Mensagem de erro ou de aviso vem do ERR: uma por condição.",
  "Decisão 1: o catálogo tem erros e avisos")

# ---------- mudancas.md ----------
FONTE = "perguntas do orquestrador de 2026-11-19, sessão das 16h14"
AVAL = "aval do humano em 2026-11-19, sessão das 16h18"
linhas = [
 ("M-20", "Suposições de trabalho: `janela_status` e `semanal_status` com os valores do campo `status` do `rate_limit_event` mais `desconhecido` para valor novo; `excedente` texto opcional (o `overageStatus`), fora da tela por ora; `caminho` da PastaContexto absoluto", "02 (ENT-14, ENT-26)", "suposição do orquestrador, aguarda aval"),
 ("M-19", "ERR-49 com teto de devolução: tarefa com `faz` vazio ou acima de 500 caracteres, ou com `pronto_quando` ou `prova` vazios, devolve o plano ao orquestrador até 2 vezes (`devolucoes`, novo em ENT-05); na 3ª, o plano chega ao Humano com as tarefas marcadas, e ele pede o preenchimento por \"Pedir alteração\"; mensagem e estado do ERR-49 definidos; entram UC-03 FA-03 e FA-04 e AC-144 e AC-145", "02 (ENT-05), 03 (UC-03 FA-03, FA-04), 04 (CMP-12, CMP-13), 05 (ERR-49), 07 (RF-08), 08 (introdução, AC-144, AC-145), README", AVAL),
 ("M-18", "Limite do chat vira aviso, sem adiamento: ao atingir `limite_tokens`, o sistema avisa e recomenda a passagem de turno e um chat novo; o Humano pode seguir no chat quantas vezes quiser, e cada continuação vai ao diário; a passagem só começa quando o Humano aceita. ERR-48 passa a `LIMITE_DO_CHAT_ATINGIDO` (`avisar`); em ENT-03, `adiamento_usado` sai e entra `continuacoes`; em ENT-25, `adiamento` vira `continuacao`", "00 (RF-20, RN-23), 01 (ATR-01), 02 (ENT-03, ENT-25), 03 (UC-02 FA-02; UC-08 passos 1 a 5, FA-01, FE-01, FE-02), 04 (CMP-07), 05 (ERR-48), 06 (NAV-17), 07 (RN-23), 08 (AC-08, AC-32, AC-33, AC-80, AC-107, AC-124)", AVAL),
 ("M-17", "ERR-47 vira aviso (`avisar`): limite de contexto do projeto ou do chat fora de 10 mil a 1 milhão é aceito e salvo, com a mensagem da faixa recomendada", "02 (ENT-01, ENT-03), 04 (CMP-07), 05 (ERR-47)", AVAL),
 ("M-16", "ERR-45 e ERR-46 ficam como erros (projeto não salvo), com uma mensagem por violação", "05 (ERR-45, ERR-46)", AVAL),
 ("M-15", "O catálogo separa erro (dado inválido, não salva) de aviso (limite de boa prática: sinaliza, recomenda e o Humano decide); entra o tratamento `avisar`", "05 (título, introdução, Tratamentos), README", AVAL),
]
novas = "".join(f"| {i} | 2026-11-19 | {o} | {b} | {FONTE} | {a} |\n" for i, o, b, a in linhas)
t("mudancas.md",
  "|---|---|---|---|---|---|\n| M-14 |",
  "|---|---|---|---|---|---|\n" + novas + "| M-14 |",
  "Decisão 7: M-15 a M-20 no topo, M-14 intacta")

aqui = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(aqui, "trocas.json"), "w", encoding="utf-8") as f:
    json.dump(T, f, ensure_ascii=False, indent=1)
print(len(T), "trocas")
