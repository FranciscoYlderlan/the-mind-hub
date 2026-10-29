---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-29
substitui: 
aliases: [Padrão de branches, Nome das branches, Branch naming, Git flow do Stonebid]
---
# ✅ Padrão de branches: `main`, `staging` e `tipo/ID-descricao-curta`

- **Proposta (plano):** sugestão da IA no chat de 2026-10-29: `main` para produção e `staging` para staging.
- **Decisão:** vale para o `stonebid-api` e o `stonebid-web`.
  - `main`: produção. O CD publica depois do CI verde na `main`.
  - `staging`: deploy de staging (segundo serviço no Cloud Run, pela [[geral-decisao-2026-10-29-hospedagem]]).
  - Branches de trabalho no formato `tipo/ID-descricao-curta` (texto do humano). Exemplos do humano:
    - `feat/RN-04-incremento-minimo`
    - `feat/RF-31-sala-em-tempo-real`
    - `feat/RN-10-anti-sniping`
    - `fix/RN-09-lances-simultaneos`
    - `test/T-06-auditoria-adulteracao`
    - `chore/RNF-11-docker-compose`
    - `docs/RNF-03-readme-execucao`
  - O boilerplate inicial é feito direto na `main` (humano).
- **Alteração:** o humano acrescentou o padrão das branches de trabalho e a exceção do boilerplate. A `staging` seguiu a sugestão da IA, sem objeção na resposta do humano.
- **Motivo:** escolha do humano; o ID liga cada branch ao item do contrato ([[contrato-requisitos-funcionais]], [[contrato-regras-de-negocio]], [[contrato-requisitos-nao-funcionais]], [[contrato-testes]]).
- **Consequências:**
  - `tipo` é o mesmo tipo do padrão de commit (`feat`, `fix`, `test`, `chore`, `docs`...).
  - `ID` é o identificador do contrato (RF, RN, RNF, T, AD) que a branch atende.
  - `descricao-curta` em kebab-case, sem acento, como nos exemplos.
  - Fora o boilerplate inicial, nenhum trabalho vai direto para a `main`: passa por branch de trabalho e CI verde.

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[geral-plano]]
- Projeto: [[geral-contexto]]
- Relacionadas: [[geral-decisao-2026-10-29-hospedagem]], [[geral-decisao-2026-10-28-stack-backend]], [[geral-decisao-2026-10-28-stack-frontend]], [[geral-decisao-2026-10-29-camada-mcp]], [[contrato-do-projeto]]
- Regras: [[manual-da-orquestra]]
