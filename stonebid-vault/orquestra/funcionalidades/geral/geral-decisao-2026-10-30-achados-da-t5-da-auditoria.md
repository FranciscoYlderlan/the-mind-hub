---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-30
substitui: "[[geral-decisao-2026-10-30-auditoria-publica]] (só a linha do que a auditoria confere)"
aliases: [Achados da T5 da auditoria, Conferência da auditoria, Venda apagada passa como íntegra, Audit review findings]
---
# ✅ Achados da T5 da auditoria: o que a conferência passa a cobrir

- **Proposta (plano):** T5 de [[auditoria-publica-plano]], 2026-10-30 14:3x. O verificador de código dos PRs #14 da API e #19 do web achou 1 bloqueante, 2 itens a corrigir e 4 opcionais; a IA propôs corrigir o bloqueante e o `seq`, documentar a cadeia vazia e deixar os opcionais fora.
- **Decisão:** humano escolheu em 2026-10-30 14:54:
  1. **O que a auditoria confere**, nesta ordem: o `verifyChain` da API (numeração, hash, selo, ligação e cabeça); o comprovante (`RECEIPT_MISMATCH`); a liquidação contra o extrato (`SETTLEMENT_MISMATCH`); os valores do lote contra a cadeia. Leitura de lote, lances, comprovante e extrato numa transação `REPEATABLE READ`.
     - **Comprovante:** lote vendido tem de ter comprovante e lote não vendido não pode ter; o comprovante confere selo, lote, contagem, hash final, pseudônimo e valor do último lance.
     - **Liquidação:** lote vendido tem exatamente um DEBIT da liquidação, do licitante e no valor do último lance, e o CREDIT correspondente do leiloeiro no mesmo valor; lote não vendido, nenhum dos dois.
     - **Resultado contra os lances (bloqueante):** lote liquidado com lances e `result` diferente de `SOLD`, ou `NO_WINNER` com lances, dá `SETTLEMENT_MISMATCH`. Hoje essa troca, junto com apagar comprovante e DEBIT, passa como `INTACT` sem o `SEAL_SECRET`.
     - **Lance atual e líder:** `currentBidCents` e `leaderId` do lote têm de bater com o último lance (lote sem lances: sem líder e sem lance atual).
  2. **`seq` do motivo:** `RECEIPT_MISMATCH` e `SETTLEMENT_MISMATCH` devolvem `seq: null` (a página mostra "registro do lote", sem destacar um lance). Muda a API e o README dela; o web, o mock e o e2e já esperam `null`.
  3. **Cadeia vazia:** apagar todos os lances e zerar a cabeça (`0/null/null`) segue passando como `INTACT`. Fica só documentado no "Limite" do README da API, sem código.
  4. **Testes:** T-06 ganha os casos do resultado trocado, do lance atual adulterado, do CREDIT adulterado e, por SQL ponta a ponta, `BAD_SEAL` e `BROKEN_LINK`.
  5. **Web:** o link "Ver auditoria" some quando a sala do lote dá 404.
- **Alteração:** nenhuma; o humano aceitou a proposta da IA e incluiu os 4 opcionais (lance atual e líder, CREDIT do leiloeiro, testes `BAD_SEAL`/`BROKEN_LINK`, link na sala em 404).
- **Motivo:**
  - O README da API promete que só quem tem o banco **e** o segredo forja o histórico; o resultado trocado quebrava essa promessa só com o banco.
  - Com `seq` do último lance, comprovante adulterado aparecia na tela como lance adulterado.
- **Consequências:**
  - Um PR novo na API (conferência, `seq`, T-06, README) e um no web (link em 404). Merge do humano, `staging` avançada e nova verificação no Chrome antes da etapa 8.
  - A cadeia vazia é limite conhecido declarado; não vira código nesta entrega.

### 🔗 Conexões
- Funcionalidade: [[auditoria-publica-contexto]]
- Plano: [[auditoria-publica-plano]]
- Projeto: [[geral-contexto]]
- Substitui em parte: [[geral-decisao-2026-10-30-auditoria-publica]]
- Relacionadas: [[geral-decisao-2026-10-29-comprovante-e-hash]], [[contrato-testes]]
- Regras: [[manual-da-orquestra]]
