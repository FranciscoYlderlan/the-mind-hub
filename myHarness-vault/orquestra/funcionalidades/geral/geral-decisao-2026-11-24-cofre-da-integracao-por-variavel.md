---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-24
substitui: 
---
# ✅ Cofre checado pela Obsidian CLI vem de variável até a etapa 5

- **Proposta (plano):** a T4 do [[integracoes-plano]] criou, sem aval, `MYHARNESS_OBSIDIAN_COFRE` (no `.env.example`: `myHarness-vault`), porque o ENT-02 (cofres do projeto) ainda não existe.
- **Decisão:** a variável fica como provisória até a etapa 5 do [[geral-plano]] (`cofres-do-projeto`, RF-33), quando o cofre passa a vir da configuração do projeto.
- **Alteração:** nenhuma.
- **Motivo:** resposta do humano em 2026-11-24, às 13h: "Aprovo até a etapa 5".
- **Consequências:** a etapa 5 retira a variável e lê o cofre de memória do projeto.

### 🔗 Conexões
- Funcionalidade: [[integracoes-contexto]]
- Plano: [[integracoes-plano]], [[geral-plano]]
- Projeto: [[geral-contexto]]
