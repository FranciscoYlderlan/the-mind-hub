---
aliases: [Pontos para validar, Perguntas Q-01 a Q-15, Dúvidas do contrato, Inconsistências do enunciado]
tags: [estudos/programacao]
tipo: referencia
tema: requisitos
status: rascunho
criado: 2026-10-29
origem: Contrato do Projeto Stonebid v0.2 (2026-10-27), seção 14
---
# 📜 Contrato: pontos para validar (Q)

> [!tldr] Em uma linha
> As seis lacunas do enunciado e as quinze perguntas (Q-01 a Q-15) que preciso responder antes de codar.

É o **checklist do piloto antes da decolagem**: cada item conferido evita um problema no ar. Seção 14 do [[contrato-do-projeto|contrato]] v0.2, copiada sem reinterpretar. Cada resposta aprovada vira uma nota de decisão em `funcionalidades/geral/`.

Antes de codar, valide estes pontos. Eles vêm de ambiguidades do enunciado e de lacunas que preenchi com propostas. Cada um muda requisitos e testes se a resposta for outra.

> [!info] Por que isso importa
> Sommerville chama de **validação de requisitos** a checagem de que os requisitos são válidos, consistentes, completos, realistas e verificáveis, o que se faz revisando com as partes interessadas. Pressman inclui a **negociação** (resolver conflitos e prioridades) antes da especificação. Aqui o "cliente" é o enunciado: onde ele é ambíguo, registramos a interpretação e a documentamos no README (o enunciado pede isso para comportamentos inesperados).

**Inconsistências e lacunas que notei no enunciado:**

1. O cancelamento aparece em dois lugares: no painel só vale para lote **sem lances**, e o opcional pede cancelamento com estorno automático (que implica lances). Tratei como base mais extensão (RF-22 e RF-23).
2. "Lance inicial" (E1) e "valor mínimo" (E2) parecem o mesmo campo.
3. A frase do anti-sniping admite duas leituras (5.4).
4. "Lote publicado com lances abertos" nos dados de teste: interpretei como lote ao vivo com lances já feitos.
5. "Posição do usuário nos lances" pode significar só liderando ou superado, ou um ranking.
6. O prazo é 7 dias no enunciado; na realidade eram 4 dias (v0.2) e, desde a v0.3, são **24 horas**, com entrega em 2026-10-30 09:00.

| ID | Pergunta | Proposta | Afeta |
|---|---|---|---|
| Q-01 | Vitrine, sala (leitura), auditoria e comprovante abrem sem login? | Sim. O lance exige login. | RF-03 |
| Q-02 | Cadastro livre com escolha de papel, um papel por conta? | Sim | RF-01 |
| Q-03 | Anti-sniping: opção A (instante + 2 min) ou B (fim + 2 min)? Prorrogações ilimitadas? | A, sem limite | RN-10, T-04 |
| Q-04 | Lance no instante exato do fim? | Recusado | RN-02 |
| Q-05 | Cancelar lote com lances: até quando, com que registro e como aparece? | Até o fim, com motivo obrigatório. Some da vitrine, a auditoria continua acessível por link e "Meus arremates" mostra "cancelado". | RN-12, RF-23 |
| Q-06 | "Lance inicial" e "valor mínimo" são o mesmo campo? | Sim | RF-21, RN-03 |
| Q-07 | Início no passado e duração mínima do lote? | Início não pode estar no passado. Duração mínima de 5 minutos, para o anti-sniping fazer sentido. | RF-21 |
| Q-08 | "Posição do usuário nos lances" | Liderando ou superado, mais o maior lance dele. Sem ranking. | RF-30 |
| Q-09 | O que o comprovante mostra? | Item, valor, data e hora, pseudônimo do vencedor, hash final e link da auditoria | RF-51 |
| Q-10 | Limites do depósito simulado? | Valor maior que 0, com teto configurável. Sem saque. | RF-41 |
| Q-11 | Como garantir lote "ao vivo" nos dados de teste durante a avaliação? | Lote com fim distante, cobrindo o período de avaliação, e um comando de reset | RNF-02, R-10 |
| Q-12 | Ordem de corte dos opcionais | A da seção 11.4 | Seção 11 |
| Q-13 | Qual API pública de itens? | Você decide (seção 12) | RF-20, R-03 |
| Q-14 | Edição de lote fica fora do escopo? | Sim | Seção 1.4 |
| Q-15 | Quanto você já domina de React, Node ou Python, e SQL? | (A resposta define o risco R-09) | Seção 12 |

Resolvido na v0.3 ([[contrato-do-projeto]]): entrega em **2026-10-30 09:00** e trabalho contínuo, sem pausa.

> [!warning] Situação em 2026-10-29
> Nenhuma das perguntas Q-01 a Q-15 foi respondida no cofre ainda. Q-13 ainda depende da escolha da API; a parte de stack de Q-15 já foi respondida pelas decisões de stack ([[contrato-tecnologias]]), mas o nível de domínio não.

> [!tip] Quando abrir esta nota
> Antes de começar a implementar e sempre que uma regra de [[contrato-regras-de-negocio]] citar um Q-xx.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** quinze perguntas abertas; cada resposta aprovada vira uma nota `geral-decisao-*`.
* **Ponto 2:** as que mais mudam código: Q-03 (anti-sniping), Q-04 (instante do fim) e Q-05 (cancelamento com lances).
* **Ponto 3:** data de entrega (2026-10-30 09:00) e ritmo (trabalho contínuo) já definidos na v0.3 ([[geral-contexto]]).

### 🔗 Conexões
- Mapa: [[contrato-do-projeto]] · [[moc-orquestra]]
- Relacionadas: [[contrato-regras-de-negocio]], [[contrato-requisitos-funcionais]], [[geral-contexto]]
- Próxima: [[contrato-glossario]]
