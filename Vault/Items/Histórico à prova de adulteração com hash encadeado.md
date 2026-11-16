---
aliases: [Hash encadeado, Hash chain, Selo HMAC, Registro só de acréscimo]
tags: [estudos/programacao]
tipo: conceito
status: rascunho
criado: 2026-11-16
origem: projeto Stonebid (stonebid-vault, decisões comprovante-e-hash e pseudonimo-por-hmac), 2026-10-29 e 2026-10-30
---
# 🔗 Histórico à prova de adulteração com hash encadeado

> [!tldr] Em uma linha
> Cada registro guarda o hash do anterior e um selo com segredo; o resumo do fim (cabeça) também é selado, senão apagar o último passa.

É o caderno de ata com páginas numeradas e carimbo em cada folha: arrancar ou trocar uma página aparece na hora. Mas se a última folha some e ninguém carimbou o "total de páginas", a ata parece inteira. A conferência de tudo o que deriva disso fica em [[Auditoria confere os dados derivados]].

> [!note] A regra e como aplicar
> 1. `hash = SHA-256` de uma **lista em ordem fixa** com versão, ex.: `["v1", id, seq, valor, instanteMs, prevHash]`; o primeiro usa um `prevHash` de gênese.
> 2. Guarde o próprio hash no registro: o diagnóstico separa "conteúdo editado" de "registro inserido ou removido".
> 3. **Selo** = HMAC com segredo do servidor e **etiqueta por tipo** (`bid:v1`, `head:v1`, `receipt:v1`), numa função só.
> 4. **Cabeça selada** (contagem, último hash, selo) atualizada na mesma transação do registro.
> 5. Dado pessoal fica fora: entra um pseudônimo por HMAC com segredo próprio, que nunca muda depois do primeiro uso.

> [!warning] Armadilha
> Serializar a partir de objeto (ordem de chaves instável) ou guardar contagem e hash final sem selo: quem apaga o último registro reescreve o resumo e a auditoria diz "íntegro".

> [!tip] Quando abrir esta nota
> Ao montar log de auditoria, histórico de lances, votos ou qualquer registro que o próprio dono do banco não pode reescrever.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** hash encadeado qualquer um recalcula; o selo exige o segredo.
* **Ponto 2:** a etiqueta impede usar o selo de um tipo como selo de outro.
* **Ponto 3:** limite conhecido: quem tem o banco **e** o segredo, ou um backup antigo, ainda forja; só uma âncora externa resolve.

### 🔗 Conexões
- Mapa: [[MOC Programação]]
- Relacionadas: [[Auditoria confere os dados derivados]], [[Regra de concorrência decidida dentro da trava]]
- Próxima: [[Auditoria confere os dados derivados]]
