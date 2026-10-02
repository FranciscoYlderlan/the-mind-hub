---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-29
substitui: 
aliases: [Imagem do lote, Cópia da imagem, RN-13, Lot image storage]
---
# ✅ Imagem do lote guardada no PostgreSQL (RN-13)

- **Proposta (plano):** [[carteira-e-lotes-plano#Pendente de aval antes da T1 (proposta da IA)]]
- **Decisão:** ao criar o lote, a imagem do item é baixada e guardada em bytes no PostgreSQL, junto com o tipo de conteúdo, e servida por `GET /lots/:id/image`. Sem bucket no Cloud Storage. Aprovada pelo humano em 2026-10-29 22:23.
- **Alteração:** nenhuma.
- **Motivo:** poucos lotes e imagens pequenas; não muda o `gcp-setup.sh`, as permissões nem o CD; cumpre a RN-13 sem infra nova.
- **Consequências:** vitrine, sala, auditoria e comprovante usam só `GET /lots/:id/image`; é proibido guardar só a URL externa da imagem. A imagem baixada tem tamanho máximo, para não inchar o banco.

### 🔗 Conexões
- Funcionalidade: [[carteira-e-lotes-contexto]]
- Plano: [[carteira-e-lotes-plano]]
- Contrato: [[contrato-regras-de-negocio]], [[contrato-modelo-de-dados]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
