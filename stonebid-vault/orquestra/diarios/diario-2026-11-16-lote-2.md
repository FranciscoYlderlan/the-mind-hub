---
tipo: diario
status: consolidada
criado: 2026-11-16
---
# 📓 Diário 2026-11-16: lote 2 no Vault

Continua a parte [[diario-2026-11-16-regras-para-o-vault]] (pacote aprovado e lote 1).

## O que foi feito
- 2026-11-16, 10:05: implementador na worktree `$HOME/wt-lote2`, branch `vault/lote-2-nucleo` (de `main`), commits `897ceb1`, `52a11ed`, `87fed8a`; `verificar` do `Vault` com 0 ERRO (conferido pelo orquestrador). Sem merge.
- N01 a N04, N12, N14 e N15 atualizadas no lugar no Manual da Orquestra (princípio 8, §3, §5, §6, §7, Passagem de turno, B e C); N05 a N11, N13, N16 a N21 na nota nova "Manual da Orquestra - Núcleo comum"; G1 a G11 na nota nova "Manual da Orquestra - Agentes em paralelo" (G5 também no passo 8 do §5). "Atualizar a memória" ajustada (N12, N15). Uma linha `antigo:` nova no `padroes` do `Vault` (registrar no fim). Manual na v9, 4403 palavras.
- Trechos de software que ficaram no Manual, para o lote do perfil prático: princípio 7, §4 Papéis, §5 passos 5, 6 e 8, §8 Dial, §9 Riscos (worktree, testes), etapas A2 e A5, tabela de Modelos (`modelo-claude-do-repositorio`).
- Ficaram no estado antigo, fora da lista do lote: `Modelos/Orquestra/modelo-claude-do-repositorio.md` ("no fim do trabalho") e `Modelos/Modelo de CLAUDE do cofre.md` (só `substitui:`, sem N01 a N03).
- Interpretações do implementador, aceitas pelo humano às 10:14 (ver abaixo): N02 "ainda não aplicada" = nada construído ou estudado em cima; N08 "resumo para quem aprende"; G11 escritores = implementadores, leitores = pesquisadores e verificadores.

- 10:14, humano: "estou querendo finalizar os ajustes acho que está decidido o core do que pedi ... oq ainda falta? execute e finalizamos". Lido pelo orquestrador como aval para os lotes 3 a 6, o merge e o `sincronizar`, e como aceite das interpretações N02, N08 e G11 acima. Numeração dos lotes 3 a 6 definida pelo orquestrador: 3 perfil prático (e perfil estudo reservado), 4 padrão de software (S01 a S25), 5 lições técnicas, 6 commits.
- Lote 5: worktree `$HOME/wt-lote5`, branch `vault/lote-5-licoes`, commit `0c8049e`, `verificar` com 0 ERRO. Nove notas de conceito no `Vault` (L3 e L7 divididas em duas), na seção "Lições de projeto" do MOC Programação; origem no `stonebid-vault`, nome do projeto só na `origem`. Pendente: links de volta a partir das lições que já existiam; o motivo de "evento depois do COMMIT" na L2 é interpretação do implementador, aprovada pelo humano às 11:27 ("tudo ok").

- Lotes 2 (fim), 3, 4 e 6 na branch `vault/lote-2-nucleo`: `e0a7db0` (modelos de CLAUDE com N01 a N03 e "assim que chega"), `f6439d1` (notas "Manual da Orquestra - Perfil projeto prático", com P01 a P16 e os trechos de software movidos, e "Manual da Orquestra - Perfil estudo", reservada; Manual neutro, v10), `f984041` ("Padrão de projeto de software", S01 a S25, com S04 a S08 e S24 só com deploy; "Referência de arquitetura e stack"; passo 4 de "Criar um novo cofre"), `0e74b44` e `422eced` (seção Commits e bloco `projeto:escopos` nos dois modelos de CLAUDE, C2 e C3; o `cofre.py` aceita o bloco e o exige). `verificar` com 0 ERRO em cada lote.
- Interpretações do implementador, aprovadas pelo humano às 11:27 ("tudo ok"): bloco de escopos no `CLAUDE.md` contra a K5; "Estudo só ganha cofre com plano"; S24 entre as regras de deploy; N15 alinhada à C2 (commit a cada registro concluído); teto do modelo de CLAUDE em 2500 (lote 1), não 1000.
- 10:3x: merge na `main` por fast-forward (lote 5 rebaseado em cima: `e8d333a`); `verificar` do `Vault` com 0 ERRO; `cofre.py sincronizar stonebid-vault` atualizou o Manual, o modelo do repositório e o `CLAUDE.md`, com 0 ERRO. O `PrepBTG-vault` ficou sem sincronizar: tem mudanças do humano sem commit, inclusive no `cofre.py`.

> [!tip] Onde parei
> - **Feito:** pacote "regras do Stonebid para o Vault" completo (lotes 1 a 6) e na `main`; `stonebid-vault` sincronizado.
> - **Próximo passo:** sincronizar o `PrepBTG-vault` depois que o humano commitar as mudanças dele.
> - **Threads abertas:** branches `vault/lote-2-nucleo` e `vault/lote-5-licoes` já mescladas (apagar só com confirmação); links de volta das lições antigas para as novas.
> - **Pendente com o humano:** commits do `stonebid-vault` (diários de hoje, `CLAUDE.md` e kit sincronizados, `.obsidian/graph.json`) e do `PrepBTG-vault`; `__pycache__` no `.gitignore`.
> - **Dúvidas para o humano:** nenhuma (interpretações aprovadas às 11:27).

### 🔗 Conexões
- Parte anterior: [[diario-2026-11-16-regras-para-o-vault]]
- Diário do dia: [[diario-2026-11-16]]
- Mapa: [[moc-orquestra]]
- Projeto: [[geral-contexto]]
