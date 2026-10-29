---
aliases: [Decisões de arquitetura do contrato, AD do Stonebid, Hash encadeado, HMAC, Lances simultâneos, Auditoria de adulteração]
tags: [estudos/programacao]
tipo: referencia
tema: arquitetura
status: rascunho
criado: 2026-10-29
origem: Contrato do Projeto Stonebid v0.2 (2026-10-27), seção 8
---
# 📜 Contrato: arquitetura (AD)

> [!tldr] Em uma linha
> As decisões de arquitetura propostas (AD-01 a AD-10), como a auditoria detecta adulteração e como lances simultâneos são tratados.

É o **projeto estrutural do prédio**: onde ficam as colunas que não se mexem depois. Seção 8 do [[contrato-do-projeto|contrato]] no texto vigente (v0.3). Os ADs aqui são **propostas**; viram decisão do cofre só com aval, numa nota `geral-decisao-*`.

> [!info] Por que isso importa
> Sommerville mostra que as decisões de arquitetura determinam o desempenho, a segurança e a manutenibilidade do sistema, e que cada decisão deve ser tomada comparando alternativas. Pressman apresenta os estilos arquiteturais e os conceitos de projeto (abstração, modularidade, separação de responsabilidades, ocultação de informação, baixo acoplamento e alta coesão). O princípio KISS ("mantenha simples"), citado por Pressman a partir de Hooker, vale em dobro com prazo de 24 horas. Anotar o porquê de cada decisão (o que, as alternativas, as consequências) também é prática de mercado conhecida como ADR.

| ID | Decisão | Alternativa descartada | Por quê | Status |
|---|---|---|---|---|
| AD-01 | **Monólito modular em camadas**: tela, API, domínio e dados | Microsserviços | Uma pessoa, 24 horas, uma unidade de deploy: menos peças para quebrar. | `[PROPOSTO]` |
| AD-02 | **Domínio isolado**: regras de lance, carteira, liquidação e auditoria num núcleo sem dependência de framework nem de banco | Regras espalhadas pelos controladores | Fica testável. A IA acerta mais quando o lugar de cada regra é claro. | `[PROPOSTO]` |
| AD-03 | Lances de um mesmo lote são **serializados** dentro de uma transação (RN-09) | Sem controle, ou uma fila externa | Sem isso, dois lances simultâneos quebram saldo e histórico (veja 8.2). | `[PROPOSTO]`. A técnica exata depende do banco: `[PENDENTE]` |
| AD-04 | **Mecanismo de tempo real** | Atualização periódica (polling), Server-Sent Events, WebSocket | Critérios: o servidor só precisa empurrar atualizações (o lance vai por requisição comum); o host do deploy precisa suportar a técnica; deve haver fallback simples. | `[PENDENTE]` (depende da stack) |
| AD-05 | **Auditoria por hash encadeado com selo HMAC** (veja 8.1) | Sem proteção, ou hash simples por registro | RN-14 e RF-61. | `[PROPOSTO]` |
| AD-06 | **Independência da API externa**: adaptador isolado, cópia do item no lote, cache e tempo limite na busca | Chamar a API em toda página | RN-13 e RNF-05. | `[PROPOSTO]` |
| AD-07 | **Dinheiro em centavos inteiros e livro de movimentos** (extrato) | Um campo "saldo" editado direto | É rastreável e auditável, e permite corrigir sem apagar o passado. | `[PROPOSTO]` |
| AD-08 | **Liquidação idempotente**, disparada por duas vias: um agendador e uma verificação "preguiçosa" quando alguém acessa o lote | Só o agendador | Hosts gratuitos podem "dormir" e um agendador parado deixaria lotes sem fechar. | `[PROPOSTO]` |
| AD-09 | **Pseudônimo público** do licitante por lote, derivado de forma irreversível | Mostrar o nome, ou um número sequencial global | Privacidade. Não dá para ligar o mesmo usuário entre lotes diferentes. | `[PROPOSTO]` |
| AD-10 | **Autorização por papel no servidor** | Esconder botões na tela | RF-02. A tela é só vitrine; a regra mora no servidor. | `[PROPOSTO]` |

Ligações com os livros: AD-01 e AD-02 (Sommerville: arquitetura em camadas e arquitetura × requisitos não funcionais; Pressman: separação de responsabilidades, modularidade, acoplamento e coesão). AD-03 (Sommerville: aplicações de processamento de transações e confiabilidade). AD-05, AD-09 e AD-10 (Sommerville: engenharia de segurança, que trata de confidencialidade, integridade e disponibilidade, da validação de toda entrada e de proteção em camadas). AD-06 (reuso de serviços de terceiros e o padrão de projeto *Adapter*, que ambos os livros situam entre os padrões de projeto). AD-08 (tolerância a falhas e confiabilidade).

## 8.1 Como a auditoria detecta adulteração (AD-05)

**Ideia, em linguagem simples.** Imagine um caderno em que cada página começa copiando a "assinatura" da página anterior, e a assinatura de cada página é calculada a partir do conteúdo dela mais a assinatura anterior. Se alguém altera a página 3, a assinatura da página 3 muda, e a página 4 passa a apontar para uma assinatura que não existe mais. A auditoria só precisa refazer as contas e achar a primeira página que não bate.

**Hash** é uma "impressão digital" de tamanho fixo calculada a partir de um conteúdo: mudou uma vírgula, muda tudo.

**Opções avaliadas:**

| Opção | Detecta edição | Detecta remoção ou inserção no meio | Resiste a quem refaz a cadeia inteira (acesso só ao banco) | Complexidade |
|---|---|---|---|---|
| Hash simples por registro | Só edição ingênua | Não | Não | Baixa |
| Hash encadeado | Sim | Sim | Não | Baixa |
| **Hash encadeado + selo HMAC (segredo fora do banco)** | Sim | Sim | **Sim** (sem o segredo) | Média-baixa |
| Assinatura digital assimétrica por registro | Sim | Sim | Sim | Média (gestão de chaves) |
| Árvore de Merkle | Sim | Sim | Não, sozinha | Média-alta |
| Âncora externa (publicar o hash fora do sistema) | Sim | Sim | Sim, até com o segredo | Alta |

**Proposta:** hash encadeado com selo HMAC. O hash de cada lance é calculado a partir de lote, ordem, pseudônimo do licitante, valor, instante e hash do lance anterior, e fica **guardado** no próprio lance. O lote guarda a **cabeça da cadeia** (número e hash do último lance, com selo), atualizada a cada lance; o comprovante guarda a contagem e o hash final com selo próprio. Campos e serialização: [[geral-decisao-2026-10-29-comprovante-e-hash]]. O selo HMAC usa um segredo guardado **fora do banco** (variável de ambiente do servidor).

**O que a página de auditoria confere:**

1. A numeração vai de 1 a n, sem buracos.
2. Para cada lance: o hash recalculado é igual ao guardado (senão, conteúdo editado), o selo confere e o hash anterior é o do lance anterior (senão, inserção ou remoção).
3. *n*, o último hash e o selo da cabeça batem com a cabeça do lote.
4. Se houver comprovante: o selo confere, a contagem e o hash final batem, e pseudônimo e valor batem com o último lance.
5. O vencedor e o valor batem com a liquidação e com o extrato.

**Pontos fracos e como cobri-los:**

- Quem tem acesso ao banco e conhece a fórmula poderia refazer a cadeia inteira. O selo HMAC, com segredo fora do banco, impede isso.
- Apagar só os **últimos** lances deixa uma cadeia "limpa", só que mais curta. Por isso a cabeça da cadeia fica no lote e a contagem e o hash final no comprovante, **sempre com selo**: sem o segredo, ninguém reescreve esse resumo para esconder o truncamento, nem com o lote ao vivo.
- **Prática:** o usuário do banco que a aplicação usa não deveria ter permissão de alterar ou apagar lances. É uma proteção em camadas.
- **Limite honesto:** quem tiver o banco **e** o segredo pode forjar o histórico. Só uma âncora externa resolveria, e ela está fora do escopo. Escreva esse limite no README: ele mostra que você entende a técnica.

> [!info] Por que isso importa
> Sommerville trata a *integridade* (dados que não podem ser alterados sem que se perceba) como um dos objetivos centrais de segurança. A ideia de proteger em camadas também vem de lá. A técnica específica (hash encadeado) é escolha sua, como diz o enunciado, mas o enunciado exige que você a **explique**. Por isso o porquê está registrado aqui.

## 8.2 Lances simultâneos (AD-03)

O lance atual é R$ 400 e o incremento mínimo é R$ 50. Ana e Bruno enviam R$ 500 no mesmo milissegundo. Sem controle, os dois podem ser aceitos como "o próximo lance", e o histórico e os saldos ficam inconsistentes. Com a serialização, um deles é processado primeiro (digamos, Ana). O lance de Bruno é então revalidado contra o novo lance atual: o mínimo passou a ser R$ 550, e ele recebe "abaixo do mínimo" com o novo valor.

**Como provar que funciona:** o teste T-02 dispara muitos lances em paralelo no mesmo lote e confere as invariantes do RNF-04.

## 8.3 Camadas `[PROPOSTO]`

- **Tela (React):** só apresentação. Não decide regra nenhuma.
- **API:** autenticação, autorização (AD-10), validação de entrada e tradução de erros em mensagens (RF-70).
- **Domínio:** estados do lote, regras de lance, carteira, anti-sniping, liquidação e verificação da auditoria (AD-02).
- **Dados:** banco de dados e livro de movimentos.
- **Adaptador da API externa:** isolado, com cache, tempo limite e cópia de imagens (AD-06).
- **Agendador:** dispara a liquidação (AD-08).

> [!tip] Quando abrir esta nota
> Antes de implementar lance, auditoria, liquidação ou o adaptador da API; e ao comparar com as decisões de estrutura ([[geral-decisao-2026-10-28-estrutura-backend]]).

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** auditoria por **hash encadeado + selo HMAC**, com o segredo fora do banco; o limite honesto vai para o README.
* **Ponto 2:** lances do mesmo lote serializados numa transação; T-02 prova ([[contrato-testes]]).
* **Ponto 3:** AD-04 (tempo real) segue `[PENDENTE]`; a escolha dependia da hospedagem ([[contrato-tecnologias]]), já decidida: o Cloud Run aceita WebSocket e SSE ([[geral-decisao-2026-10-29-hospedagem]]).

### 🔗 Conexões
- Mapa: [[contrato-do-projeto]] · [[moc-orquestra]]
- Relacionadas: [[contrato-regras-de-negocio]], [[contrato-modelo-de-dados]], [[contrato-riscos]], [[geral-decisao-2026-10-28-estrutura-backend]]
- Próxima: [[contrato-riscos]]
