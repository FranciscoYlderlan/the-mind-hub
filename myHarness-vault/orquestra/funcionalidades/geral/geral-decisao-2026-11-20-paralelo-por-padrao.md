---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-20
substitui: 
---
# ✅ Paralelo por padrão; série só quando o paralelo não é permitido

- **Proposta (plano):** pergunta do humano na sessão das 08h57, ao despachar a T3 do [[fundacao-plano]]: por que a T3 e a T4 não rodam juntas. O orquestrador mostrou que a série estava só no plano da fundação, não nos manuais.
- **Decisão:** toda tarefa (T) e todo grupo de tarefas (G) do projeto roda em paralelo, o máximo que der. Só vai em série quando o paralelo não é permitido: as duas tocam no mesmo arquivo (RN-14, princípio 5 do [[manual-da-orquestra]]), uma precisa de um combinado que a outra ainda não fechou (G1), há uma cadeia real de dependência (G3), um recurso exclusivo (G7) ou o teto de 5 agentes que escrevem (G11).
- **Alteração:** a série do [[fundacao-plano]] (T1 a T5) e a linha "Paralelo" da etapa 2 do [[geral-plano]] reescritas no estado atual.
- **Motivo:** resposta do humano em 2026-11-20, sessão das 08h57: "vamos alterar esse plano para só ser em série quando não for permitido em paralelo, vamos paralelizar o máximo que der para as tarefas T's e G's".
- **Consequências:** todo plano novo marca "Paralelo: sim" por padrão; cada "Paralelo: não" ou "Depende de" cita o motivo (arquivo em comum, combinado, cadeia, recurso ou teto). Tarefas paralelas ficam em branches próprias e se juntam na branch de integração ([[geral-decisao-2026-11-19-branches-e-pr-unica]]). Na fundação: T3 e T4 em paralelo; T5 em paralelo com a T4 e depois da T3, porque as duas tocam o `Cargo.toml` e o `Cargo.lock` da raiz.

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[fundacao-plano]], [[geral-plano]]
- Branches: [[geral-decisao-2026-11-19-branches-e-pr-unica]]
- Regras: [[manual-da-orquestra]], [[padroes]]
