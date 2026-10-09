---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-16
substitui: 
aliases: [Numeração do enunciado, E1 a E6, Como citar o enunciado, Source numbering]
---
# ✅ Numeração do enunciado: E1 a E6

- **Proposta (plano):** nenhuma. Regra do humano (2026-10-29 12:21, [[diario-2026-10-29-padronizacao]]), escrita até 2026-11-16 num bloco do `CLAUDE.md` e migrada para esta nota pela regra "regra só do projeto vira decisão em `funcionalidades/geral/`" (humano, 2026-11-16 09:28, K5 de [[diario-2026-11-16-regras-para-o-vault]]).
- **Decisão:** o enunciado do teste técnico é citado como **E1 a E6**, a numeração de [[enunciado-teste-tecnico]]: E1 O desafio, E2 Front-End, E3 Back-End, E4 Tecnologias e requisitos, E5 Opcionais, E6 Como enviar.
  - A numeração "01 a 05" do contrato original vira E1 a E5; ela só aparece dentro da transcrição.
  - O deploy obrigatório está só no E1.
  - A origem de um requisito aponta só as seções onde ele está escrito, separadas por vírgula (`E1, E2`).
- **Alteração:** nenhuma.
- **Motivo:** o humano achou o enunciado citado com numerações diferentes nas notas (a do original e a da transcrição) e pediu uma só.
- **Consequências:**
  - O bloco do [[padroes]] dá ERRO na numeração do original (a palavra "seção" seguida de 01 a 06) e em duas seções E ligadas por barra no lugar da vírgula.
  - Requisito que cita o deploy aponta o E1, nunca outra seção.

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Documento-fonte: [[enunciado-teste-tecnico]]
- Padrões checados pelo `verificar`: [[padroes]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
