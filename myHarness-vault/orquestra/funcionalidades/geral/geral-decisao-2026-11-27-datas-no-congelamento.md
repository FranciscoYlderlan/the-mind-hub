---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-27
---
# ✅ Datas da `main` redistribuídas no congelamento do projeto

- **Proposta (plano):** pedido do humano em 2026-11-27, 12h24: congelar o projeto e distribuir os commits já feitos entre os dias definidos.
- **Decisão:** as datas dos 64 commits da `main` de `FranciscoYlderlan/MyHarness` e dos commits do `the-mind-hub` saem de um calendário único, de 2026-09-21 a 2026-11-27, só de segunda a sexta, em ordem. O total por dia varia de forma orgânica: semanas boas e fracas, poucos dias vazios, no máximo 22 commits num dia. Os horários seguem sessões de manhã, tarde e noite. Autor e committer `franciscoylderlan`, sem assinatura; árvores e mensagens iguais às de antes. Os dois repositórios foram enviados com `--force-with-lease`; o histórico anterior de cada um ficou em `backup/main-antes-das-datas`.
- **Alteração:** muda só o ponto das datas de [[geral-decisao-2026-11-23-push-e-pr-no-github]]: o fim do intervalo passou a 2026-11-27 e os commits de 24 a 27/11 também foram redistribuídos.
- **Motivo:** pedidos do humano em 2026-11-27: intervalo até 27/11, só a `main` (12h30); nada linear nem robótico (12h30 e 12h43); dissolver os dias de 30 a 100 commits do `the-mind-hub` nos outros dias, com o `the-mind-hub` também de 21/09 a 27/11 e force push autorizado nos dois (12h45).
- **Consequências:** novo topo da `main` do MyHarness: `69c9124`. Os hashes do `the-mind-hub` citados nas notas e diários deixam de bater; o backup guarda os antigos. A PR #19, a `fix/integracoes-links-externos` e as branches da onda 0 não foram tocadas e não têm mais história comum com a `main`. Retomar o projeto exige refazer essas branches sobre a `main` nova. Mapa de hashes: `git log --format='%h %aI' origin/main` contra `backup/main-antes-das-datas`.

### 🔗 Conexões
- Projeto: [[geral-contexto]]
- Decisão alterada: [[geral-decisao-2026-11-23-push-e-pr-no-github]]
- Diário: [[diario-2026-11-27]]
