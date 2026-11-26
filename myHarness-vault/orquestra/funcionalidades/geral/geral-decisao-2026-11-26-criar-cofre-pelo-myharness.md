---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-26
substitui: 
---
# ✅ Criar cofre novo pelo MyHarness

- **Proposta (plano):** pedido do humano em 2026-11-26 07h33: hoje ele cria cofre seguindo Criar um novo cofre (no Vault), que roda o `cofre.py criar`; quer a mesma coisa como opção no MyHarness.
- **Decisão:** o MyHarness tem a opção "Criar novo cofre": o humano dá o nome e o app faz exatamente o que o roteiro faz hoje, rodando o `cofre.py criar` do `Vault` (pastas, modelos, manuais, `CLAUDE.md` do Modelo de CLAUDE do cofre, registro no `README.md` do `the-mind-hub`), e termina com o `cofre.py verificar` com zero ERRO.
- **Alteração:** nenhuma.
- **Motivo:** pedido do humano em 2026-11-26, sessão das 07h33.
- **Consequências:**
  - O app não reimplementa o roteiro: chama o `cofre.py` do `Vault`, para a regra continuar num lugar só.
  - Entra na etapa 5 (vários cofres), junto da `cofres-do-projeto` (RF-33): o cofre criado pode ser ligado ao projeto como memória ou consulta.
  - Passos que hoje ficam fora do `cofre.py` (o bloco nas instruções do projeto do claude.ai, o commit do cofre novo): o app mostra o que falta ou faz [a confirmar].
  - Contrato (RF novo, UC, CMP, ERR do nome inválido ou repetido, AC) preenchido no início da etapa 5, com aval.

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[geral-plano]]
- Regras: [[manual-da-orquestra]]
