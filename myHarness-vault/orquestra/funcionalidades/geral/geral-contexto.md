---
tipo: contexto
funcionalidade: geral
status: em-construcao
etapa-atual: 2
criado: 2026-11-19
aliases: [contexto do MyHarness, MyHarness context]
---
# 🧭 MyHarness — contexto geral

> [!tldr] Em uma linha
> aplicação desktop que governa agentes do Claude CLI, usando o Obsidian como memória e o humano como validador final

## Objetivo e motivação
- Construir o MyHarness: app desktop (Tauri + Rust + React) que governa o trabalho de agentes do Claude CLI. Quatro fronteiras: o Obsidian lembra, o MyHarness governa, o Modelo executa e o Humano valida.
- Motivo: tirar do cofre as regras de como os agentes trabalham (Manual da Orquestra (no Vault)) e torná-las código no núcleo, para que o agente não precise "lembrar" de obedecer.
- Documento-fonte: especificação funcional de 2026-11-18 (30 RN, 34 RF, 14 RNF, 14 UC, 6 telas), original em `Anexos/harness-especificacao-funcional-2026-11-18.txt`; a transcrição com numeração própria mora em `Anexos/contrato/00-requisitos.md` deste cofre.

## Fatos que eu informei
(o agente preserva sem reinterpretar; fato substituído sai daqui e fica no diário)
- Perfil: prático (Manual da Orquestra - Perfil projeto prático (no Vault)).
- Publicação: só local, app desktop para uma pessoa (sem o bloco "só com deploy"). Ambiente de desenvolvimento: WSL + Docker (`compose.yaml` do repositório). Plataforma final do app: Windows (nativo).
- Acesso ao Obsidian: o Obsidian roda no Windows e é acessado via MCP.
- Repositório de código: pasta local `C:\Users\Ylderlan\Documents\Projetos\my-harness`, onde o agente escreve direto; ele implementa e testa na própria máquina virtual ([[geral-decisao-2026-11-19-acesso-ao-repositorio]]). GitHub: [a preencher]. Onde fica e o que o agente pode sem perguntar vira decisão em `funcionalidades/geral/`.
- Enquanto o MyHarness está em desenvolvimento, o trabalho segue o método manual da orquestra, sem o MyHarness: governança e memória andam juntas neste cofre. Quando o MyHarness estiver pronto, a governança passa para ele e o cofre fica só como memória.
- Nesta fase inicial: vários agentes em paralelo para acelerar.
- Escopos de commit: por ID de requisito.
- Grafia do nome do projeto: MyHarness.

## O que já foi feito
- 2026-11-19: cofre criado com `cofre.py criar` ([[diario-2026-11-19]]).
- 2026-11-19: esqueleto do repositório `my-harness` na máquina virtual do agente: ambiente WSL + Docker (`compose.yaml`) e rascunho do contrato, entregues ao humano por arquivo; o contrato mora em `Anexos/contrato/` deste cofre desde 2026-11-19.

## Tempo disponível
- [a confirmar]

## Dial e modelo de IA
- Dial: medio
- Modelo de IA: Claude Opus 5.5 no orquestrador (sessão de 2026-11-19); subagentes [a confirmar]

## Áreas sensíveis
(onde ler bugs e referências antes de mexer)

## Mapa
- Roteiro: [[geral-plano]]
- Proposta de arquitetura e stack: [[geral-plano-arquitetura-e-stack]], [[geral-plano-arquitetura-e-stack-integracoes-e-testes]], [[geral-plano-arquitetura-e-stack-integracoes-e-testes-prototipos]]
- Decisões: [[geral-decisao-2026-11-19-grafia-do-nome]], [[geral-decisao-2026-11-19-repositorio-e-ambiente]], [[geral-decisao-2026-11-19-plataforma-final]], [[geral-decisao-2026-11-19-acesso-ao-obsidian]], [[geral-decisao-2026-11-19-roteiro]], [[geral-decisao-2026-11-19-estrutura]], [[geral-decisao-2026-11-19-stack]], [[geral-decisao-2026-11-19-teste-da-tela]], [[geral-decisao-2026-11-19-github-oauth-proprio]], [[geral-decisao-2026-11-19-configuracoes-dos-agentes]], [[geral-decisao-2026-11-19-ci-no-github]], [[geral-decisao-2026-11-19-acesso-ao-repositorio]], [[geral-decisao-2026-11-19-agente-por-claude-p]], [[geral-decisao-2026-11-19-fonte-do-consumo]], [[geral-decisao-2026-11-19-subagente-nao-altera-contrato]], [[geral-decisao-2026-11-19-gatilho-do-ci]], [[geral-decisao-2026-11-19-identificador-do-app]], [[geral-decisao-2026-11-19-versao-inicial]], [[geral-decisao-2026-11-19-push-e-pr-pelo-nucleo]], [[geral-decisao-2026-11-19-entidades-no-sqlite]], [[geral-decisao-2026-11-19-papel-pesquisa]], [[geral-decisao-2026-11-19-data-e-hora-em-utc]]
- Bugs: (nenhum ainda)
- Referências: [[manual-da-orquestra]], [[manual-do-cerebro]]
- Documento-fonte: `Anexos/harness-especificacao-funcional-2026-11-18.txt`

## Interpretação do agente
(separada dos fatos; marcar [a confirmar] quando for suposição)

### 🔗 Conexões
- Mapa: [[moc-orquestra]]
- Regras: [[manual-da-orquestra]]
