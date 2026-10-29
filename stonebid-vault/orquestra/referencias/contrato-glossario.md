---
aliases: [Glossário do StoneBid, Vocabulário do leilão, Glossary, Termos do contrato]
tags: [estudos/programacao]
tipo: referencia
tema: requisitos
status: rascunho
criado: 2026-10-29
origem: Contrato do Projeto Stonebid v0.2 (2026-10-27), seção 15
---
# 📜 Contrato: glossário

> [!tldr] Em uma linha
> O significado de cada termo do domínio (arremate, liquidação, saldo comprometido, pseudônimo...) para humano e IA usarem a mesma palavra.

É o **dicionário da família**: cada casa tem palavras próprias, e quem chega de fora precisa da lista. Seção 15 do [[contrato-do-projeto|contrato]] v0.2, copiada sem reinterpretar.

| Termo | Significado |
|---|---|
| Anti-sniping (prorrogação) | Estender o fim do lote quando alguém dá um lance nos últimos minutos, para evitar lances "de última hora" sem chance de resposta. |
| Arremate | A venda do lote ao vencedor no encerramento. |
| Auditoria | Verificação pública, e sem login, de que o histórico de lances não foi alterado. |
| Comprovante | Registro do arremate, compartilhável por link. |
| Critério de aceite | Forma concreta de verificar que um requisito foi cumprido. |
| Hash | "Impressão digital" de tamanho fixo calculada a partir de um conteúdo. |
| Hash encadeado | Cada registro inclui o hash do anterior, formando uma corrente. Mexer num elo quebra os seguintes. |
| HMAC | Hash calculado com um segredo. Sem o segredo, ninguém recalcula um valor válido. |
| Idempotência | Repetir a mesma operação não muda o resultado além da primeira vez. |
| Incremento | Uma fatia de funcionalidade que funciona de ponta a ponta e é entregue por inteiro. |
| Incremento mínimo | O quanto cada lance precisa superar o lance atual. |
| Lance atual | O maior lance aceito até o momento no lote. |
| Líder | O licitante dono do lance atual. |
| Liquidação | O fechamento financeiro do lote: debita o vencedor, credita o leiloeiro e gera o comprovante. |
| Lote | Um item colocado em leilão, com regras próprias de valor e horário. |
| Pseudônimo | Identificador público que representa um licitante sem revelar quem ele é. |
| Rastreabilidade | Poder seguir um requisito até o teste e a entrega que o cobrem. |
| Saldo comprometido | A parte do saldo reservada para lances em que o usuário lidera. |
| Saldo disponível | Saldo total menos o comprometido. |
| Seed (dados de teste) | Dados criados por script para percorrer o sistema sem montar tudo do zero. |
| Snapshot (cópia do item) | Cópia dos dados do item guardada no lote, para não depender mais da API externa. |
| Stonebid | Nome do projeto. *Stone* (pedra) lembra algo que não se altera, em referência ao histórico à prova de adulteração, e *bid* é o lance. |
| Superado | Estado de quem tinha o lance atual e foi coberto por outro. |

> [!tip] Quando abrir esta nota
> Ao nomear entidades, rotas, mensagens de erro ou textos da tela: usar o termo daqui.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** comprometido é o saldo preso nos lances em que lidero; disponível é o resto ([[contrato-regras-de-negocio]]).
* **Ponto 2:** liquidação fecha o lote: debita, credita e gera o comprovante.
* **Ponto 3:** hash encadeado + HMAC é a base da auditoria ([[contrato-arquitetura]]).

### 🔗 Conexões
- Mapa: [[contrato-do-projeto]] · [[moc-orquestra]]
- Relacionadas: [[contrato-regras-de-negocio]], [[contrato-arquitetura]]
- Volta ao início: [[contrato-do-projeto]]
