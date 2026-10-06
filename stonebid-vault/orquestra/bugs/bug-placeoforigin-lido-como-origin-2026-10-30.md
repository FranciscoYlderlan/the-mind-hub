---
tipo: bug
funcionalidade: carteira-e-lotes
status: resolvido
criado: 2026-10-30
aliases: [Origem da obra não aparece, placeOfOrigin, campo origin vazio, item origin missing]
---
# 🐞 `placeOfOrigin` lido como `origin`: a origem da obra nunca aparece

## Contexto
Atributos da obra na busca e na página do lote. Achado pelos implementadores da T5b e da T5c e pelo verificador da T5d, 2026-10-30 00:0x.

## Sintoma
- **Esperado:** "Origem" da obra na busca e no lote, quando a AIC informa o local.
- **Observado:** a linha "Origem" nunca aparece, nem em obra que tem o dado.

## Impacto
Perda silenciosa de informação; nenhum erro, nenhum teste vermelho.

## Hipóteses
- A AIC não manda o campo: descartada; a API do Stonebid devolve `attributes.placeOfOrigin`.
- **Nome diferente entre API e web:** confirmada.

## Linha do tempo técnica
- 2026-10-30 00:0x: achado; vira parte da T5f.
- 06:1x: humano aprova a T5f; 06:2x: merge; 06:4x: Chrome aprova.

## Pseudocódigo do problema
```text
API presenter: attributes: { placeOfOrigin: "França", ... }
web schema:    attributes: z.object({ origin: z.string().optional(), ... })  // campo opcional -> some sem erro
```

## Testes feitos
Leitura do presenter da API contra `lot-schemas.ts` e `item-attributes.tsx` do web. A API simulada do Playwright, depois da T5b, já usava `placeOfOrigin`, o que expôs a diferença.

## Evidências encontradas
O campo era opcional no schema do web: o `parse` passava e o valor ficava `undefined`.

## Correção aplicada
PR #8 do `stonebid-web` (merge `a3836fc`): schema e tela leem `placeOfOrigin`; `e2e/item-origin.spec.ts`. Detalhes: [[carteira-e-lotes-plano-correcoes-t5c-a-t5h]] (T5f).

## Solução
O schema do web segue o presenter da API, campo a campo.

## Como validar que não voltou
`e2e/item-origin.spec.ts` com a API simulada igual à real; no Chrome, "Origem" igual ao `placeOfOrigin` da resposta.

## Logs que deveriam existir
Nenhum log pega campo opcional com nome errado; só o teste de contrato pega.

## O que aprendi
- Campo opcional no schema do cliente esconde erro de nome: o `parse` aceita e o dado some.
- Lição geral no `Vault`: "API simulada conferida contra a API real".

### 🔗 Conexões
- Funcionalidade: [[carteira-e-lotes-contexto]]
- Outros bugs: [[bug-deposito-sem-teto-na-resposta-2026-10-29]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
