---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-19
substitui: 
---
# ✅ Consumo do plano vem do `rate_limit_event` (S2)

- **Proposta (plano):** [[geral-plano-arquitetura-e-stack-integracoes-e-testes]], seção 6; prova em [[geral-plano-arquitetura-e-stack-integracoes-e-testes-prototipos]] (P2).
- **Decisão:** o núcleo lê o `rate_limit_event` de toda execução do `claude -p` (`rate_limit_info.unifiedWindows.five_hour` e `.seven_day`: `utilization`, `resetsAt`, `status`; e `overageStatus`) e guarda a última leitura no SQLite (Consumo), com a hora. Sem agente rodando, o CMP-01 mostra a última leitura e a hora dela. Plano B, marcado "estimado": os registros locais de sessão da CLI, quando o evento não vier (ex.: login por chave de API). O consumo do chat (RF-17) sai do `usage` de cada resposta.
- **Alteração:** nenhuma
- **Motivo:** P2 em 2026-11-19: evento em 20 de 20 execuções, batendo com o `/usage` (71% × 72% na janela de 5 h, 11% × 12% na semana, mesmos reinícios). Aval do humano em 2026-11-19.
- **Consequências:** a janela é de 5 h (S1 respondida). Uma chamada mínima não muda o %: a leitura só anda com consumo real. O teste de RNF-04 compara com o `/usage` com tolerância de alguns pontos, pela hora da leitura.

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[geral-plano-arquitetura-e-stack-integracoes-e-testes]]
- Regras: [[manual-da-orquestra]]
