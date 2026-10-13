---
aliases: [Alimentar o cofre, Registrar no cofre, Update memory, Como salvo algo na memória]
tags: [ferramentas/obsidian, estudos/programacao]
tipo: procedimento
status: em-uso
criado: 2026-10-28
origem: Falhas de processo de 2026-10-28 (modelos sem conexões e cópias com links quebrados) e 2026-10-29 (mudança de estado sem varredura); regras N01 a N04, N12 e N15 do núcleo comum (2026-11-16)
---
# 🛠️ Atualizar a Memória

> [!tldr] Em uma linha
> Toda escrita no cofre passa pelas mesmas 6 etapas, acontece assim que o relatório ou a decisão chega e só termina com o `cofre.py verificar` em zero ERRO e o commit do cofre.

É como **guardar um documento no arquivo do escritório**: pôr na gaveta não basta, precisa anotar no índice. Senão ninguém acha, nem eu. As etapas são as mesmas da parte B das [[Manual da Orquestra#🚦 Etapas vitais|Etapas vitais]], e valem no `Vault` e em todo cofre criado por [[Criar um novo cofre]].

---

> [!note] Passo a passo
> 1. Relatório ou decisão aprovada chegou? **Registro na hora**. Acho o gatilho e **busco antes**: se a nota já existe, atualizo. Mudou um fato ou regra? **Varro o impacto**: busco o estado antigo e listo toda nota que o cita.
> 2. Classifico (tipo → modelo → pasta → nome) e peço aval quando a regra exige.
> 3. Escrevo **a partir do modelo**, nunca do zero.
> 4. Conecto nos dois sentidos: Conexões na nota e link de volta no hub ou MOC.
> 5. Propago: reescrevo no estado atual cada nota da varredura e anoto o estado antigo como `antigo:` no `padroes`; decisão mudou? Alteração reescrita, ou nota nova com `substitui:` se já aplicada; contexto e diário (dia com partes: na parte mais recente); mudou o original no `Vault`? `cofre.py sincronizar`.
> 6. Rodo `cofre.py verificar`. Com ERRO, volto ao passo 3. Com zero, commito o cofre (a cada ciclo, para desfazer com `git restore`) e digo "pronto".

> [!warning] Armadilhas
> - Conferir só link quebrado não basta: **link que falta não aparece como quebrado**. O verificar procura órfãs e notas com menos de 2 saídas.
> - Quem escreveu não se autoaprova. Quem decide é o verificar.
> - Copiar nota entre cofres à mão quebra links. Cópia é sempre pelo `cofre.py`.
> - Atualizar só a nota dona deixa o estado antigo nas outras. Aviso "onde fala X, vale Y" por cima de texto velho **é** o erro: reescrevo.
> - Juntar registros para o fim da sessão perde relatório quando o chat acaba. Registro assim que chega ([[Manual da Orquestra#1. 🎯 Tese e princípios|princípio 8]]).

> [!tip] Quando abrir esta nota
> Toda vez que eu ou um agente for criar, mudar, mover ou copiar uma nota.
> → Comando: `python Modelos/Orquestra/cofre.py verificar .` (no `Vault`) ou `python orquestra/modelos/cofre.py verificar .` (no projeto)

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** Nota só existe quando está no mapa: link de entrada e 2+ de saída, como pede o [[Manual do Meu Cérebro no Obsidian|Manual]].
* **Ponto 2:** O verificar transforma regra em portão: sem zero ERRO, não acabou.
* **Ponto 3:** Erro comum: corrigir a nota e esquecer a origem. Falha repetida vira etapa ou checagem nova aqui.

### 🔗 Conexões
- Mapa: [[MOC Programação]]
- Relacionadas: [[Manual da Orquestra]], [[Manual da Orquestra - Núcleo comum]], [[Criar um novo cofre]], [[Guia do cofre para IA]]
- Próxima: [[Criar um novo cofre]]
