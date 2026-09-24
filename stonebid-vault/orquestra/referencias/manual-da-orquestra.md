---
aliases: [Orquestra de IA, Orquestração de agentes, Multi-agent orchestration, Como os agentes trabalham juntos]
tags: [estudos/programacao, ferramentas/obsidian]
tipo: manual
status: em-uso
criado: 2026-10-28
origem: Estudos "Modelo de Orquestra de IA" e "Arquitetura Orquestra de IA" (2026-10-28), dois vídeos sobre harness de agentes [a confirmar: títulos e links] e o modelo de registro de bugs de outra desenvolvedora
---

> [!info] Cópia do Vault
> Cópia de `Vault/Items/Manual da Orquestra.md`, versão v3. O original manda: ao mudar lá, rode `cofre.py sincronizar`.

# 🎼 Manual da Orquestra

> [!tldr] Em uma linha
> Como vários agentes de IA trabalham em paralelo num projeto usando o cofre como memória: o orquestrador rege, os subagentes tocam, eu decido.

É uma **cozinha de restaurante**. O chef lê o pedido e distribui os pratos. Cada cozinheiro trabalha na própria bancada. Quem prova o prato não é quem cozinhou. E só o chef escreve no caderno de receitas. As regras de escrita das notas continuam no [[manual-do-cerebro|Manual do Cérebro]]; a abertura de um cofre segue Criar um novo cofre (no Vault).

---

## 1. 🎯 Tese e princípios

O resultado de um agente depende menos do modelo e mais do que existe em volta dele: **memória** (o cofre), **guias**, **papéis** e **verificação**.

| # | Princípio |
|---|---|
| 1 | Se a IA errou ou perguntou algo por falta de contexto, esse contexto vira nota |
| 2 | O cofre é a fonte de conhecimento do projeto. Ordem de leitura: contexto → decisões → plano |
| 3 | Plano é sugestão da IA. Decisão é minha. Nunca se misturam |
| 4 | Quem cria nunca testa. Funcionalidades diferentes, agentes diferentes |
| 5 | Tarefas independentes rodam em paralelo; tarefas que tocam nos mesmos arquivos rodam em série |
| 6 | Contexto é finito: cada agente recebe só o que a tarefa precisa e sabe onde buscar o resto |
| 7 | Feedback determinístico (testes, lint, tipos, CI) vale mais que o julgamento do agente |
| 8 | Registrar no fim, não no meio. Atualizar a nota existente em vez de duplicar |
| 9 | **Só o orquestrador escreve no cofre.** Subagentes leem e devolvem relatório |
| 10 | Eu decido em dois pontos fixos: aprovar o plano e revisar o que é crítico |

Diagnóstico quando o agente erra (antes de culpar o modelo): faltou **instrução** clara? Faltou **contexto** ou havia nota velha enviesando? Faltou **ferramenta** para testar e um critério de pronto? Faltou **memória** no cofre? A resposta vira ajuste no cofre (princípio 1).

---

## 2. 🧱 Estrutura do cofre de projeto

Vale para todo cofre de projeto. O `Vault` pessoal mantém as 5 pastas do Manual do Cérebro e guarda os modelos em `Modelos/Orquestra/`.

```
nome-do-cofre/
├── CLAUDE.md                     índice para agentes (lido sozinho)
├── orquestra/
│   ├── entradas/                 brainstorms e anotações sem destino
│   ├── funcionalidades/          o que está em construção
│   │   ├── geral/                o projeto inteiro (nunca vai para arquivos/)
│   │   │   ├── geral-contexto.md
│   │   │   └── geral-plano.md    roteiro: etapas do projeto e onde ele está
│   │   └── lances-auto/
│   │       ├── lances-auto-contexto.md
│   │       ├── lances-auto-plano.md
│   │       └── lances-auto-decisao-2026-10-28-limite-por-usuario.md
│   ├── referencias/              consulta, acervo de abordagens, cópias dos manuais
│   ├── diarios/                  diario-2026-10-28.md
│   ├── modelos/                  cópia de Vault/Modelos/Orquestra/
│   ├── arquivos/                 funcionalidades finalizadas (a pasta inteira)
│   └── bugs/                     bug-cache-expirando-cedo-2026-10-28.md
├── MOCs/                         moc-tema.md
└── Anexos/                       imagens e PDFs
```

- `funcionalidades/geral/` guarda o contexto, as decisões que valem para o projeto todo (arquitetura, stack, nível do dial) e o **roteiro** (`geral-plano`).
- O `CLAUDE.md` é o único índice. Não existe `leia-primeiro.md`.

---

## 3. ✍️ Quem escreve o quê

| Nota | Natureza | Quem escreve |
|---|---|---|
| `<func>-contexto.md` | Hub da funcionalidade: objetivo, feito, tempo, links | Orquestrador, no fim da sessão |
| `<func>-plano.md` | Proposta da IA: tarefas, prioridades, verificação | Orquestrador |
| `geral-plano.md` (roteiro) | Etapas do projeto, status e notas geradas em cada uma | Orquestrador; a lista de etapas só muda com decisão minha |
| `<func>-decisao-<data>-<titulo>.md` | Uma decisão minha por nota | Orquestrador, **só depois do meu aval** |
| `bugs/bug-<titulo>-<data>.md` | Bug não trivial resolvido | Orquestrador, com meu aval |
| `diarios/diario-<data>.md` | Fatos de uma sessão relevante | Orquestrador |
| `entradas/` | Capturas | Eu. O agente só propõe destino |
| `referencias/` | Consulta e acervo | Eu. O agente sugere lacunas |
| `modelos/` | Esqueletos | Eu. O agente copia |
| `arquivos/` | Funcionalidades finalizadas | Orquestrador move, com minha confirmação |

Decisão que contradiz outra: nasce uma nota nova com `substitui: [[nota antiga]]`, e a antiga ganha `status: substituida`. Nada é apagado.

---

## 4. 🎭 Papéis

Papel é função, não agente fixo: um agente genérico assume o papel carregando o briefing certo (`modelos/modelo-briefing-subagente.md`).

| Papel | Faz | Lê | Devolve |
|---|---|---|---|
| **Orquestrador** (sessão principal) | Lê o cofre, planeja, despacha, junta, fala comigo, registra | CLAUDE.md, contexto, decisões, plano | Escreve no cofre |
| Pesquisador | Explora código, notas e internet | O que o briefing apontar | Relatório |
| Implementador | Constrói **uma** tarefa, na própria worktree | Tarefa do plano + decisões linkadas | Relatório + código |
| Verificador | Prova que a tarefa cumpre os critérios | Critérios + diff | Relatório com prova de cada critério |
| Revisor | Segurança, requisitos, testes, arquitetura, regressão/alucinação, performance | Código e decisões | Achados: bloqueante, deve corrigir, opcional |

Regras de separação: o implementador de uma tarefa nunca é o verificador dela; o orquestrador não implementa, para manter o contexto limpo.

---

## 5. 🔁 Fluxo de uma sessão

```
1. LER         orquestrador: CLAUDE.md → contexto → decisões → plano
2. PESQUISAR   pesquisadores em paralelo, só leitura, relatório de ~1 tela
3. PLANEJAR    orquestrador escreve o plano (tarefas com "toca em", "depende de", "pronto quando")
4. DECIDIR     eu aprovo ou altero → uma nota de decisão por item
5. IMPLEMENTAR um implementador por tarefa ∥, cada um na sua git worktree, contexto zerado
6. VERIFICAR   verificador novo por tarefa + testes e lint
               ✘ falhou → implementador novo corrige (máx. 2 voltas; na 3ª, o problema sobe para mim)
7. REVISAR     revisores em paralelo → eu reviso só o crítico (negócio e arquitetura)
8. JUNTAR      orquestrador junta as worktrees uma a uma e roda a suíte inteira
9. REGISTRAR   verificação no plano, bugs, contexto, diário
               + uma pergunta única: "estes candidatos viram nota?"
10. VERIFICAR  cofre.py verificar → zero ERRO (Etapas vitais B). Antes disso, nada está pronto
```

- **O plano é a ponte.** Ele e as decisões precisam bastar para um implementador que não viu a pesquisa. Se faltar algo, é lacuna de contexto (princípio 1).
- **Relatório curto e em formato fixo** (`modelos/modelo-relatorio-subagente.md`). Cinco textões enchem o contexto do orquestrador.
- **Dúvidas sobem nos relatórios.** Subagente não pergunta para mim; marca como "dúvida" ou "candidato a nota".
- **Plano não é apagado.** Funcionalidade concluída: o plano vira `status: arquivado` e a pasta inteira vai para `arquivos/` com meu ok. O que sobrevive de verdade está nas decisões, no contexto e em `bugs/`.

---

## 6. 🔎 Quando consultar e quando alimentar

**Consultar (antes de trabalhar)**

| Gatilho | Ação |
|---|---|
| Início de qualquer tarefa | `cofre.py status` (ou o roteiro `geral-plano`) → `geral-contexto` → contexto da funcionalidade → decisões → plano |
| Antes de investigar bug | Buscar em `bugs/` por sintoma (cache, 401, race, fallback, crash) e ler as decisões |
| Antes de decisão de arquitetura | Ler as decisões. Contradizer só de forma explícita, citando a nota |
| Ao tocar em área sensível | Contexto, `referencias/` e bugs daquela área |
| Antes de criar nota | `modelos/` |
| Antes de refazer algo parecido | `arquivos/` |
| Eu pergunto sobre uma data | `diarios/` |

**Alimentar (no fim do trabalho)**

| Gatilho | Ação |
|---|---|
| Bug não trivial resolvido | Nota em `bugs/` |
| Bug registrado reaparece ou ganha informação | Atualizar a nota existente |
| Bug ficou central | Nota + link no contexto |
| Decisão aprovada | Nota de decisão + atualizar a nota responsável |
| Tarefa concluída | Contexto ("o que já foi feito") e verificação no plano |
| Etapa do roteiro concluída | `concluida`, data e notas geradas no roteiro; `cofre.py status --atualizar` |
| Sessão relevante | Nota curta em `diarios/` |
| Estrutura se repetiu pela 3ª vez | Sugerir modelo novo |
| Lacuna de referência | Sugerir em `referencias/` |
| Item em `entradas/` | Propor destino e esperar meu ok |

Bug trivial (typo, erro de compilação, ajuste simples de layout) não vira nota. Na dúvida, entra na pergunta única do fim.

Lição de um bug que vale **fora** do projeto sobe para o `Vault` como nota de conceito (regra de fronteira).

---

## 7. 📏 Convenções do cofre de projeto

- Português brasileiro.
- Arquivos e pastas em **kebab-case**, sem acento. Notas operacionais levam **prefixo da funcionalidade** (`lances-auto-plano.md`) para não haver dois `plano.md`.
- Datas **AAAA-MM-DD** em nome de arquivo e frontmatter.
- Links com `[[wikilinks]]`. Nota sem link fica perdida.
- **Notas operacionais** (contexto, plano, decisão, bug, diário) usam o modelo próprio e ficam isentas de analogia, resumo de 3 pontos e limite de ~350 palavras. Notas de `referencias/` seguem o Manual do Cérebro.
- Frontmatter operacional: `tipo` (contexto, plano, decisao, bug, diario), `status`, `criado`, `funcionalidade`; `aliases` opcional (em bug, use os sintomas); `origem` e `tags` opcionais. Extras: decisão tem `substitui`; contexto de funcionalidade tem `etapa`; `geral-contexto` tem `etapa-atual`. Notas de `referencias/` (`tipo: referencia`, com `tema`) seguem o frontmatter completo do Manual do Cérebro, com `tags`.
- `status` por tipo: plano `proposta → aprovado → arquivado`; decisão `aprovada | substituida`; bug `resolvido`; contexto e etapa do roteiro `planejada → em-construcao → em-verificacao → concluida → arquivada`; diário `consolidada`; referência `rascunho → em-uso → consolidada`.
- Fatos que eu informei ficam preservados. Interpretação do agente fica em seção separada.
- Tarefa **de agente** mora no plano. Tarefa **minha** vai para o TickTick.
- O agente pede confirmação antes de apagar. Na dúvida, arquiva.

---

## 8. 🎚️ Dial de estrutura

Registrado no `geral-contexto` (pode ser sobrescrito por funcionalidade). Mudou o modelo de IA? Reavaliar o dial.

| Nível | Quando | Plano | Tradeoff |
|---|---|---|---|
| alto | Modelo fraco ou barato, código legado | Tarefas pequenas, cada uma com critério e teste de prova | Mais lento e mais tokens, mais seguro |
| medio | Maioria dos casos | Plano único com critérios de aceite | Equilíbrio |
| baixo | Modelo forte, código bem estruturado | Plano enxuto, implementador livre, verificação forte no fim | Mais rápido, depende do checklist |

---

## 9. ⚠️ Riscos

| Risco | Mitigação |
|---|---|
| Nota velha enviesa o agente | Atualizar em vez de duplicar; decisão substituída é marcada |
| Excesso de notas vira ruído | Gatilhos de consulta, CLAUDE.md enxuto, regra do bug trivial |
| Agentes paralelos colidem | Só o orquestrador escreve no cofre; worktree por implementador; "toca em" no plano |
| Proposta registrada como decisão | Nota de decisão só nasce depois do meu aval |
| Verificador tão fraco quanto o implementador | Sempre junto com testes, lint e tipos |
| Cópias dos manuais divergem entre cofres | Cada cópia traz a versão e a data; ao mudar o original, atualizo as cópias |
| Etapa pulada ao escrever no cofre (nota sem conexão, cópia com link quebrado) | Etapas vitais A e B + `cofre.py verificar` como portão |
| Ideias vindas de dois vídeos individuais | Validar no meu fluxo antes de virar regra |

---

## 🧭 Roteiro do projeto

O roteiro responde **onde o projeto está**, sem exigir que o agente entenda o projeto inteiro. Mora em `funcionalidades/geral/geral-plano.md` ([[modelo-roteiro]]) e é a primeira consulta de toda sessão, junto com `cofre.py status`.

- Uma seção por **etapa geral**, na ordem em que o projeto acontece. Exemplo, uma loja de café: 1. Alugar o ponto · 2. Mobiliar · 3. Comprar a máquina · 4. Abrir a loja · 5. Iniciar as vendas.
- Cada etapa tem: **Status**, Objetivo, Pronto quando, Funcionalidades (links para `<func>-contexto`), **Notas geradas** (links diretos para as decisões, bugs, diários e referências daquela etapa) e Concluída em.
- Status de etapa e de funcionalidade: `planejada → em-construcao → em-verificacao → concluida → arquivada`.
- A etapa atual é a primeira que não está concluída nem arquivada. Ela aparece no `[!tldr]` do roteiro e em `etapa-atual` no `geral-contexto`; `cofre.py status --atualizar` sincroniza os dois.
- Todo cofre nasce com a etapa 1 "Definir o roteiro do projeto". As etapas são proposta da IA até eu aprovar (nota `geral-decisao-AAAA-MM-DD-roteiro`). Mudar a lista de etapas é uma nova decisão.
- Cada `<func>-contexto` declara `etapa: N` e aparece em Funcionalidades da etapa N.
- Concluiu uma etapa: o orquestrador marca `concluida`, a data e as notas geradas, e roda `cofre.py status --atualizar` (etapa B6). O `cofre.py verificar` acusa qualquer divergência.

---

## 🚦 Etapas vitais

Valem para qualquer agente, inclusive a sessão principal. **Pular etapa é erro de processo.** "Quem cria não testa" vale também para a memória: quem aprova é o `cofre.py verificar`, não o agente que escreveu.

**A. Criar um cofre de projeto** (detalhe em Criar um novo cofre (no Vault))

| # | Etapa | Prova de que aconteceu |
|---|---|---|
| A1 | Ler: `CLAUDE.md` do Vault → este manual → Criar um novo cofre | — |
| A2 | Perguntar ao humano: nome, objetivo, repositório, tempo, dial. O que faltar vira `[a confirmar]` | Respostas registradas |
| A3 | `cofre.py criar` (nunca montar à mão) | Estrutura, kit, `CLAUDE.md`, moc, geral-contexto, roteiro e diário de criação |
| A4 | Preencher o geral-contexto com os fatos de A2 e propor as etapas do roteiro. Com meu aval: nota de decisão, roteiro preenchido e etapa 1 concluída | Decisão do roteiro + `cofre.py status` |
| A5 | Ligar o repositório de código ([[modelo-claude-do-repositorio]]) | Trecho no `CLAUDE.md` do repositório |
| A6 | `cofre.py verificar` | **Zero ERRO** |
| A7 | Humano: abrir no Obsidian, pasta de modelos, README, commit | — |

**B. Atualizar a memória** (toda escrita no cofre; detalhe em Atualizar a memória (no Vault))

| # | Etapa | Prova de que aconteceu |
|---|---|---|
| B1 | Gatilho: qual linha da tabela "Alimentar" (§6) pede a escrita | — |
| B2 | Buscar antes: a nota já existe? Atualizar em vez de duplicar | Busca feita |
| B3 | Classificar: tipo → modelo → pasta → nome (§7). Pedir aval quando a regra exige | Aval, quando aplicável |
| B4 | Escrever a partir do modelo, nunca do zero | Nota com o esqueleto do modelo |
| B5 | Conectar nos dois sentidos: Conexões (saída) e hub ou MOC (entrada). Nota fora do mapa não existe | Link de entrada e 2+ de saída |
| B6 | Propagar: etapa do roteiro concluída (status, data, notas geradas, `cofre.py status --atualizar`), contexto ("o que já foi feito" e diário), decisão substituída, histórico do manual. Mudou o original no Vault → `cofre.py sincronizar` em cada cofre de projeto | Notas afetadas atualizadas |
| B7 | `cofre.py verificar` | **Zero ERRO**. Só então "pronto" |

---

## 🧩 Modelos

Ficam em `Vault/Modelos/Orquestra/`. Nos cofres de projeto, o `cofre.py` mantém uma cópia em `orquestra/modelos/`.

| Modelo | Para quê |
|---|---|
| [[modelo-contexto]] | Hub de uma funcionalidade (e o `geral-contexto` do projeto) |
| [[modelo-roteiro]] | Roteiro do projeto (`geral-plano`): etapas, status e notas geradas |
| [[modelo-plano]] | Proposta da IA, tarefas e verificação |
| [[modelo-decisao]] | Uma decisão minha por nota |
| [[modelo-bug]] | Bug não trivial resolvido |
| [[modelo-diario]] | Fatos de uma sessão |
| [[modelo-referencia]] | Uma abordagem do acervo de orquestração |
| [[modelo-moc-orquestra]] | Mapa do cofre de projeto (`MOCs/moc-orquestra.md`) |
| [[modelo-briefing-subagente]] | O que o orquestrador envia a cada subagente |
| [[modelo-relatorio-subagente]] | O que cada subagente devolve |
| [[modelo-claude-do-repositorio]] | Trecho que liga o repositório de código ao cofre |
| Modelo de CLAUDE do cofre (no Vault) | O `CLAUDE.md` do cofre de projeto |
| [[modelo-nota]] | Notas de `referencias/` e `MOCs/` (esqueleto do Manual do Cérebro) |
| `cofre.py` | Ferramenta (não é nota): `criar`, `sincronizar` e `verificar` cofres |

---

## 🔗 Conexões
- Mapa: [[moc-orquestra]]
- Relacionadas: [[manual-do-cerebro]], Criar um novo cofre (no Vault), Atualizar a memória (no Vault), Guia do cofre para IA (no Vault)
- Mapa do cofre de projeto: [[modelo-moc-orquestra]]

## 🕓 Histórico
- v1 (2026-10-28): criação, a partir dos dois estudos e das decisões: orquestra completa só em cofres de projeto, `funcionalidades/`, AAAA-MM-DD, kebab-case com prefixo, uma nota por decisão, só o orquestrador escreve, CLAUDE.md como índice, notas operacionais isentas, dial de estrutura e gatilhos estendidos. Revisão trimestral não adotada.
- v2 (2026-10-28): Etapas vitais A (criar cofre) e B (atualizar memória), passo 10 do fluxo e `cofre.py` como verificador. Origem: modelos criados sem conexões e cópias com links quebrados porque a verificação só olhava links quebrados.
- v3 (2026-10-28): roteiro do projeto (`geral-plano`) com etapas, status e notas geradas; consulta no início de toda sessão; `cofre.py status`; status de contexto com 5 fases.
