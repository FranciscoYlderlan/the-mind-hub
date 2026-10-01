---
tipo: diario
status: consolidada
criado: 2026-10-29
---
# 📓 Diário 2026-10-29: varredura de impacto

Parte do [[diario-2026-10-29]], dividida dele pelo limite de palavras. O "Onde parei" do dia fica na nota principal.

## O que foi feito
- 13:47: humano apontou que, mais de 10 vezes, um ajuste na memória deixou outras notas com o estado anterior, e pediu a correção do **processo** e o registro como bug. Registrado em [[bug-estado-anterior-preservado-apos-mudanca-2026-10-29]].
- Causa: as Etapas vitais não tinham varredura de impacto (B2 procurava só a nota a escrever; B6 propagava para uma lista fixa), o aviso "onde esta nota fala em X, vale Y" era usado como solução, e o `verificar` não conhecia estados substituídos.
- No `Vault` (original; chegou aqui por `cofre.py sincronizar`): B2 "buscar antes e varrer o impacto", B6 "reescrever no estado atual e registrar o estado antigo", regra "Uma versão só" (Manual da Orquestra v7, Modelo de CLAUDE do cofre, `CLAUDE.md` do Vault, "Atualizar a memória", checklist do Manual do Cérebro v7, `modelo-contexto`); `cofre.py verificar` com linhas `antigo:` no bloco `padroes` e ERRO para aviso de prevalência fora do histórico.
- Neste cofre: oito linhas `antigo:` no `CLAUDE.md` (prazo de 4 dias, T-01 a T-06, api_key só nas tools, restrição por IP, contrato copiado da v0.2, `App.tsx`, `useCases/`). O portão acusou 19 ERRO em 11 notas.
- Varredura: termos "4 dias", "dia 1 a 4", "T-01 a T-06", "restrição por IP", "copiada sem reinterpretar", "texto da v0.2", "Q-01 a Q-15", "Mudança M-xx", "vale a v0.3". Notas reescritas no estado atual: [[contrato-do-projeto]], [[contrato-do-projeto-mudancas]] (agora histórico de versões), [[contrato-visao-escopo-e-papeis]], [[contrato-requisitos-funcionais]], [[contrato-regras-de-negocio]], [[contrato-requisitos-nao-funcionais]], [[contrato-modelo-de-dados]], [[contrato-arquitetura]], [[contrato-riscos]], [[contrato-testes]], [[contrato-processo-e-plano]] (plano por dia da v0.2 retirado; incrementos sem coluna de dia), [[contrato-tecnologias]] (uma tabela só), [[contrato-trabalho-com-a-ia]], [[contrato-pontos-para-validar]] (Q-09 respondida), [[contrato-glossario]], [[enunciado-teste-tecnico]], [[geral-contexto]] e [[moc-orquestra]].
- `verificar`: 0 ERRO no `stonebid-vault` e no `Vault`.

## Decisões tomadas
- (nenhuma nota de decisão; regra de processo no Manual da Orquestra e no `CLAUDE.md`)

## Bugs registrados
- [[bug-estado-anterior-preservado-apos-mudanca-2026-10-29]]

## Candidatos que não viraram nota
- Nenhum.

### 🔗 Conexões
- Diário principal: [[diario-2026-10-29]]
- Mapa: [[moc-orquestra]]
- Projeto: [[geral-contexto]]
