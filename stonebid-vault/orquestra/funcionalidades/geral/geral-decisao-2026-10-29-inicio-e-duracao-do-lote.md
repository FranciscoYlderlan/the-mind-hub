---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-29
substitui: 
aliases: [Início do lote, Duração mínima, Q-07]
---
# ✅ Início do lote não pode estar no passado; duração mínima de 5 minutos (Q-07)

- **Proposta (plano):** [[carteira-e-lotes-plano#Pendente de aval antes da T1 (proposta da IA)]]
- **Decisão:** na criação do lote, o início não pode estar no passado (pela hora do servidor) e o fim fica pelo menos 5 minutos depois do início. Aprovada pelo humano em 2026-10-29 22:23.
- **Alteração:** nenhuma.
- **Motivo:** a proposta do contrato: a duração mínima dá espaço ao anti-sniping (RN-10).
- **Consequências:** o servidor recusa com mensagem clara início no passado ou duração menor que 5 minutos; a tela valida o mesmo com zod. O seed, que cria lotes ao vivo e encerrados, grava direto no banco e não passa por essa regra.

### 🔗 Conexões
- Funcionalidade: [[carteira-e-lotes-contexto]]
- Plano: [[carteira-e-lotes-plano]]
- Contrato: [[contrato-pontos-para-validar]], [[contrato-requisitos-funcionais]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
