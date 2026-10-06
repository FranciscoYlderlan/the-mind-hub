---
tipo: bug
funcionalidade: carteira-e-lotes
status: resolvido
criado: 2026-10-29
aliases: [miniaturas não carregam, imagem da busca quebrada, desafio da Cloudflare no IIIF, AIC thumbnails blocked]
---
# 🐞 Miniaturas da AIC barradas pela Cloudflare no navegador

## Contexto
Busca de obras do leiloeiro ("Novo lote"), verificação no ar da T4 de [[carteira-e-lotes-plano]], 2026-10-29. As miniaturas vinham direto do IIIF do Art Institute of Chicago ([[geral-decisao-2026-10-29-api-de-itens]]).

## Sintoma
- **Esperado:** cada resultado da busca com a miniatura da obra.
- **Observado:** todos os resultados com o marcador do `CoverImage`; abrir a URL IIIF (`www.artic.edu/iiif/2/...`) no navegador mostra o desafio anti-robô da Cloudflare ("Um momento…").

## Impacto
O leiloeiro escolhia a obra sem ver a imagem. A imagem do lote criado funcionava, porque a API copia a imagem no servidor ([[geral-decisao-2026-10-29-imagem-do-lote-no-banco]]).

## Hipóteses
- URL IIIF montada errada: descartada; a mesma URL funciona chamada pelo servidor.
- CORS ou `referrerPolicy`: descartada; a resposta é a página do desafio, não a imagem.
- **Proteção anti-robô por cliente:** confirmada; o desafio vale para o navegador e não para o Cloud Run.

## Linha do tempo técnica
- 2026-10-29 23:3x: achado na T4.
- 23:5x: humano aprova a rota da API ([[geral-decisao-2026-10-29-miniatura-da-busca-pela-api]]); T5c despachada.
- 2026-10-30 00:05: merge; 06:1x: cache e limite (T5g); 06:33: IP real atrás do proxy (T5h); 06:2x: Chrome aprova.

## Pseudocódigo do problema
```text
navegador -> GET www.artic.edu/iiif/2/<id>/full/400,/0/default.jpg -> 403/desafio HTML  -> <img> falha
servidor  -> GET mesma URL                                          -> 200 image/jpeg
```

## Testes feitos
Chrome: URL IIIF aberta direto (desafio); imagem do lote criado por `/lots/:id/image` (JPEG de 272 KB, ok).

## Evidências encontradas
A cópia feita pelo servidor na criação do lote sempre funcionou; só o pedido do navegador caía no desafio.

## Correção aplicada
- PR #4 do `stonebid-api` (merge `31c3682`): `GET /items/images/:imageId/thumbnail`, pública, id só UUID (sem SSRF), 400 px, timeout, corte em 1 MB, `Cache-Control` de 7 dias.
- PR #7 do `stonebid-web` (merge `d70333f`): card e prévia usam a rota; teste prova que nada vai a `artic.edu`.
- PR #5 e #6 do `stonebid-api`: cache LRU, limite por IP e `trustProxy` pela faixa do Cloud Run ([[geral-decisao-2026-10-30-cache-e-limite-da-miniatura]]).
- Detalhes: [[carteira-e-lotes-plano-correcoes-t5c-a-t5h]].

## Solução
Imagem de terceiro com proteção anti-robô passa pelo servidor, com identificador validado, cache e limite.

## Como validar que não voltou
Playwright `e2e/catalog-thumbnail.spec.ts` (nenhum pedido a `artic.edu`); no Chrome, busca em staging com todas as miniaturas vindas de `/items/images/<uuid>/thumbnail` (repetido na T5e, 2026-10-30 08:2x).

## Logs que deveriam existir
Na rota: status da AIC, tempo e acerto de cache por pedido; 429 contado por IP.

## O que aprendi
- Teste pelo servidor (curl, Cloud Run) não prova o que o navegador recebe de um site com anti-robô.
- Lição geral no `Vault`: "Imagem de terceiro com anti-robô passa pelo servidor".

### 🔗 Conexões
- Funcionalidade: [[carteira-e-lotes-contexto]]
- Decisões: [[geral-decisao-2026-10-29-miniatura-da-busca-pela-api]], [[geral-decisao-2026-10-30-cache-e-limite-da-miniatura]]
- Outros bugs: [[bug-deposito-sem-teto-na-resposta-2026-10-29]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
