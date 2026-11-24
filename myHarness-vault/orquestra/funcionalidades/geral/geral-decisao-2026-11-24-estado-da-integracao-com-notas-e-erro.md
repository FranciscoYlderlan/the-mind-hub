---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-24
substitui: 
---
# ✅ Estado da integração leva o número de notas e o erro

- **Proposta (plano):** propostas de contrato da T4 do [[integracoes-plano]]: (1) ENT-13 com `notas_indexadas` e o erro do catálogo no estado; (2) "desconectada pelo Humano" gravada no banco; (3) Log (ENT-12) aceitando caso do núcleo sem `execucao`.
- **Decisão:** entra só a (1): o ENT-13 ganha `notas_indexadas` (só Obsidian CLI) e `erro` (o ERR do catálogo com o motivo, quando o estado vem de uma falha), e o DTO da IPC os leva à tela.
- **Alteração:** recusadas a (2) e a (3): "Desconectar" segue só em memória ([[geral-decisao-2026-11-24-desconectar-sem-logout]]) e a falha de integração segue fora do Log, no registro do núcleo.
- **Motivo:** resposta do humano em 2026-11-24, às 13h, marcando só a (1).
- **Consequências:** contrato com M-46 (ENT-13); tarefa T4b no plano para o DTO, os bindings e a tela (AC-128 e motivo do ERR-53 na TEL-02).

### 🔗 Conexões
- Funcionalidade: [[integracoes-contexto]]
- Plano: [[integracoes-plano]]
- Decisões ligadas: [[geral-decisao-2026-11-24-erro-generico-por-fronteira]]
- Projeto: [[geral-contexto]]
