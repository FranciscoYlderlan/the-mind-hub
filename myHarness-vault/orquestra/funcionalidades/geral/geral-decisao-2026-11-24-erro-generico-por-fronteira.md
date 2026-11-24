---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-24
substitui: 
---
# ✅ Erro genérico por fronteira; erro próprio só quando necessário

- **Proposta (plano):** pedido do humano em 2026-11-24, às 07h45, ao aprovar "cofre não encontrado" no ERR-53: generalizar, com a descrição do erro no log, em vez de criar erro e teste próprios para cada caso.
- **Decisão:**
  1. Cada fronteira tem um erro genérico que carrega o motivo real, mascarado (RN-04), na mensagem e no Log (ENT-12): ERR-53 `INTEGRACAO_FALHA_INESPERADA` para as integrações e ERR-55 `FALHA_INTERNA` para o núcleo.
  2. Erro próprio novo só quando: muda o que o Humano faz (outra ação ou botão, como "Abrir Obsidian" ou "Fazer login"); uma regra do contrato exige distinguir o caso (ex.: ERR-14, push proibido); ou o núcleo decide diferente (bloqueia, repete sozinho).
  3. Testes: um por erro próprio; para o genérico, um teste só que prova que qualquer falha não catalogada vira o genérico com o motivo mascarado no Log, sem teste por mensagem.
  4. Os erros próprios já criados ficam.
- **Alteração:** nenhuma.
- **Motivo:** respostas do humano em 2026-11-24: pedido às 07h45 e "Aprovo, só neste projeto" à proposta.
- **Consequências:** contrato com M-44 (ERR-53 como genérico das integrações, com "cofre não encontrado" entre os exemplos) e M-45 (motivo do ERR-04); a regra vale para os agentes que propõem erros novos. Só neste projeto: não vai para o `Vault`.

### 🔗 Conexões
- Funcionalidade: [[integracoes-contexto]]
- Plano: [[integracoes-plano]]
- Decisões ligadas: [[geral-decisao-2026-11-23-falha-interna]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
