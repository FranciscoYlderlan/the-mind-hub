---
aliases: [Manual do Obsidian, Regras das minhas notas, Obsidian rules, Guia de escrita do cofre]
tags: [ferramentas/obsidian, perfil/regras]
tipo: manual
status: rascunho
criado: 2026-10-26
origem: Pesquisa sobre Obsidian + meus documentos de rotina (Sistema TickTick e Ciência do Sistema)
---

> [!info] Cópia do Vault
> Cópia de `Vault/Items/Manual do Meu Cérebro no Obsidian.md`, versão v6. O original manda: ao mudar lá, rode `cofre.py sincronizar`.
>
> **Escopo neste cofre:** vale para as notas de `referencias/` e `MOCs/` o perfil, o tom, o esqueleto, os links e os tipos (seções 1, 2, 5, 6, 7 e 8), e a taxonomia de tags. Pastas, nomes de arquivo e destino das notas (seção 3, item 3 da seção 10 e "Salva em Items/" do checklist) são substituídos pelo [[manual-da-orquestra]]: aqui não existe `Items/`, e arquivos são kebab-case (`moc-tema.md`). O limite de ~350 palavras (seção 6) também não vale aqui: vale o `limite-palavras` do bloco `padroes` do `CLAUDE.md`.

# 🧭 Manual do Meu Cérebro no Obsidian

> [!tldr] Em uma linha
> Este arquivo diz quem eu sou, como minhas notas devem ser escritas e quais regras valem para toda memória nova, para que eu e qualquer IA escrevamos do mesmo jeito.

Pense nele como o **ritual de acordar das notas**: é sempre igual, então não gasto decisão nenhuma na hora de escrever. O esqueleto é fixo, o conteúdo muda. Ponto de entrada do cofre: [[moc-orquestra]].

---

> [!note] Como usar (30 segundos)
> 1. Escrevendo sozinho: sigo as seções 5, 6 e 12.
> 2. Pedindo para uma IA: colo este arquivo inteiro no início da conversa e uso o comando curto da seção 10.
> 3. Dúvida de sintaxe: seção 7.
> 4. Mudou uma regra? Altero aqui e anoto no histórico (fim do arquivo).

---

## 1. 👤 Quem eu sou

> [!info] Perfil prático
> Informado por mim nos meus documentos de rotina. Serve para ajustar o formato das notas, não para me rotular.

**Rotina e energia**
- Cronotipo extremamente matutino: acordo por volta das 5h.
- Pico de energia: 6h–11h30. Queda: 15h–18h.
- Uso "Tipos de Dia" (A, B, C) em vez de dias fixos: esqueleto previsível, conteúdo variável.

**Momento de vida**
- Em busca ativa de emprego. Vagas é prioridade nº 1, todo dia útil (6h–8h), e nunca pula.
- Estudo Programação, Inglês e Investimentos. Quando for contratado, entra "Estudos do Trabalho".
- Sou inseguro. Medir **esforço**, não resultado, me protege. Silêncio de recrutador pesa mais do que parece que devia.

**Como minha cabeça funciona**
- TDAH e Autismo nível 1 (AuDHD).
- O tempo "some": prazo distante não pesa até estar em cima. Preciso de estrutura **externa e visível** no ponto de ação.
- Começar é o gargalo. Depois que engrena, flui.
- Atenção em túnel: um assunto por vez. Trocar de assunto custa energia.
- Previsibilidade me acalma. Mesmice me entedia. Por isso: esqueleto fixo, analogia nova a cada nota.

**Ferramentas**
- TickTick (plano grátis): 6 listas, Kanban, hábitos, Pomodoro 15/5. Já usei Habitica e senti falta de histórico real de progresso, sem RPG.
- Regra de ouro: **TickTick guarda o que eu faço (tarefas e tempo). Obsidian guarda o que eu sei e penso.** Nenhuma tarefa mora no Obsidian; ela só aponta para o TickTick.

**O que eu gosto nas notas**
- Divertido, lógico, direto e visualizável. Pé no chão.
- Analogias do dia a dia (o amigo que pede confirmação de tudo, o rádio amador, o timer do forno).
- Ritmo que alterna: texto fluido, pausa visual, bloco de impacto.

**O que eu NÃO quero**
- Tom gótico, sombrio, dramático ou clínico.
- Motivacional genérico.
- Parágrafo longo, jargão sem explicação, cobrança ou culpa.

> [!question]- Para eu completar depois
> - Onde mais escrevo (celular ou computador)?
> - Prefiro notas de conceito em tom neutro e memórias em 1ª pessoa (padrão atual) ou tudo em 1ª pessoa?
> - Quantos emojis estão bons para mim (padrão: 1 no título + 1 por bloco)?

---

## 2. 🔬 O que a pesquisa mostrou (e como isso vira regra para mim)

> [!warning] Nível de evidência
> Sintaxe e recursos do Obsidian vêm da documentação oficial: sólido. "Obsidian + TDAH" vem de relatos de usuários em fóruns e blogs: útil, mas anedótico. "Obsidian + autismo": quase nada encontrado. Nesse ponto, as regras vêm dos meus próprios documentos (monotropismo e previsibilidade).

| Prática | Por que importa para mim | Regra aplicada |
|---|---|---|
| Links valem mais que pastas; organização em excesso atrapalha mais que organização de menos | Decidir "em qual pasta vai?" é imposto de função executiva | Só 5 pastas. Toda nota mora em `Items/`. Navego por links, busca e MOCs |
| Sistema "oportunista", sem manutenção pesada agendada | Se exigir faxina dedicada, eu abandono | Processar o Inbox quando der (de preferência 15h–18h). Sem revisão semanal obrigatória |
| Uma ideia por nota (nota atômica) | Atenção em túnel: um assunto por vez | Nota com 2 assuntos vira 2 notas |
| Templates tiram decisões | Cada escolha pequena gasta energia | Esqueleto fixo (seção 6) salvo como modelo |
| MOC (mapa de conteúdo) quando acumula nota solta | Dá previsibilidade de "onde está tudo" | Criar MOC ao chegar em ~6 notas soltas do mesmo tema |
| Links para notas ainda inexistentes são permitidos | Capturo a ideia sem parar para criar a nota | Link "vermelho" = fila de ideias futuras |
| Customização infinita é armadilha | Posso passar semanas mexendo no app em vez de usar | Zero plugins comunitários no início (seção 3) |
| Propriedades com formato correto | Em versões recentes, `tags` e `aliases` fora do formato de lista podem ser ignorados | Sempre lista, sempre no plural (seção 4) |
| "Onde parei" (migalha de pão) em notas de projeto | Trocar de assunto custa caro | Bloco opcional `[!tip] Onde parei` |

> [!note] O que ajustei no prompt original
> 1. **Link de bloco corrigido.** O formato certo é `[[Nota#^id]]`, não `[[Nota^bloco]]`.
> 2. **Tags como lista, sem `#`** dentro do frontmatter.
> 3. **⚡ "Em uma linha"** no topo: entendo a nota em 5 segundos, sem esforço de iniciar.
> 4. **Gatilho "Quando abrir esta nota"**: estrutura externa no ponto de ação.
> 5. **Quatro tipos de nota** com o mesmo esqueleto (como meus Tipos de Dia).
> 6. **Limites de tamanho** e mapa fixo de callouts.
> 7. **Seção "Conexões"** no fim, para rastreabilidade (MOC, relacionadas, próxima).
> 8. **Propriedades `tipo`, `status`, `criado` e `origem`** para busca e rastreio.

---

## 3. 🧱 Estrutura do cofre

```
Cofre/
├── 00 Inbox/      captura rápida (1 linha basta)
├── Items/         TODAS as notas (pensamentos), incluindo a Home
├── MOCs/          mapas de assunto
├── Anexos/        imagens e PDFs
├── Modelos/       esqueletos (templates)
└── CLAUDE.md      guia do cofre para agentes de IA (ver [[Guia do cofre para IA]])
```

> [!info] Cofres de projeto são diferentes
> As 5 pastas valem para o `Vault` (minha vida). Cofres de projeto usam a estrutura `orquestra/`, com notas operacionais (contexto, plano, decisão, bug, diário) em kebab-case. Ver [[manual-da-orquestra]].

> [!note] Regra da pasta Items
> 1. Todo pensamento novo (conceito, memória, procedimento ou manual) nasce em `Items/`.
> 2. Fora dela, só: capturas no `00 Inbox`, mapas em `MOCs`, arquivos em `Anexos` e esqueletos em `Modelos`.
> 3. Ao processar o Inbox, a nota pronta **sai** do Inbox e vai para `Items/`.
> 4. Automático: Configurações → Arquivos e links → Local padrão para novas notas → "Na pasta especificada abaixo" → `Items`. Assim, clicar num link vermelho já cria a nota no lugar certo.

**Nomes de arquivo**
- Sem emoji no nome do arquivo (o emoji fica no `# Título` dentro da nota). Assim o autocomplete de `[[` e a busca ficam fáceis de digitar.
- Nome = título, curto e claro. Acentos podem.
- Evitar `# ^ [ ] | \ / :` no nome, porque quebram links.
- MOCs começam com "MOC ", por exemplo `MOC Programação`.
- Imagens: `kebab-case`, sem acento, descritivas, por exemplo `pomodoro-15-5-linha-do-tempo.png`.

**Orçamento de plugins**
- Começo só com os plugins nativos: Propriedades, Templates, Backlinks, Links de saída, Visualização em grafo, Busca.
- No plugin Templates, apontar a pasta `Modelos`. No modelo, usar `criado: {{date}}` e `# {{title}}`.
- Plugin comunitário só entra se a mesma dor se repetir por 2 semanas. Um por vez.
- Mexer no app **nunca** no bloco de Vagas (6h–8h).

**Home e MOCs**
- Começo só com `Home`. Os MOCs nascem quando houver ~6 notas soltas do mesmo tema.
- MOCs iniciais prováveis, espelhando as listas do TickTick: Carreira e Vagas, Programação, Inglês, Investimentos, Rotina e Descanso, Perfil.

---

## 4. 🏷️ Metadados (frontmatter)

Todo arquivo começa assim, sem exceção:

| Propriedade | Valores | Regra |
|---|---|---|
| `aliases` | lista de 2 a 4 | Sinônimo, termo em inglês, sigla, e "como eu falaria esquecendo o nome" |
| `tags` | lista de 1 a 3 | Da taxonomia fechada abaixo. Minúsculas, sem acento, sem `#` |
| `tipo` | conceito, memoria, procedimento, moc, manual | Um só. Em cofres de projeto, também contexto, plano, decisao, bug, diario, referencia ([[manual-da-orquestra]] §7) |
| `status` | rascunho, em-uso, consolidada, arquivado | Nasce `rascunho` |
| `criado` | AAAA-MM-DD | Data de criação |
| `origem` | texto curto ou URL | De onde veio (aula, vídeo, conversa, experiência). Opcional, mas incentivado |

> [!warning] Armadilhas de formato
> - Sempre `aliases` e `tags` no plural. As versões `alias` e `tag` deixaram de funcionar.
> - `tags` e `aliases` precisam ser **lista**, nunca texto solto.
> - Sem `#` dentro do frontmatter. O `#` é só para tag escrita no corpo da nota.
> - Sem propriedades aninhadas: ficam difíceis de editar na interface.
> - Nunca duas propriedades `tags` na mesma nota.

**Taxonomia fechada de tags** (nova tag só se nenhuma servir):

| Tag | Uso |
|---|---|
| `estudos/programacao` | código, lógica, projetos |
| `estudos/ingles` | vocabulário, listening, gramática |
| `estudos/investimentos` | conceitos de finanças e investimento |
| `carreira/vagas` | busca, candidaturas, currículo |
| `carreira/entrevistas` | preparação e aprendizados |
| `trabalho/estudos` | só depois de contratado |
| `rotina/pomodoro`, `rotina/descanso`, `rotina/ritual` | meu sistema de dia a dia |
| `perfil/cronotipo`, `perfil/tdah`, `perfil/autismo` | como eu funciono |
| `ferramentas/ticktick`, `ferramentas/obsidian` | como usar as ferramentas |

Status e tipo ficam em **propriedades**, não em tags, para não poluir a lista de tags.

---

## 5. ✍️ Regras de escrita e tom

> [!tldr] Em uma linha
> Escrever como um amigo que explica rápido, com os pés no chão e um exemplo na mão.

| Faça | Evite |
|---|---|
| Frases curtas (~15 a 20 palavras), uma ideia por frase | Parágrafo-paredão |
| **1 analogia do cotidiano por nota**, nova a cada nota | Repetir a mesma analogia em notas vizinhas |
| Verbos de ação, voz ativa | Voz passiva e rodeio |
| Termo técnico em português + (English) na 1ª vez, e o inglês vira alias | Jargão solto sem explicação |
| Esforço e fatos: "fiz 5 candidaturas" | Julgamento: "falhei", "deveria", "preguiça" |
| Erro = "ponto de ajuste" | Culpa e autocrítica |
| Humor leve, nunca sarcasmo sobre mim | Ironia que pode machucar |
| 1 a 3 palavras em **negrito** por seção | Negrito em tudo, CAIXA ALTA |
| Emoji como marcador visual (título e blocos) | Emoji decorativo em toda frase |

**Vocabulário proibido** (tom): sombrio, abismo, tormento, diagnóstico, paciente, sintoma (em tom médico), "você precisa", "nunca mais".

**Pessoa verbal (padrão):** conceitos e procedimentos em tom direto e neutro. Memórias em 1ª pessoa.

**Investimentos:** a nota ensina o conceito e registra a fonte. Nunca recomenda comprar ou vender ativo.

---

## 6. 🎼 O esqueleto e o ritmo

O ritmo vem do contraste: **fluido → pausa → impacto → rápido → impacto → resumo**. Duas coisas do mesmo tipo nunca ficam coladas.

````markdown
---
aliases: [Sinônimo, Termo em inglês, Como eu falaria no dia a dia]
tags: [area/subarea]
tipo: conceito
status: rascunho
criado: AAAA-MM-DD
origem: de onde veio (opcional)
---
# 🧩 Título Direto

> [!tldr] Em uma linha
> Uma frase com a essência da nota.

Parágrafo fluido (máx. 4 linhas) com UMA analogia do cotidiano e [[Links]] na primeira menção dos termos.

---

![[nome-da-imagem.png|400]]
*Legenda curta: o que o print, gráfico ou foto deve mostrar.*

---

> [!note] Subtítulo do bloco
> 1. Passo ou regra curta.
> 2. Passo ou regra curta.
> 3. Passo ou regra curta.
> Se ficar complexo: [[Nota#Seção|submemória]].

> [!tip] Quando abrir esta nota
> Gatilho concreto: em que situação do meu dia eu volto aqui.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** frase curta de impacto com [[Link]].
* **Ponto 2:** vantagem ou aplicação real.
* **Ponto 3:** limite, erro comum ou ponto fraco.

### 🔗 Conexões
- Mapa: [[MOC Tema]]
- Relacionadas: [[Nota A]], [[Nota B]]
- Próxima: [[Nota C]]
````

**Limites de projeto** (heurísticas minhas, ajustáveis):

| Elemento | Limite |
|---|---|
| ⚡ Em uma linha | 1 frase, até ~25 palavras |
| Parágrafo fluido | até 4 linhas |
| Callout de passos | até 6 itens, 1 linha cada |
| Resumo para o cérebro | exatamente 3 pontos |
| Callouts por nota | até 4 |
| Nota inteira | cabe em 1 a 2 telas. Passou de ~350 palavras: dividir em submemórias. Em cofre de projeto vale o limite do `CLAUDE.md` do cofre ([[manual-da-orquestra]] §7) |

**Mapa fixo de callouts** (sempre o mesmo visual para o mesmo papel):

- `[!tldr]`: a essência em uma linha.
- `[!note]`: como funciona (passos e regras).
- `[!tip]`: gatilho de uso, "Onde parei", dica prática.
- `[!warning]`: armadilha ou erro comum.
- `[!example]`: exemplo concreto.

Se o tipo de callout não for reconhecido, o Obsidian o mostra como `note`. Para esconder detalhe, usar callout dobrável: `[!note]-` (fechado) ou `[!note]+` (aberto).

**Imagem:** só quando ajudar de verdade. Se o arquivo ainda não existe, mantenha a linha: ela vira o lembrete de "falta o print". Salve a imagem em `Anexos/` com o nome exato.

---

## 7. 🔗 Links e submemórias

**Sintaxe (copiar e usar)**
- Nota inteira: `[[Nome da Nota]]`
- Seção: `[[Nome da Nota#Seção]]`
- Bloco específico: `[[Nome da Nota#^id-do-bloco]]`
- Texto de exibição amigável: `[[Nome da Nota#Seção|texto que aparece]]`
- Mostrar o conteúdo dentro de outra nota (embed): `![[Nome da Nota#Seção]]`
- Imagem com largura: `![[arquivo.png|400]]`
- Atalhos de busca ao digitar: `[[##` procura títulos no cofre inteiro, `[[^^` procura blocos.

> [!warning] Sobre links de bloco
> - O id do bloco vai no fim do bloco, com espaço antes: `... texto do bloco ^regra-5-min`
> - O id aceita só letras, números e hífen.
> - Link de bloco é recurso do Obsidian, não Markdown padrão: não funciona fora dele.
> - Prefiro link de **seção**. Bloco só para algo muito específico.

**Regras de conexão (rastreabilidade)**
1. Toda nota tem **2 ou mais links de saída** e aparece em **pelo menos um MOC** ou em outra nota. Nada fica órfão.
2. Linko o termo na **primeira menção**. Não pinto o texto inteiro de azul.
3. Criar o link antes da nota é permitido: link vermelho = ideia na fila.
4. Notas de aprendizado devem apontar para a nota de quem ensinou ou para a fonte (campo `origem`).

**Quando criar uma submemória**
- A seção passa de 6 passos ou ~8 linhas, **ou**
- aparece um segundo assunto dentro da nota.

Na nota original sobra **1 frase + o link** (`[[Nota#Seção]]`). A nota principal continua leve e curta.

---

## 8. 🧰 Os 4 tipos de nota

Mesmo esqueleto, bloco central diferente. Igual aos meus Tipos de Dia: previsível por fora, variado por dentro.

| Tipo | Emoji | Para quê | Bloco central |
|---|---|---|---|
| conceito | 🧠 | Entender algo | `[!note] Como funciona` (passos ou regras) e, se couber, `[!warning]` |
| memoria | 📓 | Algo que aconteceu, decidi ou aprendi | `[!note] O que aconteceu` (só fatos, 3 a 5 linhas) e `[!tip] O que eu levo disso` (1 ajuste prático) |
| procedimento | 🛠️ | Como fazer algo | `[!note] Passo a passo` (até 6) e `[!tip] Quando abrir`, com linha final `→ TickTick: lista X` |
| moc | 🗺️ | Mapa de um tema | Sem analogia. Título `MOC Tema`, 3 a 6 cabeçalhos, só links com meia frase de contexto |

**Memórias sobre rejeição ou silêncio de vaga:** escrever o que **eu fiz** e o que **eu controlo**. Não escrever o que "deu errado".

---

## 9. ⏰ Quando mexer no Obsidian

| Momento | O que faço |
|---|---|
| 6h–8h (Vagas) | Obsidian fechado. Ideia nova? 1 linha no `00 Inbox` e volto |
| 8h–11h30 (estudo) | Escrevo notas de **conceito** logo depois de estudar o assunto: 5 a 10 min, 1 Pomodoro por nota |
| 15h–18h (baixa energia) | Tarefas mecânicas: processar Inbox, ligar notas, criar MOC, corrigir metadados |
| Qualquer hora | Captura de 1 linha |

- Se um dia sair do combinado, nada quebra: o Inbox acumula e eu processo quando der.
- Registro de esforço (candidaturas, Pomodoros) fica no **TickTick**. No Obsidian entra só o que aprendi com isso.

---

## 10. 🤖 Instruções para a IA

> [!warning] Para a IA que ler este arquivo
> Escreva para mim usando o perfil da seção 1 e as regras das seções 4 a 8.

1. Atue como **arquiteto de conhecimento especialista em Obsidian**.
2. Entregue **uma nota por vez**, dentro de um bloco de código markdown (4 crases), pronta para colar.
3. Depois do bloco, escreva 4 linhas fixas:
   - **Arquivo:** `Items/Nome sugerido.md` (sem emoji; MOC vai em `MOCs/`)
   - **Linkar em:** o MOC onde ela entra
   - **Submemórias sugeridas:** se houver
   - **Links novos (ainda não existem):** lista
4. Se faltar algo essencial, faça **no máximo 1 pergunta**. Caso contrário, assuma e marque `[a confirmar]`.
5. **Não invente** fatos, números, citações ou fontes. Na dúvida, diga que não sabe. Se usou fontes, coloque no campo `origem`.
6. Só crie `[[links]]` plausíveis. Se eu colar a lista das minhas notas, use os nomes que já existem.
7. Respeite os limites da seção 6. Estourou? Proponha submemória em vez de alongar.
8. Tom da seção 5. Nunca gótico, dramático, clínico ou motivacional vazio. Nunca julgue. Esforço vale mais que resultado.
9. Ajustes: devolva a **nota completa** corrigida, não só o trecho.
10. "Atualize o manual": devolva só o trecho alterado + a linha de histórico.

**Comando curto de uso** (colo este arquivo no início e depois só isto):

````
Use meu Manual do Cérebro.
Tipo: conceito | memória | procedimento | moc
Tópico: ...
(Opcional) Notas que já existem: ...
````

---

## 11. 📄 Exemplo completo

````markdown
---
aliases: [Pomodoro curto, Pomodoro 15/5, Timer de foco, Pomodoro technique]
tags: [rotina/pomodoro, ferramentas/ticktick]
tipo: procedimento
status: rascunho
criado: 2026-10-26
origem: Meu sistema de produtividade no TickTick (protocolo Pomodoro personalizado)
---
# 🍅 Pomodoro Curto 15/5

> [!tldr] Em uma linha
> Ligo um timer de 15 minutos, foco até ele tocar, descanso 5: começar é a única meta.

É o **timer do forno**: não preciso "assar o bolo inteiro", só ligar o timer e esperar tocar. O relógio fica à vista e avisa o tempo que meu cérebro não avisa sozinho. Combina com [[Cegueira temporal]] e com os [[Tipos de Dia]].

---

![[pomodoro-15-5-linha-do-tempo.png|400]]
*Linha do tempo: 3 blocos de 15 min com 5 de pausa, e uma pausa longa no fim.*

---

> [!note] Como rodo
> 1. Escolho **uma** tarefa (um assunto por vez).
> 2. Inicio o timer nativo do TickTick: 15 min.
> 3. Pausa de 5 min: levanto, água, olho longe.
> 4. A cada 3 blocos: pausa longa de 15 a 20 min.
> 5. Rendendo bem? Posso esticar. A meta é começar e voltar.
> 6. Depois de 2 semanas firmes: +5 min por vez.

> [!tip] Quando abrir esta nota
> Quando travar para começar uma Vaga ou um estudo.
> → TickTick: lista Vagas & Candidaturas, bloco das 6h–8h.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** A meta é *começar*, não bater número perfeito: o timer faz o papel do [[Cegueira temporal|relógio interno]].
* **Ponto 2:** 15/5 com pausa longa a cada 3 blocos, e +5 min só depois de 2 semanas consistentes.
* **Ponto 3:** Erro comum: aumentar o bloco rápido demais. Um passo de 5 min por vez.

### 🔗 Conexões
- Mapa: [[MOC Rotina]]
- Relacionadas: [[Cegueira temporal]], [[Tipos de Dia]], [[Candidatura diária]]
````

---

## 12. ✅ Checklist antes de salvar

- [ ] Frontmatter completo: `aliases` (2–4), `tags` (1–3 da taxonomia), `tipo`, `status`, `criado`.
- [ ] `aliases` e `tags` em lista, no plural, sem `#`.
- [ ] Título com emoji dentro da nota. Nome do arquivo sem emoji.
- [ ] Salva em `Items/` (MOC em `MOCs/`).
- [ ] ⚡ Em uma linha preenchido.
- [ ] Parágrafo fluido com até 4 linhas e 1 analogia.
- [ ] Contraste de ritmo: nenhum bloco igual colado em outro.
- [ ] Resumo com exatamente 3 pontos.
- [ ] 2+ links de saída **e** link de entrada (aparece num MOC ou hub). Saída sem entrada é nota órfã.
- [ ] Segui Atualizar a memória (no Vault) e rodei `cofre.py verificar` com zero ERRO.
- [ ] Nada de tarefa solta: ação vira `→ TickTick`.
- [ ] Tom limpo: sem culpa, sem drama, sem clínico.

---

## 🔗 Conexões
- Mapa: [[moc-orquestra]]
- Relacionadas: Tipos de Dia (no Vault), Cegueira temporal (no Vault)

## 🕓 Histórico
- v1 (2026-10-26): criação, a partir da pesquisa e dos meus documentos de rotina.
- v2 (2026-10-26): todas as notas passam a morar na pasta `Items/` (seção 3, seção 10 e checklist).
- v3 (2026-10-27): todo cofre ganha um `CLAUDE.md` na raiz (seção 3).
- v4 (2026-10-28): cofres de projeto passam a usar a estrutura `orquestra/` e as notas operacionais do [[manual-da-orquestra]] (seções 3 e 4); `status` ganha `arquivado`.
- v5 (2026-10-28): checklist exige link de entrada e `cofre.py verificar`; aliases do Manual ajustados para 4 (seção 12).
- v6 (2026-10-29): o limite de ~350 palavras não vale em cofre de projeto; lá vale o limite do `CLAUDE.md` do cofre (seção 6).

## 📚 Fontes
- Links internos, blocos e embeds: https://obsidian.md/help/links
- Callouts: https://help.obsidian.md/callouts
- Glossário (propriedades, frontmatter, vault): https://obsidian.md/help/glossary
- Mudanças de `tags`, `aliases` e `cssclasses` nas versões 1.9.x: https://publish.obsidian.md/tasks/Support%20and%20Help/Missing%20tags%2C%20aliases%20and%20cssclasses%20in%20some%20Obsidian%201.9.x%20versions
- Links vs. tags: https://forum.obsidian.md/t/a-guide-on-links-vs-tags-in-obsidian/28231
- Pastas, tags, links e MOCs: https://forum.obsidian.md/t/in-what-ways-can-we-form-useful-relationships-between-notes-long-read/702
- MOCs na prática (regra de ~6 links soltos): https://obsidian.rocks/quick-tip-quickly-organize-notes-in-obsidian/
- Organização do cofre (links valem mais que pastas): https://aura-lab.siue.edu/intro-to-obsidian/08-organization.html
- Obsidian e TDAH (relatos de usuários): https://forum.obsidian.md/t/trying-to-find-a-good-setup-for-adhd/12218, https://forum.obsidian.md/t/adhd-and-obsidian/89491, https://www.obsibrain.com/blog/obsidian-for-adhd, https://typeshare.co/marcuslyons/posts/how-i-use-obsidian-to-organize-my-thoughts-as-a-software-developer-with-adhd
- Base do perfil: meus documentos "Sistema de Produtividade (TickTick)" e "A Ciência Por Trás do Seu Sistema".