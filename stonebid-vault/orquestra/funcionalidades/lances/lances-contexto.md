---
tipo: contexto
funcionalidade: lances
status: em-construcao
etapa: 4
criado: 2026-10-30
aliases: [Lances, I2, Bids]
---
# 🧭 Lances (I2)

> [!tldr] Em uma linha
> O licitante dá lance num lote ao vivo: o sistema valida, compromete o saldo, devolve o do antigo líder e grava o lance numa cadeia de hash, um lance por vez por lote.

## Objetivo e motivação
Etapa 4 do [[geral-plano]]. Pela linha I2 de [[contrato-processo-e-plano]] (11.3): RF-33, RF-70, RN-02 a RN-09 e o lado de escrita da RN-14. Pronto quando T-01 a T-03 passam, com concorrência, e a etapa está no ar.

## Fatos que eu informei
- Regras de [[contrato-regras-de-negocio]]: janela de tempo (RN-02), primeiro lance ≥ lance inicial (RN-03), seguintes ≥ atual + incremento (RN-04), líder não cobre o próprio lance (RN-05), só LICITANTE dá lance (RN-06), lance cabe no disponível e o antigo líder recebe de volta na mesma operação (RN-07, RN-08), operação indivisível, um lance por vez por lote (RN-09).
- Hash e selo do lance: [[geral-decisao-2026-10-29-comprovante-e-hash]].
- Testes que saem junto com a regra: [[geral-decisao-2026-10-29-testes-no-escopo]] (T-01 a T-03, e no I2 também T-08, T-09, T-11 do lance e a concorrência do T-10a de [[geral-decisao-2026-10-29-cancelamento-ao-vivo]]).
- Sequência no extrato no I2: [[geral-decisao-2026-10-29-sequencia-no-extrato]]. Leitor real de lances para a RN-19: [[geral-decisao-2026-10-30-obra-unica-por-lote]].
- Rota nova sai com a tool da MCP: [[geral-decisao-2026-10-29-camada-mcp]].
- Ajustes da etapa 3 seguem em paralelo (T5m de [[carteira-e-lotes-plano-correcoes]]); branches mergeadas ficam no GitHub como histórico (humano, 2026-10-30 08:28).

## O que já foi feito
- 2026-10-30: pesquisa da etapa e plano proposto em [[lances-plano]]; aval dos 6 pontos (08:4x) e implementadores da API (T2a, T2b) e do web (T3) despachados. 09:1x: segredos criados pelo humano, merge dos PRs #10 e #11 da API e #14 do web, `staging` avançada (API `55b1400`, web `c366aef`); falta a verificação no ar (T5). 11:1x: humano aprovou [[geral-decisao-2026-10-30-pseudonimo-com-6-digitos]], [[geral-decisao-2026-10-30-dar-lance-so-para-licitante]] e [[geral-decisao-2026-10-30-recarga-de-15s-ate-o-i3]], implementadas no I3 ([[sala-ao-vivo-contexto]]); 11:3x: verificador da T5 no Chrome despachado.

## Tempo disponível
Entrega em 2026-10-30 16:00 ([[geral-decisao-2026-10-30-prazo-16h]]); I3, I4 e a revisão vêm depois.

## Dial e modelo de IA
- Dial: o do [[geral-contexto]].
- Modelo de IA: o da sessão.

## Áreas sensíveis
- Concorrência e saldo: [[bug-deposito-sem-teto-na-resposta-2026-10-29]] (presenter único, mock igual à API).
- Carteira: [[carteira-e-lotes-contexto]], [[geral-decisao-2026-10-29-limites-do-deposito]].

## Mapa
- Plano: [[lances-plano]]
- Decisões: [[geral-decisao-2026-10-30-pseudonimo-por-hmac]], [[geral-decisao-2026-10-30-lance-atual-no-lote]], [[geral-decisao-2026-10-30-saldo-na-recusa-do-lance]], [[geral-decisao-2026-10-30-historico-de-lances-no-i2]], [[geral-decisao-2026-10-29-sequencia-no-extrato]] e as citadas acima.

## Interpretação do agente
- I3 fica com tempo real, anti-sniping, liquidação e comprovante; I4 com a auditoria que lê a cadeia. A transação do lance lê `endsAt` com o lote travado, para o I3 só somar a prorrogação (aval do humano, 2026-10-30 08:4x).

### 🔗 Conexões
- Mapa: [[moc-orquestra]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
