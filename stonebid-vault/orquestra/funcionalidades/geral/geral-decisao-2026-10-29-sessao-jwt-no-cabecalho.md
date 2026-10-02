---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-29
substitui: 
aliases: [Sessão por JWT, Token no cabeçalho, Authorization Bearer, Cross-origin session]
---
# ✅ Sessão por JWT no cabeçalho Authorization, sem cookie

- **Proposta (plano):** [[esqueleto-plano#Candidatos a registro]]; já implementado na etapa 2 ([[diario-2026-10-29-esqueleto]]).
- **Decisão:** a sessão entre o web (Vercel) e a API (Cloud Run) usa token JWT no cabeçalho `Authorization: Bearer`, válido por 7 dias, guardado no `localStorage` do navegador; sem cookie `SameSite=None`. Aprovada pelo humano em 2026-10-29 22:23.
- **Alteração:** nenhuma.
- **Motivo:** web e API ficam em domínios diferentes; o cabeçalho evita cookie de terceiros, que navegadores bloqueiam, e funciona igual para a MCP e para testes por `fetch`.
- **Consequências:** toda rota protegida lê o `Authorization`; o CORS libera esse cabeçalho só para as origens do web; o logout apaga o token no navegador.

### 🔗 Conexões
- Funcionalidade: [[esqueleto-contexto]]
- Plano: [[esqueleto-plano]]
- Decisões ligadas: [[geral-decisao-2026-10-29-hospedagem]], [[geral-decisao-2026-10-29-camada-mcp]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
