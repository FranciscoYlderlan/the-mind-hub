---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-29
substitui: 
aliases: [Miniatura da busca pela API, Proxy da imagem IIIF, Catalog thumbnail route]
---
# ✅ Miniatura da busca: a API entrega a imagem do item

- **Proposta (plano):** [[carteira-e-lotes-plano-correcoes#T5c: miniaturas da busca não carregam]]: rota da API que entrega a imagem do item (o servidor alcança o IIIF) ou só o título, sem imagem, até criar o lote.
- **Decisão:** a busca do leiloeiro mostra a miniatura por uma rota da API. O servidor busca a imagem IIIF da AIC e a entrega ao navegador; o navegador nunca pede o IIIF direto.
- **Alteração:** nenhuma (o humano escolheu a opção recomendada, 2026-10-29 23:5x).
- **Motivo:** as imagens IIIF da AIC abrem no navegador com o desafio anti-robô da Cloudflare, mas respondem ao servidor, como já mostra a cópia da imagem na criação do lote ([[geral-decisao-2026-10-29-imagem-do-lote-no-banco]]).
- **Consequências:** o servidor monta a URL do IIIF a partir de um identificador validado, nunca de uma URL vinda do cliente, e só chama o host da AIC. A rota precisa funcionar num `<img>`, que não manda o JWT do cabeçalho ([[geral-decisao-2026-10-29-sessao-jwt-no-cabecalho]]); as imagens são de domínio público ([[geral-decisao-2026-10-29-busca-so-em-dominio-publico]]). O item da busca traz a URL dessa rota no lugar da URL do IIIF.

### 🔗 Conexões
- Funcionalidade: [[carteira-e-lotes-contexto]]
- Plano: [[carteira-e-lotes-plano-correcoes]]
- Decisões ligadas: [[geral-decisao-2026-10-29-api-de-itens]], [[geral-decisao-2026-10-29-imagem-do-lote-no-banco]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
