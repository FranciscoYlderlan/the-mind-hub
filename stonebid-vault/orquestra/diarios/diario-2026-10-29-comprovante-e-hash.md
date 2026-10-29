---
tipo: diario
status: consolidada
criado: 2026-10-29
---
# 📓 Diário 2026-10-29: comprovante e hash

Parte do [[diario-2026-10-29]], dividida dele pelo limite de palavras. O "Onde parei" do dia fica na nota principal.

## O que foi feito
- 13:19–13:22: humano apontou duas divergências: o que o comprovante guarda ([[contrato-modelo-de-dados]] × item 4 da 8.1 de [[contrato-arquitetura]] × RF-51 e Q-09) e o Lance sem o próprio hash, que a auditoria diz recalcular. A IA achou um terceiro problema: contagem e hash final sem selo deixam passar o "último lance apagado" do T-06. Proposta (hash guardado no lance, cabeça da cadeia com selo no lote, comprovante como fotografia selada, etiquetas distintas por tipo de selo) explicada também em linguagem leiga e aprovada. Nova decisão [[geral-decisao-2026-10-29-comprovante-e-hash]] (M-12), propagada em [[contrato-do-projeto-mudancas]], [[contrato-do-projeto]], avisos M-12 em [[contrato-modelo-de-dados]], [[contrato-arquitetura]], [[contrato-requisitos-funcionais]] e [[contrato-pontos-para-validar]], [[geral-contexto]] e [[moc-orquestra]]. Erro de processo: no começo da análise (12:25) quatro notas foram lidas por shell (`cat`/`grep`) com a CLI funcionando; o resto da sessão leu pela MCP `obsidian-cli`.

## Decisões tomadas
- [[geral-decisao-2026-10-29-comprovante-e-hash]]

## Bugs registrados
- (nenhum)

## Candidatos que não viraram nota
- Nenhum.

### 🔗 Conexões
- Diário principal: [[diario-2026-10-29]]
- Mapa: [[moc-orquestra]]
- Projeto: [[geral-contexto]]
