---
aliases: [Questões extras de SQL, Extras da trilha, Variantes das operações, Extra SQL practice]
tags: [carreira/entrevistas, estudos/programacao]
tipo: referencia
tema: treino
status: em-uso
criado: 2026-11-06
origem: Criada pelo Claude em 2026-11-06 a pedido do humano; cada extra foi conferida na cópia do banco `compliance`
---
# 🔁 Trilha Didática de SQL: Extras

> [!tldr] Em uma linha
> Questões extras de cada módulo da [[trilha-sql-didatica]]: a mesma técnica de uma operação padrão já resolvida, numa situação diferente. Nenhuma ensina nada novo.

As extras são **o mesmo exercício de academia com outro peso na barra**. O movimento já foi aprendido na operação padrão; a extra só repete o movimento em outro lugar do banco para ele ficar automático. Quem pula uma extra não perde nenhum movimento.

---

> [!warning] Regras das extras
> - **Só se eu pedir**, depois da prática padrão do módulo. A IA entrega **uma por vez**, na ordem.
> - Cada extra diz de qual operação padrão é variante. Se eu travar, a IA me manda rever aquela operação, não ensina conteúdo novo.
> - **Nunca são mais difíceis nem mais importantes que as padrões.** Não fazer nenhuma extra não tira nada do que preciso para os drills.
> - Vão para o [[banco-mocado-plano-registro-sql]] com código `X` (ex.: `X3.2`), **fora do score do módulo**: contam só na evolução.
> - No cronograma, cada módulo reserva **1 bloco 15/5 opcional** para extras, depois da prática e antes da checagem. Dia apertado: é o primeiro bloco a sair ([[banco-mocado-plano]]).

## M0. Descobrir o banco
- **X0.1** (variante de O0.2) O que é uma linha de `alertas` e de `regras_monitoramento`?
- **X0.2** (variante de O0.3) Quais colunas de `socios_pj` apontam para `clientes`, e o que isso diz sobre uma PJ?
- **X0.3** (variante de O0.4 e O0.6) Na `stg_transacoes_bruto`, quais colunas parecem data e valor? Por que estão como texto?

## M1. Filtrar e ordenar
- **X1.1** (variante de O1.2) Clientes PJ do segmento CORPORATE, do maior para o menor `faturamento_anual`.
- **X1.2** (variante de O1.3) Débitos em TED acima de R$ 100 mil, os 15 maiores.
- **X1.3** (variante de O1.4) Transações de março de 2026, com o intervalo que respeita a hora.
- **X1.4** (variante de O1.5 e O1.6) Alertas das regras R02 e R05 que ainda estão ABERTO.

## M2. Agrupar e contar
- **X2.1** (variante de O2.2) Quantidade de contas por `tipo_conta` e `status`.
- **X2.2** (variante de O2.3) Soma e média de `valor_envolvido` dos alertas por regra.
- **X2.3** (variante de O2.5) Analistas com mais de 100 alertas ENCERRADO.
- **X2.4** (variante de O2.6) Quantidade de alertas por mês de `data_geracao`.

## M3. Juntar tabelas
- **X3.1** (variante de O3.1 e O3.3) Cada alerta com o nome do cliente e o nome da regra.
- **X3.2** (variante de O3.4) Soma de saques em espécie por cliente em 2026, os 10 maiores.
- **X3.3** (variante de O3.5) Remessas para países classificados como PARAISO_FISCAL, com o nome do cliente e do país.
- **X3.4** (variante da soma inflada da aula do M3) Juntar `contas` e `socios_pj` pelo cliente PJ e ver o que acontece com a contagem de contas.

## M4. O que falta
- **X4.1** (variante de O4.2) Países de `paises_risco` que nunca aparecem em `transacoes`, nas duas formas.
- **X4.2** (variante de O4.2) Clientes que nunca fizeram depósito nem saque em espécie.
- **X4.3** (variante de O4.4) Clientes com algum alerta da regra R03 (`IN` com subconsulta).
- **X4.4** (variante de O4.5) Clientes PF com `renda_mensal` acima da média dos PF.

## M5. Lógica e datas
- **X5.1** (variante de O5.1) Faixas de `score_risco` dos alertas (até 40, até 70, acima) e a contagem de cada uma.
- **X5.2** (variante de O5.2) Percentual de transações por `canal` dentro de cada `tipo` de transação.
- **X5.3** (variante de O5.3) Clientes de risco MEDIO sem revisão de KYC há mais de 18 meses.
- **X5.4** (variante de O5.4) Média de dias até o encerramento por analista.

## M6. Organizar com CTE
- **X6.1** (variante de O6.1) Reescrever a X3.2 como CTE.
- **X6.2** (variante de O6.2) Duas CTEs: alertas por cliente e volume por cliente; depois, alertas a cada R$ 1 milhão movimentado.
- **X6.3** (variante de O6.3) Clientes PF com créditos de 2026 acima de 12 vezes a `renda_mensal`.

## M7. Funções de janela
- **X7.1** (variante de O7.1) O alerta de maior `score_risco` de cada cliente.
- **X7.2** (variante de O7.2) Os 2 analistas com mais alertas dentro de cada regra.
- **X7.3** (variante de O7.3) Alertas por mês e a variação contra o mês anterior.
- **X7.4** (variante de O7.3) Contagem acumulada de alertas da regra R01 ao longo das datas.

## M8. Cara de case
- **X8.1** (variante de O8.1) Pares de saques em espécie da mesma conta no mesmo dia.
- **X8.2** (variante de O8.2) Sócios com participação de 50% ou mais em mais de uma PJ.
- **X8.3** (variante de O8.4) Documentos que aparecem em `clientes` e em `lista_restritiva`: a lista única com `UNION` e quantos estão nas duas.

> [!tip] Quando abrir esta nota
> Quando eu pedir mais prática num módulo, depois das operações padrão e antes da checagem.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** Extra é repetição em outra situação, nunca conteúdo novo.
* **Ponto 2:** Uma por vez, só se eu pedir, fora do score.
* **Ponto 3:** Pular as extras não tira nada do que os drills cobram.

### 🔗 Conexões
- Mapa: [[moc-orquestra]]
- Relacionadas: [[trilha-sql-didatica-avancado]], [[banco-mocado-plano-registro-sql]]
- Nota original: [[trilha-sql-didatica]]
