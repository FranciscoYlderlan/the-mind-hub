---
tipo: plano
funcionalidade: geral
status: proposta
criado: {{date}}
---
# 🧭 Roteiro do projeto

> [!tldr] Onde o projeto está
> Etapa atual: **1. Definir o roteiro do projeto** (em-construcao)

> [!warning] Proposta da IA até eu aprovar
> As etapas nascem como proposta. Aprovadas, viram a nota `geral-decisao-AAAA-MM-DD-roteiro` e este plano passa a `status: aprovado`. Mudar a lista de etapas é uma nova decisão.

Uma seção por etapa, na ordem em que o projeto acontece. Status: `planejada → em-construcao → em-verificacao → concluida → arquivada`. Etapa concluída tem data e links para as notas geradas nela. A linha "Etapa atual" acima é sincronizada por `cofre.py status --atualizar`.

No projeto prático, cada etapa segue, para cada funcionalidade dela, o ciclo contrato da funcionalidade em `docs/contrato/` → implementação → verificador de fluxo principal → adversarial, e termina com os fluxos de teste dela registrados em `geral-plano-teste-humano` ([[modelo-roteiro-teste-humano]]). A última etapa entrega ao humano o roteiro final, montado desse registro, antes da aceitação final.

## 1. Definir o roteiro do projeto
- **Status:** em-construcao
- **Objetivo:** listar as etapas gerais do projeto, da primeira à entrega.
- **Pronto quando:** etapas aprovadas numa nota de decisão.
- **Funcionalidades:** (nenhuma)
- **Notas geradas:** (nenhuma ainda)
- **Concluída em:** 

## 2. Nome da etapa
- **Status:** planejada
- **Objetivo:** 
- **Pronto quando:** 
- **Ciclo** (prático, toda funcionalidade): contrato da funcionalidade → implementação → verificador de fluxo principal → adversarial → fluxos de teste registrados
- **Funcionalidades:** [[nome-da-func-contexto]]
- **Notas geradas:** [[nome-da-func-decisao-AAAA-MM-DD-titulo]], [[bug-titulo-AAAA-MM-DD]]
- **Concluída em:** 

## 3. Roteiro do humano e aceitação final
- **Status:** planejada
- **Posição:** (prático) sempre a última; etapa nova entra antes dela, e a numeração segue 1..N. O `cofre.py criar` já a põe no roteiro do cofre novo.
- **Objetivo:** com todas as funcionalidades passando nos dois agentes, entregar ao humano o roteiro final, sucinto e didático (descoberta + poucos fluxos que cobrem o máximo de AC), e fazer a aceitação final.
- **Pronto quando:** roteiro testado pelo humano, achados decididos como opções e aceitação final registrada.
- **Funcionalidades:** (nenhuma)
- **Notas geradas:** `geral-plano-teste-humano`
- **Concluída em:** 

## Proposta de arquitetura e stack
Só no projeto prático de software (S25 do Padrão de projeto de software (no Vault)); em outro projeto prático, apagar esta seção. Proposta da IA a partir da Referência de arquitetura e stack (no Vault), em linguagem leiga, no passo 4 de Criar um novo cofre (no Vault). Com o aval, cada escolha vira decisão em `funcionalidades/geral/` (`geral-decisao-AAAA-MM-DD-estrutura`, `geral-decisao-AAAA-MM-DD-stack`), com o link para esta seção no campo Proposta.
- **Frontend:** [a preencher]
- **Backend:** [a preencher]
- **Tecnologias e versões:** [a preencher]
- **Ajustes do humano:** (nenhum ainda)

### 🔗 Conexões
- Projeto: [[geral-contexto]]
- Mapa: [[moc-orquestra]]
- Regras: [[manual-da-orquestra]]
