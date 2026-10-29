# Catálogo de erros (ERR)

Um erro por condição. O código do ERR é o código de erro que o servidor devolve; o frontend mostra a mensagem daqui. Fluxo de exceção (FE) só referencia um ERR. Duas condições diferentes nunca dividem a mesma mensagem.

"Servidor" é o núcleo Rust. Os códigos são proposta deste rascunho, derivados das RN e dos FE [a confirmar]. Mensagem entre aspas é texto da fonte; `<x>` é valor preenchido em tempo de execução; mensagem sem texto na fonte fica `[a confirmar]`. Erros que só o agente recebe (sem tela) estão marcados "(agente)".

| ID | Código no servidor | Condição de disparo | Tratamento | Mensagem ao usuário | Estado final |
|---|---|---|---|---|---|
| ERR-01 | `CLAUDE_CLI_NAO_INSTALADO` | o executável do Claude CLI não é encontrado (UC-01 FE-01) | bloquear | "Claude CLI não encontrado", com o link de instalação | integração em `não instalado` |
| ERR-02 | `GITHUB_OAUTH_NAO_CONCLUIDO` | o OAuth do GitHub é cancelado ou recusado (UC-01 FE-02) | voltar | "Conexão com o GitHub não concluída" | GitHub `desconectado` |
| ERR-03 | `OBSIDIAN_FECHADO` | o Obsidian está fechado ao checar o status (UC-01 FE-03, RF-02) | voltar | a mensagem da própria CLI, com a ação "Abrir Obsidian" | Obsidian CLI `desconectado` |
| ERR-04 | `LOGIN_CLAUDE_CLI_FALHOU` | o login do Claude CLI falha (TEL-02 FE-01) [a confirmar: separar do ERR-02?] | repetir | o motivo da falha [a confirmar: texto] | integração em `sem login` |
| ERR-05 | `CLAUDE_CLI_DESCONECTADO` | ação que depende do Claude CLI com ele desconectado (RN-08; UC-02 FE-01; TEL-01 FE-01) | bloquear | "Conecte o Claude CLI para enviar" [a confirmar: TEL-01 usa "Claude CLI desconectado"] | nada enviado; texto mantido no campo |
| ERR-06 | `GITHUB_DESCONECTADO` | plano ou ação que exige GitHub com ele desconectado (RN-08; UC-03 FE-02; TEL-03 FE-01) | bloquear | "Conecte o GitHub para aprovar este plano" [a confirmar: TEL-03 diz "Conecte o GitHub para aprovar"] | plano segue `proposto`; despacho parado |
| ERR-07 | `OBSIDIAN_DESCONECTADO` | ação que depende da Obsidian CLI com ela desconectada (RN-08; UC-08 FE-02) | aguardar | "Conecte o Obsidian para registrar" | a passagem de turno espera a conexão |
| ERR-08 | `LIMITE_DO_PLANO_ATINGIDO` | o limite de uso do plano Claude foi atingido (UC-02 FE-02) | aguardar | a hora do reinício [a confirmar: texto] | chat `pausado` |
| ERR-09 | `PLANO_SEM_AVAL` | despacho de subagente com plano fora de `aprovado` (RN-05) (agente) | bloquear | [a confirmar] | nenhum subagente inicia |
| ERR-10 | `DECISAO_SEM_AVAL` | gravação de decisão para ponto do plano sem aval (RN-06) (agente) | bloquear | [a confirmar] | nota de decisão não gravada |
| ERR-11 | `MODELO_NAO_DEFINIDO` | tarefa sem modelo e papel sem padrão (RN-07) | bloquear | [a confirmar: pede a escolha do modelo] | despacho bloqueado |
| ERR-12 | `TAREFAS_TOCAM_MESMOS_ARQUIVOS` | duas tarefas paralelas com "toca em" sobreposto (RN-14; UC-03 FE-01) | aguardar | "<T1> e <T2> tocam <caminho>: rodarão em série" | ordem ajustada para série |
| ERR-13 | `ESCRITA_NEGADA_PAPEL` | processo que não é o orquestrador tenta escrever no cofre (RN-01, RN-27; UC-04 FE-02) (agente) | bloquear | log: "escrita negada: papel sem permissão" | escrita recusada; log de violação; execução continua |
| ERR-14 | `COMANDO_GIT_NEGADO` | agente tenta merge, push --force ou push na branch principal (RN-17; UC-04 FE-02) (agente) | bloquear | log com a negação [a confirmar: texto] | comando negado; execução continua |
| ERR-15 | `AGUARDANDO_REGISTRO` | delegação com relatório ou decisão ainda não registrados (RN-03) (agente) | aguardar | log: "aguardando registro" | delegação espera o registro |
| ERR-16 | `WORKTREE_AUSENTE` | despacho de funcionalidade sem worktree e branch próprias (RN-16) (agente) | bloquear | [a confirmar] | despacho bloqueado |
| ERR-17 | `SUBAGENTE_CAIU` | processo de agente encerra com erro ou para de emitir eventos (UC-04 FE-01; RNF-07; TEL-01 FE-02) | voltar | [a confirmar: texto]; aba e cartão em erro com o último log | execução `falhou` |
| ERR-18 | `LEITURA_DIRETA_BLOQUEADA` | agente tenta ler .md do cofre sem a CLI e sem a exceção autorizada (RN-02) (agente) | bloquear | aviso [a confirmar: texto] | leitura bloqueada; aviso registrado |
| ERR-19 | `IMPLEMENTADOR_NAO_TESTA` | teste atribuído à mesma execução que implementou (RN-09) (agente) | bloquear | [a confirmar] | atribuição bloqueada |
| ERR-20 | `CRITERIO_SEM_PROVA` | critério marcado ✔ sem prova objetiva (RN-18; UC-05 FE-02) | bloquear | ✘ "sem prova" | critério gravado como ✘ |
| ERR-21 | `TETO_DE_VOLTAS` | tarefa reprova pela 3ª vez (RN-19; UC-05 FE-01) | bloquear | "Tarefa <T> reprovou 3 vezes" | caso na caixa de aval; funcionalidade `bloqueada` |
| ERR-22 | `CONCLUSAO_COM_PENDENCIA` | concluir funcionalidade com critério ✘ ou bug aberto (RN-20) (agente) | bloquear | [a confirmar] | status continua `em-verificacao` |
| ERR-23 | `BRIEFING_ADVERSARIAL_COM_CONTEXTO` | briefing adversarial com conversa, plano, código ou notas (RN-10) (agente) | bloquear | [a confirmar] | briefing recusado |
| ERR-24 | `ADVERSARIAL_ANTES_DO_FIM_DA_RODADA` | despacho adversarial com funcionalidade da rodada ainda em teste (RN-11) | bloquear | [a confirmar] | despacho adversarial bloqueado |
| ERR-25 | `RECURSO_OCUPADO` | recurso exclusivo em uso por outro agente (RN-15; UC-06 FE-01) | aguardar | "aguardando recurso" [a confirmar: texto] | execução aguardando o recurso |
| ERR-26 | `APLICACAO_FORA_DO_AR` | o endereço de teste não responde (UC-06 FE-02) | repetir | "Aplicação não responde em <endereço>" | rodada `falhou` |
| ERR-27 | `ACHADO_SEM_TIPO` | achado adversarial sem tipo bug ou sugestão (RN-21) (agente) | bloquear | [a confirmar] | achado não aceito no relatório |
| ERR-28 | `SUGESTAO_SEM_DECISAO` | fechar a rodada com sugestão sem decisão (RN-22; UC-07 FE-01; TEL-05 FE-01) | bloquear | "Faltam decisões em <n> sugestões", com as sugestões destacadas | rodada `aguardando decisão` |
| ERR-29 | `REGISTRO_INCOMPLETO` | "Onde parei" sem "Próximo passo" (RN-24; UC-08 FE-01) | voltar | "Registro incompleto" | chat novo não abre; orquestrador refaz o registro |
| ERR-30 | `MODELO_INDISPONIVEL` | modelo escolhido deixou de existir na CLI (UC-09 FE-01; TEL-04 FE-01) | voltar | "Modelo indisponível" [a confirmar: TEL-04 diz "Modelo indisponível na CLI"] | padrão anterior mantido; nada salvo |
| ERR-31 | `CONFLITO_DE_MERGE` | conflito entre dois PRs no merge (UC-10 FE-01) | voltar | "Conflito entre <PR-A> e <PR-B>" | PR aberto; tarefa de ajuste criada |
| ERR-32 | `PASTA_INACESSIVEL` | pasta de contexto inexistente ou sem permissão (UC-11 FE-01) | voltar | "Não foi possível acessar <pasta>" | lista de contexto não muda |
| ERR-33 | `COFRE_DO_PROJETO_NAO_ENCONTRADO` | cofre de memória do projeto não encontrado ao reabrir (UC-12 FE-01) | bloquear | "Cofre <nome> não encontrado" | chat só leitura; campo de prompt desabilitado |
| ERR-34 | `PROMPT_ACIMA_DO_LIMITE` | prompt de papel com mais de 80 palavras (RN-26; UC-13 FE-01; TEL-06 FE-01) | bloquear | "<n> palavras acima do limite" | nada salvo |
| ERR-35 | `PROMPT_VAZIO` | prompt de papel vazio ao salvar (UC-13 FE-02) | bloquear | "O prompt de papel não pode ficar vazio" | nada salvo |
| ERR-36 | `PROMPT_DE_PAPEL_AUSENTE` | chamada à LLM sem o prompt de papel do fluxo (RN-25) (agente) | bloquear | [a confirmar] | chamada bloqueada |
| ERR-37 | `COFRE_NAO_RESPONDE` | cofre ligado não responde pela Obsidian CLI (UC-14 FE-01; TEL-06 FE-02) | repetir | "Cofre <nome> não encontrado pela Obsidian CLI" | cofre `desconectado` |
| ERR-38 | `COFRE_MEMORIA_OBRIGATORIO` | tirar o único cofre de memória do projeto (RN-29; UC-14 FE-02) | bloquear | "O projeto precisa de um cofre de memória" | nada muda |
| ERR-39 | `ESCRITA_EM_COFRE_DE_CONSULTA` | gravação num cofre com função consulta (RN-29) (agente) | bloquear | [a confirmar] | escrita negada |
| ERR-40 | `RESULTADO_SEM_COFRE_DE_ORIGEM` | nota devolvida sem o nome do cofre de origem (RN-30) (agente) | bloquear | — (interno) | resultado não entregue ao agente |
| ERR-41 | `CONSUMO_INDISPONIVEL` | os dados de consumo do plano não podem ser lidos (CMP-01) | repetir | "consumo indisponível" | CMP-01 em erro |
| ERR-42 | `FALHA_NO_ENVIO` | o envio do prompt falha por motivo diferente de ERR-05 e ERR-08 (CMP-06) [a confirmar: quais causas] | repetir | [a confirmar] | texto preservado no campo |
| ERR-43 | `CAPTURA_INDISPONIVEL` | a captura de um achado não abre (CMP-15) | repetir | [a confirmar] | achado sem a imagem; decisão segue possível |
| ERR-44 | `TETO_DE_ESCRITA_ATINGIDO` | 6º subagente que escreve código com 5 rodando (RN-13; UC-04 FA-01) | aguardar | contador "x de 5 que escrevem" e a tarefa na fila (CMP-05) | execução `na fila` |

## Tratamentos

- **repetir:** falha passageira (rede, servidor ocupado); o usuário pode tentar de novo.
- **voltar:** o usuário corrige e reenvia.
- **bloquear:** não segue até corrigir; quando der, o próprio campo impede o valor (ex.: só aceita algarismos).
- **aguardar** [a confirmar: tratamento novo, não está no modelo]: a ação fica em espera e segue sozinha quando a condição some (vaga no teto, recurso livre, registro feito, integração conectada).
