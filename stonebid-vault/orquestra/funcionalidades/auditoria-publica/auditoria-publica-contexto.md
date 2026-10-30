---
tipo: contexto
funcionalidade: auditoria-publica
status: concluida
etapa: 6
criado: 2026-10-30
aliases: [Auditoria pública, I4, Auditoria do lote, Public audit]
---
# 🧭 Auditoria pública (I4)

> [!tldr] Em uma linha
> Qualquer pessoa, sem login, abre o histórico completo de um lote e vê o veredito ÍNTEGRO ou ADULTERADO, recalculado a cada acesso, com o primeiro registro inconsistente quando houver.

## Objetivo e motivação
Etapa 6 do [[geral-plano]]. Pela linha I4 de [[contrato-processo-e-plano]] (11.3): RF-60, RF-61, RN-14 e RN-15. Pronto quando o T-06 detecta as adulterações e a página está no ar.

## Fatos que eu informei
- Pontos do plano aprovados em 2026-10-30 13:2x: [[geral-decisao-2026-10-30-auditoria-publica]] e [[geral-decisao-2026-10-30-adulterado-provado-no-ci]].
- Achados da T5 (2026-10-30 14:54): o que a conferência passa a cobrir, em [[geral-decisao-2026-10-30-achados-da-t5-da-auditoria]].
- Retomada (2026-10-30 15:21): o limite de crédito da sessão acaba antes das 16:00 e reseta entre 16:30 e 16:40; o trabalho continua dali, passando da entrega das 16:00, "nada grave".
- Base: [[geral-decisao-2026-10-29-comprovante-e-hash]] (o que a auditoria confere) e [[geral-decisao-2026-10-30-caminho-da-auditoria]] (rota no web).

## O que já foi feito
- 2026-10-30 13:2x: plano aprovado; implementadores da API (T2) e do web (T3) despachados em paralelo. 13:25: merge do PR #14 da API e `staging` em `3901df8`. 13:3x: PR #19 do web em correção (import entre features). 14:0x: merge do #19 e `staging` do web em `972b7ae`. 14:5x: T5 no Chrome 5 de 5 ✔; revisão de código achou o resultado trocado sem detecção; correções T6 (API) e T7 (web) planejadas. 15:1x: T6 no PR #15 da API (`9f6b500`) e T7 no PR #20 do web (`9365f7e`), CI verde nos dois. 15:19: merge dos dois. 17:0x: T8 verificada (código 8 de 8 e Chrome 5 de 5). 17:2x: T9 (PR #16 da API) e T10 (PR #21 do web), CI verde, aguardando merge.

## Tempo disponível
Entrega em 2026-10-30 16:00 ([[geral-decisao-2026-10-30-prazo-16h]]). Etapa concluída em 2026-10-30; seguem a etapa 7 ([[opcionais-contexto]]) e a 8 ([[revisao-e-entrega-contexto]]).

## Dial e modelo de IA
- Dial: o do [[geral-contexto]].
- Modelo de IA: o da sessão.

## Áreas sensíveis
- Cadeia de hashes e selos: [[geral-decisao-2026-10-29-comprovante-e-hash]], [[lances-contexto]].
- Privacidade nas respostas públicas (RN-15): [[geral-decisao-2026-10-30-pseudonimo-com-6-digitos]].

## Mapa
- Plano: [[auditoria-publica-plano]]
- Decisões: as listadas em "Fatos que eu informei".

## Interpretação do agente
- O `verifyChain` da API já cobria numeração, hash, selo, ligação e cabeça desde o I2; o I4 amplia com comprovante e extrato e expõe o resultado.

### 🔗 Conexões
- Mapa: [[moc-orquestra]]
- Projeto: [[geral-contexto]]
- Etapa anterior: [[sala-ao-vivo-contexto]]
- Regras: [[manual-da-orquestra]]
