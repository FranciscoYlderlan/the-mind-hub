---
tipo: plano
funcionalidade: geral
status: aprovado
criado: 2026-10-28
---
# 🧭 Roteiro — Stonebid

> [!tldr] Onde o projeto está
> Etapa atual: **3. Carteira e lotes (I1)** (em-construcao)

> [!success] Aprovado
> Etapas aprovadas em [[geral-decisao-2026-10-29-roteiro]]. Mudar a lista de etapas é uma nova decisão.

Uma seção por etapa, na ordem em que o projeto acontece. Status: `planejada → em-construcao → em-verificacao → concluida → arquivada`. Etapa concluída tem data e links para as notas geradas nela. A linha "Etapa atual" acima é sincronizada por `cofre.py status --atualizar`.

> [!info] Vale para toda etapa de código
> Branch `tipo/ID-descricao` → CI verde → `staging` → `main`. Rota nova atualiza a MCP; tela nova passa pelo Playwright; teste T-xx sai junto com a regra. Pronto = [[contrato-processo-e-plano]] (11.5) e **no ar**.

## 1. Definir o roteiro do projeto
- **Status:** concluida
- **Objetivo:** fechar as etapas abaixo.
- **Pronto quando:** etapas aprovadas numa nota de decisão.
- **Funcionalidades:** (nenhuma)
- **Notas geradas:** [[geral-decisao-2026-10-28-stack-frontend]], [[geral-decisao-2026-10-28-stack-backend]], [[geral-decisao-2026-10-28-estrutura-frontend]], [[geral-decisao-2026-10-28-estrutura-backend]], [[geral-decisao-2026-10-28-criacao-de-componentes]], [[geral-decisao-2026-10-28-testes-frontend-playwright]], [[registro-de-componentes]], [[geral-decisao-2026-10-29-camada-mcp]], [[geral-decisao-2026-10-29-hospedagem]], [[geral-decisao-2026-10-29-padrao-de-branches]], [[contrato-do-projeto]], [[enunciado-teste-tecnico]], [[geral-decisao-2026-10-29-roteiro]]
- **Concluída em:** 2026-10-29

## 2. Esqueleto no ar (I0)
- **Status:** concluida
- **Objetivo:** boilerplate dos dois repositórios, GCP + Vercel, CI/CD, staging, login com papéis, seed e tema.
- **Pronto quando:** aplicação vazia no ar com os usuários de teste.
- **Funcionalidades:** [[esqueleto-contexto]]
- **Notas geradas:** [[geral-decisao-2026-10-29-modo-de-implementacao]], [[geral-decisao-2026-10-29-sessao-jwt-no-cabecalho]], [[geral-decisao-2026-10-29-prisma-7]], [[geral-decisao-2026-10-29-typescript-6-no-web]], [[geral-decisao-2026-10-29-next-themes-para-o-tema]], [[geral-decisao-2026-10-29-vercel-sem-deploy-automatico]], [[geral-decisao-2026-10-29-alias-fixo-do-staging]], [[acesso-de-teste]], [[diario-2026-10-29-esqueleto]]
- **Concluída em:** 2026-10-29

## 3. Carteira e lotes (I1)
- **Status:** em-construcao
- **Objetivo:** depósito simulado, busca na API de itens, criação do lote e vitrine.
- **Pronto quando:** lote criado aparece na vitrine; licitante deposita.
- **Funcionalidades:** [[carteira-e-lotes-contexto]]
- **Notas geradas:** [[geral-decisao-2026-10-29-api-de-itens]], [[geral-decisao-2026-10-29-imagem-do-lote-no-banco]], [[geral-decisao-2026-10-29-lance-inicial-e-valor-minimo]], [[geral-decisao-2026-10-29-inicio-e-duracao-do-lote]], [[geral-decisao-2026-10-29-limites-do-deposito]], [[geral-decisao-2026-10-29-edicao-de-lote-fora]], [[diario-2026-10-29-carteira-e-lotes]]
- **Concluída em:** 

## 4. Lances (I2)
- **Status:** planejada
- **Objetivo:** validação do lance, saldo comprometido, recusas e hash encadeado.
- **Pronto quando:** T-01 a T-03 passando.
- **Funcionalidades:** 
- **Notas geradas:** 
- **Concluída em:** 

## 5. Sala ao vivo e liquidação (I3)
- **Status:** planejada
- **Objetivo:** tempo real, anti-sniping, liquidação, comprovante e resultados.
- **Pronto quando:** um leilão completo, do início ao comprovante.
- **Funcionalidades:** 
- **Notas geradas:** 
- **Concluída em:** 

## 6. Auditoria pública (I4)
- **Status:** planejada
- **Objetivo:** histórico sem login com veredito íntegro ou adulterado.
- **Pronto quando:** T-06 detecta as adulterações.
- **Funcionalidades:** 
- **Notas geradas:** 
- **Concluída em:** 

## 7. Opcionais (I5)
- **Status:** planejada
- **Objetivo:** busca e filtros, cancelamento com estorno, tema escuro, Docker Compose.
- **Pronto quando:** opcionais no ar, respeitando a linha de corte.
- **Funcionalidades:** 
- **Notas geradas:** 
- **Concluída em:** 

## 8. Revisão e entrega
- **Status:** planejada
- **Objetivo:** README, relato do uso de IA (E6), checklist e envio.
- **Pronto quando:** checklist 11.6 completo e entrega feita até 2026-10-30 16:00.
- **Funcionalidades:** 
- **Notas geradas:** 
- **Concluída em:** 

### 🔗 Conexões
- Projeto: [[geral-contexto]]
- Mapa: [[moc-orquestra]]
- Regras: [[manual-da-orquestra]]
- Base: [[contrato-processo-e-plano]]
