---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-06
substitui: 
aliases: [Progresso a cada questão, Questão pulada conta como feita, Mostrar quantas faltam]
---
# ✅ Progresso a cada questão: feitas, puladas e as que faltam

- **Proposta (plano):** pedido direto do humano no fechamento do M0 de [[trilha-sql-didatica]] (2026-11-06, 22h14).
- **Decisão:** toda vez que eu respondo ou pulo uma questão, a IA mostra o progresso antes da próxima, no fim da mensagem, depois de um `---`. O formato é este, copiado igual por toda IA (é o que foi usado no M3, em 2026-11-07):
  ```markdown
  📊 **Progresso do M3**
  `▰▰▰▰▱▱` 4 de 6
  - **Feitas:** O3.1 ✅ · O3.2 ✅ · O3.3 ✅ · O3.4 ✅
  - **Agora:** questão 5 (remessas para países de risco)
  - **Falta:** 6 (checagem)
  - **Trilha:** M0 ✅ · M1 ✅ · M2 ✅ · **M3** · M4 · M5–M8
  ```
  - **Título:** `📊 **Progresso do <módulo>**` (ou do drill ou case em curso).
  - **Barra:** em código inline, 1 bloco por questão do módulo: `▰` feita (ou pulada), `▱` falta. Depois, "N de T". Com o módulo inteiro feito, a barra fica cheia e ganha ✅ (`▰▰▰▰▰▰` 6 de 6 ✅).
  - **Linhas:** **Feitas** (pulada leva ⏭️; some quando a lista fica longa), **Agora** (a questão atual e o que falta nela, ex.: "falta 1 condição"), **Falta/Faltam** (as próximas, com a checagem) e **Trilha** (módulos feitos com ✅, o atual em negrito, os finais agrupados como "M5–M8"). Com o módulo concluído, só o título, a barra e a Trilha.
  - A tratativa do avaliador (pergunta-relâmpago, mini-aulas, variantes `MA-`) e as extras ficam fora do total; quando estão em curso, aparecem só em **Agora**.
  1. **Questão pulada conta como feita** no progresso. Eu pulo questão que não faz sentido para mim no momento ou que é simples demais.
  2. O total do módulo inclui as operações e a checagem; as extras de [[trilha-sql-didatica-extras]] não entram no total (são opcionais).
  3. Vale para todo bloco de questões do treino: módulos da trilha, drills de [[questoes-sql-de-prova]] e cases de [[questoes-tomada-de-decisao]].
  4. No [[banco-mocado-plano-registro-sql]], a pulada é registrada com autonomia `P` e fica **fora do score** (não soma nem divide).
- **Alteração:** em 2026-11-08, 05h39, o humano trocou o formato da barra (antes, bloco de código com `▓░`, 10 blocos e porcentagem) pelo usado no chat do M3: "a forma como você fez a barra de progresso nesse chat ... use a mesma barra de progresso na descrição no obsidian para que todos usem a mesma abordagem". A regra do score para a pulada é interpretação da IA a partir de "conta como feita" e de medir o que eu fiz, não o que errei.
- **Motivo:** acompanhar o andamento me mantém no ritmo; pular o que é simples ou fora de hora evita gastar energia em exercício que não ensina nada (Sensibilidade à rejeição e AuDHD, no Vault).
- **Consequências:** o esqueleto de sessão de [[trilha-sql-didatica]], o "Papel da IA" de [[banco-mocado-plano]] e as regras de [[instrucoes-do-coach-de-entrevista]] ganham a linha de progresso; a IA não insiste numa questão pulada.

### 🔗 Conexões
- Funcionalidade: [[banco-mocado-contexto]]
- Plano: [[banco-mocado-plano]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
