---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-19
substitui: 
---
# ✅ Uma branch por tarefa e PR única por processo

- **Proposta (plano):** pergunta do orquestrador na sessão das 16h51, ao despachar a T1 do [[fundacao-plano]]: merge de cada tarefa na `main` ou um merge só no fim do G1.
- **Decisão:** depende do contexto. Tarefas que fazem parte do mesmo processo (ex.: T1 a T5 do G1) ficam cada uma na sua branch (`tipo/ID-descricao`, [[geral-plano-arquitetura-e-stack-integracoes-e-testes]]) e depois são juntadas numa branch de integração local, com os testes rodando localmente (`pnpm check`); sem acesso ao GitHub, não há PR, e o merge na `main` é local ([[geral-decisao-2026-11-20-tudo-local-sem-github]]).
- **Alteração:** nenhuma
- **Motivo:** resposta do humano em 2026-11-19, sessão das 16h51: "se fizerem parte do mesmo processo pode criar as branches separadas depois juntá-las em uma única pr mas lembre-se que ao juntar localmente para a pr é necessário rodar os testes localmente".
- **Consequências:** o merge na `main` continua pedindo confirmação (branch principal). Sem acesso ao GitHub, nenhuma PR é aberta: a branch de integração local, com `pnpm check` local, é o que o humano revisa antes do merge local na `main` ([[geral-decisao-2026-11-20-tudo-local-sem-github]]); tarefas de processos diferentes seguem em branches de integração separadas.

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[fundacao-plano]]
- Ponto alterado: [[geral-decisao-2026-11-20-tudo-local-sem-github]]
- Regras: [[manual-da-orquestra]], [[padroes]]
