---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-29
substitui: 
aliases: [Alias do staging, stonebid-web-staging, Staging URL]
---
# ✅ Web de staging no alias fixo stonebid-web-staging.vercel.app

- **Proposta (plano):** [[esqueleto-plano#Candidatos a registro]]; já implementado na etapa 2 ([[diario-2026-10-29-esqueleto]]).
- **Decisão:** o web de staging fica sempre em `https://stonebid-web-staging.vercel.app`: o `cd.yml` publica o preview da branch `staging` e aponta esse alias para ele pela API REST da Vercel (`teamId`), não pela CLI. Aprovada pelo humano em 2026-10-29 22:23.
- **Alteração:** nenhuma.
- **Motivo:** a URL do preview muda a cada deploy, e o CORS da API de staging e os testes precisam de um endereço fixo; a CLI falhava no alias com "User not found".
- **Consequências:** o `CORS_ORIGIN_STAGING` da API e o [[acesso-de-teste]] usam esse alias; mudar o nome é decisão nova.

### 🔗 Conexões
- Funcionalidade: [[esqueleto-contexto]]
- Plano: [[esqueleto-plano]]
- Decisões ligadas: [[geral-decisao-2026-10-29-modo-de-implementacao]], [[geral-decisao-2026-10-29-hospedagem]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
