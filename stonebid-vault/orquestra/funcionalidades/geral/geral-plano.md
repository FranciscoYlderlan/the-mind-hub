---
tipo: plano
funcionalidade: geral
status: aprovado
criado: 2026-10-28
---
# 🧭 Roteiro — Stonebid

> [!tldr] Onde o projeto está
> Etapa atual: **7. Opcionais (I5)** (em-construcao)

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
- **Status:** concluida
- **Objetivo:** depósito simulado, busca na API de itens, criação do lote e vitrine.
- **Pronto quando:** lote criado aparece na vitrine; licitante deposita.
- **Funcionalidades:** [[carteira-e-lotes-contexto]]
- **Notas geradas:** [[geral-decisao-2026-10-29-api-de-itens]], [[geral-decisao-2026-10-29-imagem-do-lote-no-banco]], [[geral-decisao-2026-10-29-lance-inicial-e-valor-minimo]], [[geral-decisao-2026-10-29-inicio-e-duracao-do-lote]], [[geral-decisao-2026-10-29-limites-do-deposito]], [[geral-decisao-2026-10-29-edicao-de-lote-fora]], [[geral-decisao-2026-10-29-seed-com-imagem-fixa]], [[geral-decisao-2026-10-29-seed-tambem-em-producao]], [[geral-decisao-2026-10-29-busca-so-em-dominio-publico]], [[geral-decisao-2026-10-29-codigo-do-teto-do-deposito]], [[geral-decisao-2026-10-29-sequencia-no-extrato]], [[geral-decisao-2026-10-29-miniatura-da-busca-pela-api]], [[geral-decisao-2026-10-30-cache-e-limite-da-miniatura]], [[geral-decisao-2026-10-30-obra-unica-por-lote]], [[geral-decisao-2026-10-30-prazo-16h]], [[passo-a-passo-do-agente]], [[diario-2026-10-29-carteira-e-lotes]], [[diario-2026-10-30]]
- **Concluída em:** 2026-10-30

## 4. Lances (I2)
- **Status:** concluida
- **Objetivo:** validação do lance, saldo comprometido, recusas e hash encadeado.
- **Pronto quando:** T-01 a T-03 passando.
- **Funcionalidades:** [[lances-contexto]]
- **Notas geradas:** [[geral-decisao-2026-10-30-pseudonimo-por-hmac]], [[geral-decisao-2026-10-30-lance-atual-no-lote]], [[geral-decisao-2026-10-30-saldo-na-recusa-do-lance]], [[geral-decisao-2026-10-30-historico-de-lances-no-i2]], [[geral-decisao-2026-10-30-pseudonimo-com-6-digitos]], [[geral-decisao-2026-10-30-recarga-de-15s-ate-o-i3]], [[geral-decisao-2026-10-30-dar-lance-so-para-licitante]], [[diario-2026-10-30-lances]]
- **Concluída em:** 2026-10-30

## 5. Sala ao vivo e liquidação (I3)
- **Status:** concluida
- **Objetivo:** tempo real, anti-sniping, liquidação, comprovante e resultados.
- **Pronto quando:** um leilão completo, do início ao comprovante.
- **Funcionalidades:** [[sala-ao-vivo-contexto]]
- **Notas geradas:** [[geral-decisao-2026-10-30-tempo-real-por-sse]], [[geral-decisao-2026-10-30-disparo-da-liquidacao]], [[geral-decisao-2026-10-30-movimentos-da-liquidacao]], [[geral-decisao-2026-10-30-resultado-no-lote]], [[geral-decisao-2026-10-30-limite-do-anti-sniping]], [[geral-decisao-2026-10-30-viewer-no-lote]], [[geral-decisao-2026-10-30-rotas-publicas-do-i3]], [[geral-decisao-2026-10-30-seed-com-lote-liquidado]], [[geral-decisao-2026-10-30-motivo-do-cancelamento-gravado]], [[geral-decisao-2026-10-30-caminho-da-auditoria]], [[geral-decisao-2026-10-30-sala-publica-le-a-sessao]], [[geral-decisao-2026-10-30-lot-ended-no-cancelamento]], [[geral-decisao-2026-10-30-422-no-cancelamento]], [[geral-decisao-2026-10-30-concorrencia-do-cloud-run]], [[geral-decisao-2026-10-30-posicao-cancelado-inalcancavel]], [[diario-2026-10-30-sala-ao-vivo]]
- **Concluída em:** 2026-10-30

## 6. Auditoria pública (I4)
- **Status:** concluida
- **Objetivo:** histórico sem login com veredito íntegro ou adulterado.
- **Pronto quando:** T-06 detecta as adulterações.
- **Funcionalidades:** [[auditoria-publica-contexto]]
- **Notas geradas:** [[geral-decisao-2026-10-30-auditoria-publica]], [[geral-decisao-2026-10-30-adulterado-provado-no-ci]], [[geral-decisao-2026-10-30-achados-da-t5-da-auditoria]], [[diario-2026-10-30-auditoria-publica-correcoes]], [[diario-2026-10-30-revisao-e-entrega]]
- **Concluída em:** 2026-10-30

## 7. Opcionais (I5)
- **Status:** em-construcao
- **Objetivo:** busca e filtros, cancelamento com estorno, tema escuro, Docker Compose.
- **Pronto quando:** opcionais no ar, respeitando a linha de corte.
- **Funcionalidades:** [[opcionais-contexto]]
- **Notas geradas:** [[geral-decisao-2026-10-30-estorno-no-cancelamento]], [[geral-decisao-2026-10-30-busca-na-vitrine]]
- **Concluída em:** 

## 8. Revisão e entrega
- **Status:** em-construcao
- **Objetivo:** README, relato do uso de IA (E6), checklist e envio.
- **Pronto quando:** checklist 11.6 completo e entrega feita até 2026-10-30 16:00.
- **Funcionalidades:** [[revisao-e-entrega-contexto]]
- **Notas geradas:** [[geral-decisao-2026-10-30-datas-dos-commits]], [[geral-decisao-2026-10-30-relato-de-uso-de-ia]], [[diario-2026-10-30-revisao-e-entrega]]
- **Concluída em:** 

### 🔗 Conexões
- Projeto: [[geral-contexto]]
- Mapa: [[moc-orquestra]]
- Regras: [[manual-da-orquestra]]
- Base: [[contrato-processo-e-plano]]
