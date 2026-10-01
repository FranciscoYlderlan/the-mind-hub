---
aliases: [Mapa da orquestra, Mapa do projeto, Project map]
tags: [estudos/programacao]
tipo: moc
status: em-uso
criado: 2026-10-28
origem: manual-da-orquestra
---
# 🗺️ Mapa da Orquestra — Stonebid

> [!tldr] Em uma linha
> O mapa do cofre do projeto: daqui se chega no contexto, nas funcionalidades, nas regras e nos modelos.

## 🚦 Etapas vitais
- [[manual-da-orquestra#🚦 Etapas vitais]]: toda escrita termina em `python orquestra/modelos/cofre.py verificar .` com zero ERRO.
- [[bug-estado-anterior-preservado-apos-mudanca-2026-10-29]]: por que toda mudança de estado passa pela varredura de impacto (uma versão só por nota).
- [[manual-da-orquestra#🔄 Passagem de turno]]: chat novo começa por `cofre.py status` e pelo "Onde parei" do último diário.

## 🧭 Projeto
- [[CLAUDE]]: índice que os agentes leem primeiro.
- [[geral-plano]]: roteiro — em que etapa o projeto está e as notas geradas em cada etapa.
- [[geral-contexto]]: objetivo, motivação, dial e decisões que valem para o projeto todo.
- [[enunciado-teste-tecnico]]: enunciado oficial da Verzel (fonte da verdade nº 1) e o mapa contra o contrato.
- [[contrato-do-projeto]]: contrato v0.3 (requisitos, regras de negócio, arquitetura proposta, riscos, testes, plano e perguntas Q; histórico das mudanças M-01 a M-13 em [[contrato-do-projeto-mudancas]]); perguntas da seção 14 em validação (a Q-09 já foi respondida).
- Decisões de base: [[geral-decisao-2026-10-28-stack-frontend|stack do frontend]], [[geral-decisao-2026-10-28-stack-backend|stack do backend]], [[geral-decisao-2026-10-28-estrutura-frontend|pastas do frontend]], [[geral-decisao-2026-10-28-estrutura-backend|pastas do backend]], [[geral-decisao-2026-10-28-criacao-de-componentes|criação de componentes]], [[geral-decisao-2026-10-28-testes-frontend-playwright|teste Playwright por outro agente]], [[geral-decisao-2026-10-29-camada-mcp|camada MCP]], [[geral-decisao-2026-10-29-hospedagem|hospedagem (GCP + Vercel)]], [[geral-decisao-2026-10-29-padrao-de-branches|padrão de branches]], [[geral-decisao-2026-10-29-testes-no-escopo|testes no escopo (M-11)]], [[geral-decisao-2026-10-29-comprovante-e-hash|comprovante selado e hash do lance (M-12)]], [[geral-decisao-2026-10-29-cancelamento-ao-vivo|cancelamento de lote ao vivo (M-13)]], [[geral-decisao-2026-10-29-roteiro|roteiro em 8 etapas]].

## 🚧 Funcionalidades
- [[esqueleto-contexto]]: etapa 2, esqueleto no ar (I0): repositórios, login com papéis, seed, CI e deploy no GCP + Vercel.

## 📦 Arquivadas
- (nenhuma ainda)

## 📚 Regras e referências
- [[manual-da-orquestra]]: estrutura, papéis, fluxo e gatilhos.
- [[manual-do-cerebro]]: tom e esqueleto das notas de referência.
- [[registro-de-componentes]]: o que já existe no frontend; consultar antes de criar componente.

## 🧩 Modelos
- Notas operacionais: [[modelo-contexto]], [[modelo-plano]], [[modelo-decisao]], [[modelo-bug]], [[modelo-diario]]
- Notas de consulta: [[modelo-referencia]], [[modelo-nota]]
- Subagentes: [[modelo-briefing-subagente]], [[modelo-relatorio-subagente]]
- Repositório de código: [[modelo-claude-do-repositorio]]

## 🔗 Conexões
- Índice para agentes: [[CLAUDE]]
- Regras: [[manual-da-orquestra]]
