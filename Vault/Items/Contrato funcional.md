---
aliases: [Contrato de frontend, Especificação funcional, Functional contract, Onde a tela tira as regras]
tags: [estudos/programacao]
tipo: manual
status: em-uso
criado: 2026-11-17
origem: Pacote "contrato funcional e validação" aprovado pelo humano em 2026-11-17, depois da avaliação técnica do Stonebid (servidor bem avaliado, interface fraca)
---
# 📐 Contrato funcional

> [!tldr] Em uma linha
> O que o produto faz, escrito em 8 blocos com IDs em `Anexos/contrato/` do cofre do projeto, para a interface ter regra tão firme quanto o servidor.

É o **manual de montagem do móvel**: cada peça só entra onde o desenho manda. Faltou peça? Corrige o desenho antes de improvisar com fita. A tela é a peça; o contrato é o desenho. Regras de uso no [[Manual da Orquestra - Perfil projeto prático|perfil projeto prático]] (Q01 a Q06); os blocos, um a um, em [[Contrato funcional - Os 8 blocos]].

---

## ⚖️ Por que existe

Fala do humano (2026-11-17), sobre a interface fraca: "acredito que caiu nesse erro pois o frontend não havia nenhuma documentação ou contrato do lado do frontend apenas do backend". Objetivo: "Refinar o vault responsável por criar vault's para que os próximos vaults já venham com a estrutura pre definida para garantir a consistencia do frontend ... assim como é feito hoje nas regras de negócio no backend que foi pontuado como bem feito".

O contrato funcional é a **contraparte de frontend** do que o backend já tinha no [[Padrão de projeto de software]]:

| No backend (já existia) | No contrato funcional |
|---|---|
| Regra de negócio no domínio (S14) | ENT-xx: campos e invariantes que toda tela herda (S26) |
| Erro com código próprio (S15) | ERR-xx: o código é o do servidor; uma mensagem por erro |
| Estado inválido provado no CI (S22) | AC-xx: a prova, executada pelos dois agentes ao final de cada funcionalidade (Q04 e Q05) |

---

> [!note] Ordem de preenchimento
> 1. Atores (ATR) e entidades (ENT), depois dos requisitos RF, RNF e RN.
> 2. Casos de uso (UC) com os três tipos de fluxo: principal, alternativo (FA) e exceção (FE).
> 3. Erros (ERR), alimentados pelos FE.
> 4. Só com interface: componentes (CMP) e, depois, navegação (NAV).
> 5. Rastreabilidade e critérios de aceite (AC).
> 6. Só então o código (e as telas, se houver).

> [!warning] Regra da tela
> Cada tela lista os CMP, UC e NAV que realiza e **não cria regra**. Regra que falta entra primeiro no contrato, pelos 5 passos do P01, com o item M-xx em `Anexos/contrato/mudancas.md`. Validação vem do ENT; mensagem vem do ERR.

## 📍 Onde mora

- No cofre do projeto, em `Anexos/contrato/`: os 8 blocos, o `README.md` e o `mudancas.md`, em Markdown puro (não são notas: sem frontmatter nem Conexões), com os requisitos RF, RNF e RN no `00-requisitos.md`. Ali o contrato nasce e é editado durante todo o projeto, ao lado das decisões e do diário.
- Os modelos ficam no `Vault`, em `Modelos/Orquestra/contrato/`. O `cofre.py criar` os copia para `Anexos/contrato/` de todo cofre de projeto prático; o `sincronizar` nunca sobrescreve o contrato de um cofre que já existe.
- Só o orquestrador altera o contrato. Subagente que precisar de mudança devolve no relatório o arquivo, o trecho atual, o trecho novo e o motivo, e a mudança segue os 5 passos do P01.
- Implementador, verificadores e adversarial leem o contrato pela Obsidian CLI (`obsidian read path="Anexos/contrato/03-casos-de-uso.md"`) ou, sem CLI, pelo arquivo, avisando no relatório. Frontend em repositório separado lê o mesmo contrato do cofre.
- O repositório de código só recebe o contrato na aceitação final: depois do aceite do humano, o orquestrador copia `Anexos/contrato/` para `docs/contrato/`, num commit só, com escopo `contrato`, e nenhum subagente altera essa cópia. O [[modelo-claude-do-repositorio]] diz aos agentes que trabalham no código onde ler.

> [!tip] Quando abrir esta nota
> Ao criar um cofre de projeto prático, ao começar qualquer funcionalidade ou quando uma tela pedir uma regra que não está escrita.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** A tela segue o contrato como o servidor segue o domínio: a regra mora num lugar só.
* **Ponto 2:** Os AC são a prova: os [[modelo-briefing-subagente|agentes de validação]] os executam ao final de cada funcionalidade.
* **Ponto 3:** Erro comum: escrever o contrato só do backend. Ver [[Contrato só do backend deixa a interface sem regra]].

### 🔗 Conexões
- Mapa: [[MOC Programação]]
- Detalhe: [[Contrato funcional - Os 8 blocos]]
- Relacionadas: [[Manual da Orquestra - Perfil projeto prático]], [[Padrão de projeto de software]], [[Referência de arquitetura e stack]], [[modelo-roteiro-teste-humano]]

## 🕓 Histórico
- v1 (2026-11-17): criação, com os 8 blocos, a ordem de preenchimento, a regra da tela e `docs/contrato/` no repositório.
- v2 (2026-11-19): o contrato mora em `Anexos/contrato/` do cofre do projeto, criado pelo `cofre.py criar`; só o orquestrador o altera; o repositório recebe a cópia em `docs/contrato/` só na aceitação final.
