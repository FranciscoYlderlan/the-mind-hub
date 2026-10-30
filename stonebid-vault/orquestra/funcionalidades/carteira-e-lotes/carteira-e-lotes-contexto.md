---
tipo: contexto
funcionalidade: carteira-e-lotes
status: em-construcao
etapa: 3
criado: 2026-10-29
aliases: [Carteira e lotes, I1, Depósito simulado, Criação de lote, Vitrine, Wallet and lots]
---
# 🧭 Carteira e lotes (I1)

> [!tldr] Em uma linha
> O licitante deposita saldo simulado e o leiloeiro cria lotes a partir de itens de uma API pública, que aparecem na vitrine sem depender dessa API.

## Objetivo e motivação
Etapa 3 do [[geral-plano]] (I1 de [[contrato-processo-e-plano]]): RF-40 a RF-42, RF-20 a RF-22, RF-25, RF-10, RN-13, RN-16 a RN-18. Pronto quando o leiloeiro cria um lote a partir da API e ele aparece na vitrine, e o licitante deposita. É a base de dinheiro e de lote sobre a qual o I2 (lances) grava.

## Fatos que eu informei
- 2026-10-30 00:10: "registre esses próximos passos para o próximo agente e salve no onde parou stonebid-vault".
- 2026-10-29 23:58: "só que verificações deve ser utilizando o chrome pois é um teste verídico".
- 2026-10-29 23:5x: a miniatura da busca vem por uma rota da API ([[geral-decisao-2026-10-29-miniatura-da-busca-pela-api]]); confirmou que o erro não captado era o toast do `ZodError` no depósito.
- 2026-10-29 23:40: "apareceu um erro que não foi captado ... adicione todos esse pontos no vault pois irei delegar subagentes para realizar as correções".
- 2026-10-29 23:01: aprovou seed com imagem fixa e também em produção, busca só em domínio público, `DEPOSIT_LIMIT_EXCEEDED`, sequência no extrato no I2 e a arrumação do PR #3 (hooks em `src/hooks/`, `SubmitButton` comum).
- 2026-10-29 22:23: aprovou a API do Art Institute of Chicago, a imagem em bytes no PostgreSQL e as propostas Q-06, Q-07, Q-10 e Q-14.
- 2026-10-29 22:24: "gostaria que a construção fosse multi thread para agilizar os processos".
- 2026-10-29 22:20: "O próximo passo é marcar a etapa 2 como concluída no [[geral-plano]] e começar a etapa 3 (I1)."

## O que já foi feito
- 2026-10-29: etapa aberta; plano [[carteira-e-lotes-plano]] escrito como proposta; decisões da etapa aprovadas às 22:23.
- 2026-10-29 22:45–22:55: T1a (carteira, PR #1 do `stonebid-api`), T1b (lotes, PR #2 do `stonebid-api`) e T2 (telas, PR #3 do `stonebid-web`) entregues por três subagentes em paralelo, todos com CI verde ([[carteira-e-lotes-plano]]).
- 2026-10-29 23:05–23:20: merge do humano dos PRs #1 e #2 do `stonebid-api` e #3 e #4 do `stonebid-web`; `staging` atualizada, CD verde (T3).
- 2026-10-29 23:30–23:40: verificação no ar (T4) em staging: busca, criação de lote, depósito idempotente e 403 provados; bloqueante no depósito pela tela e outros três achados, devolvidos como T5a a T5e em [[carteira-e-lotes-plano-correcoes]] ([[carteira-e-lotes-plano-correcoes-t5a-e-t5b]]).
- 2026-10-29 23:47 – 2026-10-30 00:10: T5a (PR #3 do `stonebid-api`), T5b (PR #6), T5d (PR #5) e T5c (PR #4 do `stonebid-api` e #7 do `stonebid-web`) entregues por subagentes em paralelo e mergeadas pelo humano. T5a, T5b e T5d aprovadas por verificadores de código e por um verificador no Chrome em staging; T5c ainda sem a verificação no Chrome. Achados viraram a T5f (proposta).
- 2026-10-30: T5c verificada no Chrome (miniaturas pela API, nada em `artic.edu`; centavos da T5a batem). Mergeados: T5f (#8 do web, `a3836fc`), T5g (#5 da API, `7246bf1`) e T5h (#6 da API, `ad06247`); staging igual à `main`. Em andamento: T5i (feedback ao criar lote) e T5j (RN-19 na API).

## Tempo disponível
O do [[geral-contexto]]: entrega em 2026-10-30 16:00.

## Dial e modelo de IA
- Dial: medio (o do [[geral-contexto]])
- Modelo de IA: Claude Opus 5.5 (`claude-opus-5-5`) [a confirmar]

## Áreas sensíveis
- Dinheiro e idempotência (RN-16, RN-18), base do saldo comprometido do I2: [[contrato-regras-de-negocio]] e [[contrato-modelo-de-dados]].
- API externa e cópia do item (RN-13, AD-06): [[contrato-arquitetura]] e [[contrato-tecnologias]].
- Papéis no servidor (RF-02): [[contrato-requisitos-funcionais]].
- Toda rota nova atualiza a MCP: [[geral-decisao-2026-10-29-camada-mcp]].
- Componentes: [[registro-de-componentes]] e [[geral-decisao-2026-10-28-criacao-de-componentes]].

## Mapa
- Plano: [[carteira-e-lotes-plano]]; correções da T4: [[carteira-e-lotes-plano-correcoes]]
- Decisões: [[geral-decisao-2026-10-29-api-de-itens]], [[geral-decisao-2026-10-29-imagem-do-lote-no-banco]], [[geral-decisao-2026-10-29-lance-inicial-e-valor-minimo]], [[geral-decisao-2026-10-29-inicio-e-duracao-do-lote]], [[geral-decisao-2026-10-29-limites-do-deposito]], [[geral-decisao-2026-10-29-edicao-de-lote-fora]], [[geral-decisao-2026-10-29-seed-com-imagem-fixa]], [[geral-decisao-2026-10-29-seed-tambem-em-producao]], [[geral-decisao-2026-10-29-busca-so-em-dominio-publico]], [[geral-decisao-2026-10-29-codigo-do-teto-do-deposito]], [[geral-decisao-2026-10-29-sequencia-no-extrato]], [[geral-decisao-2026-10-29-miniatura-da-busca-pela-api]], [[geral-decisao-2026-10-30-cache-e-limite-da-miniatura]], [[geral-decisao-2026-10-30-obra-unica-por-lote]], [[geral-decisao-2026-10-29-modo-de-implementacao]], [[geral-decisao-2026-10-29-padrao-de-branches]], [[geral-decisao-2026-10-29-testes-no-escopo]]
- Diário: [[diario-2026-10-29-carteira-e-lotes]], [[diario-2026-10-30]]
- Acesso: [[acesso-de-teste]]

## Interpretação do agente
- "Multi thread" foi lido como subagentes implementadores em paralelo (T1a, T1b e T2), não como concorrência no código.

### 🔗 Conexões
- Mapa: [[moc-orquestra]]
- Etapa anterior: [[esqueleto-contexto]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
