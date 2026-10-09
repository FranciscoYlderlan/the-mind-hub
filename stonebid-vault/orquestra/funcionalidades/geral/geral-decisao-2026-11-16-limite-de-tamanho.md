---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-16
substitui: 
aliases: [Limite de tamanho das notas, Limite de 2073 palavras, limite-palavras, Note size limit]
---
# ✅ Limite de tamanho: 2073 palavras por nota

- **Proposta (plano):** nenhuma. Regra do humano (2026-10-29 12:21, [[diario-2026-10-29-padronizacao]]; notas `contrato-*` só no texto vigente pelo [[bug-estado-anterior-preservado-apos-mudanca-2026-10-29]]), escrita até 2026-11-16 num bloco do `CLAUDE.md` e migrada para esta nota pela regra "regra só do projeto vira decisão em `funcionalidades/geral/`" (humano, 2026-11-16 09:28, K5 de [[diario-2026-11-16-regras-para-o-vault]]).
- **Decisão:** o limite de tamanho deste cofre é **2073 palavras**, o tamanho de [[contrato-do-projeto]], a maior nota registrada em 2026-10-29. Vale também para as notas `contrato-*`, que trazem só o texto vigente do contrato (o histórico de versões fica em [[contrato-do-projeto-mudancas]]). É o `limite-palavras` do [[padroes]].
- **Alteração:** nenhuma.
- **Motivo:** o limite de ~350 palavras do Manual do Cérebro não cabe em notas de projeto, e sem limite as notas cresciam sem divisão. O humano fixou o limite na maior nota que existia quando a regra nasceu. O limite de cofre novo (2000) não muda este cofre, que nasceu antes (humano, 2026-11-16, K6 de [[diario-2026-11-16-regras-para-o-vault]]).
- **Consequências:**
  - Nota acima de 2073 palavras dá ERRO no `cofre.py verificar`: divida em nota nova `<original>-<assunto>`, com 1 frase + link na original e links nos dois sentidos.
  - Manuais e modelos copiados do `Vault` ficam fora da conta; o `CLAUDE.md` tem teto próprio, de 2500.

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Padrões checados pelo `verificar`: [[padroes]]
- Nota que fixou o número: [[contrato-do-projeto]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
