---
aliases: [Visão e escopo, Fora do escopo, Restrições do projeto, Papéis do StoneBid]
tags: [estudos/programacao]
tipo: referencia
tema: requisitos
status: rascunho
criado: 2026-10-29
origem: Contrato do Projeto Stonebid v0.2 (2026-10-27), seções 1, 2 e 3
---
# 📜 Contrato: visão, escopo, restrições e papéis

> [!tldr] Em uma linha
> O que o StoneBid é, o que fica fora, os limites fixos (prazo de 24 horas, os 5 opcionais) e quem usa o sistema.

É a **cerca do terreno**: mostra até onde a obra vai e o que fica do lado de fora. Seções 1 a 3 do [[contrato-do-projeto|contrato]] v0.2, copiadas sem reinterpretar.

> [!warning] Prazo mudou em 2026-10-29
> O prazo real passou de 4 dias para **24 horas** (a partir de 2026-10-29 09:06). Onde esta nota fala em 4 dias, vale o prazo novo; o texto do contrato segue como estava até a v0.3. Fato registrado em [[geral-contexto]].

## 1. Visão e escopo

### 1.1 O que é

O **Stonebid** é uma casa de leilões online. O leiloeiro monta lotes a partir de itens de uma API pública, e licitantes disputam cada lote com lances ao vivo, usando um saldo simulado. Quem vence recebe um comprovante compartilhável por link. Qualquer pessoa, **sem login**, pode auditar o histórico de lances de um lote e verificar se ele foi adulterado. A aplicação precisa estar no ar (deploy).

### 1.2 Objetivos de sucesso

1. Cumprir todos os requisitos base e os 5 opcionais em 4 dias.
2. Ter uma base sólida: nada de desmoronar nas etapas finais (deploy no dia 1, regras críticas testadas).
3. Ter um projeto de portfólio explicável: decisões documentadas e README claro.
4. Aprender: cada decisão tem um porquê e uma base teórica.
5. Ter um contrato que humano e IA conseguem ler e seguir.

### 1.3 Dentro do escopo

Contas e papéis, vitrine, painel do leiloeiro, sala do lote ao vivo, carteira, meus arremates, auditoria pública, mensagens de feedback, regras de lance, saldo comprometido, anti-sniping, liquidação, histórico à prova de adulteração, privacidade, resiliência à API externa, deploy, dados de teste, README e os 5 opcionais.

### 1.4 Fora do escopo `[PROPOSTO]`

Tudo abaixo não foi pedido e custaria tempo que você não tem. Só entra se o contrato mudar (seção 13.4).

| Fora do escopo | Por quê |
|---|---|
| Pagamento real e saque | O saldo é simulado |
| E-mails, notificações push | Não pedido |
| Recuperação de senha, verificação de e-mail | Não pedido |
| Editar um lote depois de criado (só cancelar) | Não pedido, aumenta as regras |
| Mais de um item por lote | Simplifica o modelo |
| Lance automático até um teto (proxy bidding) | Não pedido |
| Painel de administrador e moderação | Só há dois papéis |
| Frete, entrega, múltiplos idiomas | Fora do tema |

### 1.5 O projeto em uma página (W5HH)

| Pergunta | Resposta |
|---|---|
| Por que (*Why*)? | Passar no teste técnico e construir um projeto de portfólio |
| O que (*What*)? | Casa de leilões online com lances ao vivo, carteira, comprovante e auditoria |
| Quando (*When*)? | 24 horas a partir de 2026-10-29 09:06 (v0.3; eram 4 dias na v0.2). Entrega: **2026-10-30 09:00** |
| Quem (*Who*)? | Você (decide e responde pelo projeto) e a IA (implementa e explica) |
| Onde (*Where*)? | Repositório de código e aplicação em produção (URL no README) |
| Como (*How*)? | Entrega incremental com testes nas regras críticas (seção 11) |
| Quanto (*How much*)? | Trabalho contínuo, sem pausa, nas 24 horas; infraestrutura gratuita ou de baixo custo |

> [!info] Por que isso importa
> Pressman descreve a atividade de *comunicação* como o começo do trabalho: entender o problema, quem é afetado e qual é o objetivo, antes de construir qualquer coisa. Ele também apresenta o princípio W5HH (de Barry Boehm): sete perguntas que definem um projeto. Sommerville trata a engenharia de requisitos de forma parecida: primeiro entender o que o sistema deve fazer e onde ele termina. Os dois livros tratam a mudança de requisitos como inevitável e pedem que ela seja controlada. Daí vêm a lista "fora do escopo" e o protocolo de mudança da seção 13.4. O princípio de Hooker "a razão de tudo existir" (citado por Pressman) diz o mesmo: todo requisito deve servir ao objetivo do sistema.

## 2. Restrições e premissas

| Restrição | Valor | Status | Origem |
|---|---|---|---|
| Prazo | 4 dias (enunciado: 7) | `[DECIDIDO]` | Você |
| Opcionais | Todos os 5 serão feitos | `[DECIDIDO]` | Você |
| Deploy | Obrigatório | `[DECIDIDO]` | E1/E2 (quadro "Deploy") |
| Front-end | React, com ou sem framework | `[DECIDIDO]` | E4 |
| Back-end | Node.js ou Python | `[DECIDIDO]` | E4 |
| Banco de dados | PostgreSQL, MySQL ou NoSQL (ex.: MongoDB) | `[DECIDIDO]` | E4 |
| Itens do leilão | Devem vir de uma API pública | `[DECIDIDO]` | E1 |
| Documentação | README detalhado, com comportamentos inesperados explicados | `[DECIDIDO]` | E4 |
| Dados de teste | 1 leiloeiro, 2 clientes e ao menos 1 lote publicado com lances abertos | `[DECIDIDO]` | E4 |
| Desenvolvimento com IA | Permitido (*vibe coding*) | `[DECIDIDO]` | Você |
| Versões das tecnologias | As mais recentes; você escolhe e preenche na seção 12 | `[PENDENTE]` | Você |
| Autor | Júnior; aprender é um objetivo do projeto | `[DECIDIDO]` | Você |
| Nome e repositórios | Stonebid, com `stonebid-web` (front-end) e `stonebid-api` (back-end) | `[DECIDIDO]` | Você |

> [!info] Por que isso importa
> Sommerville classifica o prazo e as regras da organização como requisitos não funcionais "organizacionais": eles limitam o projeto, mas não aparecem na tela. Pressman e Sommerville tratam escopo, prazo, recursos e qualidade como forças que se compensam. Com o prazo fixo, o que se ajusta é o escopo e a ordem de entrega. Por isso o plano (seção 11) tem uma **linha de corte** definida de antemão.

## 3. Papéis (quem usa o sistema)

| Papel | Pode | Não pode |
|---|---|---|
| **Leiloeiro** (vendedor) | Buscar itens na API, criar e cancelar os próprios lotes, ver resultados e total recebido | Dar lances, depositar saldo, mexer em lotes de outro leiloeiro |
| **Licitante** (cliente) | Depositar saldo, dar lances, arrematar, ver arremates e comprovantes | Criar ou cancelar lotes |
| **Visitante** (sem login) | Ver a vitrine, a sala (só leitura), a auditoria e comprovantes compartilhados | Dar lances, depositar |
| **Avaliador** | Percorre o fluxo com os dados de teste | (não é usuário do sistema, mas é quem o julga) |

> [!info] Por que isso importa
> Sommerville e Pressman pedem para identificar, logo no início, todas as partes interessadas (*stakeholders*) no sistema. Requisitos esquecidos quase sempre vêm de um papel que ninguém lembrou. Aqui o avaliador e o visitante anônimo (que audita) são tão importantes quanto os dois papéis do enunciado.

> [!tip] Quando abrir esta nota
> Quando surgir "e se a gente fizesse também...": conferir o fora do escopo antes e, se for entrar, seguir o protocolo de mudança em [[contrato-trabalho-com-a-ia]].

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** prazo real de **24 horas** (entrega em 2026-10-30 09:00), com os 5 opcionais; o corte de emergência está em [[contrato-processo-e-plano]].
* **Ponto 2:** dois papéis no sistema (leiloeiro e licitante), mais o visitante sem login que audita.
* **Ponto 3:** tudo fora do escopo só entra mudando o contrato.

### 🔗 Conexões
- Mapa: [[contrato-do-projeto]] · [[moc-orquestra]]
- Relacionadas: [[contrato-requisitos-funcionais]], [[contrato-pontos-para-validar]]
- Próxima: [[contrato-requisitos-funcionais]]
