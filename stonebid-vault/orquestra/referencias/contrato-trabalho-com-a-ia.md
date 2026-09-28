---
aliases: [Contrato com a IA, Regras de trabalho com a IA, Fonte da verdade, Protocolo de mudança do contrato]
tags: [estudos/programacao]
tipo: referencia
tema: orquestracao
status: rascunho
criado: 2026-10-29
origem: Contrato do Projeto Stonebid v0.2 (2026-10-27), seção 13
---
# 📜 Contrato: trabalho com a IA (A)

> [!tldr] Em uma linha
> Quem decide, qual fonte vence num conflito, as doze regras de trabalho da IA e como o contrato muda.

É o **combinado entre motorista e copiloto**: o copiloto lê o mapa e sugere, mas quem vira o volante é o motorista. Seção 13 do [[contrato-do-projeto|contrato]] v0.2, copiada sem reinterpretar. Complementa as regras do cofre em [[manual-da-orquestra]].

Esta seção é o acordo de trabalho entre você e a IA.

## 13.1 Papéis

- **Você** decide, valida, é dono do código e responde pelo que entrega. Se não entendeu algo, peça explicação antes de aceitar.
- **A IA** propõe, implementa, testa e explica. Ela **não decide sozinha** o que é requisito.

## 13.2 Fonte da verdade, em ordem

1. O enunciado oficial do desafio.
2. Este contrato.
3. As decisões registradas (AD).
4. O código.

Se duas fontes entram em conflito, **pare e pergunte**. A fonte de cima vence.

## 13.3 Regras de trabalho

| ID | Regra |
|---|---|
| A-01 | Leia este contrato antes de qualquer tarefa e cite os IDs atendidos (RF, RN, RNF). |
| A-02 | NÃO invente requisitos, regras nem números. Diante de ambiguidade, liste as opções, recomende uma e pergunte. |
| A-03 | Trabalhe em **uma fatia pequena por vez**, de ponta a ponta, ligada a IDs. |
| A-04 | Regras de negócio (RN) têm teste escrito antes ou junto do código. NUNCA altere um teste só para fazê-lo passar sem avisar e justificar. |
| A-05 | Regras de negócio moram **só** no domínio (AD-02). Autorização, validação e dinheiro ficam sempre no servidor. |
| A-06 | Não adicione dependência nova sem justificar: para quê, qual a alternativa e qual o custo de manutenção. |
| A-07 | Segredos ficam fora do código. Use variáveis de ambiente e um arquivo de exemplo sem valores reais. |
| A-08 | NÃO simule sucesso: nada de mock que esconde falha, de erro engolido, de dado de teste fixo na lógica ou de "TODO" escondido. Se deixar algo pendente, registre. |
| A-09 | Se um comportamento ficar diferente do esperado, ou algo for contornado, registre na seção de comportamentos inesperados do README. |
| A-10 | Em dúvida sobre segurança ou dinheiro, escolha o caminho mais conservador e avise. |
| A-11 | Commits pequenos, com mensagens que citam os IDs. |
| A-12 | Mudança no contrato só pelo protocolo da seção 13.4. |

## 13.4 Protocolo de mudança do contrato

1. Alguém (você ou a IA) aponta o conflito ou a necessidade.
2. A IA propõe a alteração com o texto exato e o impacto em RF, RN, testes e plano.
3. Você aprova ou recusa.
4. O contrato e o histórico de versões são atualizados.
5. Só então o código muda.

> [!info] Por que isso importa
> Pressman inclui o gerenciamento de requisitos e de mudanças como parte da engenharia de requisitos, com rastreabilidade. Sommerville trata o gerenciamento de configuração (versões, mudanças, releases) como disciplina própria, porque uma mudança sem controle é a forma mais comum de um projeto perder o rumo. **Prática:** uma IA é como um desenvolvedor muito rápido que não tem contexto. O contrato é o contexto dela.

## 13.5 Formato das respostas da IA

Toda entrega da IA deve trazer:

1. **Resumo** do que foi feito, em linguagem de quem está aprendendo.
2. **IDs atendidos** (RF, RN, RNF) e testes (T-xx) relacionados.
3. **Arquivos** alterados.
4. **Como testar** o resultado.
5. **Decisões e trade-offs**: o que foi escolhido e por quê.
6. **Dúvidas e riscos** que ficaram.

## 13.6 Modelo de pedido (humano para IA)

> Contexto: leia o contrato (versão X). Tarefa: implementar [ID(s)]. Fora do escopo: [o que não mexer]. Pronto quando: [critério de aceite]. Restrições: [se houver]. Responda no formato da seção 13.5.

> [!tip] Quando abrir esta nota
> Ao montar um briefing de subagente ([[modelo-briefing-subagente]]) e sempre que surgir um conflito entre enunciado, contrato, decisão e código.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** a IA propõe; **eu decido** o que é requisito.
* **Ponto 2:** conflito entre fontes: parar e perguntar; enunciado vence contrato, que vence decisão, que vence código.
* **Ponto 3:** mudança de escopo segue os 5 passos do protocolo antes de tocar no código.

### 🔗 Conexões
- Mapa: [[contrato-do-projeto]] · [[moc-orquestra]]
- Relacionadas: [[manual-da-orquestra]], [[modelo-briefing-subagente]], [[contrato-pontos-para-validar]]
- Próxima: [[contrato-pontos-para-validar]]
