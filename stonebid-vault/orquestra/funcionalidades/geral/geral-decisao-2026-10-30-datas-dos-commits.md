---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-30
aliases: [Datas dos commits, Histórico de commits, Reescrita do histórico, Commit dates]
---
# ✅ Datas e formato dos commits dos repositórios

- **Proposta (plano):** humano pediu em 2026-10-30 17:44 distribuir os commits entre 26 e 30/10 no formato do Padrão de commit do `Vault`. A IA apontou que o código foi escrito em 29 e 30/10 e que a modelagem foi de 26 a 28.
- **Decisão:** humano escolheu em 2026-10-30 17:4x a opção "modelagem pelo cofre", depois de perguntar se a mudança seria detectável (é):
  1. Os dias 26 a 28 aparecem pelos commits do cofre no `the-mind-hub`.
  2. Os commits de `stonebid-api` e `stonebid-web` ficam nas datas reais (29 e 30/10); a reescrita só ajusta mensagem e autor ao Padrão de commit.
  3. A reescrita exige `--force` na `main` dos dois repositórios: só com a confirmação explícita do humano, no momento do push.
- **Alteração:** a IA propôs; o humano havia pedido datas de 26 a 30 também no código e trocou depois da resposta sobre detecção.
- **Motivo:** o GitHub guarda a criação do repositório (o `stonebid-web` é de 2026-10-28 11:37 UTC), os horários de PRs e execuções do CI/CD e os deploys, que não mudam com a reescrita.
- **Consequências:** tarefa R2 em [[revisao-e-entrega-plano]], depois das tarefas abertas.

### 🔗 Conexões
- Funcionalidade: [[revisao-e-entrega-contexto]]
- Relacionadas: [[geral-decisao-2026-10-29-padrao-de-branches]], [[passo-a-passo-do-agente]]
- Regras: [[manual-da-orquestra]]
