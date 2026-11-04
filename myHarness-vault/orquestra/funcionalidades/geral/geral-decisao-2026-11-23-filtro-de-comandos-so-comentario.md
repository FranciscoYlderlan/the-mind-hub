---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-23
substitui: 
---
# ✅ Filtro de comandos no banco: só corrigir o comentário

- **Proposta (plano):** segunda verificação da T4 do [[fundacao-plano]]: o filtro de `comandos` no banco deixa passar `git -C x push`, `"git" push`, `git --no-pager push` e afins, ao contrário do comentário da `0003`.
- **Decisão:** o filtro fica como está (melhor esforço); corrige-se o comentário, que passa a dizer que a barreira real é o portão (RN-27).
- **Alteração:** recusado endurecer o filtro.
- **Motivo:** resposta do humano em 2026-11-23, às 17h26: "corrige".
- **Consequências:** nenhum teste pode tratar o filtro do banco como barreira; a negação de push, merge e push --force é do portão (ERR-14, RN-27).

### 🔗 Conexões
- Funcionalidade: [[fundacao-contexto]]
- Plano: [[fundacao-plano]]
- Candidatos: [[fundacao-plano-candidatos]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
