---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-29
substitui: 
aliases: [Seed com imagem fixa, Imagens do seed, Seed images]
---
# ✅ Lotes do seed com item e imagem fixos no repositório

- **Proposta (plano):** [[carteira-e-lotes-plano#Pendente de aval antes da T1 (proposta da IA)]]; já implementado no PR #2 do `stonebid-api`.
- **Decisão:** os lotes do seed usam dados do item e imagens guardados no repositório do `stonebid-api`, e não buscam nada na API do Art Institute of Chicago. Aprovada pelo humano em 2026-10-29 23:01.
- **Alteração:** nenhuma.
- **Motivo:** o seed roda no CD antes de publicar; se dependesse da API externa, uma queda dela ou o limite de 60 requisições por minuto derrubaria o deploy.
- **Consequências:** o seed roda sem rede externa e é reexecutável (RNF-02); a imagem do seed vai para o banco como a de qualquer lote ([[geral-decisao-2026-10-29-imagem-do-lote-no-banco]]); trocar a imagem de um lote do seed é trocar o arquivo no repositório.

### 🔗 Conexões
- Funcionalidade: [[carteira-e-lotes-contexto]]
- Plano: [[carteira-e-lotes-plano]]
- Decisões ligadas: [[geral-decisao-2026-10-29-imagem-do-lote-no-banco]], [[geral-decisao-2026-10-29-seed-tambem-em-producao]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
