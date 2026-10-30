---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-29
substitui: 
aliases: [Modo de implementação, Como implementar e publicar, Fluxo container GitHub Actions, Implementation workflow]
---
# ✅ Modo de implementação: container → GitHub → Actions → GCP/Vercel, e o Chrome para consoles e testes no ar

- **Proposta (plano):** [[esqueleto-plano#T3: deploy (GCP, Vercel) e CD]]. A IA descreveu ao humano (2026-10-29 22:12) como a T3 foi implementada e testada.
- **Decisão:** é o padrão de todo o projeto daqui para frente. Os agentes seguem os passos abaixo sem precisar ler o diário.
  1. **Código:** o subagente clona o repositório do GitHub no container, implementa e roda lint, Prettier, tipos, testes e build ali mesmo. Depois faz `git push` para uma branch `tipo/ID-descricao-curta` e abre um PR, seguindo a [[geral-decisao-2026-10-29-padrao-de-branches]]. O CI do GitHub precisa ficar verde. O merge na `main` é do humano. Depois do merge, a IA avança a `staging` para a `main`, só como avanço de ponteiro.
  2. **Publicação:** quem publica é sempre o `cd.yml` do GitHub Actions, nunca o agente direto. Um push na `main` publica a API no Cloud Run e o web na Vercel, em produção. Um push na `staging` publica a API de staging, com a MCP ligada, e o web de staging no alias `stonebid-web-staging.vercel.app`, criado pela API REST da Vercel ([[geral-decisao-2026-10-29-hospedagem]]).
  3. **Consoles:** o orquestrador opera pelo Claude in Chrome o Cloud Shell do GCP, a Vercel e os secrets e variables do GitHub, que ficam no site. O humano só entra para reautenticar ou criar tokens.
  4. **Testes no ar:** o agente testa sempre, em staging e em produção, pelo Chrome. Na API, roda `fetch` no console a partir da página do web, já que o CORS libera essa origem. Na interface, testa por cliques e campos. Em staging, faz login com os usuários de [[acesso-de-teste]]. Em produção, testa só o que não pede senha, e o login em produção fica com o humano.
  5. **MCP:** a MCP se testa por cliente MCP (`claude mcp add` com a api_key), não pelo `fetch` do navegador. O CORS barra o cabeçalho da api_key.
- **Alteração:** nenhuma.
- **Motivo:** o humano pediu, em 2026-10-29 22:13: "adicione modo de implementação como descrição de como está sendo feito para os próximos agentes não precisarem olhar o diário e já ter esse esquema como o padrão adotado daqui para frente". A rede impõe esse caminho. O proxy do container libera o GitHub (git) e os registries npm. Ele recusa `*.run.app`, `*.vercel.app`, a API de Actions do GitHub, `ui.shadcn.com`, `binaries.prisma.sh` e os registries Docker. O shell do computador do humano também não alcança `*.vercel.app` nem `*.run.app`: o `curl` dá 000.
- **Consequências:** é proibido tentar `curl` dos endereços no ar a partir do container ou do shell do computador. Também é proibido cadastrar secrets pela API do GitHub ou publicar fora do `cd.yml`. Quando uma etapa precisar de rede que o container não alcança, ela vai para o Chrome. Um briefing de subagente que implementa diz que o trabalho termina no push com CI verde. O teste no ar fica com o orquestrador no Chrome, a não ser que o subagente tenha o Chrome.

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[esqueleto-plano]]
- Acesso e usuários: [[acesso-de-teste]]
- Decisões ligadas: [[geral-decisao-2026-10-29-hospedagem]], [[geral-decisao-2026-10-29-padrao-de-branches]], [[geral-decisao-2026-10-29-camada-mcp]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
