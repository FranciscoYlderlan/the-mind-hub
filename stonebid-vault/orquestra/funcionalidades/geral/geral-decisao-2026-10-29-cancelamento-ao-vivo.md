---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-10-29
substitui: 
aliases: [Cancelamento ao vivo, Cancelar lote ao vivo sem lances, Tabela 5.1 corrigida, Live lot cancellation]
---
# ✅ Lote ao vivo sem lances pode ser cancelado até o fim, sem depender do OPC-2 (M-13)

- **Proposta (plano):** sugestão da IA no chat de 2026-10-29 (12:24–13:31), a partir de uma divergência apontada pelo humano: a tabela 5.1 de [[contrato-regras-de-negocio]] dizia que AO_VIVO só vai para CANCELADO "se `[OPC-2]` e houver lances", enquanto o RF-22 ([[contrato-requisitos-funcionais]]) e a RN-12 permitem cancelar qualquer lote sem lances até o encerramento, o que inclui um lote ao vivo ainda sem lance.
- **Decisão:** humano aprovou em 2026-10-29 13:31 ("vamos deixar os dois casos").
  - Linha AO_VIVO da tabela 5.1: "ENCERRADO (pelo relógio) ou CANCELADO (sem lances; com lances, só se `[OPC-2]`)".
  - O RF-22, o RF-23 e a RN-12 ficam como estão: a tabela passa a dizer o mesmo que eles.
  - **Uma função só** no domínio decide o cancelamento, para lote agendado e ao vivo, e devolve o motivo da recusa:
    1. lote já cancelado → "lote já cancelado";
    2. `agora >= fimAtual` (hora do servidor) → "lote encerrado";
    3. há lances e o `[OPC-2]` está desligado → "lote já recebeu lances";
    4. senão → cancela (com estorno ao líder, RF-23, se houver lances).
  - O `[OPC-2]` é um **sinalizador de configuração**: desligado, vale só o caso base.
  - **Concorrência:** o cancelamento usa a mesma serialização por lote do lance (RN-09): trava a linha do lote e, já com a trava, conta os lances e compara com o `fimAtual`, que uma prorrogação pode ter mudado.
    - Lance chegou antes: sem o `[OPC-2]`, cancelamento recusado com o motivo; com o `[OPC-2]`, segue o estorno.
    - Cancelamento chegou antes: o lance é recusado com "lote cancelado" (RF-70).
    - Cancelar no instante exato do fim é recusado, como o lance na Q-04.
    - A liquidação também trava o lote e ignora lote cancelado: nenhum lote fica cancelado e "sem vencedor" ao mesmo tempo.
- **Alteração:** nenhuma.
- **Motivo:**
  - O enunciado vence o contrato (seção 13.2 de [[contrato-trabalho-com-a-ia]]): o E2 pede cancelar lote "que ainda não recebeu lances", sem limitar o estado. O RF-22 e a RN-12 já diziam isso; só a tabela 5.1 divergia.
  - A célula da tabela trazia só a extensão do opcional e perdeu o caso base. O erro vem do contrato v0.2 (a nota copia a seção 5 sem reinterpretar).
  - Seguindo a tabela, um lote ao vivo sem lances não poderia ser cancelado, mas com lances poderia: o opcional permitiria mais que o requisito base.
  - Com o prazo até 2026-10-30 16:00, o `[OPC-2]` é o item com mais chance de cair; o cancelamento sem lances precisa funcionar sem ele.
- **Consequências:**
  - Lote cancelado guarda `cancelado_em` e o motivo (obrigatório também sem lances) e congela a cabeça da cadeia, como na liquidação ([[geral-decisao-2026-10-29-comprovante-e-hash]]). Lote sem lances: cadeia vazia, auditoria ÍNTEGRO com "cancelado em…".
  - A sala ao vivo recebe o evento de cancelamento sem recarregar (RF-31), fecha o formulário de lance e mostra o aviso; o lote sai da seção "ao vivo" da vitrine (RF-10).
  - O T-10a ([[contrato-testes]], [[geral-decisao-2026-10-29-testes-no-escopo]]) cobre: lote ao vivo sem lances cancelado; lote ao vivo com lances e sem o `[OPC-2]` recusado; cancelamento e lance ao mesmo tempo (só um passa); cancelamento no instante do fim recusado.
  - Proibido: regra de cancelamento espalhada por rota ou tela; checar lances ou horário fora da trava do lote.
  - Afeta a seção 5.1 do contrato; registrada como M-13 em [[contrato-do-projeto-mudancas]].

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[geral-plano]]
- Projeto: [[geral-contexto]]
- Relacionadas: [[contrato-regras-de-negocio]], [[contrato-requisitos-funcionais]], [[contrato-pontos-para-validar]], [[contrato-testes]], [[enunciado-teste-tecnico]], [[contrato-do-projeto-mudancas]]
- Regras: [[manual-da-orquestra]]
