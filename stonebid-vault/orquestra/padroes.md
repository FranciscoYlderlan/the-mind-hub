---
tipo: padroes
status: em-uso
criado: 2026-11-16
aliases: [padroes do projeto, padronização, bloco padroes]
---
# 📏 Padrões — Stonebid

> [!tldr] Em uma linha
> O bloco abaixo é lido pelo `cofre.py verificar`: termo fora do padrão, estado substituído (`antigo:`) e limite de palavras por nota dão ERRO.

```padroes
# termo fora do padrão => forma certa   ("re:" no início = expressão regular)
StoneBid => Stonebid (grafia do contrato-glossario)
re:[Ss]e(ç|c)(ão|ões|ao|oes) 0[1-6]\b => E1 a E6 (numeração do enunciado-teste-tecnico)
re:\bE[1-6]/E[1-6]\b => E1, E2 (vírgula, e só as seções onde o requisito está escrito)
re:\buse-(?!mobile\.)[a-z0-9-]+\.tsx?\b => useAlgo.ts (arquivo de hook em camelCase; só use-mobile.ts do shadcn fica)
# estado substituído (fora de diário, bug, decisão substituída e seções Histórico/Mudanças/Linha do tempo é ERRO):
# antigo: termo do estado antigo => estado atual (nota dona)
antigo: re:\b(4|quatro) dias\b => prazo de 2026-10-29 09:06 até a entrega, em 2026-10-30 16:00 (geral-decisao-2026-10-30-prazo-16h)
antigo: re:\b24 horas\b => prazo de 2026-10-29 09:06 até a entrega, em 2026-10-30 16:00 (geral-decisao-2026-10-30-prazo-16h)
antigo: re:T-01 a T-06 => T-01 a T-09 e T-10a sempre; T-10b com o OPC-2; T-11 com a RN-18 (geral-decisao-2026-10-29-testes-no-escopo)
antigo: re:(?i)só nas (tools|features) (com|que necessitam de) autenticação => api_key em toda conexão com o /mcp, em todos os ambientes (geral-decisao-2026-10-29-camada-mcp)
antigo: re:(?i)restrição por IP => api_key para conectar ao /mcp (geral-decisao-2026-10-29-camada-mcp)
antigo: re:(?i)copiad[ao]s? (do documento original )?sem reinterpretar => notas contrato-* com só o texto vigente (contrato-do-projeto)
antigo: re:texto da v0\.2 => notas contrato-* no texto vigente, v0.3 (contrato-do-projeto)
antigo: re:\bApp\.tsx\b => app.tsx (geral-decisao-2026-10-28-estrutura-frontend)
antigo: re:\buseCases/ => use-cases/ (geral-decisao-2026-10-28-estrutura-backend)
antigo: re:\b(React 19\.3|Vite 8\.3\.4|Tailwind CSS v4\.3|Fastify v5\.12\.7|Prisma v8|Vitest v5\.0\.5|Node 26\.13\.0|zod 4\.6)\b(?!\+| ou mais recente) => versão citada ou mais recente, sem trava (geral-decisao-2026-10-28-stack-frontend e geral-decisao-2026-10-28-stack-backend)
antigo: re:(?i)(só a Q-09 (já )?foi respondida|a Q-09 já foi respondida|quatorze perguntas abertas|API não escolhida) => Q-06, Q-07, Q-09, Q-10, Q-13 e Q-14 respondidas; API do Art Institute of Chicago (contrato-pontos-para-validar, geral-decisao-2026-10-29-api-de-itens)
antigo: re:\bPrisma (v)?8\b => Prisma 7.10.1+ (geral-decisao-2026-10-29-prisma-7)
antigo: re:(?i)Zustand[^|\n]{0,20}\btema\b|cookie `SameSite=None; Secure` ou token => tema no next-themes; sessão por JWT no cabeçalho (geral-decisao-2026-10-29-next-themes-para-o-tema, geral-decisao-2026-10-29-sessao-jwt-no-cabecalho)
antigo: re:2026-10-30 09:00 => entrega em 2026-10-30 16:00 (geral-decisao-2026-10-30-prazo-16h)
antigo: re:(?i)(sequência|seq)[^|\n]{0,40}(crescente |única )?por carteira => sequência global crescente no WalletMovement (geral-decisao-2026-10-29-sequencia-no-extrato)
antigo: re:/audits/:id|/auditoria/:lotId|audits/\$id => /lots/:id/audit (geral-decisao-2026-10-30-caminho-da-auditoria)
antigo: re:(?i)_public[^|\n]{0,10} nunca lê (a )?sessão => só a sala do lote lê a sessão já resolvida (geral-decisao-2026-10-30-sala-publica-le-a-sessao)
antigo: re:memória guarda padrões do projeto, planos => memória guarda padrões, workflow, andamento, planos, decisões e bugs (geral-decisao-2026-10-30-relato-de-uso-de-ia)
antigo: re:(?i)acesso à aplicação no ar:\*\* livre|fica no ar no máximo 7 dias => aplicação offline desde 2026-11-13; ficou no ar de 2026-10-29 a 2026-11-13 (acesso-de-teste)
antigo: re:projeto:(padronizacao|repositorios)|Regras deste projeto|seção "Repositórios e acesso" => regra do projeto em decisão de orquestra/funcionalidades/geral/ e este bloco em orquestra/padroes.md (geral-decisao-2026-11-16-repositorios-e-acesso e as demais de 2026-11-16)
limite-palavras: 2073
```

## Como usar
- Cada linha cita a nota dona: a decisão em `orquestra/funcionalidades/geral/` que fixou a regra.
- Despadronização achada: primeiro a regra (decisão + linha aqui), depois as notas.
- Mudou um estado: o antigo entra como linha `antigo:` (varredura de impacto, etapas B2 e B6).

## Regras deste cofre (cada uma em decisão)
- Grafia do nome: [[geral-decisao-2026-11-16-grafia-do-nome]].
- Documento-fonte e numeração: [[geral-decisao-2026-11-16-numeracao-do-enunciado]].
- Exceções de nome de arquivo (hooks do React, gerados ou exigidos por ferramenta): [[geral-decisao-2026-10-28-estrutura-frontend]] e [[geral-decisao-2026-10-28-estrutura-backend]].
- Limite de tamanho (`limite-palavras`): [[geral-decisao-2026-11-16-limite-de-tamanho]].
- Forma das notas de decisão: [[geral-decisao-2026-11-16-forma-das-notas-de-decisao]]; diário com partes: [[geral-decisao-2026-11-16-diario-com-partes]].

### 🔗 Conexões
- Índice: [[CLAUDE]]
- Mapa: [[moc-orquestra]]
- Regras: [[manual-da-orquestra]]
