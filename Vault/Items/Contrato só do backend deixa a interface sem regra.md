---
aliases: [Frontend sem contrato, Interface sem especificação, Backend-only contract, Por que a tela ficou fraca]
tags: [estudos/programacao]
tipo: conceito
status: em-uso
criado: 2026-11-17
origem: projeto Stonebid (feedback da avaliação técnica e diagnóstico do humano), 2026-11-17
---
# 🧩 Contrato só do backend deixa a interface sem regra

> [!tldr] Em uma linha
> Quando só o servidor tem regra escrita, cada tela inventa a sua; o remédio é um contrato funcional que a interface segue e dois agentes que o provam.

É a casa com projeto elétrico detalhado e nenhuma planta de móveis: a fiação passa na vistoria, mas o sofá tampa a tomada e a porta bate no armário. Vale para todo projeto com [[Manual da Orquestra|agentes]] escrevendo frontend e backend.

> [!note] Como funciona
> 1. **Sintoma:** servidor impecável e interface fraca: ação principal difícil de achar, campo de valor aceitando letras, a mesma mensagem para erros diferentes, menu que só aparece depois de um clique, clique perdido durante a atualização automática, comentários longos citando códigos de uma especificação que não está no repositório.
> 2. **Causa:** o contrato descrevia só o backend; a tela não tinha de onde tirar campos, erros, estados e navegação. Fala do humano: "acredito que caiu nesse erro pois o frontend não havia nenhuma documentação ou contrato do lado do frontend apenas do backend".
> 3. **O que fazer:** [[Contrato funcional]] em `docs/contrato/` (Q01), tela que não cria regra (Q02), contrato antes da primeira tela (Q03), verificador de fluxo principal (Q04), adversarial (Q05) e roteiro do humano no fim (Q06), do [[Manual da Orquestra - Perfil projeto prático|perfil projeto prático]].
> 4. **No código:** campo com schema tirado do ENT e mensagem por violação (S26); comentário curto e pontual (S27), do [[Padrão de projeto de software]].

> [!tip] Quando abrir esta nota
> Ao planejar a primeira tela de um projeto ou quando a interface "funciona" mas confunde quem usa.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** Regra que não está escrita para a tela vira improviso, um diferente por tela.
* **Ponto 2:** O teste do caminho feliz não pega descoberta nem ataque; por isso o adversarial e o roteiro do humano.
* **Ponto 3:** Limite: o contrato não substitui o olhar do humano sobre a experiência; ele só garante a regra.

### 🔗 Conexões
- Mapa: [[MOC Programação]]
- Relacionadas: [[Contrato funcional]], [[API simulada conferida contra a API real]], [[Tempo real por SSE com recarga de reserva]]
