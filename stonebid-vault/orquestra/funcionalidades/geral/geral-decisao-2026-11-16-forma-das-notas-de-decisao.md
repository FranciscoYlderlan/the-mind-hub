---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-16
substitui: 
aliases: [Forma das notas de decisão, Quando substituir uma decisão, Substituição parcial, Decision note rules]
---
# ✅ Forma das notas de decisão: Alteração, mudança e substituição

- **Proposta (plano):** nenhuma. Regras do humano (2026-10-29 13:13, [[diario-2026-10-29]]; substituição parcial em 2026-10-29 23:01, [[diario-2026-10-29-carteira-e-lotes]]), escritas até 2026-11-16 num bloco do `CLAUDE.md` e migradas para esta nota pela regra "regra só do projeto vira decisão em `funcionalidades/geral/`" (humano, 2026-11-16 09:28, K5 de [[diario-2026-11-16-regras-para-o-vault]]).
- **Decisão:**
  1. **Alteração:** mostra só o estado atual da diferença em relação à proposta da IA. A cada mudança o campo é **reescrito**, nunca acrescentado no fim; a cronologia fica no diário do dia.
  2. **Decisão ainda sem código:** mudança do humano entra na própria nota (corpo e Alteração) e ganha uma linha no diário.
  3. **Decisão já implementada:** mudança que a contradiz vira nota nova com `substitui:`; a antiga fica com `status: substituida`, intacta, descrevendo o que o código fez até ali.
  4. **Substituição parcial:** decisão já implementada em que só um ponto muda ganha nota nova só para esse ponto, com `substitui: [[antiga]] (só a linha de X)`. Na antiga, a linha do ponto é reescrita em 1 frase com link para a nota nova, e a antiga segue `aprovada`, porque o resto dela vale. Modelo: [[geral-decisao-2026-10-29-prisma-7]] e [[geral-decisao-2026-10-29-next-themes-para-o-tema]].
- **Alteração:** nenhuma.
- **Motivo:** o Alteração de [[geral-decisao-2026-10-29-camada-mcp]] guardava a api_key "só nas tools com autenticação", já desfeita pelo corpo da nota: o campo tinha virado cronologia, e o cofre não dizia quando corrigir no lugar e quando criar nota com `substitui:` (2026-10-29). A substituição parcial veio da dúvida das decisões do Prisma e do tema, que contradiziam só uma linha de decisões já implementadas.
- **Consequências:**
  - Proibido acumular datas no Alteração; quem quer a cronologia lê o diário.
  - Decisão `substituida` não se edita: é histórico.
  - O que vale para todo o projeto mora aqui; a regra geral de "uma decisão por nota" e `substitui:` está no [[manual-da-orquestra]].

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Exemplos: [[geral-decisao-2026-10-29-prisma-7]], [[geral-decisao-2026-10-29-next-themes-para-o-tema]], [[geral-decisao-2026-10-29-camada-mcp]]
- Modelo: [[modelo-decisao]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
