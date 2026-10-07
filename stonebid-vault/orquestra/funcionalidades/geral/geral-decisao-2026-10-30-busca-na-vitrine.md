---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-30
aliases: [Busca na vitrine, Filtro de lotes, OPC-1, RF-11, Showcase search]
---
# ✅ Busca e filtro na vitrine (OPC-1, RF-11)

- **Proposta (plano):** pesquisador da etapa 7, 2026-10-30 17:4x, em [[opcionais-plano]]. Hoje o `GET /lots` devolve três seções fixas, sem parâmetros, com até 30 encerrados.
- **Decisão:** humano aprovou em 2026-10-30 17:4x, como proposto:
  1. **Rota nova pública** `GET /lots/search` com `q` (2 a 100 caracteres), `status` (LIVE, SCHEDULED, ENDED; vários; nunca CANCELED), `minPriceCents`, `maxPriceCents`, `sort` (`ending` ou `newest`), `page` e `pageSize` (1 a 50, padrão 12). Resposta `{ serverTime, items, page, pageSize, total }`. Parâmetro inválido ou mínimo maior que o máximo: 400 `VALIDATION_ERROR` em português. O `GET /lots` não muda.
  2. **Busca** sem distinção de maiúsculas no título e nos valores dos atributos (`concat_ws` com ILIKE; `%` e `_` escapados); nada de `attributes::text`.
  3. **Preço do filtro:** o lance atual ou, sem lance, o inicial.
  4. **Estado** pelo relógio do servidor, como na vitrine; encerrados do resultado passam pelo `settleIfDue`.
  5. **Ordenação:** `ending` traz os não encerrados por fim crescente e os encerrados por último; `newest` por criação decrescente.
  6. **Sem migração** (ILIKE basta no volume do projeto).
  7. **Tela:** busca com espera de 300 ms, filtros e ordenação na URL; sem filtro, as três seções de hoje; com filtro, grade única com contagem, "Anterior/Próxima" e estado vazio, funcionando a 305 px.
  8. **MCP:** tool `lots_search`.
  9. **Testes:** E2E da rota e da tool e Playwright, registrados na rastreabilidade como "RF-11, E2E", sem T-12.
- **Alteração:** nenhuma; o humano aceitou a proposta da IA.
- **Motivo:** rota própria não muda o formato do `GET /lots` nem arrisca o RF-10.
- **Consequências:** corte em degraus pela linha 11.4 de [[contrato-processo-e-plano]]: primeiro faixa de preço e ordenação; depois o filtro só no navegador.

### 🔗 Conexões
- Funcionalidade: [[opcionais-contexto]]
- Plano: [[opcionais-plano]]
- Relacionadas: [[geral-decisao-2026-10-29-camada-mcp]], [[contrato-processo-e-plano]]
- Regras: [[manual-da-orquestra]]
