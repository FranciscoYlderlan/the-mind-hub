---
tipo: plano
funcionalidade: geral
status: aprovado
criado: 2026-11-19
---
# 🧭 Roteiro — MyHarness

> [!tldr] Onde o projeto está
> Etapa atual: **2. Fundação e protótipo das suposições** (em-construcao)

> [!warning] Proposta da IA até eu aprovar
> As etapas nascem como proposta. Aprovadas, viram a nota `geral-decisao-AAAA-MM-DD-roteiro` e este plano passa a `status: aprovado`. Mudar a lista de etapas é uma nova decisão.

Uma seção por etapa, na ordem em que o projeto acontece. Status: `planejada → em-construcao → em-verificacao → concluida → arquivada`. Etapa concluída tem data e links para as notas geradas nela. A linha "Etapa atual" acima é sincronizada por `cofre.py status --atualizar`.

No projeto prático, cada etapa segue, para cada funcionalidade dela, o ciclo contrato da funcionalidade em `Anexos/contrato/` → implementação → verificador de fluxo principal → adversarial, e termina com os fluxos de teste dela registrados em `geral-plano-teste-humano` ([[modelo-roteiro-teste-humano]]). A última etapa é a aceitação final: verificadores e avaliador primeiro, depois o roteiro final ao humano, montado desse registro e passando por todas as funcionalidades; o aceite dele fecha o projeto.

Durante o desenvolvimento, a governança roda pelo método manual da Orquestra (este cofre, orquestrador na sessão principal do Claude Code). A etapa 9 é a virada: o MyHarness passa a governar o próprio projeto. Fonte: especificação funcional "Harness" de 2026-11-18 (RN-01 a RN-30, RF-01 a RF-34, RNF-01 a RNF-14, UC-01 a UC-14, TEL-01 a TEL-06, D1 a D6, S1 a S15).

## 1. Definir o roteiro do projeto
- **Status:** concluida
- **Objetivo:** listar as etapas gerais do projeto, da primeira à entrega.
- **Pronto quando:** etapas aprovadas numa nota de decisão.
- **Funcionalidades:** (nenhuma)
- **Notas geradas:** [[geral-decisao-2026-11-19-roteiro]], [[geral-decisao-2026-11-19-estrutura]], [[geral-decisao-2026-11-19-stack]], [[geral-decisao-2026-11-19-teste-da-tela]], [[geral-decisao-2026-11-19-grafia-do-nome]], [[geral-decisao-2026-11-19-repositorio-e-ambiente]], [[geral-decisao-2026-11-19-plataforma-final]], [[geral-decisao-2026-11-19-acesso-ao-obsidian]], [[diario-2026-11-19]]
- **Concluída em:** 2026-11-19

## 2. Fundação e protótipo das suposições
- **Status:** em-construcao
- **Objetivo:** criar o repositório e o esqueleto Tauri + Rust + React + SQLite (WAL), preencher o contrato em `Anexos/contrato/` a partir da especificação e provar, num protótipo descartável, as suposições que decidem a arquitetura do backend: saída de `claude -p` em fluxo JSON com modelo, ferramentas, pastas e instruções por parâmetro (S3); CLI direta ou Claude Agent SDK num processo Node (S4); fonte legível por máquina do consumo semanal e da janela, com o plano B dos registros locais (S2); duração da janela, 4 h ou 5 h (S1); forma de login das três integrações (S5).
- **Pronto quando:** `Anexos/contrato/` com `00-requisitos` preenchido do documento-fonte e rastreabilidade RF → UC → TEL; decisões de estrutura, stack, S3/S4 e fonte do consumo aprovadas em `funcionalidades/geral/`; app vazio compila e abre na máquina virtual do agente, com o SQLite criado; interfaces comuns definidas (G1): trait `Integracao` (RNF-11), esquema SQLite das entidades, contrato de comandos e eventos Tauri (IPC), módulo de mascaramento de segredo (RN-04) e módulo de "montagem da chamada" ao Claude CLI.
- **Ciclo** (prático): sem funcionalidade de produto; protótipo de pesquisa com relatório e prova (saída real do `claude -p` e da fonte de consumo anexada), depois tarefas-interface (P12, G1).
- **Funcionalidades:** `fundacao` (sem RF próprio; prepara RF-05, RF-10, RF-18, RF-29, RF-32)
- **Paralelo:** os protótipos S2, S3/S4 e S5 são pesquisa, só leitura, sem teto (G11) e em paralelo; o esqueleto do repositório é uma cadeia com um agente só (G3); as tarefas-interface rodam em série depois da decisão S3 × S4.
- **Notas geradas:** [[geral-decisao-2026-11-19-agente-por-claude-p]], [[geral-decisao-2026-11-19-fonte-do-consumo]], [[geral-decisao-2026-11-19-subagente-nao-altera-contrato]], [[geral-decisao-2026-11-19-gatilho-do-ci]], [[geral-decisao-2026-11-19-identificador-do-app]], [[geral-decisao-2026-11-19-versao-inicial]]
- **Concluída em:** 

## 3. Integrações
- **Status:** planejada
- **Objetivo:** conectar e mostrar o status de Claude CLI, Obsidian CLI e GitHub (OAuth com token no cofre de credenciais do SO), cada uma atrás da interface própria.
- **Pronto quando:** AC de UC-01 e TEL-02 (principal, FA-01, FE-01 a FE-03) passando no verificador de fluxo principal e no adversarial; busca automatizada sem token em texto puro (RNF-05).
- **Ciclo** (prático): contrato da funcionalidade → implementação → verificador de fluxo principal → adversarial → fluxos de teste registrados
- **Funcionalidades:** `integracoes` (RF-01, RF-02, RF-03, RF-04)
- **Paralelo:** RF-01, RF-02 e RF-03 em paralelo, um módulo por integração sobre a trait da etapa 2 (G1, G2); RF-04 (frontend, CMP-03 e CMP-11) depois deles.
- **Notas geradas:** 
- **Concluída em:** 

## 4. Conversa com o orquestrador
- **Status:** planejada
- **Objetivo:** abrir um chat do orquestrador, enviar prompt com modelo escolhido e prompt de papel anexado, e ver a resposta em tempo real na aba do orquestrador.
- **Pronto quando:** AC de UC-02 (principal, FE-01, FE-02), UC-09, UC-13 e TEL-04 passando nos dois agentes; RNF-01 (200 ms) e RNF-13 (150 tokens) medidos.
- **Ciclo** (prático): contrato da funcionalidade → implementação → verificador de fluxo principal → adversarial → fluxos de teste registrados
- **Funcionalidades:** `chat-orquestrador` (RF-05, RF-07, RF-30), `prompts-de-papel` (RF-31, RF-32), `modelos` (RF-13)
- **Paralelo:** `prompts-de-papel` e `modelos` em paralelo; `chat-orquestrador` depende dos dois pela "montagem da chamada" da etapa 2 (G1), então pode partir junto só se a interface estiver fechada; senão, em série depois deles.
- **Notas geradas:** 
- **Concluída em:** 

## 5. Memória, contexto e vários cofres
- **Status:** planejada
- **Objetivo:** levar ao núcleo as regras de memória (só o orquestrador grava, leitura só pela CLI, um cofre de memória por projeto) e mostrar ao humano o que os agentes leem e quais pastas estão em contexto.
- **Pronto quando:** AC de UC-11 e UC-14 e de RN-01, RN-02, RN-29, RN-30 passando nos dois agentes; RNF-14 (3 s em 3 cofres) medido.
- **Ciclo** (prático): contrato da funcionalidade → implementação → verificador de fluxo principal → adversarial → fluxos de teste registrados
- **Funcionalidades:** `memoria` (RF-28), `contexto-de-leitura` (RF-14, RF-15, RF-16), `cofres-do-projeto` (RF-33, RF-34)
- **Paralelo:** `memoria` (caminho de escrita) e `contexto-de-leitura` (caminho de leitura) em paralelo; `cofres-do-projeto` depois de `contexto-de-leitura`, porque RF-34 depende de RF-15 e os dois tocam no módulo da Obsidian CLI (RN-14, G2).
- **Notas geradas:** 
- **Concluída em:** 

## 6. Consumo, logs, histórico e passagem de turno
- **Status:** planejada
- **Objetivo:** mostrar o tempo todo o consumo do plano e do chat, registrar e exibir cada comando com segredo mascarado, guardar o histórico de projetos e chats e fazer a passagem de turno automática com "Onde parei" gravado antes do chat novo.
- **Pronto quando:** AC de UC-08 e UC-12 e de RN-04, RN-23, RN-24 passando nos dois agentes; RNF-04 (2 s e 60 s) e RNF-08 (retomada sem perda) provados.
- **Ciclo** (prático): contrato da funcionalidade → implementação → verificador de fluxo principal → adversarial → fluxos de teste registrados
- **Funcionalidades:** `consumo` (RF-17, RF-18, RF-19), `logs` (RF-21, RF-22), `historico` (RF-23), `passagem-de-turno` (RF-20)
- **Paralelo:** `consumo`, `logs` e `historico` em paralelo (3 que escrevem, dentro do teto G11); `passagem-de-turno` depois de `consumo` (RF-17) e usa RF-07 e RF-28 já prontos. G4: um pesquisador já levanta o Claude in Chrome e o plano B de MCP de navegador (S6) para a etapa 8.
- **Notas geradas:** 
- **Concluída em:** 

## 7. Plano de delegação e despacho de subagentes
- **Status:** planejada
- **Objetivo:** receber do orquestrador o plano estruturado, segurá-lo até o aval, despachar um processo do Claude CLI por tarefa com briefing, modelo e ferramentas do papel, em worktree e branch próprias, até o push e o PR, e acompanhar cada subagente em abas e cartões.
- **Pronto quando:** AC de UC-03, UC-04 e UC-10 e de RN-03, RN-05 a RN-08, RN-12 a RN-14, RN-16, RN-17, RN-27 passando nos dois agentes; suíte de tentativas proibidas por papel com 100% negadas (RNF-06); queda detectada em até 5 s (RNF-07); RNF-02, RNF-09 e RNF-10 medidos.
- **Ciclo** (prático): contrato da funcionalidade → implementação → verificador de fluxo principal → adversarial → fluxos de teste registrados
- **Funcionalidades:** `plano-delegacao` (RF-08, RF-09), `despacho-subagentes` (RF-10, RF-11, RF-29, RF-06, RF-12), `worktree-pr` (RF-27)
- **Paralelo:** tarefa-interface antes (G1): formato do plano (Tarefa) e da Execução/Relatório no SQLite e no IPC. Depois, `plano-delegacao` e `worktree-pr` em paralelo; `despacho-subagentes` em série depois de `plano-delegacao` (cadeia RF-08 → RF-10 → RF-11 → RF-06/RF-12, G3), com RF-06 e RF-12 (frontend) em paralelo entre si no fim.
- **Notas geradas:** 
- **Concluída em:** 

## 8. Teste, adversarial e revisão de achados
- **Status:** planejada
- **Objetivo:** despachar o subagente de teste (quem implementa não testa, ✔ só com prova, teto de 2 voltas) e o adversarial sem contexto pelo Claude in Chrome, e deixar o humano decidir cada achado.
- **Pronto quando:** AC de UC-05, UC-06 e UC-07 e de RN-09 a RN-11, RN-15, RN-18 a RN-22 passando nos dois agentes; recurso exclusivo do navegador provado com dois adversariais (RN-15).
- **Ciclo** (prático): contrato da funcionalidade → implementação → verificador de fluxo principal → adversarial → fluxos de teste registrados
- **Funcionalidades:** `teste-de-funcionalidade` (RF-24), `adversarial` (RF-25), `revisao-de-achados` (RF-26)
- **Paralelo:** `teste-de-funcionalidade` e `adversarial` em paralelo sobre a entidade Achado/Critério definida antes (G1); `revisao-de-achados` (frontend, TEL-05) depois dos dois. Na verificação, o navegador é recurso exclusivo (G7).
- **Notas geradas:** 
- **Concluída em:** 

## 9. Virada: o MyHarness governa o próprio projeto
- **Status:** planejada
- **Objetivo:** ligar o `myHarness-vault` como cofre de memória e o `Vault` como consulta, e rodar pelo MyHarness um ciclo completo real (pedido → plano → aval → despacho → teste → adversarial → achados → PR → merge do humano), deixando o método manual como plano B.
- **Pronto quando:** um ciclo completo registrado no cofre pelo MyHarness, com a inspeção de RNF-09 (rastreabilidade) e RNF-05 (zero token em texto puro) depois do ciclo; RNF-03 (400 MB em 8 h) medido; o verificador do conjunto (G8) passa depois do último merge; decisão da virada aprovada.
- **Ciclo** (prático): sem funcionalidade nova; verificação do conjunto (G8) e achados como opções (P06).
- **Funcionalidades:** (nenhuma nova; usa todas as anteriores)
- **Paralelo:** em série; é uma rodada só, com recurso exclusivo (navegador) e um humano validando.
- **Notas geradas:** 
- **Concluída em:** 

## 10. Roteiro do humano e aceitação final
- **Status:** planejada
- **Posição:** (prático) sempre a última; etapa nova entra antes dela, e a numeração segue 1..N. O `cofre.py criar` já a põe no roteiro do cofre novo.
- **Objetivo:** com todas as funcionalidades passando nos dois agentes, fazer a aceitação final: verificadores e avaliador independente primeiro; depois, o roteiro final ao humano, curto e didático, passando por todas as funcionalidades. O aceite do humano fecha a etapa.
- **Pronto quando:** toda funcionalidade coberta no roteiro, roteiro testado pelo humano, achados decididos como opções e aceite do humano registrado.
- **Funcionalidades:** (nenhuma)
- **Notas geradas:** `geral-plano-teste-humano`
- **Concluída em:** 

## Proposta de arquitetura e stack
Só no projeto prático de software (S25 do Padrão de projeto de software (no Vault)); em outro projeto prático, apagar esta seção. Proposta da IA a partir da Referência de arquitetura e stack (no Vault), em linguagem leiga, no passo 4 de Criar um novo cofre (no Vault). Com o aval, cada escolha vira decisão em `funcionalidades/geral/` (`geral-decisao-AAAA-MM-DD-estrutura`, `geral-decisao-AAAA-MM-DD-stack`), com o link para esta seção no campo Proposta.

**Ideia geral, numa frase:** a tela (React) só mostra e pede; o núcleo (Rust) decide tudo, inclusive o que cada agente pode fazer; cada agente é um processo do Claude CLI que o núcleo abre já "de mãos amarradas" para o seu papel.

- **Frontend:** React + Vite + TypeScript, Tailwind + shadcn/ui, TanStack Query, Zustand, zod; lista virtualizada para a saída dos agentes. Sem rotas de URL no começo.
- **Backend:** núcleo em Rust dentro do Tauri 2, em camadas (regras → casos de uso → integrações), com cada integração atrás de uma interface trocável (RNF-11). Agentes rodam como `claude -p` direto (S3), com permissão imposta em quatro camadas. S4 descartada pelo P1.
- **Tecnologias e versões:** a mais recente estável no momento de criar o repositório, sem trava (S16); conferir que não é rc. Lista na tabela abaixo.
- **Detalhe e protótipos:** [[geral-plano-arquitetura-e-stack]] (tela, núcleo, banco, S3 × S4) e [[geral-plano-arquitetura-e-stack-integracoes-e-testes]] (integrações, consumo, testes, pastas) e [[geral-plano-arquitetura-e-stack-integracoes-e-testes-prototipos]] (protótipos).
- **Ajustes do humano:** nenhum; aprovada em [[geral-decisao-2026-11-19-estrutura]] e [[geral-decisao-2026-11-19-stack]]


### 🔗 Conexões
- Projeto: [[geral-contexto]]
- Proposta de stack: [[geral-plano-arquitetura-e-stack]], [[geral-plano-arquitetura-e-stack-integracoes-e-testes]], [[geral-plano-arquitetura-e-stack-integracoes-e-testes-prototipos]]
- Mapa: [[moc-orquestra]]
- Regras: [[manual-da-orquestra]]
