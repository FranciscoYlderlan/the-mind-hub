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
- [[contrato-do-projeto]]: contrato v0.3 (requisitos, regras de negócio, arquitetura proposta, riscos, testes, plano e perguntas Q; histórico das mudanças M-01 a M-13 em [[contrato-do-projeto-mudancas]]); perguntas da seção 14 em validação (Q-06, Q-07, Q-09, Q-10, Q-13 e Q-14 já respondidas).
- Decisões de base: [[geral-decisao-2026-10-28-stack-frontend|stack do frontend]], [[geral-decisao-2026-10-28-stack-backend|stack do backend]], [[geral-decisao-2026-10-28-estrutura-frontend|pastas do frontend]], [[geral-decisao-2026-10-28-estrutura-backend|pastas do backend]], [[geral-decisao-2026-10-28-criacao-de-componentes|criação de componentes]], [[geral-decisao-2026-10-28-testes-frontend-playwright|teste Playwright por outro agente]], [[geral-decisao-2026-10-29-camada-mcp|camada MCP]], [[geral-decisao-2026-10-29-hospedagem|hospedagem (GCP + Vercel)]], [[geral-decisao-2026-10-29-padrao-de-branches|padrão de branches]], [[geral-decisao-2026-10-29-testes-no-escopo|testes no escopo (M-11)]], [[geral-decisao-2026-10-29-comprovante-e-hash|comprovante selado e hash do lance (M-12)]], [[geral-decisao-2026-10-29-cancelamento-ao-vivo|cancelamento de lote ao vivo (M-13)]], [[geral-decisao-2026-10-29-roteiro|roteiro em 8 etapas]], [[geral-decisao-2026-10-29-modo-de-implementacao|modo de implementação (container → GitHub → Actions; Chrome no ar)]], [[geral-decisao-2026-10-29-api-de-itens|API de itens (Art Institute of Chicago)]], [[geral-decisao-2026-10-29-imagem-do-lote-no-banco|imagem do lote no banco]], [[geral-decisao-2026-10-29-lance-inicial-e-valor-minimo|lance inicial = valor mínimo (Q-06)]], [[geral-decisao-2026-10-29-inicio-e-duracao-do-lote|início e duração do lote (Q-07)]], [[geral-decisao-2026-10-29-limites-do-deposito|limites do depósito (Q-10)]], [[geral-decisao-2026-10-29-edicao-de-lote-fora|sem edição de lote (Q-14)]], [[geral-decisao-2026-10-29-sessao-jwt-no-cabecalho|sessão por JWT no cabeçalho]], [[geral-decisao-2026-10-29-prisma-7|Prisma 7]], [[geral-decisao-2026-10-29-typescript-6-no-web|TypeScript 6 no web]], [[geral-decisao-2026-10-29-next-themes-para-o-tema|tema pelo next-themes]], [[geral-decisao-2026-10-29-vercel-sem-deploy-automatico|Vercel sem deploy automático]], [[geral-decisao-2026-10-29-alias-fixo-do-staging|alias fixo do staging]], [[geral-decisao-2026-10-29-seed-com-imagem-fixa|seed com imagem fixa]], [[geral-decisao-2026-10-29-seed-tambem-em-producao|seed também em produção]], [[geral-decisao-2026-10-29-busca-so-em-dominio-publico|busca só em domínio público]], [[geral-decisao-2026-10-29-codigo-do-teto-do-deposito|código do teto do depósito]], [[geral-decisao-2026-10-29-sequencia-no-extrato|sequência no extrato (I2)]], [[geral-decisao-2026-10-29-node-26|Node 26]], [[geral-decisao-2026-10-29-miniatura-da-busca-pela-api|miniatura da busca pela API]], [[geral-decisao-2026-10-30-cache-e-limite-da-miniatura|cache e limite da miniatura]], [[geral-decisao-2026-10-30-obra-unica-por-lote|obra única por lote (RN-19)]], [[geral-decisao-2026-10-30-prazo-16h|entrega às 16h]].

## 🚧 Funcionalidades
- [[carteira-e-lotes-contexto]]: etapa 3 (concluída), carteira e lotes (I1): depósito simulado, busca na API de itens, criação do lote e vitrine.
- [[esqueleto-contexto]]: etapa 2 (concluída), esqueleto no ar (I0): repositórios, login com papéis, seed, CI e deploy no GCP + Vercel.

## 📦 Arquivadas
- (nenhuma ainda)

## 📚 Regras e referências
- [[manual-da-orquestra]]: estrutura, papéis, fluxo e gatilhos.
- [[manual-do-cerebro]]: tom e esqueleto das notas de referência.
- [[registro-de-componentes]]: o que já existe no frontend; consultar antes de criar componente.
- [[acesso-de-teste]]: endereços no ar e usuários de teste (login livre para humano e agentes).
- [[passo-a-passo-do-agente]]: comandos já provados para retomar o projeto: anexar os repositórios com escrita, push, PR pela REST, CI, `staging`, teste no Chrome e commit do cofre.

## 🧩 Modelos
- Notas operacionais: [[modelo-contexto]], [[modelo-plano]], [[modelo-decisao]], [[modelo-bug]], [[modelo-diario]]
- Notas de consulta: [[modelo-referencia]], [[modelo-nota]]
- Subagentes: [[modelo-briefing-subagente]], [[modelo-relatorio-subagente]]
- Repositório de código: [[modelo-claude-do-repositorio]]

## 🔗 Conexões
- Índice para agentes: [[CLAUDE]]
- Regras: [[manual-da-orquestra]]
