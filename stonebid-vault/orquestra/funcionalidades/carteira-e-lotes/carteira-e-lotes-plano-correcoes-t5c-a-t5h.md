---
tipo: plano
funcionalidade: carteira-e-lotes
status: proposta
criado: 2026-10-30
aliases: [T5c a T5h, Correções da T4 verificadas]
---
# 📋 Carteira e lotes: correções T5c a T5h (verificadas)

> [!warning] Proposta da IA
> Nada aqui é decisão. Decisões ficam nas notas `-decisao-` linkadas abaixo.

Parte de [[carteira-e-lotes-plano-correcoes]], separada pelo limite de palavras.

## Tarefas

### T5c: miniaturas da busca não carregam
- **Achado:** as imagens IIIF da AIC (`www.artic.edu/iiif/2/...`) abrem no navegador com o desafio anti-robô da Cloudflare ("Um momento…"); o `<img>` falha e o `CoverImage` mostra o marcador em todos os resultados. A cópia feita pelo servidor na criação do lote funciona (JPEG de 272 KB, servido por `/lots/:id/image`).
- **Faz:** rota da API que entrega a miniatura do item a partir de um identificador validado ([[geral-decisao-2026-10-29-miniatura-da-busca-pela-api]]); a busca do web usa essa URL no lugar do IIIF.
- **Toca em:** `stonebid-api` (`src/infra/external/`, `src/infra/http/`, MCP) e/ou `stonebid-web` (`catalog-item-card.tsx`, `create-lot-dialog.tsx`).
- **Depende de:** nenhuma
- **Paralelo:** sim, com T5a, T5b e T5d
- **Pronto quando:**
  - [ ] a busca em staging mostra imagem (ou o que for aprovado) sem pedir ao navegador o IIIF da AIC
- **Prova:** Chrome em staging
- **Verificação:**
  - Data: 2026-10-30 00:05 (merge) e 2026-10-30 06:2x (Chrome, staging)
  - Critérios ✔/✘ com a prova de cada um:
    - PR #4 do `stonebid-api` (merge `31c3682`): `GET /items/images/:imageId/thumbnail`, pública, id só UUID (sem SSRF), IIIF de 400 px, timeout, corte em 1 MB, `Cache-Control` de 7 dias; 68 testes e CI verdes.
    - PR #7 do `stonebid-web` (merge `d70333f`): card e prévia usam a rota; `e2e/catalog-thumbnail.spec.ts` prova que nada vai a `artic.edu`; 29 testes e CI verdes.
    - ✔ Chrome: buscas "monet" e "vaso ceramica", 24 de 24 miniaturas de `/items/images/<uuid>/thumbnail` (200, `image/jpeg`); prévia do "Novo lote" com imagem real; nenhuma requisição a `artic.edu`. Ids não UUID voltam 400 sem busca externa.
  - Devolvido para correção: não
  - Riscos anotados pelo implementador viraram a T5g e a T5h (aprovadas pelo humano).

### T5d: sem caminho para o painel e a carteira
- **Achado:** na vitrine e no cabeçalho não há link para `/auctioneer` nem para `/wallet`; o menu do usuário tem só "Minha conta" e "Sair". O menu lateral com "Painel do leiloeiro" ou "Carteira" só aparece dentro da área logada, aberta pela URL.
- **Faz:** no `stonebid-web`, o menu do usuário (e o cabeçalho, se couber) leva ao painel quando o papel é LEILOEIRO e à carteira quando é LICITANTE.
- **Toca em:** `stonebid-web`: componente do cabeçalho e menu do usuário, `e2e/`.
- **Depende de:** nenhuma
- **Paralelo:** sim, com T5a e T5b
- **Pronto quando:**
  - [ ] da vitrine, cada papel chega à sua área em um clique; Playwright cobre os dois papéis; CI verde
- **Prova:** Playwright
- **Verificação:**
  - Data: 2026-10-30 00:03 (código) e 2026-10-30 00:05 (Chrome, staging)
  - Critérios ✔/✘ com a prova de cada um:
    - ✔ PR #5 do `stonebid-web` (merge `5c5c800`): atalho no cabeçalho e no menu do usuário em `session-actions.tsx`, a partir de `navItemsFor`; `e2e/role-shortcut.spec.ts`; CI verde.
    - ✔ Verificador de código: 1 clique por papel a 375 e 1280 px; nenhum papel vê o atalho do outro; visitante sem atalho; nome acessível, foco por Tab e Enter; 20/20 testes.
    - ✔ Chrome: licitante → `/wallet` e leiloeiro → `/auctioneer` em 1 clique; deslogado sem atalho. A janela não redimensionou, então a largura estreita ficou provada só no Playwright.
  - Devolvido para correção: não. Achado: o cabeçalho passa da largura da tela no celular (2 px com o nome padrão a 375 px; até 118 px com nome longo a 320 px), virou a T5f.

### T5f: cabeçalho no celular e origem da obra
- **Achado:** (1) a 375 px o cabeçalho passa da largura da tela: o nome do usuário e o botão novo da T5d somam mais que a tela (2 px com o nome padrão; 63 px com nome longo a 375 px, 118 px a 320 px). Os testes só rodam na largura de desktop. (2) A API manda `attributes.placeOfOrigin`, mas o web lê `origin` (`lot-schemas.ts`, `item-attributes.tsx`), então a "Origem" da obra nunca aparece. Achados pelos verificadores da T5d e pelos implementadores da T5b e da T5c.
- **Faz:** no `stonebid-web`, esconder o nome do usuário abaixo de `sm` e deixar o lado direito do cabeçalho encolher (`min-w-0`), com teste do Playwright a 320 e 375 px sem rolagem horizontal; o schema e a tela dos atributos leem `placeOfOrigin`, e a API simulada já usa esse nome.
- **Toca em:** `stonebid-web`: cabeçalho e `session-actions.tsx`, `src/features/lots/` (schema e `item-attributes.tsx`), `e2e/`.
- **Depende de:** nenhuma (aval do humano em 2026-10-30)
- **Paralelo:** sim, com a verificação da T5c no Chrome
- **Pronto quando:**
  - [ ] a 320 e 375 px a página não rola na horizontal, com nome longo
  - [ ] a "Origem" aparece no lote que tem `placeOfOrigin`; lint, Prettier, tipos, build e Playwright; CI verde
- **Prova:** Playwright; Chrome em staging
- **Verificação:**
  - Data: 2026-10-30 06:2x (merge) e 06:4x (Chrome, staging)
  - Critérios ✔/✘ com a prova de cada um:
    - ✔ Chrome (iframe de 320 e 375 px; o `resize_window` não estreita): sem rolagem horizontal para leiloeiro, licitante e visitante; atalho e menu com nome acessível e 1 clique. Visitante a 320 px com folga zero ("Cadastrar" termina em 308 px): com barra de rolagem clássica sobram 2 px.
    - ✔ "Origem" na página do lote e na busca, igual ao `placeOfOrigin` da API.
    - PR #8 do `stonebid-web` (merge `a3836fc`): cabeçalho encolhe abaixo de `sm` (avatar sem nome; "Entrar" vira ícone), `placeOfOrigin` no schema e na tela; `e2e/mobile-header.spec.ts` e `e2e/item-origin.spec.ts`; 37 testes e CI verdes.
  - Devolvido para correção: não

### T5g: cache e limite da miniatura
- **Achado:** risco da T5c: rota pública sem limite e sem cache no servidor.
- **Faz:** cache LRU em memória e limite por IP só na rota ([[geral-decisao-2026-10-30-cache-e-limite-da-miniatura]]).
- **Toca em:** `stonebid-api`: `src/infra/external/`, `src/app.ts`, `src/infra/http/`, `test/`.
- **Verificação:**
  - Data: 2026-10-30 06:2x (merge) e 06:4x (Chrome, staging)
  - Critérios ✔/✘ com a prova de cada um:
    - ✔ Chrome: miniaturas 200 sem `artic.edu`; cache no servidor (1º pedido ~580 ms, seguintes ~100 ms); rajada de 130: 120 com 200 e 429 a partir do 121º, corpo `TOO_MANY_REQUESTS`; `/health` 200 logo depois. `retry-after` sem prova pelo navegador (CORS não expõe o cabeçalho).
    - PR #5 do `stonebid-api` (merge `7246bf1`): `thumbnail-cache.ts`, `@fastify/rate-limit` com `global: false`, erro `TOO_MANY_REQUESTS`; 80 testes e CI verdes.
  - Devolvido para correção: não

### T5h: IP real atrás do proxy do Cloud Run
- **Achado:** sem `trustProxy`, todos os clientes de uma instância dividiam o mesmo balde.
- **Faz:** `trustProxy` pela faixa `169.254.0.0/16` ([[geral-decisao-2026-10-30-cache-e-limite-da-miniatura]]).
- **Verificação:**
  - Data: 2026-10-30 06:33 (merge, PR #6 do `stonebid-api`, `ad06247`); 83 testes e CI verdes.
  - ✔ Chrome, Cloud Logging (07:0x): os pedidos novos registram o IP do cliente em `jsonPayload.req.remoteAddress`, igual ao `httpRequest.remoteIp` do Cloud Run; um pedido de antes da correção registrou `169.254.169.126`. `X-Forwarded-For` forjado sem prova pelo navegador (o CORS não deixa mandar).
  - Devolvido para correção: não

### 🔗 Conexões
- Plano: [[carteira-e-lotes-plano-correcoes]]
- Funcionalidade: [[carteira-e-lotes-contexto]]
