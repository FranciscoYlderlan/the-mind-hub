# Modelo de dados e invariantes (ENT)

As validações pertencem à entidade, não à tela: toda tela que mostra ou edita o campo herda as regras daqui. No backend, a entidade é o domínio; no frontend, o schema do campo sai desta tabela. Cada violação tem o seu erro, para a mensagem dizer o que está errado.

Fonte: tabela "Entidades e onde moram" do documento-fonte (ENT-01 a ENT-16). As ENT-17 a ENT-25 não estão nessa tabela: aparecem só no campo "Dados" das RN e estão aqui para que toda RN tenha entidade [a confirmar]. Tipos, tamanhos e formatos que a fonte não dá ficam `[a confirmar]`. Campo marcado "(RN-xx)" é citado só pela regra e não está na tabela da fonte.

## ENT-01 Projeto

Mora em: SQLite.

### Campos

| Campo | Tipo | Tamanho ou faixa | Obrigatório | Formato | Valores permitidos | Erro por violação |
|---|---|---|---|---|---|---|
| nome | texto | [a confirmar] | sim [a confirmar] | livre | — | [a confirmar] |
| repositorio | texto (caminho ou URL) [a confirmar] | — | [a confirmar] | [a confirmar] | — | [a confirmar] |
| limite_contexto_padrao | inteiro (tokens) | > 0 [a confirmar] | sim | só algarismos | padrão 100 mil (S7) | [a confirmar] |

### Invariantes (nunca violadas, em nenhum fluxo)

- Todo projeto tem exatamente um cofre de memória (RN-29; violação: ERR-38).

## ENT-02 Cofre

Mora em: SQLite.

### Campos

| Campo | Tipo | Tamanho ou faixa | Obrigatório | Formato | Valores permitidos | Erro por violação |
|---|---|---|---|---|---|---|
| projeto | referência | — | sim | id de ENT-01 | — | [a confirmar] |
| nome | texto | — | sim | nome do cofre no Obsidian | cofre que a Obsidian CLI enxerga | não responde: ERR-37 |
| funcao | enumeração | — | sim | — | memoria, consulta | escrita em consulta: ERR-39 |
| ativo | booleano | — | sim | — | sim, não | — |
| status | enumeração | — | sim | — | conectado, desconectado [a confirmar] | — |

### Invariantes (nunca violadas, em nenhum fluxo)

- Um só cofre com `funcao = memoria` por projeto (RN-29; tirar o único: ERR-38).
- O orquestrador só grava no cofre de memória (RN-29; violação: ERR-39).
- Cofre desativado sai das buscas, mas continua ligado (UC-14 FA-01).
- Trocar a memória exige confirmação; o antigo vira consulta (UC-14 FA-01).

## ENT-03 Chat

Mora em: SQLite.

### Campos

| Campo | Tipo | Tamanho ou faixa | Obrigatório | Formato | Valores permitidos | Erro por violação |
|---|---|---|---|---|---|---|
| projeto | referência | — | sim | id de ENT-01 | — | — |
| limite_tokens | inteiro | > 0 [a confirmar] | sim | só algarismos | padrão: o do projeto (100 mil, S7) | [a confirmar] |
| tokens_usados | inteiro | ≥ 0 | sim | — | — | — |
| chat_anterior | referência | — | não | id de ENT-03 | só chat encerrado por passagem | — |
| status | enumeração | — | sim | — | ativo, pausado, encerrado, só leitura [a confirmar] | — |
| adiamento_usado | booleano (RN-23) [a confirmar] | — | sim | — | — | segundo adiamento: [a confirmar] |

### Invariantes (nunca violadas, em nenhum fluxo)

- Ao atingir `limite_tokens`, começa a passagem de turno (RN-23), salvo adiamento único (RN-23).
- Chat de continuação só existe depois do "Onde parei" com próximo passo gravado (RN-24; violação: ERR-29).

### Estados do ciclo de vida

| Estado | Entra quando | Pode ir para |
|---|---|---|
| ativo | "Novo chat", reabertura ou continuação | pausado, encerrado |
| pausado | limite de uso do plano atingido (UC-02 FE-02) | ativo [a confirmar: ao reinício da janela] |
| encerrado | passagem de turno concluída (UC-08) | (final; reabre só para leitura [a confirmar]) |
| só leitura | cofre do projeto não encontrado ao reabrir (UC-12 FE-01) | ativo [a confirmar] |

## ENT-04 Mensagem

Mora em: SQLite.

### Campos

| Campo | Tipo | Tamanho ou faixa | Obrigatório | Formato | Valores permitidos | Erro por violação |
|---|---|---|---|---|---|---|
| chat | referência | — | sim | id de ENT-03 | — | — |
| autor | enumeração [a confirmar] | — | sim | — | Humano, orquestrador [a confirmar] | — |
| texto | texto | [a confirmar] | sim | livre | segredos mascarados (RN-04) | — |
| uso_tokens | inteiro | ≥ 0 | [a confirmar] | — | — | — |

### Invariantes (nunca violadas, em nenhum fluxo)

- Nenhum segredo em texto puro (RN-04; o trecho é mascarado como ••••).

## ENT-05 PlanoDelegação

Mora em: SQLite + decisão no cofre.

### Campos

| Campo | Tipo | Tamanho ou faixa | Obrigatório | Formato | Valores permitidos | Erro por violação |
|---|---|---|---|---|---|---|
| chat | referência | — | sim | id de ENT-03 | — | — |
| versao | inteiro | ≥ 1 | sim | — | sobe a cada "Pedir alteração" | — |
| status | enumeração | — | sim | — | proposto, aprovado, recusado | despacho sem aval: ERR-09 |
| aprovado_em | data e hora | — | só se aprovado | [a confirmar] | — | — |

### Invariantes (nunca violadas, em nenhum fluxo)

- Nenhum subagente inicia com o plano fora de `aprovado` (RN-05; violação: ERR-09), salvo pesquisa só de leitura [a confirmar, S10].
- "Aprovar" só com as integrações exigidas pelo plano conectadas (RN-08; violação: ERR-06).

### Estados do ciclo de vida

| Estado | Entra quando | Pode ir para |
|---|---|---|
| proposto | o orquestrador propõe (RF-08) ou chega versão nova após "Pedir alteração" | aprovado, recusado, proposto (versão nova) |
| aprovado | o Humano aprova (RF-09) | (final) |
| recusado | o Humano recusa | (final) |

## ENT-06 Tarefa

Mora em: SQLite + plano no cofre.

### Campos

| Campo | Tipo | Tamanho ou faixa | Obrigatório | Formato | Valores permitidos | Erro por violação |
|---|---|---|---|---|---|---|
| faz | texto | [a confirmar] | sim | livre | — | [a confirmar] |
| toca_em | lista de caminhos | — | sim [a confirmar] | caminho relativo ao repositório | — | sobreposição com tarefa paralela: ERR-12 |
| depende_de | lista de referências | — | não | ids de ENT-06 | — | — |
| paralelo | booleano | — | sim | — | sim, não | — |
| pronto_quando | texto | — | sim | livre | — | — |
| prova | texto | — | sim | comando ou evidência | — | — |
| papel | referência | — | sim | id de ENT-15 | funcionalidade, teste, adversarial (pesquisa [a confirmar]) | — |
| modelo | texto | — | não | id de modelo da CLI | modelo disponível na CLI | sem modelo e sem padrão: ERR-11 |
| voltas | inteiro | 0 a 2 | sim | — | — | 3ª reprovação: ERR-21 |
| implementada_por (RN-09) | referência | — | [a confirmar] | id de ENT-07 | — | — |
| testada_por (RN-09) | referência | — | [a confirmar] | id de ENT-07 | ≠ implementada_por | igual: ERR-19 |

### Invariantes (nunca violadas, em nenhum fluxo)

- Tarefas com `toca_em` sobreposto nunca rodam ao mesmo tempo (RN-14; violação: ERR-12).
- `testada_por` ≠ `implementada_por` (RN-09; violação: ERR-19).
- `voltas` ≤ 2; a 3ª reprovação sobe ao Humano (RN-19; violação: ERR-21).
- Modelo efetivo = `modelo` ou, sem ele, `Papel.modelo_padrao` (RN-07; nenhum dos dois: ERR-11).

## ENT-07 Execução

Mora em: SQLite.

### Campos

| Campo | Tipo | Tamanho ou faixa | Obrigatório | Formato | Valores permitidos | Erro por violação |
|---|---|---|---|---|---|---|
| tarefa | referência | — | sim (salvo orquestrador [a confirmar]) | id de ENT-06 | — | — |
| papel | referência | — | sim | id de ENT-15 | orquestrador, funcionalidade, teste, adversarial | ação fora do papel: ERR-13, ERR-14 |
| modelo | texto | — | sim | id de modelo da CLI | — | ERR-11 |
| prompt_versao | inteiro | ≥ 1 | sim | — | versão vigente no início (RN-28) | sem prompt: ERR-36 |
| worktree | caminho | — | sim para funcionalidade | caminho no disco | — | ausente: ERR-16 |
| branch | texto | — | sim para funcionalidade | `tipo/ID-descricao` | — | ausente: ERR-16 |
| status | enumeração | — | sim | — | na fila, rodando, concluido, falhou, interrompida | — |
| comandos (RN-17) | lista | — | — | — | sem merge, push --force, push na principal | ERR-14 |

### Invariantes (nunca violadas, em nenhum fluxo)

- `prompt_versao` não muda durante a execução (RN-28).
- No máximo 5 execuções de funcionalidade em `rodando` (RN-13; excedente: ERR-44).
- Execução de funcionalidade sempre com worktree e branch próprias (RN-16; violação: ERR-16).
- As ferramentas da execução são só as do papel, impostas pelo núcleo (RN-27, RNF-06).

### Estados do ciclo de vida

| Estado | Entra quando | Pode ir para |
|---|---|---|
| na fila | teto atingido (RN-13), espera de "toca em" (RN-14) ou de recurso (RN-15) [a confirmar: "aguardando recurso" é estado próprio?] | rodando |
| rodando | o processo inicia | concluido, falhou, interrompida |
| concluido | o relatório chega (RF-11) | (final) |
| falhou | o processo cai ou para de emitir eventos (RNF-07; ERR-17) | (final) |
| interrompida | o app fecha durante a execução (RNF-08) | [a confirmar] |

## ENT-08 PromptPapel

Mora em: SQLite.

### Campos

| Campo | Tipo | Tamanho ou faixa | Obrigatório | Formato | Valores permitidos | Erro por violação |
|---|---|---|---|---|---|---|
| fluxo | enumeração | — | sim | — | orquestrador, funcionalidade, teste, adversarial, passagem de turno | — |
| texto | texto | 1 a 80 palavras (S14) | sim | livre | — | vazio: ERR-35; acima de 80 palavras: ERR-34 |
| versao | inteiro | ≥ 1 | sim | — | — | — |
| palavras | inteiro | 1 a 80 | sim | calculado | — | ERR-34 |
| tokens | inteiro | até 150 por chamada (RNF-13) [a confirmar] | sim | calculado | — | [a confirmar: bloqueia ou só avisa?] |
| vigente | booleano | — | sim | — | uma versão vigente por fluxo | — |

### Invariantes (nunca violadas, em nenhum fluxo)

- Todo fluxo tem uma versão vigente; nasce com o padrão de fábrica (CMP-16).
- Salvar cria versão nova; a anterior fica no histórico (RF-31).
- O texto não altera permissões (RN-27).

### Valores de fábrica (versão 1)

| Fluxo | Prompt de papel | Palavras (segundo a fonte) |
|---|---|---|
| Orquestrador | Você é o orquestrador. Antes de responder, busque na memória pela Obsidian CLI. Divida o trabalho em tarefas pequenas, cada uma com o que toca, do que depende e quando está pronta. Proponha o plano e espere o aval antes de delegar. Registre relatórios e decisões aprovadas assim que chegam. Não implemente: delegue. | 54 |
| Funcionalidade | Você implementa uma única tarefa, na sua worktree. Toque só nos arquivos da tarefa. Rode a prova antes de dizer que terminou e termine com push e PR. Devolva o relatório no formato pedido, com dúvidas e o que notou fora do escopo. | 45 |
| Teste | Você testa uma funcionalidade que não construiu. Procure falhas; não confirme por confiança. Para cada critério, dê ✔ ou ✘ com a prova. Não corrija nada: cada falha vira bug com passos, esperado e obtido. | 38 |
| Adversarial | Você usa esta aplicação pela primeira vez e não sabe como foi feita. Tente cumprir cada objetivo pela tela, como um usuário. Fluxo que não se completa é bug; fluxo que se completa com dificuldade é sugestão de UI/UX. Relate sempre com passos e captura. | 47 |
| Passagem de turno | O chat chegou ao limite de contexto. Registre na memória o "Onde parei": próximo passo, threads abertas e dúvidas. Não comece trabalho novo. | 24 |

Regra de contagem de palavras [a confirmar]: uma contagem por espaços dá 52, 43, 33, 43 e 23.

## ENT-09 Relatório

Mora em: SQLite + resumo no cofre.

### Campos

| Campo | Tipo | Tamanho ou faixa | Obrigatório | Formato | Valores permitidos | Erro por violação |
|---|---|---|---|---|---|---|
| resultado | enumeração [a confirmar] | — | sim | — | concluído, falhou, bloqueado [a confirmar] | — |
| o_que_fez | texto | até 1,5 mil tokens no total (RNF-10) | sim | livre | — | — |
| arquivos | lista de caminhos | — | não | — | — | — |
| prova | texto | — | sim | — | — | — |
| criterios | lista de ENT-24 | — | [a confirmar] | — | — | — |
| duvidas | lista de texto | — | não | — | — | — |
| candidatos_a_nota | lista de texto | — | não | — | — | — |
| registrado_em (RN-03) | data e hora | — | sim antes da próxima delegação | — | — | não registrado: ERR-15 |

### Invariantes (nunca violadas, em nenhum fluxo)

- Nenhuma delegação nova com relatório recebido e não registrado (RN-03; ERR-15).
- Pergunta direta do subagente vira item de `duvidas` (RN-12).

## ENT-10 Achado

Mora em: SQLite + bug no cofre.

### Campos

| Campo | Tipo | Tamanho ou faixa | Obrigatório | Formato | Valores permitidos | Erro por violação |
|---|---|---|---|---|---|---|
| tipo | enumeração | — | sim | — | bug, sugestao | sem tipo: ERR-27 |
| passos | texto | — | sim | lista numerada [a confirmar] | — | [a confirmar] |
| esperado | texto | — | sim | livre | — | — |
| obtido | texto | — | sim | livre | — | — |
| captura | arquivo | — | sim para adversarial [a confirmar] | imagem | — | indisponível: ERR-43 |
| decisao | enumeração | — | sim para sugestão ao fechar a rodada | — | corrigir, limite, opcional | faltando: ERR-28 |
| status (RN-20) | enumeração [a confirmar] | — | sim | — | aberto, fechado [a confirmar] | — |

### Invariantes (nunca violadas, em nenhum fluxo)

- Bug tem `decisao = corrigir`, fixa (CMP-15, UC-07 FA-01).
- Toda sugestão tem decisão antes de fechar a rodada (RN-22; ERR-28).
- Fluxo não completado = bug; completado com dificuldade = sugestão (RN-21).

## ENT-11 Leitura

Mora em: SQLite.

### Campos

| Campo | Tipo | Tamanho ou faixa | Obrigatório | Formato | Valores permitidos | Erro por violação |
|---|---|---|---|---|---|---|
| execucao | referência | — | sim | id de ENT-07 | — | — |
| caminho | caminho | — | sim | — | — | — |
| cofre | referência | — | sim quando origem = cli | id de ENT-02 | — | sem origem: ERR-40 |
| origem | enumeração | — | sim | — | cli, arquivo | leitura direta de nota sem autorização: ERR-18 |
| hora | data e hora | — | sim | — | — | — |

### Invariantes (nunca violadas, em nenhum fluxo)

- Leitura de nota com `origem = arquivo` só com a exceção de RN-02 e aparece marcada "sem CLI".
- Toda nota devolvida traz o cofre de origem (RN-30; ERR-40).

## ENT-12 Log

Mora em: SQLite.

### Campos

| Campo | Tipo | Tamanho ou faixa | Obrigatório | Formato | Valores permitidos | Erro por violação |
|---|---|---|---|---|---|---|
| execucao | referência | — | sim | id de ENT-07 | — | — |
| comando | texto | — | sim | — | — | — |
| inicio | data e hora | — | sim | — | — | — |
| fim | data e hora | — | não (rodando) | — | ≥ inicio | — |
| codigo_saida | inteiro | — | não (rodando) | — | — | — |
| saida_mascarada | texto | — | não | — | segredos como •••• (RN-04) | — |

### Invariantes (nunca violadas, em nenhum fluxo)

- Nenhum segredo em texto puro (RN-04, RNF-05).
- Toda ação relevante tem quem, o quê, quando e de qual chat (RNF-09) [a confirmar: o Log tem "chat"?].

## ENT-13 Integração

Mora em: SQLite (status) + cofre de credenciais do SO.

### Campos

| Campo | Tipo | Tamanho ou faixa | Obrigatório | Formato | Valores permitidos | Erro por violação |
|---|---|---|---|---|---|---|
| tipo | enumeração | — | sim | — | Claude CLI, Obsidian CLI, GitHub | — |
| status | enumeração | — | sim | — | conectado, desconectado, sem login, não instalado | ERR-01, ERR-05, ERR-06, ERR-07 |
| conta | texto | — | não | — | — | — |
| versao | texto | — | não | — | — | — |
| credencial (RN-04) | segredo | — | só GitHub (S5) | — | só no cofre de credenciais do SO | — |

### Invariantes (nunca violadas, em nenhum fluxo)

- A credencial nunca vai ao SQLite, a arquivo, a log nem ao cofre Obsidian (RN-04, RNF-05).
- "Desconectar" fica desabilitado durante execução que depende da integração (CMP-11).

## ENT-14 Consumo

Mora em: SQLite.

### Campos

| Campo | Tipo | Tamanho ou faixa | Obrigatório | Formato | Valores permitidos | Erro por violação |
|---|---|---|---|---|---|---|
| semanal_pct | percentual | 0 a 100 | sim | — | — | indisponível: ERR-41 |
| janela_pct | percentual | 0 a 100 | sim | — | — | indisponível: ERR-41 |
| proximo_reinicio | data e hora | — | sim | — | janela de 4 h ou 5 h [a confirmar, S1] | — |

## ENT-15 Papel

Mora em: código do núcleo.

### Campos

| Campo | Tipo | Tamanho ou faixa | Obrigatório | Formato | Valores permitidos | Erro por violação |
|---|---|---|---|---|---|---|
| nome | enumeração | — | sim | — | orquestrador, funcionalidade, teste, adversarial (pesquisa [a confirmar]) | — |
| ferramentas_permitidas | lista | — | sim | — | fixa no núcleo (RN-27) | fora do papel: ERR-13, ERR-14 |
| modelo_padrao | texto | — | sim | id de modelo da CLI | modelo disponível | indisponível: ERR-30 |
| cartao_de_briefing | texto | até 3 mil tokens no briefing (RNF-10) [a confirmar] | sim | gerado (RF-29) | adversarial: só objetivo, endereço e acesso (RN-10) | ERR-23 |

### Invariantes (nunca violadas, em nenhum fluxo)

- Subagente não tem ferramenta de escrita no cofre (RN-01, RF-29).
- Padrões de fábrica restauráveis (UC-09 FA-01) [a confirmar: quais são os de fábrica].

## ENT-16 Recurso

Mora em: SQLite.

### Campos

| Campo | Tipo | Tamanho ou faixa | Obrigatório | Formato | Valores permitidos | Erro por violação |
|---|---|---|---|---|---|---|
| nome | texto | — | sim | — | navegador do Claude in Chrome, banco de teste | — |
| em_uso_por | referência | — | não | id de ENT-07 | uma execução por vez | ocupado: ERR-25 |

### Invariantes (nunca violadas, em nenhum fluxo)

- No máximo uma execução usa o recurso por vez (RN-15).

## ENT-17 Escrita [a confirmar: fora da tabela da fonte]

Citada em RN-01 (Escrita.caminho) e RF-28 (nota, motivo, hora). Mora em: [a confirmar].

| Campo | Tipo | Tamanho ou faixa | Obrigatório | Formato | Valores permitidos | Erro por violação |
|---|---|---|---|---|---|---|
| caminho | caminho | — | sim | — | dentro do cofre de memória | papel sem permissão: ERR-13; cofre de consulta: ERR-39 |
| motivo | texto | — | sim | — | — | — |
| hora | data e hora | — | sim | — | — | — |

## ENT-18 Decisão [a confirmar: fora da tabela da fonte]

Citada em RN-03 (registrada_em) e RN-06 (aval_id). Mora no cofre e [a confirmar] no SQLite.

| Campo | Tipo | Tamanho ou faixa | Obrigatório | Formato | Valores permitidos | Erro por violação |
|---|---|---|---|---|---|---|
| aval_id | referência | — | sim | id do aval do Humano | — | sem aval: ERR-10 |
| registrada_em | data e hora | — | sim antes da próxima delegação | — | — | ERR-15 |

## ENT-19 Briefing [a confirmar: fora da tabela da fonte]

Citado em RN-10 (Briefing.conteudo).

| Campo | Tipo | Tamanho ou faixa | Obrigatório | Formato | Valores permitidos | Erro por violação |
|---|---|---|---|---|---|---|
| conteudo | texto | até 3 mil tokens (RNF-10) [a confirmar] | sim | — | adversarial: só objetivo, endereço, acesso de teste | ERR-23 |

## ENT-20 Rodada [a confirmar: fora da tabela da fonte]

Citada em RN-11 (Rodada.status).

| Campo | Tipo | Tamanho ou faixa | Obrigatório | Formato | Valores permitidos | Erro por violação |
|---|---|---|---|---|---|---|
| status | enumeração | — | sim | — | [a confirmar: em andamento,] aprovada, falhou, aguardando decisão | ERR-24, ERR-26, ERR-28 |

## ENT-21 Funcionalidade [a confirmar: fora da tabela da fonte]

Citada em RN-11 e RN-20 (Funcionalidade.status).

| Campo | Tipo | Tamanho ou faixa | Obrigatório | Formato | Valores permitidos | Erro por violação |
|---|---|---|---|---|---|---|
| status | enumeração | — | sim | — | em-verificacao, concluida, bloqueada [a confirmar: outros] | concluir com pendência: ERR-22 |

### Invariantes (nunca violadas, em nenhum fluxo)

- `concluida` só com todos os critérios ✔ e nenhum bug aberto (RN-20), salvo exceção do Humano com escopo fechado.

## ENT-22 Configuração [a confirmar: fora da tabela da fonte]

Citada em RN-13.

| Campo | Tipo | Tamanho ou faixa | Obrigatório | Formato | Valores permitidos | Erro por violação |
|---|---|---|---|---|---|---|
| teto_escrita | inteiro | ≥ 1 [a confirmar] | sim | — | padrão 5 (S8) | — |

## ENT-23 PR [a confirmar: fora da tabela da fonte]

Citado em RN-17 (PR.status).

| Campo | Tipo | Tamanho ou faixa | Obrigatório | Formato | Valores permitidos | Erro por violação |
|---|---|---|---|---|---|---|
| status | enumeração | — | sim | — | aberto, merged [a confirmar: outros] | merge por agente: ERR-14; conflito: ERR-31 |

## ENT-24 Critério [a confirmar: fora da tabela da fonte]

Citado em RN-18 (Critério.status, Critério.prova).

| Campo | Tipo | Tamanho ou faixa | Obrigatório | Formato | Valores permitidos | Erro por violação |
|---|---|---|---|---|---|---|
| status | enumeração | — | sim | — | ✔, ✘ ("sem prova"), "não verificado, presumido" | ✔ sem prova: ERR-20 |
| prova | texto ou arquivo | — | sim para ✔ | saída de teste, captura, resposta | — | ERR-20 |

## ENT-25 Diário [a confirmar: fora da tabela da fonte; mora no cofre]

Citado em RN-24 (Diário.onde_parei).

| Campo | Tipo | Tamanho ou faixa | Obrigatório | Formato | Valores permitidos | Erro por violação |
|---|---|---|---|---|---|---|
| onde_parei | texto | — | sim na passagem | próximo passo, threads abertas, dúvidas | "Próximo passo" obrigatório | ERR-29 |
| adiamento | texto | — | não | — | um por chat (RN-23) | — |
