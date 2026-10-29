---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-28
substitui: 
aliases: [Teste do frontend com Playwright, Subthread de teste, Frontend E2E testing, Como validar uma funcionalidade do frontend]
---
# ✅ Toda funcionalidade do frontend é testada com Playwright por outro agente

- **Proposta (plano):** nenhuma. A definição veio direto do humano.
- **Decisão:** sempre que uma funcionalidade for criada no `stonebid-web`, uma **subthread dedicada a testes** (agente diferente do que implementou) usa o **Playwright** para validar a funcionalidade e **reporta os bugs encontrados**. Essas subthreads só testam e reportam: não corrigem e não implementam.
- **Alteração:** 2026-10-28: os testes não ficam como suíte em pasta do repositório; são executados pelas subthreads de teste.
- **Motivo:** garantir que a funcionalidade funciona de verdade no navegador, com prova independente de quem a construiu.
- **Consequências:**
  - No fluxo da [[manual-da-orquestra|Orquestra]], a subthread de teste assume o papel **Verificador**, com contexto zerado, depois do Implementador. Quem implementou nunca testa a própria funcionalidade.
  - O plano de cada funcionalidade do frontend traz, no "pronto quando", os fluxos que a subthread precisa testar.
  - O relatório da subthread traz o que foi testado, o resultado e cada bug encontrado (passos para reproduzir, esperado e obtido).
  - Bug reportado: um implementador novo corrige e uma subthread de teste nova valida de novo (máx. 2 voltas; na 3ª, sobe para o humano).
  - Funcionalidade só está pronta com a validação no Playwright sem bugs abertos.
  - Bug não trivial resolvido vira nota em `bugs/`, pelo orquestrador.
  - Não há testes unitários nem de componente no frontend: esta é a validação do frontend.

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[geral-plano]]
- Projeto: [[geral-contexto]]
- Relacionadas: [[geral-decisao-2026-10-28-stack-frontend]], [[geral-decisao-2026-10-28-estrutura-frontend]]
- Regras: [[manual-da-orquestra]]
