---
tipo: contexto
funcionalidade: sala-ao-vivo
status: concluida
etapa: 5
criado: 2026-10-30
aliases: [Sala ao vivo, I3, Liquidação, Live room]
---
# 🧭 Sala ao vivo e liquidação (I3)

> [!tldr] Em uma linha
> A sala do lote atualiza sozinha (SSE), o anti-sniping prorroga o fim, o lote vencido é liquidado uma vez só, o vencedor recebe um comprovante público por link e o leiloeiro vê o total recebido.

## Objetivo e motivação
Etapa 5 do [[geral-plano]]. Pela linha I3 de [[contrato-processo-e-plano]] (11.3): RF-30 a RF-32, RF-24, RF-50 a RF-52, RN-10 e RN-11. Pronto quando um leilão completo, do início ao comprovante, funciona no ar.

## Fatos que eu informei
- Decisões aprovadas pelo humano em 2026-10-30 11:1x–11:2x: [[geral-decisao-2026-10-30-tempo-real-por-sse]], [[geral-decisao-2026-10-30-disparo-da-liquidacao]], [[geral-decisao-2026-10-30-movimentos-da-liquidacao]], [[geral-decisao-2026-10-30-resultado-no-lote]], [[geral-decisao-2026-10-30-limite-do-anti-sniping]], [[geral-decisao-2026-10-30-viewer-no-lote]], [[geral-decisao-2026-10-30-rotas-publicas-do-i3]], [[geral-decisao-2026-10-30-seed-com-lote-liquidado]], [[geral-decisao-2026-10-30-motivo-do-cancelamento-gravado]]. Desvios e caminho da auditoria aprovados em 2026-10-30 12:44: [[geral-decisao-2026-10-30-caminho-da-auditoria]], [[geral-decisao-2026-10-30-sala-publica-le-a-sessao]], [[geral-decisao-2026-10-30-lot-ended-no-cancelamento]], [[geral-decisao-2026-10-30-422-no-cancelamento]], [[geral-decisao-2026-10-30-concorrencia-do-cloud-run]], [[geral-decisao-2026-10-30-posicao-cancelado-inalcancavel]].
- Pendências do I2 que entram aqui: [[geral-decisao-2026-10-30-pseudonimo-com-6-digitos]] (lances de teste refeitos pelo seed, humano 2026-10-30 11:2x), [[geral-decisao-2026-10-30-dar-lance-so-para-licitante]], [[geral-decisao-2026-10-30-recarga-de-15s-ate-o-i3]].
- Comprovante e hash: [[geral-decisao-2026-10-29-comprovante-e-hash]]; testes do I3 (T-04, T-05, T-07, T-09): [[geral-decisao-2026-10-29-testes-no-escopo]].

## O que já foi feito
- 2026-10-30 11:1x–11:2x: plano proposto e 9 pontos aprovados (sessão anterior; o plano e este contexto não chegaram a ser gravados e foram refeitos às 11:3x a partir das decisões). 11:3x: contrato da T1 fixado; quatro implementadores (API: liquidação e SSE; web: sala e arremates) despachados em paralelo. 11:49–12:3x: merge dos PRs #12 e #13 da API (`staging` em `f756ac2`, lances de teste apagados e refeitos pelo seed) e do #15 do web; 12:30: merge do #16 e `staging` do web avançada (`728210a`). Falta a verificação no ar (T6).
- 2026-10-30 13:0x: T6 verificada sem bloqueante (código e Chrome em staging, ver [[sala-ao-vivo-plano]]); etapa 5 concluída no [[geral-plano]]. Falta a T7 (PR #18 do `viewer`) no ar.
- 2026-10-30 13:3x: T7 verificada no Chrome em staging, 4 de 4 ✔ (ver [[sala-ao-vivo-plano]]).

## Tempo disponível
Entrega em 2026-10-30 16:00 ([[geral-decisao-2026-10-30-prazo-16h]]); I4 e revisão vêm depois. Primeiro corte se apertar: o seed com lote liquidado.

## Dial e modelo de IA
- Dial: o do [[geral-contexto]].
- Modelo de IA: o da sessão.

## Áreas sensíveis
- Liquidação concorrente e saldo: [[lances-contexto]], [[bug-deposito-sem-teto-na-resposta-2026-10-29]].
- SSE no Cloud Run (buffer e instância única): consequências de [[geral-decisao-2026-10-30-tempo-real-por-sse]].

## Mapa
- Plano: [[sala-ao-vivo-plano]]
- Decisões: as listadas em "Fatos que eu informei".

## Interpretação do agente
- A sessão que aprovou os pontos caiu antes de gravar o plano; os números dos pontos citados nas decisões (1 a 9) foram mantidos no plano refeito.

### 🔗 Conexões
- Mapa: [[moc-orquestra]]
- Projeto: [[geral-contexto]]
- Etapa anterior: [[lances-contexto]]
- Regras: [[manual-da-orquestra]]
