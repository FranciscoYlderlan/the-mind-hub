---
aliases: [Riscos do projeto, Riscos do Stonebid, RMMM, Project risks]
tags: [estudos/programacao]
tipo: referencia
tema: gestao
status: rascunho
criado: 2026-10-29
origem: Contrato do Projeto Stonebid v0.2 (2026-10-27), seção 9
---
# 📜 Contrato: riscos (R)

> [!tldr] Em uma linha
> Os onze riscos do projeto, cada um com mitigação e o sinal de alerta que mostra que ele está acontecendo.

É o **guarda-chuva na mochila**: decidido antes de sair de casa, não quando começa a chover. Seção 9 do [[contrato-do-projeto|contrato]] no texto vigente (v0.3).

> [!note] Situação do R-02
> O risco já se materializou em parte: três dias passaram só com requisitos e arquitetura, e o prazo ficou em **24 horas** a partir de 2026-10-29 09:06 ([[geral-contexto]]).

> [!info] Por que isso importa
> Pressman distingue a estratégia *reativa* (esperar o problema aparecer) da *proativa* (listar riscos antes, estimar probabilidade e impacto, e planejar mitigação, monitoramento e contingência, o chamado RMMM). Sommerville descreve o mesmo ciclo: identificar, analisar, planejar e monitorar os riscos. Probabilidade e impacto abaixo são **estimativas qualitativas minhas**; revise-as.

| ID | Risco | Prob. | Impacto | Mitigação | Sinal de alerta |
|---|---|---|---|---|---|
| R-01 | Deploy deixado para o fim e falhar | Média | Alta | Deploy no primeiro incremento (I0) com a aplicação "vazia". Cada incremento vai para produção. | O I0 terminou sem URL no ar |
| R-02 | Estourar o prazo de 24 horas | Alta | Alta | Incrementos pequenos, núcleo primeiro e linha de corte (11.4) | Na metade do prazo, RN-02 a RN-09 sem testes passando |
| R-03 | API externa lenta, com limite de chamadas ou fora do ar | Média | Média | Escolher API sem chave e com imagens estáveis. Cópia do item, cache e tempo limite (AD-06). | Respostas de erro 429 ou 5xx já no I0 |
| R-04 | Condição de corrida nos lances | Média | Alta | AD-03 e teste T-02 | Saldo negativo ou dois "líderes" num teste |
| R-05 | Tempo real não funcionar no host do deploy | Média | Média | Testar no ambiente real já no I0. Ter fallback por polling. | A conexão cai poucos segundos depois de abrir |
| R-06 | Lote não liquidar (agendador parado, servidor "dormindo") | Média | Alta | AD-08 (liquidação também no acesso) e teste T-05 | Lote com fim vencido ainda aparecendo como ao vivo |
| R-07 | Auditoria não detectar algum tipo de adulteração | Média | Alta | AD-05 e T-06 (editar, apagar no meio, inserir, apagar o último) | Algum caso do T-06 resulta em ÍNTEGRO |
| R-08 | A IA gerar código que foge do contrato ou quebra regras | Alta | Média | Seção 13, incrementos pequenos, testes junto e revisão sua | Alterações enormes, regra no lugar errado, teste alterado só para passar |
| R-09 | Curva de aprendizado de alguma tecnologia | Média | Média | Usar o que você já conhece sempre que possível. Limitar um "spike" de estudo a 1 hora. | Mais de 1 hora travado na mesma coisa |
| R-10 | Dados de teste vencidos na hora da avaliação (o lote "ao vivo" já encerrou) | Média | Média | Q-11: lote do seed cobre o período de avaliação, mais um comando de reset | Lote do seed já encerrado |
| R-11 | Escopo inflado por entusiasmo | Média | Média | Seção 1.4 e o protocolo de mudança (13.4) | "Só mais uma coisinha…" |

> [!tip] Quando abrir esta nota
> No fim de cada incremento do plano: conferir se algum sinal de alerta apareceu.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** deploy no I0 (R-01) e teste do tempo real no host real (R-05).
* **Ponto 2:** os riscos de impacto alto são prazo, corrida nos lances, liquidação e auditoria ([[contrato-arquitetura]]).
* **Ponto 3:** escopo inflado se controla com o protocolo de [[contrato-trabalho-com-a-ia]].

### 🔗 Conexões
- Mapa: [[contrato-do-projeto]] · [[moc-orquestra]]
- Relacionadas: [[contrato-processo-e-plano]], [[contrato-testes]], [[contrato-arquitetura]]
- Próxima: [[contrato-testes]]
