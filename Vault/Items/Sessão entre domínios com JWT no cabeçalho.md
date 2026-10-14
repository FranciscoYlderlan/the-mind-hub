---
aliases: [JWT no Authorization, Auth opcional sem 401, Cross-origin session, Redirect só interno]
tags: [estudos/programacao]
tipo: conceito
status: rascunho
criado: 2026-11-16
origem: projeto Stonebid (stonebid-vault, decisões sessao-jwt-no-cabecalho, viewer-no-lote, sala-publica-le-a-sessao e estrutura-frontend; T5m de carteira-e-lotes-plano-correcoes), 2026-10-29 e 2026-10-30
---
# 🪪 Sessão entre domínios com JWT no cabeçalho

> [!tldr] Em uma linha
> Web e API em domínios diferentes: token no `Authorization`, rota pública com login opcional que nunca dá 401, e cache pessoal descartado na troca de sessão.

É o crachá de evento: você mostra na entrada de cada sala, em vez de depender de um carimbo na mão que a portaria do prédio vizinho apaga. Cookie de terceiros é o carimbo: navegadores bloqueiam.

> [!note] A regra e como aplicar
> 1. **JWT no cabeçalho** `Authorization: Bearer`; o CORS libera esse cabeçalho só para as origens do web; o mesmo serve para testes e agentes por `fetch`.
> 2. **Login opcional sem 401:** rota pública aceita token; válido traz o dado pessoal (ex.: `viewer`), ausente ou inválido traz `null`.
> 3. **Cache pessoal:** se o dado pessoal entra no cache de uma consulta pública, descarte essas consultas no login e no logout.
> 4. **Redirect interno:** o `?redirect` do login aceita só caminho que começa com uma barra e não com duas (`/^\/(?!\/)/`), contra redirecionamento aberto.
> 5. Falha do "quem sou eu" que não é 401: avise e mantenha o token; só o 401 desloga.

> [!warning] Armadilha
> Trocar de conta sem recarregar e ver "você está ganhando" da sessão anterior: o cache e o stream guardaram o dado pessoal da outra pessoa.

> [!tip] Quando abrir esta nota
> Ao separar front e API em hosts diferentes, ou ao pôr dado do usuário numa página pública.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** cabeçalho funciona entre domínios; cookie de terceiros não.
* **Ponto 2:** página pública não quebra por token velho: `null`, nunca 401.
* **Ponto 3:** stream público não leva dado pessoal ([[Tempo real por SSE com recarga de reserva]]).

### 🔗 Conexões
- Mapa: [[MOC Programação]]
- Relacionadas: [[Busca e cache em rota pública]], [[API simulada conferida contra a API real]]
- Próxima: [[Busca e cache em rota pública]]
