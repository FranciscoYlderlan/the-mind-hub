---
tipo: contexto
funcionalidade: integracoes
status: em-construcao
etapa: 3
criado: 2026-11-23
aliases: [Integrações, Integracoes, UC-01]
---
# 🧭 Integrações — Claude CLI, Obsidian CLI e GitHub

> [!tldr] Em uma linha
> Conectar e mostrar o status das três integrações (RF-01 a RF-04, UC-01), cada uma atrás da trait `Integracao` da fundação.

## Objetivo e motivação
Fechar a etapa 3 do [[geral-plano]]: AC de UC-01 e TEL-02 (principal, FA-01, FE-01 a FE-04) passando no verificador de fluxo principal e no adversarial, e busca automatizada sem token em texto puro (RNF-05). As etapas 4 a 9 dependem destas integrações reais.

## Fatos que eu informei
- 2026-11-24 (07h43): `client_id` do app OAuth: `Ov23li904l2z5LWigHyr`.
- 2026-11-23 (17h45): "Sim, seguir" ao [[integracoes-plano]] (T0a, T0b, T1 a T5); repositório de testes já criado: `FranciscoYlderlan/myharness-teste`.
- 2026-11-23 (16h45): o teste com o GitHub real entra nesta etapa, num repositório só de testes, nunca o `MyHarness` ([[geral-decisao-2026-11-23-github-real-na-etapa-3]]).
- 2026-11-19: GitHub por app OAuth próprio, com device flow; o `client_id` vai no `.env` do repositório ([[geral-decisao-2026-11-19-github-oauth-proprio]]).

## O que já foi feito
- 2026-11-23: funcionalidade aberta; plano aprovado ([[integracoes-plano]]); contrato de UC-01 já preenchido na fundação (ENT-13, ERR-01 a ERR-07, ERR-53, AC-01 a AC-05, AC-88 a AC-91, AC-127 a AC-129, AC-153, AC-154).

## Tempo disponível
- [a confirmar]

## Dial e modelo de IA
- Dial: o do [[geral-contexto]]
- Modelo de IA: Claude Opus 5.5 no orquestrador; subagentes [a confirmar]

## Áreas sensíveis
- Token do GitHub e mensagens da CLI: mascaramento (RN-04, [[fundacao-plano-mascaramento]]).
- GitHub: [[bug-github-sem-acesso-em-chat-novo-2026-11-23]].

## Mapa
- Plano: [[integracoes-plano]]
- Decisões: [[geral-decisao-2026-11-23-github-real-na-etapa-3]], [[geral-decisao-2026-11-19-github-oauth-proprio]], [[geral-decisao-2026-11-23-falha-interna]], [[geral-decisao-2026-11-23-banco-antigo-apagado]], [[geral-decisao-2026-11-23-filtro-de-comandos-so-comentario]], [[geral-decisao-2026-11-23-comandos-na-tela-de-execucao]], [[geral-decisao-2026-11-24-erro-generico-por-fronteira]], [[geral-decisao-2026-11-24-servidor-mcp-do-obsidian]], [[geral-decisao-2026-11-24-desconectar-sem-logout]]
- Interfaces herdadas: [[fundacao-contexto]]

## Interpretação do agente
- O código parte de módulos vazios em `src-tauri/src/infra/{claude,obsidian,github,secrets}` e do `Nucleo` provisório em `commands/nucleo.rs`, que devolve as três integrações como `desconectado` [a confirmar no plano].

### 🔗 Conexões
- Mapa: [[moc-orquestra]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
