---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-30
aliases: [Concorrência do Cloud Run, concurrency 1000, Cloud Run concurrency]
---
# ✅ Cloud Run da API com --concurrency=1000

- **Proposta (plano):** desvio da T2b em [[sala-ao-vivo-plano]].
- **Decisão:** o `cd.yml` da API publica com `--max-instances=1 --concurrency=1000 --timeout=3600`. Aprovada pelo humano em 2026-10-30 12:44.
- **Alteração:** nenhuma.
- **Motivo:** cada stream SSE ocupa uma vaga de concorrência; com o padrão de 80, o 81º visitante ficaria na fila. 512Mi aguenta streams parados (verificador de código da T6).
- **Consequências:** subir de 1000 conexões abertas ou de uma instância exige decisão nova ([[geral-decisao-2026-10-30-tempo-real-por-sse]]).

### 🔗 Conexões
- Funcionalidade: [[sala-ao-vivo-contexto]]
- Plano: [[sala-ao-vivo-plano]]
- Decisões ligadas: [[geral-decisao-2026-10-30-tempo-real-por-sse]], [[geral-decisao-2026-10-29-hospedagem]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
