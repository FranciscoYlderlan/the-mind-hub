---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-16
substitui: 
aliases: [Diário com partes, Onde parei vigente, Último diário, Diary parts]
---
# ✅ Diário com partes: o "Onde parei" vigente mora na parte mais recente

- **Proposta (plano):** nenhuma. Regra do humano (2026-10-29 23:20, [[diario-2026-10-29-carteira-e-lotes]]), escrita até 2026-11-16 num bloco do `CLAUDE.md` e migrada para esta nota pela regra "regra só do projeto vira decisão em `funcionalidades/geral/`" (humano, 2026-11-16 09:28, K5 de [[diario-2026-11-16-regras-para-o-vault]]).
- **Decisão:** quando o dia tem partes (`diario-AAAA-MM-DD-<assunto>.md`), o "Onde parei" vigente mora só na parte mais recente. O diário principal (`diario-AAAA-MM-DD.md`) aponta para ela no próprio "Onde parei". "Último diário", no início de sessão, é essa parte.
- **Alteração:** nenhuma.
- **Motivo:** o humano perguntou onde o próximo chat veria que seguia para a T3 e a T4: o principal de 2026-10-29 ainda mandava para a etapa 2, com a etapa 3 em andamento, e podia ser lido como "último diário".
- **Consequências:**
  - Parte nova do dia: o "Onde parei" das partes anteriores e do principal passa a apontar para ela.
  - O `cofre.py verificar` cobra que o principal aponte para a parte vigente e que ela tenha "Próximo passo".

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Modelo: [[modelo-diario]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
