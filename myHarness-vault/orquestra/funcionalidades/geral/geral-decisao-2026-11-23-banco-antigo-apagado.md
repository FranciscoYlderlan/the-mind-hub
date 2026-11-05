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
- **Alteração:** recusado só avisar. Em 2026-11-24, antes de aplicada: apaga só no caso da `0003` parando por linha sem ligação obrigatória (NOT NULL); outra falha de migração não apaga.
- **Motivo:** resposta do humano em 2026-11-23, às 17h26: "apaga"; restrição aprovada em 2026-11-24 ("Sim, só no caso da 0003"), depois de o verificador da T0b do [[integracoes-plano]] provar que apagar em qualquer falha perde dados sem relação. Ainda não há versão publicada; esse banco só existe em máquina de desenvolvimento.
- **Consequências:** ao abrir um banco anterior à `0003`, se a `0003` falha pela ligação obrigatória (NOT NULL), o núcleo apaga o arquivo e cria o banco do zero; qualquer outra falha de migração (checksum, disco cheio, banco travado) volta como erro e o banco fica intacto; vale até a primeira versão publicada, quando a regra volta ao humano [a confirmar].

### 🔗 Conexões
- Funcionalidade: [[fundacao-contexto]]
- Plano: [[fundacao-plano]], [[integracoes-plano]]
- Candidatos: [[fundacao-plano-candidatos]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
