---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-29
substitui: 
aliases: [Camada MCP, Servidor MCP do backend, MCP layer, Testar o fluxo pela Claude]
---
# ✅ Camada MCP no backend, atualizada a cada feature e rota

- **Proposta (plano):** proposta da IA no chat de 2026-10-29: uma camada MCP no `stonebid-api` que expõe as rotas como tools, para testar o fluxo de trabalho pela Claude.
- **Decisão:** o `stonebid-api` ganha uma camada MCP em `src/infra/mcp/`, ao lado de `infra/http/`, que expõe as rotas da API como tools. **Sempre que uma feature e uma rota forem criadas, a camada MCP é atualizada** (texto do humano: "sempre que uma feature e uma rota forem criadas deve ser atualizada a mcp").
- **Uso principal (humano, 2026-10-29):** conectar a MCP no Claude como conector, para o Claude acessar as features diretamente da máquina virtual dele (sessão na nuvem), sem passar pelo frontend.
- **Como o Claude se conecta (docs da Anthropic, consultadas em 2026-10-29):**
  - O conector personalizado do Claude chama o servidor a partir da nuvem da Anthropic (saída pela faixa `160.79.104.0/21`), não da máquina do humano. Por isso o uso principal depende do `/mcp` de **staging**, com URL pública e HTTPS; o `localhost` da máquina do humano não é alcançável por esse caminho.
  - Autenticação que o conector aceita: OAuth, cabeçalho fixo (api key; beta, só para algumas organizações) ou nenhuma. O conector usa o **cabeçalho fixo com a api_key** (ver "Acesso ao `/mcp`"); o login nas rotas protegidas é feito dentro do servidor, com o usuário de teste.
  - Na máquina do humano, o Claude Code local se conecta direto em `http://localhost:3333/mcp`, também com a api_key.
- **Testes pela URL publicada (humano, 2026-10-29):** os testes do fluxo pela MCP são feitos na URL publicada de staging, depois do deploy. O `localhost` fica para o desenvolvimento.
- **Estrutura proposta:**

```
src/infra/mcp/
├── plugin.ts       # Plugin Fastify: monta /mcp, ligado só com MCP_ENABLED, exige a api_key
├── session.ts      # Login com o usuário de teste do seed e sessão usada nas rotas protegidas
├── server.ts       # Cria o servidor MCP e registra as tools
├── call-route.ts   # Helper: executa a rota via app.inject() e devolve o resultado
└── tools/          # Um arquivo por feature, uma tool por rota
```

- **Como funciona:**
  - **As tools chamam as rotas, não os casos de uso (humano, 2026-10-29).** Uma tool por rota, executada com `app.inject()` no mesmo processo: passa por validação, auth, tratamento de erro e serialização reais.
  - O `inputSchema` da tool reaproveita o schema zod da rota; nenhuma regra duplicada.
  - Transporte Streamable HTTP em `/mcp`, no mesmo Fastify. Local: Claude Code com `claude mcp add --transport http stonebid http://localhost:3333/mcp`; app do Claude: URL pública do ambiente de staging.
  - **Ambientes (humano, 2026-10-29):** ligada na máquina local e em staging; desligada em produção. Liga só com `MCP_ENABLED=true` (validado em `env/`).
  - **Rotas protegidas: login com o usuário de teste do seed (humano, 2026-10-29).** As tools de features que necessitam de autenticação fazem login com o usuário de teste criado pelo seed e usam a sessão dele nas rotas protegidas (texto do humano: "podemos fazer o login usando o usuário de teste que será o seed para acessar rotas protegidas"). A api_key segue só para conectar ao `/mcp` (abaixo).
    - Tools de features públicas (ex.: auditar o histórico de um lote, ver comprovante) não fazem login, como as rotas públicas.
    - O login passa pela rota de login real (via `call-route.ts`), então a autenticação também é testada.
    - Credenciais do usuário de teste no env (validado em `env/`) e, em staging, nos *secrets* do GitHub; nunca no repositório.
    - **Tool `entrar` (humano, 2026-10-29):** o seed cria mais de um usuário de teste e a tool `entrar` escolhe com qual deles agir; ela faz o login e guarda a sessão na sessão MCP, e as tools protegidas usam essa sessão. Trocar de usuário é chamar `entrar` de novo, o que permite ao Claude simular uma disputa entre licitantes.
    - **Seed (humano, 2026-10-29):** um leiloeiro e dois licitantes. Nomes sugeridos pela IA: `leiloeiro`, `licitante-1`, `licitante-2`.
  - **Acesso ao `/mcp` com api_key (humano, 2026-10-29: "vamos manter a api_key").** A api_key protege a conexão com o `/mcp`, para que só quem tem a chave aja como os usuários de teste. Ela não identifica usuário: quem age é escolhido pela tool `entrar`.
    - Vai no cabeçalho de toda requisição (`x-api-key` ou `Authorization: Bearer`, nomes que o conector do Claude aceita); sem chave ou com chave inválida, 401. Nunca na URL (a documentação da Anthropic proíbe chave em query string).
    - A chave fica no env (validado em `env/`) e, em staging, nos *secrets* do GitHub; nunca no repositório.
    - Claude Code: `claude mcp add --transport http stonebid <url>/mcp --header "x-api-key: <chave>"`.
    - Ponto de atenção da IA: no app do Claude, o cabeçalho fixo está em beta e só aparece para algumas organizações (seção "Request headers" ao adicionar o conector). Se não aparecer na conta do humano, o conector do app não consegue enviar a chave e só o Claude Code se conecta [a confirmar].
    - **Exigida em todos os ambientes onde a MCP liga, inclusive na máquina local (humano, 2026-10-29).** Não existe modo sem chave.
  - MCP é pedido/resposta: o Claude acompanha lances consultando o histórico; o canal em tempo real segue validado pelo Playwright no frontend.
- **Alteração:** o humano acrescentou a regra de atualização obrigatória. 2026-10-29: ambientes definidos (local e staging, não produção) e o `MCP_TOKEN` da proposta virou acesso por api_key, exigida só nas tools de features que necessitam de autenticação, para outras máquinas se conectarem. 2026-10-29: as rotas protegidas passaram a usar o login com o usuário de teste do seed, escolhido pela tool `entrar`; a api_key ficou só para conectar ao `/mcp`. 2026-10-29: confirmado que as tools chamam as rotas e que o seed cria um leiloeiro e dois licitantes. 2026-10-29: hospedagem do staging no GCP ([[geral-decisao-2026-10-29-hospedagem]]).
- **Motivo:** expor as rotas e testar o fluxo de trabalho pela Claude (texto do humano).
- **Consequências:**
  - **Feature ou rota nova no `stonebid-api` só está pronta com a tool MCP correspondente criada ou atualizada.** Rota alterada (contrato, schema) ou removida atualiza ou remove a tool na mesma tarefa.
  - O "pronto quando" do plano de toda funcionalidade com rota lista as tools MCP que ela cria ou muda.
  - O briefing do implementador do backend aponta para esta nota; o relatório lista as tools criadas, alteradas ou removidas.
  - O verificador do backend confere se cada rota nova tem tool e exercita o fluxo pela MCP na URL de staging, depois do deploy.
  - Feature ou rota só é testada pela MCP depois que o CD publica em staging: o deploy de staging entra antes do teste no fluxo de cada funcionalidade do backend.
  - O deploy de staging precisa existir antes da primeira funcionalidade com rota: staging no GCP, como segundo serviço no Cloud Run com banco separado (proposta da IA em [[geral-decisao-2026-10-29-hospedagem]]); branch de staging [a confirmar].
  - A camada MCP não tem regra de negócio: só traduz tool → rota. `domain/` não conhece o MCP.
  - Dependência nova no backend: SDK oficial de MCP para TypeScript (versão [a confirmar] na implementação).
  - Árvore de pastas: [[geral-decisao-2026-10-28-estrutura-backend]].

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[geral-plano]]
- Projeto: [[geral-contexto]]
- Relacionadas: [[geral-decisao-2026-10-28-estrutura-backend]], [[geral-decisao-2026-10-28-stack-backend]], [[geral-decisao-2026-10-28-testes-frontend-playwright]], [[geral-decisao-2026-10-29-hospedagem]]
- Regras: [[manual-da-orquestra]]
