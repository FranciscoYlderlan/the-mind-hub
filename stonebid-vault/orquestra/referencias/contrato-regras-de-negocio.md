---
aliases: [Regras de negócio, RN do Stonebid, Regras do leilão, Anti-sniping, Saldo comprometido, Liquidação]
tags: [estudos/programacao]
tipo: referencia
tema: requisitos
status: rascunho
criado: 2026-10-29
origem: Contrato do Projeto Stonebid v0.2 (2026-10-27), seção 5
---
# 📜 Contrato: regras de negócio (RN)

> [!tldr] Em uma linha
> As "leis" do leilão: estados do lote, quando um lance vale, saldo comprometido, anti-sniping, liquidação e histórico só de acréscimo.

São as **regras do jogo de futebol**: o juiz (o domínio) aplica, ninguém negocia no meio da partida. Seção 5 do [[contrato-do-projeto|contrato]] no texto vigente (v0.3).

> [!info] Por que isso importa
> Regras de negócio são as "leis" do domínio. Elas são a parte mais valiosa e mais frágil do sistema, e é onde a IA mais erra se a regra estiver vaga. Pressman recomenda que requisitos sejam elaborados e negociados até virarem uma especificação sem ambiguidade. Sommerville acrescenta a ideia de registrar o *porquê* de cada requisito. Por isso aqui cada regra é curta, numerada e testável.

## 5.1 Estados do lote

| Estado | Quando | Pode ir para |
|---|---|---|
| AGENDADO | agora < início | AO_VIVO (pelo relógio) ou CANCELADO |
| AO_VIVO | início ≤ agora < fim | ENCERRADO (pelo relógio) ou CANCELADO (sem lances; com lances, só se `[OPC-2]`) |
| ENCERRADO | agora ≥ fim (o fim pode ter sido prorrogado) | Estado final: resultado ARREMATADO ou SEM_VENCEDOR |
| CANCELADO | O leiloeiro cancelou | Estado final |

> [!note] Corrigido na v0.3 (M-13)
> A linha AO_VIVO dizia "CANCELADO (se `[OPC-2]` e houver lances)" e perdia o caso base do RF-22 e da RN-12. Corrigida em 2026-10-29: [[geral-decisao-2026-10-29-cancelamento-ao-vivo]].

Os estados agendado, ao vivo e encerrado **derivam do relógio do servidor**. O cancelamento e o resultado da liquidação são **gravados**.

## 5.2 Regras

| ID | Regra | Origem |
|---|---|---|
| RN-01 | O estado do lote é derivado do relógio do servidor. Só o cancelamento e o resultado da liquidação são gravados. | Prop. |
| RN-02 | Um lance só é aceito se início ≤ agora < fim e o lote não está cancelado. Um lance no instante exato do fim é recusado (Q-04). | E3 |
| RN-03 | O **primeiro** lance DEVE ser maior ou igual ao lance inicial. | E3 |
| RN-04 | Os lances **seguintes** DEVEM ser maiores ou iguais ao lance atual + incremento mínimo. | E3 |
| RN-05 | O licitante que lidera NÃO PODE cobrir o próprio lance. | E3 |
| RN-06 | Só LICITANTE dá lance. O leiloeiro NUNCA dá lance. | E1 |
| RN-07 | Disponível = total − comprometido. **Comprometido** = soma dos lances em que o usuário é líder neste momento. Um lance só é aceito se o valor couber no disponível. | E3 |
| RN-08 | Quando um lance é superado, o valor do antigo líder volta ao disponível **imediatamente**, na mesma operação que registra o novo lance. | E3 |
| RN-09 | Registrar um lance é uma operação **indivisível**: validar, gravar o lance, atualizar o lance atual, comprometer e liberar saldo, e prorrogar se for o caso. Lances do mesmo lote são processados **um por vez**. Se dois chegam juntos, um é aceito e o outro é revalidado contra o novo lance atual. | Prop. (deriva de E3) |
| RN-10 | **Anti-sniping:** um lance aceito quando faltam 2 minutos ou menos move o fim para o instante do lance + 2 minutos (o fim nunca diminui). Sem limite de prorrogações. `[PROPOSTO]` (Q-03) | E3 |
| RN-11 | **Liquidação** no encerramento. Com lances: o valor comprometido do vencedor vira débito, o leiloeiro é creditado, o comprovante é gerado e o lote fica ARREMATADO. Sem lances: o lote fecha sem vencedor. A liquidação executa **exatamente uma vez** por lote, mesmo se for disparada duas vezes. | E3 |
| RN-12 | **Cancelamento** só antes do encerramento. Base: só se não há lances. Com `[OPC-2]`: se há lances, o valor comprometido do líder é liberado, o motivo é registrado e o histórico continua auditável (Q-05). | E2, E5 |
| RN-13 | Os dados do item vêm da API externa **só na busca do painel**. Ao criar o lote, os dados do item, inclusive a **imagem**, são copiados para o sistema. Vitrine, sala, auditoria e comprovante NÃO DEVEM chamar a API externa. | E3 |
| RN-14 | O histórico de lances é **só de acréscimo**: nunca é editado nem apagado pela aplicação. Cada registro é encadeado ao anterior por hash (AD-05). | E3 |
| RN-15 | Páginas públicas e comprovante NÃO DEVEM expor nome, e-mail ou qualquer dado pessoal. Licitantes aparecem por um **pseudônimo** estável dentro do lote (AD-09). | E3 |
| RN-16 | Dinheiro é guardado em **centavos inteiros** (reais simulados). Nunca em ponto flutuante. | Prática |
| RN-17 | O servidor é a única fonte da hora. Datas ficam em UTC no banco e são exibidas no fuso do usuário. | Prática |
| RN-18 | Depósito e lance são **idempotentes**: repetir a mesma requisição (duplo clique, nova tentativa de rede) não duplica o efeito. | Prática |

## 5.3 Exemplo da carteira (RN-07 e RN-08)

Ana deposita R$ 1.000. Acompanhe o saldo dela a cada passo:

| Passo | O que acontece | Total | Comprometido | Disponível |
|---|---|---|---|---|
| 1 | Ana deposita R$ 1.000 | 1.000 | 0 | 1.000 |
| 2 | Ana lidera o lote A com R$ 300 | 1.000 | 300 | 700 |
| 3 | Ana lidera o lote B com R$ 500 | 1.000 | 800 | 200 |
| 4 | Ana tenta dar R$ 300 no lote C: recusado, saldo insuficiente (só há R$ 200 disponíveis) | 1.000 | 800 | 200 |
| 5 | Bruno cobre Ana no lote A com R$ 350. Os R$ 300 dela voltam na hora | 1.000 | 500 | 500 |
| 6 | O lote B encerra e Ana vence. Os R$ 500 viram débito e o leiloeiro recebe R$ 500 | 500 | 0 | 500 |

## 5.4 Exemplo do anti-sniping (RN-10)

O lote termina às 20:00:00. Um lance aceito às 19:58:30 (faltando 1 min 30 s) prorroga o fim:

- **Opção A (proposta):** novo fim = instante do lance + 2 min = **20:00:30**.
- **Opção B:** novo fim = fim atual + 2 min = **20:02:00**.

Um lance às 19:50:00 não prorroga nada. O enunciado não deixa claro qual das opções vale; a escolha está em Q-03 e deve ser registrada no README.

> [!tip] Quando abrir esta nota
> Antes de mexer em lance, carteira, liquidação, cancelamento ou auditoria: estas são as áreas sensíveis do projeto.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** registrar um lance é **indivisível** e serializado por lote (RN-09); a técnica está em [[contrato-arquitetura]].
* **Ponto 2:** dinheiro em centavos inteiros, liquidação exatamente uma vez, depósito e lance idempotentes.
* **Ponto 3:** RN-10 (opção A ou B) e o lance no instante do fim ainda dependem de [[contrato-pontos-para-validar]].

### 🔗 Conexões
- Mapa: [[contrato-do-projeto]] · [[moc-orquestra]]
- Relacionadas: [[geral-decisao-2026-10-29-cancelamento-ao-vivo]], [[contrato-requisitos-funcionais]], [[contrato-arquitetura]], [[contrato-testes]], [[contrato-modelo-de-dados]]
- Próxima: [[contrato-requisitos-nao-funcionais]]
