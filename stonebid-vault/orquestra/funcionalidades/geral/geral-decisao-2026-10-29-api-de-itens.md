---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-29
substitui: 
aliases: [API de itens, Q-13, Art Institute of Chicago, External items API]
---
# ✅ API de itens: Art Institute of Chicago (Q-13)

- **Proposta (plano):** [[carteira-e-lotes-plano#Pendente de aval antes da T1 (proposta da IA)]]; a IA comparou Art Institute of Chicago, Scryfall e The Met.
- **Decisão:** a API pública de itens é a do **Art Institute of Chicago** (`api.artic.edu`), sem chave; imagens pelo IIIF da própria instituição. Aprovada pelo humano em 2026-10-29 22:23.
- **Alteração:** nenhuma.
- **Motivo:** obras de arte combinam com casa de leilões; a busca devolve os campos do item numa chamada só (o The Met pede uma chamada por item e tem muitas obras sem imagem); dispensa chave, como pede o critério de [[contrato-tecnologias]].
- **Consequências:** a busca do painel (RF-20) passa por um adaptador (AD-06) com timeout e erro claro; só obras com imagem entram no resultado; limites de uso e termos são conferidos pelo implementador antes de fixar o adaptador. Nenhuma outra tela chama a API (RN-13).

### 🔗 Conexões
- Funcionalidade: [[carteira-e-lotes-contexto]]
- Plano: [[carteira-e-lotes-plano]]
- Contrato: [[contrato-tecnologias]], [[contrato-pontos-para-validar]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
