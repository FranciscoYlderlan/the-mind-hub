# Edicoes propostas: (arquivo, texto atual exato, texto novo). Cada texto atual deve ocorrer 1 vez.
E = []
def e(f, a, n): E.append((f, a, n))

P = "Items/Manual da Orquestra - Perfil projeto prático.md"
e(P, "o que foi combinado com o humano mora em `docs/contrato/` do repositório de código (Q01), com as mudanças aprovadas em `docs/contrato/mudancas.md` (itens M-xx); o cofre guarda as decisões e o diário, com link para lá.",
     "o que foi combinado com o humano mora em `Anexos/contrato/` do cofre do projeto (Q01), com as mudanças aprovadas em `Anexos/contrato/mudancas.md` (itens M-xx), ao lado das decisões e do diário.")
e(P, "(4) o bloco do contrato passa a dizer o estado novo e o M-xx entra em `mudancas.md`;",
     "(4) o orquestrador reescreve o bloco do contrato no estado novo e registra o M-xx em `mudancas.md`;")
e(P, "depois vem o roteiro do humano (Q06), e o aceite dele é a palavra final.",
     "depois vem o roteiro do humano (Q06), e o aceite dele é a palavra final. Com o aceite, o orquestrador copia `Anexos/contrato/` para `docs/contrato/` do repositório, num commit só (Q01).")
e(P, "ligar o repositório com o [[modelo-claude-do-repositorio]] e copiar `orquestra/modelos/contrato/` do cofre novo (original no `Vault`: `Modelos/Orquestra/contrato/`) para `docs/contrato/`, com o `00-requisitos` preenchido do documento-fonte (Q01);",
     "ligar o repositório com o [[modelo-claude-do-repositorio]] e preencher, a partir do documento-fonte, o `Anexos/contrato/00-requisitos.md` que o `cofre.py criar` pôs no cofre novo (Q01);")
e(P, "| \"Trabalhe em\" = worktree; \"Prova\" = comando de teste, lint ou tipos; cartões do verificador de fluxo principal e do adversarial (Q04 e Q05) |",
     "| \"Trabalhe em\" = worktree; \"Prova\" = comando de teste, lint ou tipos; cartões do verificador de fluxo principal e do adversarial (Q04 e Q05); todo subagente lê o contrato no cofre e não o altera (Q01) |")
e(P, """- **Q01 Contrato funcional no repositório:** os 8 blocos do [[Contrato funcional]] moram em `docs/contrato/` do repositório de código, junto com RF, RNF e RN quando eles não estão em outro lugar do repositório. Com frontend e backend em repositórios separados, ficam só no do backend, e o do frontend aponta para lá (decisão do humano, 2026-11-17: "Frontend e backend em repositórios separados: onde fica `docs/contrato/`? ... deixar no repositório do backend, com o do frontend apontando para ele. Concordo"). Os modelos (no `Vault`, `Modelos/Orquestra/contrato/`) chegam ao cofre de projeto em `orquestra/modelos/contrato/` pelo `cofre.py`, e de lá ao repositório na criação ([[Criar um novo cofre]], passo 4).""",
     """- **Q01 Contrato funcional no cofre:** os 8 blocos do [[Contrato funcional]], o `README.md` e o `mudancas.md` moram em `Anexos/contrato/` do cofre do projeto, em Markdown puro (não são notas: sem frontmatter), com RF, RNF e RN no `00-requisitos.md`. O `cofre.py criar` os cria a partir de `Modelos/Orquestra/contrato/` do `Vault` ([[Criar um novo cofre]], passo 2), e ali eles são editados durante todo o projeto. Durante o projeto, o repositório de código não tem `docs/contrato/`: na aceitação final, depois do aceite do humano, o orquestrador copia `Anexos/contrato/` para `docs/contrato/` do repositório, num commit só (P07). **Só o orquestrador altera o contrato**, no cofre e na cópia do repositório. Subagente que precisar de mudança devolve no relatório o arquivo, o trecho atual, o trecho novo e o motivo, e a mudança segue os 5 passos do P01. No cofre, onde subagente já não escreve, essa regra se sustenta sozinha. Implementador, verificadores e adversarial leem o contrato pela Obsidian CLI (`obsidian read path="Anexos/contrato/03-casos-de-uso.md"`) ou, sem CLI, pelo arquivo, avisando no relatório. Com frontend e backend em repositórios separados, os dois leem o mesmo contrato do cofre (decisão do humano, 2026-11-19).""")
e(P, "Regra que falta entra primeiro no contrato, pelos 5 passos do P01; validação de campo vem do ENT (S26).",
     "Regra que falta entra primeiro no contrato (`Anexos/contrato/`), pelos 5 passos do P01, com o item M-xx em `mudancas.md`; validação de campo vem do ENT (S26).")
e(P, "§4 com os agentes, a cópia do contrato e os cartões.",
     "§4 com os agentes, a cópia do contrato e os cartões.\n- v4 (2026-11-19): Q01 com o contrato funcional em `Anexos/contrato/` do cofre do projeto (criado pelo `cofre.py criar`, alterado só pelo orquestrador, lido pelos subagentes pela CLI) e copiado para `docs/contrato/` do repositório só na aceitação final, depois do aceite do humano; P01, P07, Q02 e §4 no mesmo estado. Origem: decisão do humano em 2026-11-19.")

C = "Items/Contrato funcional.md"
e(C, "> O que o produto faz, escrito em 8 blocos com IDs em `docs/contrato/` do repositório, para a interface ter regra tão firme quanto o servidor.",
     "> O que o produto faz, escrito em 8 blocos com IDs em `Anexos/contrato/` do cofre do projeto, para a interface ter regra tão firme quanto o servidor.")
e(C, "pelos 5 passos do P01, com o item M-xx em `mudancas.md`.",
     "pelos 5 passos do P01, com o item M-xx em `Anexos/contrato/mudancas.md`.")
e(C, """- No repositório de código, em `docs/contrato/`, com os requisitos RF, RNF e RN quando eles não estão em outro lugar do repositório.
- Frontend e backend em repositórios separados: o contrato fica só no repositório do backend, e o `CLAUDE.md` do frontend aponta para ele, sem cópia. Decisão do humano (2026-11-17): "Frontend e backend em repositórios separados: onde fica `docs/contrato/`? ... deixar no repositório do backend, com o do frontend apontando para ele. Concordo".
- Os modelos ficam no `Vault`, em `Modelos/Orquestra/contrato/`. O `cofre.py` os leva a `orquestra/modelos/contrato/` de todo cofre de projeto prático, e é de lá que o passo 4 de [[Criar um novo cofre]] os copia para `docs/contrato/` do repositório.
- O cofre do projeto guarda as decisões e o diário, com link para lá. O [[modelo-claude-do-repositorio]] avisa os agentes que trabalham no código.""",
     """- No cofre do projeto, em `Anexos/contrato/`: os 8 blocos, o `README.md` e o `mudancas.md`, em Markdown puro (não são notas: sem frontmatter nem Conexões), com os requisitos RF, RNF e RN no `00-requisitos.md`. Ali o contrato nasce e é editado durante todo o projeto, ao lado das decisões e do diário.
- Os modelos ficam no `Vault`, em `Modelos/Orquestra/contrato/`. O `cofre.py criar` os copia para `Anexos/contrato/` de todo cofre de projeto prático; o `sincronizar` nunca sobrescreve o contrato de um cofre que já existe.
- Só o orquestrador altera o contrato. Subagente que precisar de mudança devolve no relatório o arquivo, o trecho atual, o trecho novo e o motivo, e a mudança segue os 5 passos do P01.
- Implementador, verificadores e adversarial leem o contrato pela Obsidian CLI (`obsidian read path="Anexos/contrato/03-casos-de-uso.md"`) ou, sem CLI, pelo arquivo, avisando no relatório. Frontend em repositório separado lê o mesmo contrato do cofre.
- O repositório de código só recebe o contrato na aceitação final: depois do aceite do humano, o orquestrador copia `Anexos/contrato/` para `docs/contrato/`, num commit só, e nenhum subagente altera essa cópia. O [[modelo-claude-do-repositorio]] diz aos agentes que trabalham no código onde ler.""")
e(C, "> Ao ligar o repositório de um projeto prático novo, ao começar",
     "> Ao criar um cofre de projeto prático, ao começar")
e(C, "a regra da tela e `docs/contrato/` no repositório.",
     "a regra da tela e `docs/contrato/` no repositório.\n- v2 (2026-11-19): o contrato mora em `Anexos/contrato/` do cofre do projeto, criado pelo `cofre.py criar`; só o orquestrador o altera; o repositório recebe a cópia em `docs/contrato/` só na aceitação final.")

B = "Items/Contrato funcional - Os 8 blocos.md"
e(B, "com o ID dele e o arquivo de `docs/contrato/` onde mora.", "com o ID dele e o arquivo de `Anexos/contrato/` onde mora.")
e(B, "(no cofre de projeto prático, em `orquestra/modelos/contrato/`)", "(no cofre de projeto prático, o contrato em uso fica em `Anexos/contrato/`)")
e(B, "- v1 (2026-11-17): criação, separada do [[Contrato funcional]] pelo tamanho.",
     "- v1 (2026-11-17): criação, separada do [[Contrato funcional]] pelo tamanho.\n- v2 (2026-11-19): os arquivos moram em `Anexos/contrato/` do cofre do projeto.")

M = "Items/Manual da Orquestra.md"
e(M, "└── Anexos/                       imagens e PDFs", "└── Anexos/                       imagens e PDFs; no prático, contrato/ (contrato funcional)")
e(M, "| `arquivos/` | Funcionalidades finalizadas | Orquestrador move, com minha confirmação |",
     "| `arquivos/` | Funcionalidades finalizadas | Orquestrador move, com minha confirmação |\n| `Anexos/contrato/` (prático) | [[Contrato funcional]] do projeto | Só o orquestrador, com meu aval; subagente propõe a mudança no relatório |")
e(M, "Prático: repositório, com o contrato copiado de `orquestra/modelos/contrato/` do cofre novo para `docs/contrato/` ([[Contrato funcional]]);",
     "Prático: repositório ligado pelo [[modelo-claude-do-repositorio]] e `Anexos/contrato/00-requisitos.md` preenchido do documento-fonte ([[Contrato funcional]]);")
e(M, "| `contrato/` | Arquivos do [[Contrato funcional]] para `docs/contrato/` do repositório (perfil prático; Markdown puro, não são notas) |",
     "| `contrato/` | Arquivos do [[Contrato funcional]], que o `cofre.py criar` copia para `Anexos/contrato/` do cofre novo (perfil prático; Markdown puro, não são notas) |")
e(M, "Origem: pacote \"contrato funcional e validação\" (Q01 a Q06 do perfil projeto prático).",
     "Origem: pacote \"contrato funcional e validação\" (Q01 a Q06 do perfil projeto prático).\n- v13 (2026-11-19): o contrato funcional mora em `Anexos/contrato/` do cofre do projeto (estrutura, §3 e A5), criado pelo `cofre.py criar` e alterado só pelo orquestrador; o repositório recebe a cópia só na aceitação final. Origem: decisão do humano em 2026-11-19.")

N = "Items/Criar um novo cofre.md"
e(N, "Nascem também `orquestra/padroes.md` (bloco `padroes`, `limite-palavras: 2000`) e,",
     "Nascem também `orquestra/padroes.md` (bloco `padroes`, `limite-palavras: 2000`), no prático o [[Contrato funcional]] em `Anexos/contrato/` e,")
e(N, "(o nome da pasta e `readme` são do `the-mind-hub`), copio `orquestra/modelos/contrato/` para `docs/contrato/` do repositório (com frontend e backend separados, só no do backend; o trecho colado no frontend aponta para lá) e preencho o `00-requisitos.md` a partir do documento-fonte ([[Contrato funcional]], Q01);",
     "(o nome da pasta e `readme` são do `the-mind-hub`) e preencho o `Anexos/contrato/00-requisitos.md` do cofre a partir do documento-fonte ([[Contrato funcional]], Q01: o repositório só recebe o contrato na aceitação final);")
e(N, "e a última etapa entrega o roteiro do humano (Q06).",
     "e a última etapa entrega o roteiro do humano (Q06) e, depois do aceite, copia o contrato para `docs/contrato/` do repositório.")

G = "Items/Guia do cofre para IA.md"
e(G, "No perfil prático, leva também a pasta `contrato/` para `orquestra/modelos/contrato/`, sem converter: são os arquivos do [[Contrato funcional]] para `docs/contrato/` do repositório, não notas, e o `verificar` não os lê.",
     "O [[Contrato funcional]] fica de fora: no perfil prático, o `criar` copia a pasta `contrato/` uma vez para `Anexos/contrato/`, sem converter (não são notas, e o `verificar` não os lê), e o `sincronizar` nunca a sobrescreve, porque ali ela é o contrato do projeto.")

R = "Items/Referência de arquitetura e stack.md"
e(R, "Na raiz do repositório de código (com frontend e backend separados, no do backend) fica `docs/contrato/`, o [[Contrato funcional]] que frontend e backend seguem (Q01 do [[Manual da Orquestra - Perfil projeto prático|perfil]]):",
     "Em `Anexos/contrato/` do cofre do projeto fica o [[Contrato funcional]] que frontend e backend seguem; o repositório de código só recebe a cópia em `docs/contrato/` na aceitação final (Q01 do [[Manual da Orquestra - Perfil projeto prático|perfil]]):")
e(R, "docs/contrato/   README.md (índice), 00-requisitos a 08-criterios-de-aceite, mudancas.md",
     "Anexos/contrato/   README.md (índice), 00-requisitos a 08-criterios-de-aceite, mudancas.md")
e(R, "executam os AC de `docs/contrato/`;", "executam os AC do contrato (`Anexos/contrato/` do cofre);")
e(R, "e o contrato em `docs/contrato/` como fonte das regras da tela.", "e o contrato em `Anexos/contrato/` do cofre como fonte das regras da tela.")

S = "Items/Padrão de projeto de software.md"
e(S, "tem schema zod tirado do ENT-xx de `docs/contrato/` (tipo,", "tem schema zod tirado do ENT-xx do contrato (`Anexos/contrato/02-entidades.md` do cofre do projeto) (tipo,")
e(S, "ID citado só se existir em `docs/contrato/`.", "ID citado só se existir no contrato (`Anexos/contrato/` do cofre do projeto).")
e(S, "e S27 (comentário curto e pontual).", "e S27 (comentário curto e pontual).\n- v4 (2026-11-19): S26 e S27 apontam para o contrato em `Anexos/contrato/` do cofre do projeto.")

e("Items/Contrato só do backend deixa a interface sem regra.md",
  "[[Contrato funcional]] em `docs/contrato/` (Q01),", "[[Contrato funcional]] em `Anexos/contrato/` do cofre, alterado só pelo orquestrador (Q01),")
e("MOCs/MOC Programação.md", "os 8 blocos em `docs/contrato/` do repositório,", "os 8 blocos em `Anexos/contrato/` do cofre do projeto,")

K = "Modelos/Modelo de CLAUDE do cofre.md"
e(K, "- **Contrato antes do código:** toda funcionalidade começa preenchendo os blocos dela em `docs/contrato/` do repositório (ENT, UC com FA e FE, ERR, AC; com interface, também CMP e NAV; modelos em `orquestra/modelos/contrato/`); tela não cria regra.",
     "- **Contrato antes do código:** toda funcionalidade começa preenchendo os blocos dela em `Anexos/contrato/` deste cofre (ENT, UC com FA e FE, ERR, AC; com interface, também CMP e NAV); tela não cria regra.\n"
     "- **Só o orquestrador altera o contrato:** subagente lê pela CLI (`obsidian read path=\"Anexos/contrato/03-casos-de-uso.md\"`; sem CLI, pelo arquivo, avisando) e devolve a mudança proposta no relatório (arquivo, trecho atual, trecho novo, motivo). O repositório só recebe a cópia em `docs/contrato/` na etapa final, depois do aceite do humano, num commit só.")

O = "Modelos/Orquestra/"
e(O+"modelo-claude-do-repositorio.md", """- Frontend em repositório separado do backend: o contrato mora só em `docs/contrato/` do repositório do backend (`{{caminho-ou-link-do-backend}}`); neste repositório, todo `docs/contrato/` abaixo se lê lá, sem cópia. Repositório único ou do backend: apague esta linha.
- `docs/contrato/` é a fonte de verdade do que o produto faz: requisitos, atores (ATR), entidades (ENT), casos de uso (UC), componentes (CMP), erros (ERR), navegação (NAV) e critérios de aceite (AC). Ordem e regras em `docs/contrato/README.md`.
- Tela não cria regra: cada tela realiza CMP, UC e NAV do contrato. Regra que falta entra primeiro no contrato, com aval do humano e item em `docs/contrato/mudancas.md`.""",
  """- O contrato mora no cofre, em `{{caminho-do-cofre}}/Anexos/contrato/`: é a fonte de verdade do que o produto faz, para backend e frontend (mesmo em repositório separado): requisitos, atores (ATR), entidades (ENT), casos de uso (UC), componentes (CMP), erros (ERR), navegação (NAV) e critérios de aceite (AC). Ordem e regras no `README.md` de lá.
- Leia o contrato pela Obsidian CLI (`obsidian read path="Anexos/contrato/03-casos-de-uso.md"`, com `vault="{{nome-do-cofre}}"`); sem CLI, pelo arquivo, avisando no relatório.
- Só o orquestrador altera o contrato. Subagente que precisar de mudança devolve no relatório o arquivo, o trecho atual, o trecho novo e o motivo.
- Este repositório não tem `docs/contrato/` durante o projeto: na aceitação final, depois do aceite do humano, o orquestrador copia `Anexos/contrato/` para `docs/contrato/`, num commit só. Nenhum subagente altera essa cópia.
- Tela não cria regra: cada tela realiza CMP, UC e NAV do contrato. Regra que falta entra primeiro no contrato, com aval do humano e item em `Anexos/contrato/mudancas.md`.""")
e(O+"modelo-claude-do-repositorio.md", "ID citado só se existir em `docs/contrato/` (S27).", "ID citado só se existir no contrato (S27).")
e(O+"modelo-claude-do-repositorio.md", "(modelos no `Vault` em `Modelos/Orquestra/contrato/`; no cofre de projeto, em `orquestra/modelos/contrato/`)",
  "(modelos no `Vault` em `Modelos/Orquestra/contrato/`; no cofre de projeto, o contrato em uso em `Anexos/contrato/`)")

F = O+"modelo-briefing-subagente.md"
e(F, "- **Não pode:** escrever no cofre; tocar fora da lista;", "- **Não pode:** escrever no cofre; alterar o contrato, no cofre ou no repositório (mudança necessária vai no relatório); tocar fora da lista;")
e(F, "- Faça: trabalhe só no seu espaço isolado e no que o \"Toca em\" lista; rode a prova; liste o que tocou.\n- Não faça: mudar o escopo;",
     "- Leia: no projeto prático, os blocos do contrato da funcionalidade em `Anexos/contrato/` do cofre, pela CLI (sem CLI, pelo arquivo, avisando no relatório).\n- Faça: trabalhe só no seu espaço isolado e no que o \"Toca em\" lista; rode a prova; liste o que tocou.\n- Não faça: alterar o contrato (proponha no relatório: arquivo, trecho atual, trecho novo, motivo); mudar o escopo;")
e(F, "- Leia: em `docs/contrato/` do repositório, os UC da funcionalidade",
     "- Leia: em `Anexos/contrato/` do cofre, pela CLI (`obsidian read path=\"Anexos/contrato/03-casos-de-uso.md\"`; sem CLI, pelo arquivo, avisando no relatório), os UC da funcionalidade")
e(F, "- Leia: em `docs/contrato/`, os UC (FA e FE),", "- Leia: em `Anexos/contrato/` do cofre, pela CLI (sem CLI, pelo arquivo, avisando no relatório), os UC (FA e FE),")

e(O+"modelo-relatorio-subagente.md", "- **Fora do escopo que notei:**",
  "- **Mudança proposta no contrato:** arquivo, trecho atual, trecho novo e motivo (o orquestrador decide e aplica)\n- **Fora do escopo que notei:**")

e(O+"modelo-roteiro.md", "o ciclo contrato da funcionalidade em `docs/contrato/` → implementação", "o ciclo contrato da funcionalidade em `Anexos/contrato/` → implementação")
e(O+"modelo-roteiro.md", "o aceite dele fecha o projeto.", "o aceite dele fecha o projeto, e então o orquestrador copia `Anexos/contrato/` para `docs/contrato/` do repositório, num commit só.")
e(O+"modelo-roteiro.md", "achados decididos como opções e aceite do humano registrado.",
  "achados decididos como opções, aceite do humano registrado e, depois dele, `Anexos/contrato/` copiado para `docs/contrato/` do repositório, num commit só.")
e(O+"modelo-roteiro-teste-humano.md", "`docs/contrato/08-criterios-de-aceite.md`", "`Anexos/contrato/08-criterios-de-aceite.md`")

e(O+"contrato/README.md", "Tela nenhuma cria regra.\n",
  "Tela nenhuma cria regra.\n\n## Onde mora e quem altera\n\n- Mora em `Anexos/contrato/` do cofre do projeto. Na aceitação final, depois do aceite do humano, o orquestrador o copia para `docs/contrato/` do repositório, num commit só.\n- Só o orquestrador altera o contrato, aqui e na cópia do repositório. Subagente lê e, se precisar de mudança, devolve no relatório o arquivo, o trecho atual, o trecho novo e o motivo.\n")
e(O+"contrato/README.md", "4. O bloco passa a dizer só o estado novo, e a mudança entra em `mudancas.md` (M-xx).",
  "4. O orquestrador reescreve o bloco no estado novo e registra a mudança em `mudancas.md` (M-xx).")

e("CLAUDE.md", "=> contrato funcional e itens M-xx em docs/contrato/ do repositório de código; o cofre guarda decisões e diário (Manual da Orquestra - Perfil projeto prático, P01 e Q01)",
  "=> contrato funcional e itens M-xx em Anexos/contrato/ do cofre do projeto, ao lado das decisões e do diário (Manual da Orquestra - Perfil projeto prático, P01 e Q01)")
