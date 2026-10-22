---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-05
substitui: 
aliases: [Condução do treino, Listar questões antes de executar, Ensinar antes de pedir]
---
# ✅ Condução do treino: listar as questões e ensinar antes de pedir

- **Proposta (plano):** pedido direto do humano no primeiro treino da T0b.
- **Decisão:** no treino, a IA segue 3 regras.
  1. **Listar antes de executar:** antes de pedir qualquer execução, apresenta todas as questões do caso, com o que cada uma pede e a ordem.
  2. **Ensinar antes de pedir:** antes de pedir uma resposta, explica o que o humano ainda não viu (termo, ferramenta ou método), como o método das 5 lacunas do passo 1 em [[esqueleto-de-6-passos]]. Isso não é dica da solução; a regra de dicas em degraus continua.
  3. **Formato claro:** diz em palavras simples o que espera receber e mostra o formato da resposta.
- **Alteração:** nenhuma.
- **Motivo:** no primeiro treino o humano não sabia para que servia cada biblioteca nem quais perguntas fazer. Pedir resposta sem esse chão trava o treino.
- **Consequências:** [[instrucoes-do-coach-de-entrevista]] e o "Papel da IA" de [[banco-mocado-plano]] ganham essas regras.

### 🔗 Conexões
- Funcionalidade: [[banco-mocado-contexto]]
- Plano: [[banco-mocado-plano]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
