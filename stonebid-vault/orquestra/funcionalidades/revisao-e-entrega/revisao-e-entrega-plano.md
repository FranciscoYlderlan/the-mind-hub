---
tipo: plano
funcionalidade: revisao-e-entrega
status: proposta
criado: 2026-10-30
aliases: [Plano da entrega, Plano da etapa 8]
---
# 📋 Revisão e entrega: plano

> [!warning] Proposta da IA
> Nada aqui é decisão. Decisões ficam nas notas `-decisao-` linkadas abaixo.

## Objetivo desta rodada
READMEs e correções do checklist no ar; depois os refinamentos R1, R2 e R3. Base: [[revisao-e-entrega-contexto]].

## Decisões que este plano respeita
- [[geral-decisao-2026-10-30-datas-dos-commits]], [[geral-decisao-2026-10-30-relato-de-uso-de-ia]], [[geral-decisao-2026-10-29-modo-de-implementacao]].

## Tarefas

### E1: READMEs de entrega
- **Faz:** README da API (PR #17) e do web com as telas (PR #22).
- **Verificação:** 2026-10-30 17:1x a 17:3x. API `a4fce52`, CI verde; seção CI/CD corrigida para merge na `main` antes da `staging`. Web `dc91c32`, CI verde, 13 telas em `docs/telas/` pela API simulada; endereços de staging do [[acesso-de-teste]].
- **Estado:** concluída; merges #17 da API e #22 do web. Seção "Características de funcionamento e limites" nos PRs #18 da API e #24 do web (2026-10-30 19:04).

### E2: checklist 11.6 no ar
- **Verificação:** 2026-10-30 17:3x, Chrome, staging e produção sem login: sem bloqueante. Deve corrigir: "Cancelar" em lote com lances. Opcionais: "Fim" da sala parado após prorrogação; campo de lance pré-preenchido. Faltam busca na vitrine e estorno ([[opcionais-plano]]). Criado em staging: lote `7adc44bd-b882-4a07-ac82-44595b3cea4f`, comprovante `qEo88Ve3HxV0tawDC_Sr9A`, depósito de R$ 5.

### T11: correções do checklist (web)
- **Faz:** botão "Cancelar" só em lote cancelável; "Fim" da sala segue a prorrogação; campo de lance sem valor que estrague a digitação.
- **Toca em:** `stonebid-web`, branch `fix/RF-24-ajustes-do-checklist`.
- **Verificação:** 2026-10-30 18:0x. PR #23 do `stonebid-web` (`6bafcc6`), CI verde, 130 testes Playwright (3 novos, cada um falhava sem a correção). "Cancelar" em lote agendado ou ao vivo, antes do fim, com ou sem lances (com lances, o líder recebe estorno: [[geral-decisao-2026-10-30-estorno-no-cancelamento]]). "Fim" já tinha fonte única; faltavam os segundos, e prorrogação no mesmo minuto não aparecia: agora `formatDateTimeWithSeconds`. Campo de lance seleciona o conteúdo no foco (o mínimo continua preenchido). Merge feito. Conferido no Chrome em staging depois da reescrita (2026-10-30 19:2x): link "Ver auditoria" na sala, "Fim" com a prorrogação sem recarregar, campo de lance substitui o mínimo.

### R1: padrão de commit em todo cofre de projeto (`Vault`)
- **Faz:** Criar um novo cofre e Modelo de CLAUDE do cofre passam a levar as regras de Padrão de commit e Commitar no the-mind-hub; `cofre.py verificar` dá ERRO sem essa seção; `cofre.py sincronizar` no `stonebid-vault`.
- **Verificação:** 2026-10-30 18:3x. Seção Commits obrigatória no modelo; `cofre.py verificar` dá ERRO sem ela (provado em cópia temporária); `sincronizar` no `stonebid-vault`, 0 ERRO.

### R2: mensagens e autor dos commits
- **Faz:** [[geral-decisao-2026-10-30-datas-dos-commits]]; `--force` só com confirmação.
- **Verificação:** 2026-10-30 19:1x. `--force-with-lease` em `main` e `staging`: API `f6f07e9` (33 commits), web `955d2f0` (47). Escopo = ID do requisito (humano, 19:04); árvore idêntica, datas preservadas, 0 Co-Authored-By.

### R3: relato do uso de IA
- **Faz:** `.md` próprio com o conteúdo de [[geral-decisao-2026-10-30-relato-de-uso-de-ia]], diagrama do grafo em Mermaid e a tabela; link nos dois READMEs.
- **Verificação:** 2026-10-30 18:4x. `docs/uso-de-ia.md` no web (PR #25), link na API (PR #19); Mermaid renderiza; CI verde; merge feito.

## Próxima tarefa e a seguinte
Verificação no Chrome em staging de T11, estorno e READMEs; depois a busca na vitrine ([[opcionais-plano]]).

### 🔗 Conexões
- Funcionalidade: [[revisao-e-entrega-contexto]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
