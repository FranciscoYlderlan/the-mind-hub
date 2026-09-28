---
aliases: [Contrato do projeto, Contrato do StoneBid, Especificação do StoneBid, Project contract]
tags: [estudos/programacao]
tipo: referencia
tema: requisitos
status: rascunho
criado: 2026-10-29
origem: Contrato do Projeto Stonebid v0.2 (2026-10-27), fornecido pelo humano
---
# 📜 Contrato do projeto StoneBid

> [!tldr] Em uma linha
> O acordo entre mim e a IA: o que construir, o que não construir, como decidir na dúvida e como trabalhar juntos.

Funciona como a **planta de uma obra**: o pedreiro não decide onde vai a parede, consulta a planta. Este é o hub do contrato v0.2; cada seção mora numa nota própria, para o agente ler só o que a tarefa precisa. O texto foi copiado do documento original sem reinterpretar.

> [!warning] Prazo mudou em 2026-10-29
> O prazo real passou de 4 dias para **24 horas** (a partir de 2026-10-29 09:06). Onde esta nota fala em 4 dias, vale o prazo novo; o texto do contrato segue como estava até a v0.3. Fato registrado em [[geral-contexto]].

## 📋 Ficha

| | |
|---|---|
| Projeto | **Stonebid** (*stone*, pedra que não se altera + *bid*, lance) |
| Repositórios | `stonebid-web` (front-end) e `stonebid-api` (back-end) |
| Versão | 0.2 (rascunho para validação) |
| Data | 27/10/2026 |
| Autor | [A PREENCHER] |
| Prazo real | **4 dias** (o enunciado fala em 7; vale o prazo real) |
| Entrega | [A PREENCHER: data e hora] |
| Horas por dia | [A PREENCHER] |
| Tecnologias | [A PREENCHER na seção 12] |
| Status | Aguardando validação (veja a seção 14) |

## 🗺️ Onde está cada seção

| Seção | Nota |
|---|---|
| 0. Como ler este documento | Esta nota (abaixo) |
| 1. Visão e escopo · 2. Restrições e premissas · 3. Papéis | [[contrato-visao-escopo-e-papeis]] |
| 4. Requisitos funcionais (RF) | [[contrato-requisitos-funcionais]] |
| 5. Regras de negócio (RN) | [[contrato-regras-de-negocio]] |
| 6. Requisitos não funcionais (RNF) | [[contrato-requisitos-nao-funcionais]] |
| 7. Modelo de dados (conceitual) | [[contrato-modelo-de-dados]] |
| 8. Arquitetura: decisões (AD) | [[contrato-arquitetura]] |
| 9. Riscos (R) | [[contrato-riscos]] |
| 10. Qualidade e testes (T) | [[contrato-testes]] |
| 11. Processo e plano | [[contrato-processo-e-plano]] |
| 12. Tecnologias | [[contrato-tecnologias]] |
| 13. Contrato com a IA (A) | [[contrato-trabalho-com-a-ia]] |
| 14. Pontos para você validar (Q) | [[contrato-pontos-para-validar]] |
| 15. Glossário | [[contrato-glossario]] |
| 16. Referências e roteiro de estudo | Esta nota (abaixo) |

## 0. Como ler este documento

Este documento é um **contrato** entre duas partes: você (autor, júnior em formação) e a IA que vai ajudar a programar. Ele diz o que construir, o que **não** construir, como decidir quando houver dúvida e como trabalhar juntos. Se algo não está aqui, ou está ambíguo, o caminho é perguntar e atualizar o contrato, não adivinhar.

**Leitura sugerida (cerca de 20 minutos):** comece pelas seções 1, 2 e 14 (o que é o projeto e o que preciso que você valide). Depois leia as seções 5, 8 e 13. O resto serve de consulta.

### Convenções

- **DEVE / NÃO DEVE** = obrigatório. **DEVERIA** = desejável. **PODE** = opcional. Sommerville recomenda usar essa linguagem de forma consistente (o "shall" e o "should" do inglês) para que ninguém leia o mesmo requisito de dois jeitos.
- **IDs** (servem para a IA e para você apontarem para a mesma coisa):

| Prefixo | Significa |
|---|---|
| RF | Requisito funcional (o que o sistema faz) |
| RN | Regra de negócio (as "leis" do leilão) |
| RNF | Requisito não funcional (como o sistema deve ser: seguro, rápido, resiliente) |
| AD | Decisão de arquitetura |
| R | Risco |
| T | Teste |
| A | Regra de trabalho com a IA |
| Q | Pergunta para você validar |
| OPC | Opcional do enunciado (OPC-1 a OPC-5, na ordem em que aparecem lá) |

- **Status das decisões:** `[DECIDIDO]` veio do enunciado ou de você. `[PROPOSTO]` é sugestão minha, e você valida. `[PENDENTE]` só você pode decidir.
- **Origem dos requisitos:** E1 a E5 são as seções do enunciado (E1 O desafio, E2 Front-End, E3 Back-End, E4 Tecnologias e requisitos, E5 Opcionais). **Prop.** é uma proposta deste documento.
- **Caixas "Por que isso importa"** trazem a base teórica. Ideias que vêm de prática de mercado, e não dos livros, estão marcadas como **Prática**.

### Sobre as citações

Cito Sommerville (*Engenharia de Software*) e Pressman & Maxim (*Engenharia de Software: Uma Abordagem Profissional*) **por tema**, sem número de capítulo ou página, porque a numeração muda entre edições. Todas as ideias estão parafraseadas. Confira o tema no sumário do seu exemplar. A seção 16 traz um roteiro de estudo.

### Histórico de versões

| Versão | Data | O que mudou |
|---|---|---|
| 0.1 | 26/10/2026 | Primeiro rascunho, para validação |
| 0.2 | 27/10/2026 | Nome do projeto definido (Stonebid) e padrão de repositórios `stonebid-web` e `stonebid-api` |

## 16. Referências e roteiro de estudo

**Livros:**

- SOMMERVILLE, Ian. *Engenharia de Software*. [Confira editora e edição no seu exemplar.]
- PRESSMAN, Roger S.; MAXIM, Bruce R. *Engenharia de Software: Uma Abordagem Profissional*. [Confira editora e edição no seu exemplar.]
- Enunciado do desafio (seções 01 a 05).

**Roteiro de estudo.** Procure estes temas no sumário dos seus exemplares e leia na ordem em que o projeto os usa:

| Tema | Em Sommerville | Em Pressman & Maxim | Onde usamos |
|---|---|---|---|
| Processos e agilidade | Modelos de processo, desenvolvimento incremental, métodos ágeis | Modelos de processo, atividades do arcabouço, agilidade | Seção 11 |
| Engenharia de requisitos | Requisitos funcionais e não funcionais, levantamento, especificação, validação, mudanças | Concepção, levantamento, elaboração, negociação, especificação, validação, gerenciamento | Seções 4 a 6 e 14 |
| Modelagem | Modelos de sistema (contexto, interação, estrutura, comportamento) | Modelagem de requisitos (cenários, casos de uso, classes) | Seções 5.1 e 7 |
| Projeto e arquitetura | Decisões e padrões arquiteturais, arquitetura × requisitos não funcionais, processamento de transações | Conceitos de projeto, projeto arquitetural, padrões de projeto | Seção 8 |
| Testes e qualidade | Testes de desenvolvimento, de release e de usuário, TDD | Estratégias de teste, garantia de qualidade | Seção 10 |
| Segurança e confiabilidade | Engenharia de segurança, confiabilidade e resiliência | Segurança de software (se constar na sua edição) | RNF-07, RNF-08, AD-05, AD-08 |
| Gerência de projeto e riscos | Planejamento, estimativas, gerenciamento de riscos | Gerência de projetos (4 Ps, W5HH), estimativas, riscos (RMMM) | Seções 1.5, 9 e 11 |
| Gerência de configuração e mudanças | Controle de versão, gerenciamento de mudanças, integração contínua | Gerência de configuração e de mudanças | Seção 13 |

**Como estudar com este contrato:** a cada seção que você validar, abra o tema correspondente nos livros e leia só a parte que justifica a decisão. Assim a teoria vem junto com a prática, e você consegue explicar cada escolha numa entrevista.

## 🤖 Interpretação do agente
(separada do contrato; registrada em 2026-10-29)
- O contrato está em **rascunho (v0.2, aguardando validação)**. Itens `[PROPOSTO]` e as perguntas Q-01 a Q-15 **não** viraram notas de decisão; isso só acontece com o meu aval, uma decisão por nota ([[manual-da-orquestra]]).
- Os itens `[DECIDIDO]` que vieram de mim foram copiados para "Fatos que eu informei" em [[geral-contexto]].
- A seção 12 já foi em boa parte respondida pelas decisões de 2026-10-28 e 2026-10-29; a comparação está em [[contrato-tecnologias]]. O contrato ainda marca a seção como `[PENDENTE]` e pode ganhar uma v0.3.
- A camada MCP ([[geral-decisao-2026-10-29-camada-mcp]]) e o teste do frontend só com Playwright ([[geral-decisao-2026-10-28-testes-frontend-playwright]]) não aparecem no contrato. Pelo protocolo da seção 13.4, entrariam como mudança do contrato [a confirmar].
- O enunciado original, fonte da verdade nº 1 pela seção 13.2, está em [[enunciado-teste-tecnico]] (com o PDF em `Anexos/`). Ele tem uma seção E6 "Como enviar" que o contrato não cobre.

> [!tip] Quando abrir esta nota
> Antes de qualquer tarefa de implementação: achar a seção do contrato que cobre o ID (RF, RN, RNF, AD) e seguir para a nota dela.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** o contrato diz o que construir e o que fica de fora; as regras estão em [[contrato-regras-de-negocio]].
* **Ponto 2:** fonte da verdade, em ordem: enunciado → contrato → decisões → código ([[contrato-trabalho-com-a-ia]]).
* **Ponto 3:** antes de codar, validar as perguntas de [[contrato-pontos-para-validar]].

### 🔗 Conexões
- Mapa: [[moc-orquestra]]
- Projeto: [[geral-contexto]], [[geral-plano]]
- Fonte: [[enunciado-teste-tecnico]]
- Seções: [[contrato-visao-escopo-e-papeis]], [[contrato-requisitos-funcionais]], [[contrato-regras-de-negocio]], [[contrato-requisitos-nao-funcionais]], [[contrato-modelo-de-dados]], [[contrato-arquitetura]], [[contrato-riscos]], [[contrato-testes]], [[contrato-processo-e-plano]], [[contrato-tecnologias]], [[contrato-trabalho-com-a-ia]], [[contrato-pontos-para-validar]], [[contrato-glossario]]
