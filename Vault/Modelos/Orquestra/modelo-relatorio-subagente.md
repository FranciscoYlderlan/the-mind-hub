# Relatório de subagente

Formato fixo que todo subagente devolve ao orquestrador. Não é nota do cofre: o orquestrador transcreve o que importa para o plano, os bugs e as decisões.

```markdown
## Relatório — papel — T?
- **Resultado:** concluído | falhou | bloqueado
- **O que fiz ou achei:** até 5 linhas
- **Arquivos tocados:** 
- **Prova:** comando rodado + saída resumida
- **Critérios:** ✔/✘ cada um, com a prova (verificador)
- **Achados:** bloqueante / deve corrigir / opcional (revisor)
- **Fora do escopo que notei:** arquivos ou mudanças sem relação com a tarefa
- **Candidatos a nota:** bug | decisão | referência, uma linha cada
- **Dúvidas para o humano:** 
```

### 🔗 Conexões
- Pedido que gera este relatório: [[modelo-briefing-subagente]]
- Onde a verificação é registrada: [[modelo-plano]]
- Candidatos viram: [[modelo-bug]], [[modelo-decisao]]
- Regras: [[Manual da Orquestra]]
