---
aliases: [Testes do contrato, T-01 a T-11, Rastreabilidade, Estratégia de testes]
tags: [estudos/programacao]
tipo: referencia
tema: testes
status: rascunho
criado: 2026-10-29
origem: Contrato do Projeto Stonebid v0.2 (2026-10-27), seção 10
---
# 📜 Contrato: qualidade e testes (T)

> [!tldr] Em uma linha
> Os testes (T-01 a T-11) que provam as regras críticas (dinheiro, concorrência e auditoria) e a tabela que liga requisito, teste e entrega.

É a **prova dos nove** da conta de cabeça: o resultado só vale depois de conferido. Seção 10 do [[contrato-do-projeto|contrato]] no texto vigente (v0.3).

> [!info] Por que isso importa
> Sommerville descreve três níveis de teste: **de desenvolvimento** (unidades, componentes e sistema), **de release** (o sistema como um todo, contra os requisitos) e **de usuário**. Ele também apresenta o desenvolvimento dirigido por testes (escrever o teste antes do código) e o teste de regressão (rodar tudo de novo para ver se algo quebrou). Pressman organiza a estratégia em teste de unidade, de integração, de validação e de sistema. Os dois dizem, em essência, a mesma coisa: **derive os testes dos requisitos**. A estratégia aqui é dar mais testes ao que mais dói se quebrar: dinheiro, concorrência e auditoria.

O teste só sai do escopo junto com o requisito que prova ([[geral-decisao-2026-10-29-testes-no-escopo]]).

| ID | Teste | Garante |
|---|---|---|
| T-01 | Regras de lance: primeiro lance, incremento mínimo, líder cobrindo a si mesmo, janela de tempo | RN-02 a RN-06 |
| T-02 | Muitos lances paralelos no mesmo lote | RN-09, RNF-04 |
| T-03 | Invariantes de saldo, incluindo o exemplo da Ana (5.3) | RN-07, RN-08 |
| T-04 | Anti-sniping, incluindo o lance exatamente 2 minutos antes e depois do fim | RN-10 |
| T-05 | Liquidação exatamente uma vez, com e sem lances, e com disparo duplo | RN-11 |
| T-06 | Auditoria: lote íntegro; valor editado; lance apagado no meio; lance inserido; último lance apagado | RN-14, RF-61 |
| T-07 | API externa fora do ar: vitrine, sala, auditoria e comprovante funcionam | RN-13, RNF-05 |
| T-08 | Autorização por papel chamando a API direto | RF-02, RN-06 |
| T-09 | Respostas públicas e comprovante sem dados pessoais | RN-15, RNF-08 |
| T-10a | Cancelamento sem lances, e recusa quando há lances | RN-12, RF-22 |
| T-10b | Cancelamento com lances e estorno (sai junto com o OPC-2) | RN-12, RF-23 |
| T-11 | Idempotência de depósito e de lance (sai só se a RN-18 for afrouxada) | RN-18 |

## Rastreabilidade

Cada requisito deve poder ser seguido até o teste que o prova e até a entrega que o implementou. Pressman chama isso de tabela de rastreabilidade (faz parte do gerenciamento de requisitos). Mantenha uma tabela simples como esta, preenchida ao longo do projeto:

| Requisito | Teste | Incremento | Commit ou PR |
|---|---|---|---|
| RN-04 | T-01 | I2 | |
| RN-10 | T-04 | I3 | |
| RF-61 | T-06 | I4 | |

> [!tip] Quando abrir esta nota
> Ao escrever o "pronto quando" de uma tarefa de backend e ao briefar um verificador: o T-xx da regra entra junto.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** mais testes onde mais dói: dinheiro, concorrência e auditoria ([[contrato-regras-de-negocio]]).
* **Ponto 2:** o teste só sai junto com o requisito que prova: T-01 a T-09 e T-10a ficam sempre; T-10b sai com o OPC-2 e T-11 com a RN-18 (M-11, [[geral-decisao-2026-10-29-testes-no-escopo]]).
* **Ponto 3:** no backend os testes rodam com Vitest ([[geral-decisao-2026-10-28-stack-backend]]); no frontend, Playwright por outro agente ([[geral-decisao-2026-10-28-testes-frontend-playwright]]).

### 🔗 Conexões
- Mapa: [[contrato-do-projeto]] · [[moc-orquestra]]
- Relacionadas: [[geral-decisao-2026-10-29-testes-no-escopo]], [[contrato-requisitos-funcionais]], [[contrato-requisitos-nao-funcionais]], [[contrato-regras-de-negocio]]
- Próxima: [[contrato-processo-e-plano]]
