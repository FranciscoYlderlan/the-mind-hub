---
aliases: [Requisitos funcionais, RF do Stonebid, Critérios de aceite, Functional requirements]
tags: [estudos/programacao]
tipo: referencia
tema: requisitos
status: rascunho
criado: 2026-10-29
origem: Contrato do Projeto Stonebid v0.2 (2026-10-27), seção 4
---
# 📜 Contrato: requisitos funcionais (RF)

> [!tldr] Em uma linha
> Cada serviço que o Stonebid oferece, com um critério de aceite que diz como provar que ficou pronto.

> [!warning] Mudança M-12 (2026-10-29)
> RF-51: a **tela** do comprovante mostra tudo o que está aqui; o **registro** guarda só o que não se deriva (item e link da auditoria vêm do lote e da rota), mais a contagem, o hash final e um selo. Detalhe em [[geral-decisao-2026-10-29-comprovante-e-hash]] ([[contrato-do-projeto-mudancas]]).

É o **cardápio com a foto do prato**: diz o que sai da cozinha e como o prato deve chegar à mesa. Seção 4 do [[contrato-do-projeto|contrato]] v0.2, copiada sem reinterpretar.

> [!info] Por que isso importa
> Um requisito funcional descreve um serviço que o sistema oferece. Sommerville lista qualidades de um bom requisito: ele deve ser verificável, sem ambiguidade, completo e consistente com os outros. Por isso cada RF abaixo tem um **critério de aceite**: uma forma concreta de testar se foi cumprido. Pressman chama essa etapa de validação dos requisitos. A coluna "Origem" mostra o que foi exigido pelo enunciado e o que foi inferido por este documento.

## 4.1 Contas e acesso

| ID | Requisito | Critério de aceite | Origem |
|---|---|---|---|
| RF-01 | Cadastro e login por e-mail e senha. Cada conta tem exatamente **um** papel: LEILOEIRO ou LICITANTE. | Criar duas contas de papéis diferentes. O login persiste ao recarregar a página. A senha nunca é guardada em texto puro. | E1, Prop. |
| RF-02 | O **servidor** DEVE bloquear ações fora do papel: leiloeiro não dá lance nem deposita; licitante não cria nem cancela lote; leiloeiro só gerencia os próprios lotes. | Chamar a API direto, sem usar a tela, com o papel errado retorna "proibido". Esconder o botão na tela não conta como proteção. | E1 |
| RF-03 | Vitrine, sala do lote (só leitura), auditoria e comprovante DEVEM abrir sem login. Dar lance exige login. | Em janela anônima, as quatro páginas abrem. O botão de lance leva ao login. | Prop. (Q-01) |

## 4.2 Vitrine

| ID | Requisito | Critério de aceite | Origem |
|---|---|---|---|
| RF-10 | Vitrine com três seções: **ao vivo**, **agendados** e **encerrados**. Lotes cancelados NÃO DEVEM aparecer. Cada card mostra imagem, título, lance atual (ou inicial) e contagem para início ou fim. | Com lotes nos quatro estados, aparecem três seções, e o cancelado não aparece em nenhuma. | E2 |
| RF-11 `[OPC-1]` | Busca por texto, filtros (estado, faixa de preço) e ordenação (encerra primeiro, mais recentes), com paginação. | Buscar um termo retorna só lotes cujo título ou atributos o contêm. Os filtros se combinam. | E5 |

## 4.3 Painel do leiloeiro

| ID | Requisito | Critério de aceite | Origem |
|---|---|---|---|
| RF-20 | Buscar itens na API externa e listar os resultados com imagem, título e atributos. | A busca retorna resultados. Com a API fora do ar, aparece uma mensagem clara e o resto do painel continua funcionando. | E2, E3 |
| RF-21 | Criar lote a partir de um item: imagem, título, atributos (copiados do item), lance inicial (> 0), incremento mínimo (> 0), início e fim (fim > início). | O lote criado aparece como agendado (ou ao vivo, se o início já passou). Os dados continuam disponíveis mesmo se a API sumir. | E1, E2 |
| RF-22 | Cancelar um lote que **ainda não recebeu lances**. | Cancelar um lote sem lances o remove da vitrine. Com lances, a ação é recusada com motivo (até o RF-23 existir). | E2 |
| RF-23 `[OPC-2]` | Cancelar um lote **com** lances, com estorno automático: o valor comprometido do líder volta ao saldo disponível. | Após o cancelamento, o disponível do líder volta ao valor anterior ao lance. O histórico continua auditável. | E5 |
| RF-24 | Ver o resultado de cada lote encerrado (arrematado ou sem vencedor, e o valor final) e o **total recebido**. | O total é a soma dos valores dos lotes arrematados e confere com o extrato do leiloeiro. | E2 |
| RF-25 | Listar os próprios lotes, por estado. | O leiloeiro A não vê lotes do leiloeiro B. | Prop. |

## 4.4 Sala do lote ao vivo

| ID | Requisito | Critério de aceite | Origem |
|---|---|---|---|
| RF-30 | Mostrar lance atual, histórico de lances, posição do usuário nos lances, contagem regressiva e um indicador claro de "você está ganhando" ou "você foi superado". | Com dois licitantes, o indicador de cada um muda corretamente a cada lance. | E2 |
| RF-31 | A sala DEVE se atualizar **sem recarregar a página**: novo lance, prorrogação, encerramento e cancelamento. | Com duas janelas abertas, um lance feito numa aparece na outra em até 2 segundos. | E2 |
| RF-32 | A contagem regressiva DEVE usar a hora do servidor e refletir as prorrogações. | Mudar o relógio do computador não altera a contagem. Após uma prorrogação, a contagem aumenta. | Prop. |
| RF-33 | O licitante dá lance informando um valor (a tela sugere o mínimo aceitável). | Lance válido atualiza a sala. Lance inválido mostra a mensagem do RF-70. | E2 |

## 4.5 Carteira do licitante

| ID | Requisito | Critério de aceite | Origem |
|---|---|---|---|
| RF-40 | Mostrar saldo **total**, **comprometido** e **disponível**. | Disponível = total − comprometido, sempre. Confere com o exemplo da seção 5.3. | E2 |
| RF-41 | Depósito simulado (valor > 0, com teto configurável). | O depósito aumenta o total. Um duplo clique não deposita duas vezes (RN-18). | E2 |
| RF-42 | Extrato de movimentos: depósito, comprometimento, liberação, débito, crédito e estorno. | Toda mudança de saldo tem uma linha no extrato. | Prop. |

## 4.6 Meus arremates

| ID | Requisito | Critério de aceite | Origem |
|---|---|---|---|
| RF-50 | Listar os lotes em que o usuário deu lance, com a situação: liderando, superado, arrematado, perdido ou cancelado. | Cada lote aparece na situação correta, inclusive depois do encerramento. | E2 |
| RF-51 | Gerar o **comprovante de arremate** na liquidação: item (cópia dos dados), valor, data e hora, pseudônimo do vencedor, hash final do histórico e link para a auditoria. | O comprovante existe para todo lote arrematado e não contém nome nem e-mail. | E1, E2 |
| RF-52 | Link público para compartilhar o comprovante, com identificador aleatório e impossível de adivinhar. | O link abre sem login. Trocar um caractere do link leva a "não encontrado". | E1, E2 |

## 4.7 Auditoria pública

| ID | Requisito | Critério de aceite | Origem |
|---|---|---|---|
| RF-60 | Página pública, por lote, com o histórico completo (ordem, pseudônimo, valor, horário), o resultado e o veredito **ÍNTEGRO** ou **ADULTERADO**. | Funciona sem login para lotes ao vivo, encerrados e cancelados. | E1, E2 |
| RF-61 | O veredito é **recalculado a cada acesso** (nunca guardado). Se for ADULTERADO, a página indica o primeiro registro inconsistente. | Editar um valor, apagar um lance, inserir um lance ou apagar o último lance direto no banco resulta em ADULTERADO. | E3 |

## 4.8 Mensagens de feedback

| ID | Requisito | Critério de aceite | Origem |
|---|---|---|---|
| RF-70 | Todo lance recusado DEVE devolver um motivo claro, em português. Motivos do enunciado: abaixo do mínimo, saldo insuficiente, você já está ganhando, lote ainda não iniciado, lote encerrado. Motivos adicionais: lote cancelado, papel não permitido, login necessário. | Cada motivo tem um teste. A mensagem inclui o valor mínimo atual quando for relevante. | E2, Prop. |

> [!tip] Quando abrir esta nota
> Ao montar o plano de uma funcionalidade ou o briefing de um implementador: copiar o RF e o critério de aceite para o "pronto quando".

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** todo RF tem critério de aceite; ele vira o "pronto quando" do plano e o teste de [[contrato-testes]].
* **Ponto 2:** autorização mora no servidor (RF-02); esconder botão não protege nada.
* **Ponto 3:** as páginas públicas abrem sem login e não chamam a API externa ([[contrato-regras-de-negocio]]).

### 🔗 Conexões
- Mapa: [[contrato-do-projeto]] · [[moc-orquestra]]
- Relacionadas: [[contrato-regras-de-negocio]], [[contrato-testes]], [[contrato-pontos-para-validar]]
- Próxima: [[contrato-regras-de-negocio]]
