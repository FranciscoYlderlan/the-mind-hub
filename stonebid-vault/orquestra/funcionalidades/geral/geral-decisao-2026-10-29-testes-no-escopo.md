---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-29
substitui: 
aliases: [Testes no escopo, Mínimo de testes, Linha de corte dos testes, Test scope rule]
---
# ✅ Testes no escopo: o teste sai só junto com o requisito que prova (M-11)

- **Proposta (plano):** sugestão da IA no chat de 2026-10-29 (12:25), para resolver a ambiguidade do hub [[contrato-do-projeto]]: ele dizia que "continua da v0.2 sem mudança... testes T-01 a T-06", mas [[contrato-testes]] lista T-01 a T-11 e o RNF-12 cobre os onze.
- **Decisão:** humano aprovou ("aprovo") em 2026-10-29 12:28.
  - **Regra:** nenhum teste é cortado por conta própria. Ele só sai do escopo junto com o requisito que prova.
  - **Ficam sempre:** T-01 a T-09 e **T-10a** (cancelamento sem lances, e recusa quando há lances: RF-22, RN-12 base).
  - **Saem junto com o requisito:** **T-10b** (cancelamento com estorno) sai se o OPC-2 (RF-23) for cortado; **T-11** (idempotência) sai só se a RN-18 for afrouxada por mudança registrada.
  - **RNF-12 passa a ler:** testes de todo requisito implementado, executáveis com um comando (`npm test`) e rodando no CI.
- **Alteração:** nenhuma.
- **Motivo:**
  - Diagnóstico: T-01 a T-06 era o **mínimo** da linha de corte (11.4 de [[contrato-processo-e-plano]]), não o escopo inteiro; o hub copiou o mínimo como se fosse a lista.
  - Esse mínimo, pensado para 4 dias, deixava sem teste três itens que o enunciado exige ([[enunciado-teste-tecnico]]): API externa fora do ar (T-07, E3), papéis (T-08, E1) e privacidade (T-09, E3).
  - T-07 a T-09 são baratos com `app.inject` do Fastify e Vitest [a confirmar na implementação]; o custo grande está em T-02 (concorrência) e T-06 (auditoria), que já ficavam sempre.
  - Uma regra só ("o teste segue o requisito") elimina a segunda lista que precisaria ser mantida em sincronia.
- **Consequências:**
  - Pergunta "este teste está no escopo?" tem a mesma resposta que "o requisito dele está no escopo?".
  - Cortar o OPC-2 ou afrouxar a RN-18 exige registrar a saída do teste correspondente junto.
  - O "pronto quando" de cada tarefa de backend inclui o T-xx da regra ([[contrato-testes]]).
  - Proibido: requisito implementado sem o teste que o prova, e teste cortado com o requisito ainda no escopo.
  - Afeta as seções 6 (RNF-12), 10 e 11.4 do contrato; registrada como M-11 em [[contrato-do-projeto-mudancas]].

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[geral-plano]]
- Projeto: [[geral-contexto]]
- Relacionadas: [[contrato-testes]], [[contrato-processo-e-plano]], [[contrato-requisitos-nao-funcionais]], [[contrato-do-projeto]], [[geral-decisao-2026-10-28-stack-backend]]
- Regras: [[manual-da-orquestra]]
