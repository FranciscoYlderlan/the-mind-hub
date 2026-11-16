---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-16
substitui: 
aliases: [Repositórios e acesso, Onde ficam os repositórios, Acesso aos repositórios, Repository access]
---
# ✅ Repositórios e acesso: onde fica o código e o que o agente pode sem perguntar

- **Proposta (plano):** nenhuma. Regras do humano (links, pasta e acesso: 2026-10-29 10:31, [[diario-2026-10-29]]; modo de implementação: 2026-10-29 22:13; passo a passo: 2026-10-30 08:10; aplicação offline: 2026-11-13, [[diario-2026-11-13]]), escritas até 2026-11-16 num bloco do `CLAUDE.md` e migradas para esta nota pela regra "regra só do projeto vira decisão em `funcionalidades/geral/`" (humano, 2026-11-16 09:28, K5 de [[diario-2026-11-16-regras-para-o-vault]]).
- **Decisão:**

| O quê | Onde |
|---|---|
| Backend `stonebid-api` | https://github.com/FranciscoYlderlan/stonebid-api |
| Frontend `stonebid-web` | https://github.com/FranciscoYlderlan/stonebid-web |
| Pasta do projeto no computador | `C:\Users\Ylderlan\Documents\Projetos\stonebid` |

  - **Aplicação offline:** o Stonebid ficou no ar de 2026-10-29 a 2026-11-13 e está offline desde que a conta de faturamento do GCP foi encerrada ([[diario-2026-11-13]]). Só o ambiente local funciona; endereços antigos e usuários de teste em [[acesso-de-teste]].
  - **Passo a passo do agente:** comandos já provados (anexar repositório com escrita, push, PR, CI, `staging`, Chrome, commit do cofre) em [[passo-a-passo-do-agente]]. Agente novo lê essa nota antes de mexer nos repositórios.
  - **Modo de implementação (padrão):** código no container → `git push` e PR no GitHub → CI verde → merge do humano → `cd.yml` do GitHub Actions publica no GCP e na Vercel. Consoles (Cloud Shell, Vercel, secrets do GitHub) e todo teste no ar, em staging e em produção, são feitos pelo agente no Chrome. O container e o shell do computador não alcançam `*.run.app` nem `*.vercel.app`. Detalhes em [[geral-decisao-2026-10-29-modo-de-implementacao]].
  - **Acesso na etapa de programação:** autorizado pelo humano para aquela etapa em `stonebid-api` ou `stonebid-web` (pasta do projeto e repositório no GitHub). Peça o acesso à pasta ou anexe o repositório direto, sem perguntar antes se pode.
  - **Fora da etapa de programação** (planejamento, cofre, pesquisa): pedir antes de acessar os repositórios.
  - Apagar arquivos, forçar push ou mexer na branch principal fora do fluxo de CI/CD sempre pede confirmação.
- **Alteração:** nenhuma.
- **Motivo:** o humano informou os links e a pasta e liberou o acesso nas etapas de programação para não ser perguntado a cada tarefa; o modo de implementação e o passo a passo foram pedidos para que um agente novo siga igual sem ler os diários.
- **Consequências:**
  - Briefing de implementador cita esta nota e o [[passo-a-passo-do-agente]].
  - `--force`, apagar arquivos ou mudar a `main` fora do CI/CD sem confirmação é erro de processo.

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Modo de implementação: [[geral-decisao-2026-10-29-modo-de-implementacao]]
- Comandos: [[passo-a-passo-do-agente]]
- Acesso de teste: [[acesso-de-teste]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
