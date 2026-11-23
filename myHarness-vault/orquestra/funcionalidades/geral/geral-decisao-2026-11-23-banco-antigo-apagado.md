---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-23
substitui: 
---
# ✅ Banco antigo que não abre é apagado

- **Proposta (plano):** segunda verificação da T4 do [[fundacao-plano]]: um banco da migração `0002` com linha em `tarefa`, `relatorio`, `achado` ou `escrita` não abre depois da `0003`.
- **Decisão:** o app apaga esse banco e cria um novo.
- **Alteração:** recusado só avisar.
- **Motivo:** resposta do humano em 2026-11-23, às 17h26: "apaga". Ainda não há versão publicada; esse banco só existe em máquina de desenvolvimento.
- **Consequências:** ao abrir, se a migração falha num banco anterior à `0003`, o núcleo apaga o arquivo e cria o banco do zero; vale até a primeira versão publicada, quando a regra volta ao humano [a confirmar].

### 🔗 Conexões
- Funcionalidade: [[fundacao-contexto]]
- Plano: [[fundacao-plano]]
- Candidatos: [[fundacao-plano-candidatos]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
