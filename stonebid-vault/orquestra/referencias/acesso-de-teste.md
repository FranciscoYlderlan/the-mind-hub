---
aliases: [Acesso de teste, Login de teste, Usuários de teste, Credenciais de teste, Test access]
tags: [estudos/programacao]
tipo: referencia
tema: orquestracao
status: em-uso
criado: 2026-10-29
origem: humano, 2026-10-29 21:40
---
# 📚 Acesso de teste do Stonebid

> [!tldr] Em uma linha
> Onde entrar e com qual usuário: o Stonebid é uma aplicação de teste, de acesso livre, e qualquer agente pode entrar e usar a plataforma para testar.

## O que é
A **porta da frente** da aplicação no ar, com as chaves penduradas ao lado. Serve para o humano entrar à mão nos testes de interface e para os agentes testarem sem pedir licença a cada vez.

## Autorização do humano
- Humano, 2026-10-29 21:40: "como essa é uma aplicação de teste você pode fazer o login e acessar a plataforma como bem entender para testar e logar já que o projeto em si é de teste". O projeto é de **acesso livre**.
- Vale para o orquestrador e para os subagentes, em produção e em staging.
- Humano, 2026-10-29 22:06: "Sempre no staging e em prod quem irá testar é o agente para agilizar os processos". **Quem testa no ar é sempre o agente**, em staging e em produção; o humano só entra onde o limite abaixo impede o agente.
- Como testar no ar (Chrome, `fetch` no console e cliques; rede do container e do computador barrada): [[geral-decisao-2026-10-29-modo-de-implementacao]].
- **Limite do agente no navegador:** a ferramenta do agente só digita senha em ambiente local (`localhost`) ou em host de teste que o humano nomeie no pedido (ex.: staging). Na produção pelo navegador, o login fica com o humano (dados fictícios não mudam isso: a regra olha o endereço, não os dados); o agente testa a produção pela API ou pelos fluxos sem login, e o staging pela tool `entrar` da MCP (ela faz o login no servidor, sem digitar senha).

## Endereços
| Ambiente | Web | API |
|---|---|---|
| Produção | https://stonebid-web.vercel.app (login em `/login`) | https://stonebid-api-7idhzkkvpq-rj.a.run.app (`/health`) |
| Staging | https://stonebid-web-staging.vercel.app (login em `/login`) | https://stonebid-api-staging-7idhzkkvpq-rj.a.run.app (`/health`, `/mcp` com api_key) |
| Local | http://localhost:5173 | http://localhost:3333 (`/mcp` com api_key) |

## Usuários de teste
Criados pelo seed (`prisma/seed.ts` do `stonebid-api`), iguais em todos os ambientes.

| Papel | E-mail | Senha |
|---|---|---|
| Leiloeiro | `leiloeiro@stonebid.dev` | `stonebid123` |
| Licitante 1 | `licitante-1@stonebid.dev` | `stonebid123` |
| Licitante 2 | `licitante-2@stonebid.dev` | `stonebid123` |

- A senha é o segredo `SEED_PASSWORD`: `stonebid123` no `gcp-setup.sh`, no `.env.example` e no `docker-compose.yml` (já público nos repositórios).
- Também dá para criar conta nova em `/register`, escolhendo o papel.
- **Fora daqui:** a `MCP_API_KEY_STAGING` fica só no Secret Manager do GCP, e os tokens da Vercel e do GitHub ficam nas contas do humano.

## Como usar
> [!example] Teste de interface à mão
> 1. Abrir `https://stonebid-web.vercel.app/login`.
> 2. Entrar com o leiloeiro para criar lotes; com um licitante, numa janela anônima, para dar lances.
> 3. Auditoria e comprovante abrem sem login.

> [!example] Agente pela MCP (staging)
> `claude mcp add --transport http stonebid https://stonebid-api-staging-7idhzkkvpq-rj.a.run.app/mcp` com a api_key no cabeçalho; depois a tool `entrar` com `leiloeiro`, `licitante-1` ou `licitante-2` ([[geral-decisao-2026-10-29-camada-mcp]]).

> [!warning] Só para teste
> Nada real passa por aqui: o saldo é simulado e os dados podem ser apagados pelo seed. A aplicação fica no ar no máximo 7 dias ([[geral-decisao-2026-10-29-hospedagem]]).

### 🔗 Conexões
- Mapa: [[moc-orquestra]]
- Relacionadas: [[geral-decisao-2026-10-29-modo-de-implementacao]], [[esqueleto-contexto]], [[esqueleto-plano]], [[geral-decisao-2026-10-29-camada-mcp]], [[geral-decisao-2026-10-29-hospedagem]]
- Regras: [[manual-da-orquestra]]
