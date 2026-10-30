---
aliases: [Passo a passo do agente, Como trabalhar no Stonebid, Push e PR pelo container, Agent runbook]
tags: [estudos/programacao]
tipo: referencia
tema: orquestracao
status: em-uso
criado: 2026-10-30
origem: humano, 2026-10-30 08:10
---
# 📚 Passo a passo do agente no Stonebid

> [!tldr] Em uma linha
> O caminho já provado para um agente novo, sem nada da conversa anterior, retomar o projeto: ler o cofre, anexar os repositórios, implementar, abrir PR, avançar a `staging`, testar no ar e commitar o cofre.

## O que é
O **manual de bordo** do projeto: a decisão [[geral-decisao-2026-10-29-modo-de-implementacao]] diz o caminho (container → GitHub → Actions → GCP/Vercel, Chrome no ar); esta nota diz os comandos e os contornos do proxy que fazem esse caminho funcionar. Pedido do humano (2026-10-30 08:10): "para que se eu vier a utilizar um agente diferente sem o conhecimento dessas informações ele consiga dar prosseguimento igual a como foi definido para esse projeto".

## 1. Início de sessão
1. Ler o cofre **só pela Obsidian CLI** (ferramentas `obsidian_read`, `obsidian_search`, `obsidian_backlinks` do servidor `obsidian-cli`, com `vault="stonebid-vault"`). Nada de `cat`, `ls`, `find`, `grep` ou `Read` nas notas: o erro se repetiu em quatro sessões de 2026-10-30. O shell do computador só escreve notas e roda o `cofre.py`.
2. `python orquestra/modelos/cofre.py status`, de dentro da pasta do cofre (sem argumento, o `status` e o `verificar` usam a pasta atual).
3. O "Onde parei" da parte mais recente do diário (regra "Diário com partes" do [[CLAUDE]]).

## 2. Repositórios
- `stonebid-api` e `stonebid-web` só existem no GitHub (`FranciscoYlderlan/...`). Não há cópia local no computador; a pasta `C:\Users\Ylderlan\Documents\Projetos\stonebid` guarda só arquivos de passagem (ex.: patches).
- **Anexar com escrita:** ferramenta `add_repo` com `owner: FranciscoYlderlan`, `repo: stonebid-api` (e `stonebid-web`) e **`access: "push"`**. Anexado só para leitura, o `git push` toma 403 do proxy mesmo com o repositório conectado (2026-10-30 07:5x e 08:1x). Na etapa de programação o acesso já é autorizado: anexar sem perguntar.
- **Clonar** um de cada vez, raso e com tempo folgado (~10 min): `git clone --depth 1 https://github.com/FranciscoYlderlan/stonebid-web /home/claude/stonebid-web`. Dois clones do mesmo repositório ao mesmo tempo dão 429.
- **Worktree por implementador:** `git worktree add /home/claude/wt-<repo>-<tarefa> -b <branch> origin/main`. Branch no formato `tipo/ID-descricao-curta` ([[geral-decisao-2026-10-29-padrao-de-branches]]). Worktrees do web em paralelo dividem a porta 4173 do Playwright (`reuseExistingServer`): usar uma porta por worktree.

## 3. Implementar e provar no container
- Lint, Prettier, tipos, testes e build rodam no container antes do push.
- `binaries.prisma.sh` é bloqueado: os testes da API rodam com `PRISMA_SCHEMA_ENGINE_BINARY` apontando para um binário falso e as migrations aplicadas por `psql`; o CI roda o fluxo real ([[geral-decisao-2026-10-29-prisma-7]]).
- `ui.shadcn.com` é bloqueado: componente novo sai do registro local gerado a partir do código-fonte do shadcn ([[geral-decisao-2026-10-28-criacao-de-componentes]]).
- O container pode reiniciar no meio: subagente em andamento se retoma do transcript.

## 4. Push e PR
1. Antes do push: `git fetch origin main` (pacote fino; de clone raso velho o push dá 413).
2. `git push -u origin <branch>`.
3. **PR pela REST**, porque o GraphQL é bloqueado e `gh pr create` falha:
   `gh api repos/FranciscoYlderlan/<repo>/pulls -f title="<mensagem do commit>" -f head=<branch> -f base=main -f body="<resumo>"`. Corrigir título ou corpo: `gh api -X PATCH repos/FranciscoYlderlan/<repo>/pulls/<n> -f body="..."`.
4. Cada implementador abre o próprio PR assim que termina, sem esperar os outros (humano, 2026-10-30 08:0x).
5. **CI:** `gh api repos/FranciscoYlderlan/<repo>/commits/<sha>/check-runs --jq '.check_runs[]|"\(.name) \(.status) \(.conclusion)"'`. Web: "Lint, formatação, tipos e build" e "Playwright (API simulada)"; API: "ci". Esperar todos `success`.
6. O **merge é do humano**. O agente não faz merge na `main`.

> [!warning] Se o push for recusado
> Commitar na worktree, gerar `git format-patch origin/main --stdout > <arquivo>.patch` e gravar o arquivo pelo bridge em `C:\Users\Ylderlan\Documents\Projetos\stonebid\patches-<tarefa>\`. Na sessão seguinte: anexar com `push`, clonar, `git checkout -b <branch>`, `git am <arquivo>.patch`, push e PR (feito assim na T5l, PRs #12 do web e #9 da API).

## 5. Depois do merge: avançar a `staging` para a `main`
### Como
1. Esperar o merge do humano no GitHub.
2. Em cada repositório que recebeu merge: `git fetch origin main && git push origin origin/main:refs/heads/staging`.
3. Conferir a saída: `<sha antigo>..<sha novo>  origin/main -> staging`. Anotar os dois sha no plano e no diário.
4. O push na `staging` dispara o `cd.yml`, que publica a API de staging no Cloud Run e o web de staging no alias `stonebid-web-staging.vercel.app` ([[geral-decisao-2026-10-29-alias-fixo-do-staging]]). O agente nunca publica direto.
5. Esperar o CD de staging e só então mandar o verificador no Chrome (seção 6).
6. **Recusado como "non-fast-forward"?** A `staging` tem commit que a `main` não tem. Parar e avisar o humano. Nunca usar `--force` sem confirmação ([[CLAUDE]], "Repositórios e acesso").

### Por quê (fatos registrados)
- **Avanço de ponteiro, não merge:** a decisão [[geral-decisao-2026-10-29-modo-de-implementacao]] manda a IA avançar a `staging` para a `main` depois do merge, "só como avanço de ponteiro". A `main` só recebe código por PR com CI verde e merge do humano ([[geral-decisao-2026-10-29-padrao-de-branches]]). A `staging` não tem PR nem trabalho próprio.
- **Por que existe a `staging`:** a MCP fica ligada só no ambiente local e em staging, desligada em produção ([[geral-decisao-2026-10-29-camada-mcp]]). Por isso a [[geral-decisao-2026-10-29-hospedagem]] criou um segundo serviço no Cloud Run, com `MCP_ENABLED=true` e banco separado.
- **Por que testar ali:** quem testa no ar é o agente. Na produção, o login pelo navegador fica com o humano, e no staging o agente entra com os usuários de teste ([[acesso-de-teste]]). Os dados de teste (lotes, depósitos) ficam em staging (humano, 2026-10-30 07:05). A verificação vale no Chrome, por ser teste verídico (humano, 2026-10-29 23:58).
- **Por que `git push` e não a API:** o proxy da sessão recusa escrita de ref por `gh api .../git/refs`, e o `git push` passa (diário de 2026-10-30, 06:48).
- **Por que só o `cd.yml`:** nenhum deploy fora do CI verde; a integração Git da Vercel fica desligada para não publicar duas vezes nem publicar com CI vermelho ([[geral-decisao-2026-10-29-vercel-sem-deploy-automatico]]).

### Motivação (humano, 2026-10-30 08:22: "é exatamente isso")
- A `staging` fica sempre no mesmo commit da `main`. O que o verificador aprova no Chrome é exatamente o que está em produção, sem histórico divergente, commit de merge extra nem conflito entre as duas branches.
- O push sem `--force` só anda para a frente: se a `staging` tiver algo fora da `main`, o git recusa sozinho, e nada se perde em silêncio.
- A ordem "merge na `main` primeiro, staging depois" é o que o projeto faz hoje. Testar na staging antes do merge na `main` exigiria outro fluxo, e mudar isso é decisão nova.

## 6. Apagar branch
- Apagar branch não passa pelo proxy: o humano apaga pelo GitHub.

## 7. Testar no ar
- Container e shell do computador não alcançam `*.run.app` nem `*.vercel.app`: todo teste no ar é pelo Claude in Chrome, com os usuários de [[acesso-de-teste]].
- Quem verifica é um subagente diferente do implementador, e só um verificador no Chrome por vez, porque o navegador é um só. Se a extensão estiver desconectada, pedir ao humano para conectar.
- Briefing pelo [[modelo-briefing-subagente]]; o relatório volta pelo [[modelo-relatorio-subagente]].

## 8. Registrar e commitar o cofre
1. Escrever pelas Etapas vitais do [[CLAUDE]] e rodar `python orquestra/modelos/cofre.py verificar .` com zero ERRO.
2. O `.git` mora em `C:\Users\Ylderlan\Documents\Projetos\the-mind-hub`: pedir acesso a essa pasta e permissão de apagar nela (arquivos `.lock`).
3. Autor só no comando, sem `git config`: `git -c user.name=franciscoylderlan -c user.email=ylderlan@nca.ufma.br commit ...`. Mensagem no formato `:emoji: tipo(escopo): Description`, sem `Co-Authored-By` nem link de sessão. Regras completas nas notas "Commitar no the-mind-hub" e "Padrão de commit" do cofre `Vault`.

### 🔗 Conexões
- Mapa: [[moc-orquestra]]
- Relacionadas: [[geral-decisao-2026-10-29-modo-de-implementacao]], [[geral-decisao-2026-10-29-padrao-de-branches]], [[acesso-de-teste]], [[geral-decisao-2026-10-29-hospedagem]]
- Regras: [[manual-da-orquestra]]
