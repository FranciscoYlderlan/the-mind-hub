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
- 2026-10-29 23:01: aprovou seed com imagem fixa e também em produção, busca só em domínio público, `DEPOSIT_LIMIT_EXCEEDED`, sequência no extrato no I2 e a arrumação do PR #3 (hooks em `src/hooks/`, `SubmitButton` comum).
- 2026-10-29 22:23: aprovou a API do Art Institute of Chicago, a imagem em bytes no PostgreSQL e as propostas Q-06, Q-07, Q-10 e Q-14.
- 2026-10-29 22:24: "gostaria que a construção fosse multi thread para agilizar os processos".
- 2026-10-29 22:20: "O próximo passo é marcar a etapa 2 como concluída no [[geral-plano]] e começar a etapa 3 (I1)."

## O que já foi feito
- 2026-10-29: etapa aberta; plano [[carteira-e-lotes-plano]] escrito como proposta; decisões da etapa aprovadas às 22:23.
- 2026-10-29 22:45–22:55: T1a (carteira, PR #1 do `stonebid-api`), T1b (lotes, PR #2 do `stonebid-api`) e T2 (telas, PR #3 do `stonebid-web`) entregues por três subagentes em paralelo, todos com CI verde; aguardam o merge do humano ([[carteira-e-lotes-plano]]).

## Tempo disponível
O do [[geral-contexto]]: entrega em 2026-10-30 09:00.

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
- Plano: [[carteira-e-lotes-plano]]
- Decisões: [[geral-decisao-2026-10-29-api-de-itens]], [[geral-decisao-2026-10-29-imagem-do-lote-no-banco]], [[geral-decisao-2026-10-29-lance-inicial-e-valor-minimo]], [[geral-decisao-2026-10-29-inicio-e-duracao-do-lote]], [[geral-decisao-2026-10-29-limites-do-deposito]], [[geral-decisao-2026-10-29-edicao-de-lote-fora]], [[geral-decisao-2026-10-29-seed-com-imagem-fixa]], [[geral-decisao-2026-10-29-seed-tambem-em-producao]], [[geral-decisao-2026-10-29-busca-so-em-dominio-publico]], [[geral-decisao-2026-10-29-codigo-do-teto-do-deposito]], [[geral-decisao-2026-10-29-sequencia-no-extrato]], [[geral-decisao-2026-10-29-modo-de-implementacao]], [[geral-decisao-2026-10-29-padrao-de-branches]], [[geral-decisao-2026-10-29-testes-no-escopo]]
- Diário: [[diario-2026-10-29-carteira-e-lotes]]
- Acesso: [[acesso-de-teste]]

## Interpretação do agente
- "Multi thread" foi lido como subagentes implementadores em paralelo (T1a, T1b e T2), não como concorrência no código.

### 🔗 Conexões
- Mapa: [[moc-orquestra]]
- Etapa anterior: [[esqueleto-contexto]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
