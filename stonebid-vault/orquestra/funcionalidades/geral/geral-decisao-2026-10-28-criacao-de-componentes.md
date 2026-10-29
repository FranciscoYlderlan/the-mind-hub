---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-28
substitui: 
aliases: [Como criar componentes, Regras de componentes, shadcn first, Component guidelines]
---
# ✅ Criação de componentes no frontend

- **Proposta (plano):** nenhuma. A definição veio direto do humano, como base do projeto.
- **Decisão:** componente novo no `stonebid-web` passa por este roteiro, nesta ordem:
  1. **Já existe?** Consultar o [[registro-de-componentes]] neste cofre. Existindo, reutilizar.
  2. **Vai ser reutilizado?** Avaliar se o componente pode ser usado em outras telas.
  3. **Está no shadcn/ui?** Checar o catálogo e o comando de instalação, e instalar pela CLI (`npx shadcn@latest add <componente>`). Evitar criar do zero.
  4. **Só então criar**, se nada acima resolver: em `components/common/` quando compartilhado, em `features/<feature>/components/` quando é do domínio.
  5. **Registrar** o componente no [[registro-de-componentes]].
- **Regras de escrita:**
  - Evitar elementos HTML nativos quando o shadcn/ui tem equivalente pronto (`Button`, `Input`, `Select`, `Dialog`...).
  - Nada de telas ou componentes muito grandes. Código limpo, sem repetição; o que pede refatoração vira componentes menores.
  - Para padrões que se repetem, usar templates de estruturação, evitando reescrita de código e mutações desnecessárias.
  - Componente próprio nunca vai para `components/ui/` (reservado ao shadcn).
- **Alteração:** nenhuma.
- **Motivo:** evitar duplicação e retrabalho, aproveitando o que o shadcn/ui já entrega.
- **Consequências:**
  - Toda tarefa de frontend que cria ou instala componente termina com o registro atualizado. Como só o orquestrador escreve no cofre, o implementador lista os componentes novos no relatório e o orquestrador registra.
  - O briefing de implementador do frontend aponta para o [[registro-de-componentes]] e para esta nota.
  - Estrutura das pastas: [[geral-decisao-2026-10-28-estrutura-frontend]].

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[geral-plano]]
- Projeto: [[geral-contexto]]
- Relacionadas: [[registro-de-componentes]], [[geral-decisao-2026-10-28-stack-frontend]]
- Regras: [[manual-da-orquestra]]
