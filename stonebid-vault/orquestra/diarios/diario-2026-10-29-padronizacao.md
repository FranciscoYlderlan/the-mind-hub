---
tipo: diario
status: consolidada
criado: 2026-10-29
---
# 📓 Diário 2026-10-29: padronização

Parte do [[diario-2026-10-29]], dividida dele pelo limite de palavras. O "Onde parei" do dia fica na nota principal.

## O que foi feito
- 12:21: humano apontou despadronizações (grafia do nome, numeração do enunciado, `useDebounce` contra o kebab-case, notas `contrato-*` acima de ~350 palavras) e pediu a correção na causa: as regras ficam na porta de entrada. Feito:
  - No `Vault` (original, chega por `cofre.py sincronizar`): seção Padronização e bloco `padroes` no Modelo de CLAUDE do cofre; Manual da Orquestra v6 (§7 e tabela de falhas); Manual do Cérebro v6 (limite de tamanho em cofre de projeto); Guia do cofre para IA; `cofre.py verificar` passa a dar ERRO em termo fora do bloco `padroes`, em nota acima do `limite-palavras` e em `CLAUDE.md` de projeto sem Padronização.
  - Neste cofre: Padronização no `CLAUDE.md` com grafia `Stonebid` (a do [[contrato-glossario]]), enunciado citado como E1 a E6 ([[enunciado-teste-tecnico]]), origem do deploy só no E1, exceção dos hooks do React (ajustada às 12:35, abaixo) em [[geral-decisao-2026-10-28-estrutura-frontend]] e limite de **2073 palavras** (tamanho de [[contrato-do-projeto]], a maior nota registrada). O limite de ~350 palavras não vale neste cofre.
  - Antes da regra, o `verificar` dava 0 ERRO com tudo isso no cofre; com a regra, deu 21 ERRO, corrigidos nas notas.

## Decisões tomadas
- (nenhuma nota de decisão; regras no `CLAUDE.md`)

## Bugs registrados
- (nenhum)

## Candidatos que não viraram nota
- Nenhum.

### 🔗 Conexões
- Diário principal: [[diario-2026-10-29]]
- Mapa: [[moc-orquestra]]
- Projeto: [[geral-contexto]]
