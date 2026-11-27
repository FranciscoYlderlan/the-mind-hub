---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-27
---
# ✅ Datas da `main` redistribuídas no congelamento do projeto

- **Proposta (plano):** pedido do humano em 2026-11-27, 12h24: congelar o projeto e distribuir os commits já feitos entre os dias definidos.
- **Decisão:** a `main` de `FranciscoYlderlan/MyHarness` foi reescrita: 64 commits com datas de autor e de commit de 2026-09-21 a 2026-11-27, só de segunda a sexta, em ordem, em ritmo irregular. De 2026-10-26 em diante, os commits caem só nos 15 dias úteis com commit no `the-mind-hub`, com peso pela contagem e horário na janela real de cada dia; antes disso, rajadas e pausas no mesmo estilo. Autor e committer `franciscoylderlan`, sem assinatura. Árvores e mensagens iguais às de antes. Push com `--force-with-lease`; o topo antigo `f35574a` ficou em `backup/main-antes-das-datas`.
- **Alteração:** muda só o ponto das datas de [[geral-decisao-2026-11-23-push-e-pr-no-github]]: o fim do intervalo passou a 2026-11-27 e os commits de 24 a 27/11 também foram redistribuídos.
- **Motivo:** respostas do humano às 12h30: intervalo até 27/11, só a `main`, force push autorizado; distribuição menos linear, pelo ritmo do `the-mind-hub` (12h30); "faça para mim" (12h37).
- **Consequências:** novo topo da `main`: `275e36b`. A PR #19, a `fix/integracoes-links-externos` e as branches da onda 0 não foram tocadas e não têm mais história comum com a `main`. Retomar o projeto exige refazer essas branches sobre a `main` nova. Mapa de hashes: `git log --format='%h %aI' origin/main` contra `backup/main-antes-das-datas`.

### 🔗 Conexões
- Projeto: [[geral-contexto]]
- Decisão alterada: [[geral-decisao-2026-11-23-push-e-pr-no-github]]
- Diário: [[diario-2026-11-27]]
