---
aliases: [Alimentar o cofre, Registrar no cofre, Update memory, Como salvo algo na memória]
tags: [ferramentas/obsidian, estudos/programacao]
tipo: procedimento
status: em-uso
criado: 2026-10-28
origem: Falha de processo de 2026-10-28 (modelos sem conexões e cópias com links quebrados)
---
# 🛠️ Atualizar a Memória

> [!tldr] Em uma linha
> Toda escrita no cofre passa pelas mesmas 6 etapas e só termina quando o `cofre.py verificar` dá zero ERRO.

É como **guardar um documento no arquivo do escritório**: pôr na gaveta não basta, precisa anotar no índice. Senão ninguém acha, nem eu. As etapas são as mesmas da parte B das [[Manual da Orquestra#🚦 Etapas vitais|Etapas vitais]], e valem no `Vault` e em todo cofre criado por [[Criar um novo cofre]].

---

> [!note] Passo a passo
> 1. Acho o gatilho e **busco antes**: se a nota já existe, atualizo em vez de criar outra.
> 2. Classifico (tipo → modelo → pasta → nome) e peço aval quando a regra exige.
> 3. Escrevo **a partir do modelo**, nunca do zero.
> 4. Conecto nos dois sentidos: Conexões na nota e link de volta no hub ou MOC.
> 5. Propago: contexto e diário; mudou o original no `Vault`? `cofre.py sincronizar` nos cofres de projeto.
> 6. Rodo `cofre.py verificar`. Com ERRO, volto ao passo 3. Com zero, digo "pronto".

> [!warning] Armadilhas
> - Conferir só link quebrado não basta: **link que falta não aparece como quebrado**. O verificar procura órfãs e notas com menos de 2 saídas.
> - Quem escreveu não se autoaprova. Quem decide é o verificar.
> - Copiar nota entre cofres à mão quebra links. Cópia é sempre pelo `cofre.py`.

> [!tip] Quando abrir esta nota
> Toda vez que eu ou um agente for criar, mudar, mover ou copiar uma nota.
> → Comando: `python Modelos/Orquestra/cofre.py verificar .` (no `Vault`) ou `python orquestra/modelos/cofre.py verificar .` (no projeto)

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** Nota só existe quando está no mapa: link de entrada e 2+ de saída, como pede o [[Manual do Meu Cérebro no Obsidian|Manual]].
* **Ponto 2:** O verificar transforma regra em portão: sem zero ERRO, não acabou.
* **Ponto 3:** Erro comum: corrigir a nota e esquecer a origem. Falha repetida vira etapa ou checagem nova aqui.

### 🔗 Conexões
- Mapa: [[MOC Programação]]
- Relacionadas: [[Manual da Orquestra]], [[Criar um novo cofre]], [[Guia do cofre para IA]]
- Próxima: [[Criar um novo cofre]]
