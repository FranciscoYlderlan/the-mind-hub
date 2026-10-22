---
tipo: plano
funcionalidade: banco-mocado
status: proposta
criado: 2026-11-06
aliases: [Evolução do treino, Placar do treino, Rubrica de avaliação, Training scoreboard]
---
# 📈 Evolução do treino até o teste

> [!tldr] Em uma linha
> A régua com que cada resposta é avaliada e o placar que mostra se estou melhorando até 2026-11-09, 15h.

## Rubricas (0 a 3 por critério)
0 = ausente · 1 = fraco · 2 = bom · 3 = nível de contratação.

### SQL (nota máxima 12)
| Critério | O que vale 3 |
|---|---|
| Correção | resultado certo, granularidade certa, sem linha duplicada |
| Bordas | trata nulo (`COALESCE`), duplicado, data com hora e divisão inteira |
| Legibilidade | CTE com nome que explica, alias claro, comentário de 1 linha |
| Tempo | dentro do alvo de [[questoes-sql-de-prova]] (estourou até 50%: 2; mais: 1) |

Também registro: **acertou sem rodar?** (sim/não).

### Discursiva de decisão (nota máxima 18)
Critérios ligados aos passos de [[esqueleto-de-6-passos]].

| Critério | O que vale 3 |
|---|---|
| Decisão | decisão clara na primeira frase |
| Esclarecer e referência (passos 1 e 2) | no máximo 2 perguntas que mudam a decisão; risco nomeado com tamanho e base regulatória quando cabe |
| Caminhos (passo 3) | 2 ou 3 opções com o custo de cada uma; regra simples antes de sofisticada |
| Proporcionalidade e explicação (passo 4) | pesa falso positivo e impacto no cliente e no negócio; o analista entende o porquê |
| Medir (passo 5) | métrica que prova que funcionou e o que a decisão deixa passar |
| Governar (passo 6) | registro, escalonamento, quem aprova, prazo e o que eu automatizaria |

## Metas
- **Linha de base:** a retomada dos drills, depois da [[trilha-sql-didatica]]. O desempenho na trilha fica em [[banco-mocado-plano-registro-sql]].
- **Domingo à noite:** média de SQL ≥ 9/12 e de decisão ≥ 13/18, sem nenhum critério em 0 nos dois últimos simulados.
- **Prova de domínio:** acertar sem rodar em pelo menos 2 de cada 3 drills de nível 2.

## Placar
| Data | Sessão | Item | Tipo | Nota | Tempo | Lacuna principal |
|---|---|---|---|---|---|---|
| 2026-11-06 | Diagnóstico | D2 | Decisão | sem nota (gabarito pedido) | ~10 min | Decisão: travou em "libera ou segura"; analisou o cliente em vez da contraparte do alerta |

## Mapa de lacunas
Atualizado ao fim de cada dia: o critério com menor média vira o foco do dia seguinte.

| Critério | Média sex | Média sáb | Média dom |
|---|---|---|---|
| SQL: correção | | | |
| SQL: bordas | | | |
| SQL: legibilidade | | | |
| SQL: tempo | | | |
| Decisão: decisão | | | |
| Decisão: esclarecer e referência | | | |
| Decisão: caminhos | | | |
| Decisão: proporcionalidade e explicação | | | |
| Decisão: medir | | | |
| Decisão: governar | | | |

## Como a IA avalia
- Dá a nota por critério com **uma frase de motivo** cada, depois o que faltou e o que reordenar ([[instrucoes-do-coach-de-entrevista]]).
- Nota só depois da minha resposta completa; sem elogio vazio.
- Ao fim de cada sessão, a IA entrega as linhas do placar e o orquestrador grava aqui.

### 🔗 Conexões
- Funcionalidade: [[banco-mocado-contexto]]
- Plano (nota original): [[banco-mocado-plano]]
- Trilha e registro: [[trilha-sql-didatica]], [[banco-mocado-plano-registro-sql]]
- Questões: [[questoes-sql-de-prova]], [[questoes-tomada-de-decisao]], [[questoes-por-cenario]]
