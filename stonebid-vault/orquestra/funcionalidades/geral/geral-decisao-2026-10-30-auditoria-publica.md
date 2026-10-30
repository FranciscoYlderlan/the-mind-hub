---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-30
substitui: 
aliases: [Auditoria pública, Veredito da auditoria, Rota da auditoria na API, Public audit]
---
# ✅ Auditoria pública: rota, veredito, T-06 e página (I4)

- **Proposta (plano):** pontos 1 a 5 de [[auditoria-publica-plano]], 2026-10-30 13:1x.
- **Decisão:** humano aprovou os 5 pontos como propostos em 2026-10-30 13:2x.
  1. **API:** `GET /lots/:id/audit` público (sem login), recalculado a cada acesso e nunca guardado (RF-61), com `Cache-Control: no-store`. Lote encerrado e ainda não liquidado é liquidado na leitura, como no `GET /lots/:id`. Devolve o lote público, os lances (ordem, pseudônimo, valor, horário, `prevHash`, `hash`), o veredito `INTACT` ou `TAMPERED` e o primeiro registro inconsistente com o motivo.
  2. **O que confere:** a lista vigente está em [[geral-decisao-2026-10-30-achados-da-t5-da-auditoria]] (o que o código fez até ali: `verifyChain`, comprovante, DEBIT da liquidação e leitura em `REPEATABLE READ`).
  3. **T-06:** os 5 casos de [[contrato-testes]] (íntegro, valor editado, lance apagado no meio, lance inserido, último lance apagado), com o lote ao vivo e depois da liquidação, por SQL direto no banco de teste. O `REVOKE UPDATE, DELETE` opcional fica fora e só é citado no README.
  4. **MCP:** tool `lots_audit`, com o mesmo corpo da rota ([[geral-decisao-2026-10-29-camada-mcp]]).
  5. **Web:** página `/lots/$id/audit` em `_public` ([[geral-decisao-2026-10-30-caminho-da-auditoria]]) com o selo ÍNTEGRO ou ADULTERADO, a linha inconsistente destacada com o motivo em português, a tabela do histórico, o botão "Verificar de novo" e o link "Ver auditoria" na sala.
- **Alteração:** a conferência do comprovante e do extrato ficou mais rígida que a proposta (que conferia o comprovante só "se existir"): exige comprovante em lote vendido e proíbe em lote não vendido, exige exatamente um DEBIT da liquidação, e a leitura é feita em `REPEATABLE READ`. Proposta do implementador da T2, aceita pelo humano em 2026-10-30 13:4x, porque apagar o comprovante passaria sem ser detectado.
- **Motivo:**
  - O `verifyChain` já existia desde o I2; faltava expor o resultado, conferir comprovante e extrato e provar as adulterações no banco real.
  - Recalcular a cada acesso, sem cache, é o que o RF-61 pede; liquidar na leitura deixa o resultado igual ao da sala.
- **Consequências:**
  - O link "auditoria" do comprovante deixa de dar 404.
  - Nenhum dado pessoal na resposta nem na página (RN-15, T-09): só pseudônimo.
  - O ADULTERADO não aparece no ar: [[geral-decisao-2026-10-30-adulterado-provado-no-ci]].

### 🔗 Conexões
- Funcionalidade: [[auditoria-publica-contexto]]
- Plano: [[auditoria-publica-plano]]
- Projeto: [[geral-contexto]]
- Substituída em parte por: [[geral-decisao-2026-10-30-achados-da-t5-da-auditoria]]
- Relacionadas: [[geral-decisao-2026-10-29-comprovante-e-hash]], [[geral-decisao-2026-10-30-caminho-da-auditoria]], [[contrato-testes]]
- Regras: [[manual-da-orquestra]]
