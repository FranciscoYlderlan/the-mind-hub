---
aliases: [Enunciado do teste técnico, Teste técnico Elite Dev Verzel, Enunciado E1 a E6, Desafio da Verzel]
tags: [estudos/programacao]
tipo: referencia
tema: requisitos
status: em-uso
criado: 2026-10-29
origem: PDF "Teste técnico: Elite Dev na Verzel" (gerado em 2026-10-22), fornecido pelo humano
---
# 📄 Enunciado do teste técnico (Elite Dev na Verzel)

> [!tldr] Em uma linha
> O pedido original da Verzel: uma Casa de Leilões online com deploy obrigatório; é a fonte da verdade nº 1, acima do contrato.

É o **edital do concurso**: o resto (contrato, decisões, código) é a minha resposta a ele, e onde houver conflito o edital vence. Transcrição fiel do PDF, seguida do mapa contra o [[contrato-do-projeto|contrato]] e as decisões do cofre.

Arquivo original: [[teste-tecnico-elite-dev-verzel.pdf]]

## Transcrição

**Abertura.** Olá! Que bom ter você nesta etapa. Seu desafio é construir uma Casa de Leilões online, do jeito que faria no dia a dia de um time de desenvolvimento.

### E1. O desafio (proposta de solução)

Você deve criar uma Casa de Leilões online, onde um leiloeiro coloca itens em leilão e licitantes disputam cada lote com lances ao vivo. O que será leiloado é escolha sua: obras de arte, carros, cartas colecionáveis, discos, livros raros, o que você quiser, desde que os itens venham de uma API pública.

O leiloeiro monta um lote a partir de um item buscado na API externa que você escolheu, definindo lance inicial, incremento mínimo, horário de início e fim, e outros campos relevantes. O licitante deposita um saldo simulado na sua carteira, acompanha os lotes ao vivo, dá lances e, se vencer, recebe um comprovante de arremate que pode compartilhar por link. Qualquer pessoa, mesmo sem login, pode auditar o histórico de lances de um lote e verificar que ele não foi adulterado.

**Requisitos funcionais base**
- **Deploy:** o deploy da aplicação é **obrigatório**.
- **Usuários e autenticação:** a plataforma possui dois papéis distintos.
  - **Leiloeiro (vendedor):** cria e gerencia os próprios lotes. Não pode dar lances.
  - **Licitante (cliente):** deposita saldo, dá lances e arremata itens.
- **Referências** (para ver como esses fluxos costumam ser resolvidos; não copie, use como ponto de partida): catawiki.com/pt, liveauctioneers.com, superbid.net.

### E2. Front-End

| Tela | O que o enunciado pede |
|---|---|
| Vitrine de lotes | Interface que exibe os itens leiloados, separando lotes ao vivo, agendados e encerrados. Lotes cancelados não aparecem na vitrine. |
| Painel do leiloeiro | Permite buscar itens na API escolhida e criar um lote a partir deles (com imagem, título, atributos do item, data de início/fim e valor mínimo); cancelar um lote que ainda não recebeu lances; e ver o resultado de cada lote encerrado (se foi arrematado e por quanto) e o total recebido. |
| Sala do lote ao vivo | Exibe o lance atual, histórico de lances, posição do usuário nos lances, contagem regressiva e um indicador claro de "você está ganhando" / "você foi superado". Tudo atualizado sem recarregar a página. |
| Carteira do licitante | Mostra saldo total, saldo comprometido, saldo disponível e opção de depósito simulado. |
| Meus arremates | Interface onde o usuário vê os itens em que deu lance e os lotes vencidos, com o respectivo comprovante e link de compartilhamento. |
| Página de auditoria | Pública e sem login, mostra o histórico completo de lances de um lote e informa se ele está íntegro ou foi adulterado. |
| Mensagens de feedback | Mensagem clara para cada lance recusado, dizendo o motivo (abaixo do mínimo, saldo insuficiente, você já está ganhando, lote ainda não iniciado ou lote encerrado). |

### E3. Back-End

- **Gestão da API externa:** APIs têm limites e instabilidades. Sua aplicação não pode ficar inutilizável por causa disso. A vitrine, as salas, a auditoria e o comprovante devem continuar funcionando mesmo que a API caia.
- **Regras de lance:** só são aceitos em lotes ao vivo (entre início e fim). O primeiro lance deve ser ≥ ao lance inicial. Os seguintes devem ser ≥ ao lance atual + incremento mínimo. O licitante líder não pode cobrir o próprio lance.

| Tema | O que o enunciado pede |
|---|---|
| Saldo comprometido | Saldo disponível = saldo total − comprometido. Quando o licitante lidera, o valor fica comprometido; se superado, volta ao disponível imediatamente. O lance só é aceito se couber no disponível. |
| Prorrogação (anti-sniping) | Lance aceito nos últimos 2 minutos estende o fim do lote para +2 minutos. |
| Liquidação | Ao encerrar, debita-se o valor do vencedor e credita-se ao leiloeiro, gerando o comprovante. Lotes sem lances fecham sem vencedor. |
| Histórico à prova de adulteração | Qualquer alteração, remoção ou inserção posterior no histórico (mesmo direto no banco de dados) deve ser detectada pela auditoria. A técnica é escolha sua; explique-a. |
| Privacidade | A auditoria e o comprovante identificam licitantes sem expor dados pessoais. |

### E4. Tecnologias e requisitos

**Tecnologias obrigatórias**
- **Front-End:** React, com ou sem framework (Next.js, Vite, Remix ou o que preferir).
- **Back-End:** NodeJS ou Python. Fique à vontade com o framework (NestJS, Express, FastAPI, Django etc.).
- **Banco de dados:** PostgreSQL, MySQL ou um banco NoSQL (como MongoDB). Certifique-se de incluir no README instruções claras sobre como configurar e utilizá-lo.

**Requisitos não funcionais**
- **Prazo:** você tem 7 dias corridos a partir do recebimento deste desafio para completá-lo.
- **Dados de teste:** deixe semeados um leiloeiro, dois clientes e ao menos um lote publicado com lances abertos, para que possamos percorrer o fluxo sem montar tudo do zero.
- **Documentação:** o projeto deve incluir um README detalhado explicando o passo a passo para configurar e executar a aplicação. Funcionalidades com comportamento inesperado devem ser mencionadas. A ausência de explicações impactará negativamente na nota final.

### E5. Opcionais

Nenhum dos itens abaixo é obrigatório, mas todos são considerados na avaliação.
- Busca e filtro de lotes.
- Cancelamento de lote com estorno automático.
- Docker Compose.
- Testes automatizados.
- Dark Mode: interface com suporte a tema claro e escuro.

**Não precisa fazer:** nota fiscal, revenda entre usuários, aplicativo nativo ou recuperação de senha.

### E6. Como enviar

Envie pelo formulário `https://elitedev.verzel.com.br/?elite-dev-2026-2` preenchendo os campos assim:

| Campo | O que preencher |
|---|---|
| Nome completo e e-mail | Seus dados de contato. |
| Repositório | O link do repositório **público** no GitHub com a aplicação. |
| Tem mais de um repositório? | Se front e back estiverem separados, informe os dois. |
| Deploy | O link público da aplicação **(obrigatório)**. |
| Onde e como você usou IA | Usar IA é permitido. Conte onde e como usou e o que revisou ou ajustou. Se não usou, conte isso também. |

## 🗺️ Mapa: enunciado × planejamento (2026-10-29)

| Item do enunciado | Onde está no planejamento | Situação |
|---|---|---|
| E1 Deploy obrigatório | RNF-01, R-01 ([[contrato-requisitos-nao-funcionais]]) | Coberto no papel; **não iniciado**; hospedagem escolhida em 2026-10-29: GCP + Vercel ([[geral-decisao-2026-10-29-hospedagem]]) |
| E1 API pública de itens | RN-13, AD-06, Q-13 ([[contrato-tecnologias]]) | Coberto; **API não escolhida** |
| E1 Dois papéis | RF-01, RF-02, RN-06 | Coberto |
| E1 Lote com lance inicial, incremento, início, fim | RF-21 | Coberto |
| E1 Comprovante compartilhável | RF-51, RF-52 | Coberto |
| E1 Auditoria sem login | RF-03, RF-60 | Coberto |
| E2 Vitrine (cancelados ocultos) | RF-10 | Coberto |
| E2 Painel do leiloeiro | RF-20 a RF-24 | Coberto; "valor mínimo" = lance inicial é a proposta Q-06 |
| E2 Sala ao vivo sem recarregar | RF-30 a RF-33, AD-04 | Coberto; **mecanismo de tempo real não decidido** |
| E2 Carteira | RF-40, RF-41 | Coberto |
| E2 Meus arremates | RF-50 a RF-52 | Coberto |
| E2 Auditoria íntegro/adulterado | RF-60, RF-61 | Coberto |
| E2 Mensagens de feedback (5 motivos) | RF-70 | Coberto (e amplia com 3 motivos) |
| E3 API externa cai, resto funciona | RN-13, RNF-05, AD-06, T-07 | Coberto |
| E3 Regras de lance | RN-02 a RN-05, T-01 | Coberto |
| E3 Saldo comprometido | RN-07, RN-08, T-03 | Coberto |
| E3 Anti-sniping | RN-10, T-04 | Coberto; leitura de "+2 minutos" é a pergunta Q-03 |
| E3 Liquidação | RN-11, AD-08, T-05 | Coberto |
| E3 Histórico à prova de adulteração, explicado | RN-14, AD-05, T-06 ([[contrato-arquitetura]]) | Coberto, com a explicação pronta para o README |
| E3 Privacidade | RN-15, AD-09, T-09 | Coberto |
| E4 React / Node ou Python / banco | [[geral-decisao-2026-10-28-stack-frontend]], [[geral-decisao-2026-10-28-stack-backend]] | Coberto (Vite + React, Fastify, PostgreSQL) |
| E4 README com configuração do banco | RNF-03 | Coberto no papel |
| E4 Prazo de 7 dias | Prazo real de 24 horas ([[geral-contexto]]) | Coberto (prazo real menor) |
| E4 Dados de teste | RNF-02, Q-11 | Coberto |
| E4 Comportamentos inesperados no README | RNF-03, A-09 | Coberto |
| E5 Opcionais (5) | RF-11, RF-23, RNF-11, RNF-12, RNF-13 | Coberto; o contrato faz todos, o que não cabe em 24 horas |
| E5 Não precisa fazer | Fora do escopo (1.4) | Parcial: recuperação de senha está lá; nota fiscal, revenda e app nativo não estão listados |
| E1 Referências (Catawiki, LiveAuctioneers, Superbid) | — | Não citadas; são só inspiração |
| E6 Repositório **público** no GitHub (os dois, se separados) | [[geral-contexto]]: dois repositórios, criados em 2026-10-29 às 10:31 (conferir se estão públicos) | **Lacuna:** o contrato não fala em público nem em envio |
| E6 Link do deploy no formulário | RNF-01 | Coberto pelo deploy |
| E6 Onde e como usou IA, o que revisou ou ajustou | — | **Lacuna:** o contrato só cobre E1 a E5; não há registro planejado do uso de IA |

## 🤖 Interpretação do agente
(separada do enunciado; marcar [a confirmar] quando for suposição)
- O contrato cobre **todos** os requisitos de E1 a E5. As lacunas estão em E6: repositório público e o relato do uso de IA. Os diários do cofre já registram boa parte desse uso e podem virar o relato.
- O enunciado **não fala em live coding**. O que ele permite é usar IA, desde que o candidato conte onde, como e o que revisou.
- O enunciado não pede: camada MCP ([[geral-decisao-2026-10-29-camada-mcp]]), ambiente de staging, teste de cada tela com Playwright por outro agente ([[geral-decisao-2026-10-28-testes-frontend-playwright]]) nem a tabela de rastreabilidade. Com 24 horas, esses itens disputam tempo com o deploy, que é obrigatório. Em 2026-10-29 decidi mantê-los: a primeira etapa é deixar o projeto no ar ([[geral-contexto]]).
- "Do jeito que faria no dia a dia de um time de desenvolvimento" sugere que a avaliação olha também o processo: commits pequenos, README e CI ([[contrato-trabalho-com-a-ia]]) [a confirmar].

> [!tip] Quando abrir esta nota
> Sempre que o contrato e o enunciado parecerem divergir: o enunciado vence ([[contrato-trabalho-com-a-ia]], seção 13.2). E antes do envio, para conferir os campos do formulário.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** deploy e README pesam mais que qualquer opcional; os opcionais "são considerados", não obrigatórios.
* **Ponto 2:** no envio: repositórios **públicos**, link do deploy e o relato do uso de IA.
* **Ponto 3:** o mapa mostra que o contrato está alinhado; o risco é de tempo, não de escopo faltando.

### 🔗 Conexões
- Mapa: [[contrato-do-projeto]] · [[moc-orquestra]]
- Relacionadas: [[geral-contexto]], [[contrato-pontos-para-validar]], [[contrato-processo-e-plano]]
