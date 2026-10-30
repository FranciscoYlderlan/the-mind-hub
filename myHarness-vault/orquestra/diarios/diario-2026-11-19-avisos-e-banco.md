---
tipo: diario
status: em-andamento
criado: 2026-11-19
---
# 📓 Diário 2026-11-19 — erros × avisos e revisão do banco

## O que foi feito
- Sessão das 16h14 (chat novo): perguntas ao humano sobre ERR-45 a ERR-49 e os pontos 5 a 8 do relatório das 15h35. O humano separou **erro** (dado inválido) de **aviso** (limite de boa prática que recomenda e deixa o humano decidir).
- Pesquisador varreu o contrato (lido sem a Obsidian CLI, cópias no container): 47 trocas; o orquestrador acrescentou 3 (ERR-50, AC-146, invariante do ENT-14) e aplicou as 50 em `Anexos/contrato/` (M-15 a M-20). Prova: 50/50 únicas, nenhum termo do adiamento fora do histórico, 0 órfãos. Íntegra e 8 pontos `[a confirmar]` em `Anexos/trocas-contrato-2026-11-19-16h/`.

## Decisões tomadas
- Aval do humano (16h18 e 16h23), como itens do contrato: ERR-45 e ERR-46 erros de fato; ERR-47 aviso; limite do chat vira aviso ERR-48 `LIMITE_DO_CHAT_ATINGIDO`, sem adiamento, o humano segue quantas vezes quiser e cada continuação vai ao diário; ERR-49 devolve o plano ao orquestrador até 2 vezes e depois chega ao humano marcado; ENT-14 em lista fechada mais `desconhecido`, com aviso ERR-50 e o valor bruto no Log para rastrear status novo (AC-146); ENT-26 caminho absoluto.
- [[geral-decisao-2026-11-19-modo-simulado]]: núcleo simulado fica como ferramenta de desenvolvimento.
- [[geral-decisao-2026-11-19-gravacao-dupla]] (16h35): revisão do banco concluída. O modelo fica como está e o que mora nos dois lugares é gravado nos dois com o mesmo conteúdo (RN-31, ERR-51, AC-147, AC-148; M-21, 14 trocas em `Anexos/trocas-contrato-2026-11-19-16h35/`).

## Bugs registrados
- (nenhum)

## Candidatos que não viraram nota
- O `gerar.py` do pesquisador ficou defasado em relação ao `trocas.json` (o orquestrador editou o JSON depois): a fonte é o JSON.

> [!tip] Onde parei
> - **Próximo passo:** G1 em série (trait `Integracao`, esquema SQLite, contrato IPC, mascaramento, chamada ao `claude -p`).
> - **Ambiente:** pedir `Projetos\my-harness` e `Projetos\the-mind-hub` com permissão de apagar (git).
> - **Threads abertas:** 8 pontos `[a confirmar]` do relatório das 16h18; grupo B (dúvidas 13 a 30); 11 dúvidas da especificação; GitHub ainda inexistente.
> - **Dúvidas para o humano:** os 8 pontos acima; ENT-18 `registrada_em`; quando roda a conferência da gravação dupla.

### 🔗 Conexões
- Mapa: [[moc-orquestra]]
- Parte anterior do dia: [[diario-2026-11-19-contrato-e-p3]]
- Funcionalidades tocadas: [[geral-contexto]]
