---
aliases: [Falha fora do cache, LIKE escapado, Filtro em rota nova, Public route search and cache]
tags: [estudos/programacao]
tipo: conceito
status: rascunho
criado: 2026-11-16
origem: projeto Stonebid (stonebid-vault, decisões busca-na-vitrine e cache-e-limite-da-miniatura), 2026-10-30
---
# 🔎 Busca e cache em rota pública

> [!tldr] Em uma linha
> Filtro novo ganha rota nova, o termo do `LIKE` é escapado e falha nunca entra no cache.

É a geladeira da cozinha: você guarda a comida boa para não ir ao mercado toda hora, mas não guarda o pote vazio dizendo "acabou". Senão, todo mundo que abrir depois acha que não tem nada.

> [!note] A regra e como aplicar
> 1. **Filtro em rota nova** (ex.: `GET /items/search`): a rota antiga não muda de formato e o que já funciona não corre risco.
> 2. Parâmetros validados com limites (tamanho do termo, página de 1 a 50, mínimo ≤ máximo); inválido dá 400 com mensagem legível.
> 3. **`LIKE` escapado:** `%` e `_` do usuário viram literais; busca em campos escolhidos (ex.: `concat_ws` com `ILIKE`), nunca no JSON inteiro como texto.
> 4. **Cache em memória** com teto de itens, de bytes e validade; pedidos simultâneos da mesma chave fazem uma busca só.
> 5. **Falha fora do cache:** só resposta boa é guardada.
> 6. Limite de pedidos por IP só na rota cara, com `429` e `retry-after`.

> [!warning] Armadilha
> Guardar o erro do serviço externo por 24 h: a falha de um minuto vira um dia inteiro de imagem quebrada.

> [!tip] Quando abrir esta nota
> Ao criar busca, filtro ou rota pública que chama serviço externo.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** rota nova para o filtro protege o contrato da antiga.
* **Ponto 2:** `%` digitado pelo usuário não pode virar curinga.
* **Ponto 3:** rota pública nasce com cache e limite, como em [[Imagem de terceiro com anti-robô passa pelo servidor]].

### 🔗 Conexões
- Mapa: [[MOC Programação]]
- Relacionadas: [[Sessão entre domínios com JWT no cabeçalho]], [[API externa escolhida por versão, licença e chave]]
- Próxima: [[API externa escolhida por versão, licença e chave]]
