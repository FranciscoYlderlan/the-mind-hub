---
tipo: contexto
funcionalidade: fundacao
status: em-construcao
etapa: 2
criado: 2026-11-19
aliases: [Fundação, Interfaces comuns, G1]
---
# 🧭 Fundação — interfaces comuns (G1)

> [!tldr] Em uma linha
> As interfaces comuns que as etapas 3 a 8 usam: trait `Integracao`, mascaramento de segredo, montagem da chamada ao `claude -p`, esquema SQLite e contrato IPC.

## Objetivo e motivação
Fechar o "Pronto quando" da etapa 2 do [[geral-plano]]: sem estas interfaces, as funcionalidades das etapas seguintes não podem partir em paralelo (G1). Sem RF próprio; prepara RF-05, RF-10, RF-18, RF-29 e RF-32.

## Fatos que eu informei
- 2026-11-19 (sessão das 16h56): "ok para todos" ao plano T1 a T5 em série e aos 8 pontos `[a confirmar]` do relatório das 16h18.

## O que já foi feito
- 2026-11-19: plano T1 a T5 aprovado; T1 (trait `Integracao`) entregue e verificada.
- 2026-11-20: T2 (mascaramento) refeita sem adivinhar, por prefixo conhecido e segredo guardado ([[geral-decisao-2026-11-20-mascaramento-sem-adivinhar]]), e verificada ([[diario-2026-11-20]]).
- 2026-11-23: código no GitHub (`FranciscoYlderlan/MyHarness`), histórico com datas de 2026-09-21 a 2026-11-23; uma PR por tarefa, mergeada pelo humano ([[geral-decisao-2026-11-23-push-e-pr-no-github]], [[geral-decisao-2026-11-23-uma-pr-por-tarefa]], [[diario-2026-11-23]]).

## Tempo disponível
- Humano até as 18h de 2026-11-19.

## Dial e modelo de IA
- Dial: o do [[geral-contexto]]
- Modelo de IA: o do [[geral-contexto]]

## Áreas sensíveis
- Mascaramento (RN-04, RNF-05): nenhum token em texto puro.
- Esquema SQLite: [[geral-decisao-2026-11-19-entidades-no-sqlite]], [[geral-decisao-2026-11-19-gravacao-dupla]], [[geral-decisao-2026-11-19-data-e-hora-em-utc]].

## Mapa
- Plano: [[fundacao-plano]]
- Decisões: [[geral-decisao-2026-11-19-branches-e-pr-unica]], [[geral-decisao-2026-11-19-agente-por-claude-p]], [[geral-decisao-2026-11-19-stack]]
- Bugs: (nenhum)
- Referências: [[geral-plano-arquitetura-e-stack]]

## Interpretação do agente
- (nenhuma)

### 🔗 Conexões
- Candidatos: [[fundacao-plano-candidatos]]
- Mapa: [[moc-orquestra]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
