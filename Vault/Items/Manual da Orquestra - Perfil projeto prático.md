---
aliases: [Perfil projeto prático, Regras de cofre de projeto prático, Hands-on project profile, Como a orquestra roda num projeto de entrega]
tags: [estudos/programacao, ferramentas/obsidian]
tipo: manual
status: em-uso
criado: 2026-11-16
origem: Regras P01 a P16 do pacote aprovado pelo humano em 2026-11-16 (diario-2026-11-16-regras-para-o-vault, no stonebid-vault) e trechos do Manual da Orquestra até a v9; Q01 a Q06 do pacote "contrato funcional e validação" de 2026-11-17, depois da avaliação técnica do Stonebid
---
# 🏗️ Manual da Orquestra: perfil projeto prático

> [!tldr] Em uma linha
> O que vale a mais num cofre de projeto que entrega algum produto: contrato funcional, roteiro em fatias, verificação por agentes, aceitação final e o lado concreto (worktree, diff, testes) das regras neutras do Manual.

É a **obra com planta aprovada**: o regulamento do condomínio ([[Manual da Orquestra - Núcleo comum]]) vale para todo mundo, mas quem está construindo tem também alvará, vistoria e entrega das chaves. Este é um perfil do [[Manual da Orquestra]]; o outro é o [[Manual da Orquestra - Perfil estudo]]. Projeto de software soma o [[Padrão de projeto de software]] e, na criação, a proposta da [[Referência de arquitetura e stack]].

---

## 1. 📜 Contrato e roteiro

- **P01 Contrato versionado:** o que foi combinado com o humano mora em `docs/contrato/` do repositório de código (Q01), com as mudanças aprovadas em `docs/contrato/mudancas.md` (itens M-xx); o cofre guarda as decisões e o diário, com link para lá. Mudança de escopo segue 5 passos: (1) alguém aponta o conflito ou a necessidade; (2) a IA propõe o texto exato e o impacto em requisitos, critérios de aceite e plano; (3) o humano aprova ou recusa; (4) o bloco do contrato passa a dizer o estado novo e o M-xx entra em `mudancas.md`; (5) só então o produto muda.
- **P02 Etapa = fatia de ponta a ponta:** cada etapa do roteiro atravessa o produto inteiro, liga-se aos IDs dos requisitos que atende e vai para o ar.
- **P13 Teste e requisito saem juntos:** um teste só sai do escopo junto com o requisito que ele prova.
- **P14 Definição de pronto global:** uma lista única, valendo para toda tarefa, além do "pronto quando" de cada uma. Funcionalidade com interface só fica pronta com os AC dos UC passando no verificador de fluxo principal e no adversarial (Q03 a Q05).

## 2. 🔍 Verificação e aceitação

- **P04 Duas frentes:** a verificação olha o ambiente real e o código, em rodadas com nome.
- **P03 Seção "Desvios"** na Verificação: desvios aprovados (com link para a decisão) e desvios "sem aval".
- **P05 Recurso único:** atende um verificador por vez (forma geral em G7, [[Manual da Orquestra - Agentes em paralelo]]).
- **P06 Achados vão ao humano como opções:** corrigir, registrar como limite ou deixar como opcional.
- **P15 Bug com passos, esperado e obtido.** O verificador não corrige.
- **P16 Dados de teste** criados em ambiente compartilhado ficam listados na Verificação.
- **P07 Aceitação final** contra o documento-fonte, depois do roteiro do humano (Q06): verificadores por área mais um avaliador independente (nota de 0 a 10). O encerramento registra o período no ar e o estado final.

## 3. 🤖 Agentes e acesso

- **P08 Manual de bordo do agente** e nota de acesso de teste. Segredo real nunca entra no cofre.
- **P09 Mapa do que cada ambiente alcança** (nuvem, computador do humano, navegador). Insistir em caminho bloqueado é proibido.
- **P10 Briefing do implementador** cita as regras de forma do humano, como o [[Padrão de commit]].
- **P11 Entrega assim que termina:** cada implementador entrega quando acaba; o orquestrador registra enquanto os outros trabalham.
- **P12 Tarefa-interface** antes de tarefas paralelas que dependem uma da outra (forma geral em G1).

## 4. 🛠️ O lado concreto das regras neutras

O [[Manual da Orquestra]] diz cada regra em forma neutra; no projeto prático ela fica assim:

| Onde no Manual | No projeto prático |
|---|---|
| Princípio 7 (prova objetiva) | Testes, lint, tipos e CI valem mais que o julgamento do agente |
| §4 Papéis, §5 passo 5 (espaço isolado) | Cada implementador na própria git worktree e branch |
| §4 e §5 passo 6 (verificador) | Lê o diff inteiro atrás de mudança fora do escopo; roda testes, lint e tipos. Ao final de cada funcionalidade, o verificador de fluxo principal e o adversarial executam os AC do contrato (Q04 e Q05) |
| §4 (revisor) | Lê código e decisões; especialidades: segurança, requisitos, testes, arquitetura, regressão e alucinação, performance |
| §5 passo 8 (juntar) | Merge das branches só com aval do humano; depois, a suíte inteira |
| §8 Dial | `alto` para código legado; `baixo` para código bem estruturado |
| §9 Riscos | Worktree por implementador evita colisão; verificador sempre junto com testes, lint e tipos; interface sem regra escrita: contrato funcional e os dois agentes (Q01 a Q05) |
| A2 e A5 de [[Criar um novo cofre]] | Perguntar o repositório e se o projeto será publicado ou só local (`--publicado` do `cofre.py criar`); ligar o repositório com o [[modelo-claude-do-repositorio]] e copiar `Modelos/Orquestra/contrato/` para `docs/contrato/`, com o `00-requisitos` preenchido do documento-fonte (Q01); em software, propor arquitetura e stack no `geral-plano` (S25) |
| "Acesso" do [[Modelo de CLAUDE do cofre]] | Onde ficam os repositórios vira decisão em `funcionalidades/geral/`; apagar arquivos, forçar push ou mexer na branch principal fora do CI/CD: sempre com confirmação |
| [[modelo-briefing-subagente]] | "Trabalhe em" = worktree; "Prova" = comando de teste, lint ou tipos; cartões do verificador de fluxo principal e do adversarial (Q04 e Q05) |

## 5. 🧾 Contrato funcional e validação

O backend já tinha regra no domínio (S14), erro com código (S15) e estado inválido provado no CI (S22). Estas regras dão o mesmo à interface: ENT é o domínio que toda tela herda, ERR é o código de erro do servidor e AC é a prova. Fala do humano (2026-11-17): "Refinar o vault responsável por criar vault's para que os próximos vaults já venham com a estrutura pre definida para garantir a consistencia do frontend ... assim como é feito hoje nas regras de negócio no backend que foi pontuado como bem feito".

- **Q01 Contrato funcional no repositório:** os 8 blocos do [[Contrato funcional]] moram em `docs/contrato/` do repositório de código, junto com RF, RNF e RN quando eles não estão em outro lugar do repositório. Os modelos chegam ao cofre pelo `cofre.py` e ao repositório na criação ([[Criar um novo cofre]], passo 4).
- **Q02 Tela não cria regra:** cada tela lista os CMP, UC e NAV que realiza. Regra que falta entra primeiro no contrato, pelos 5 passos do P01; validação de campo vem do ENT (S26).
- **Q03 Contrato antes da primeira tela:** cada funcionalidade com interface começa preenchendo os blocos dela. O "pronto quando" dela é "AC dos UC passando nos dois agentes" (Q04 e Q05).
- **Q04 Verificador de fluxo principal:** roda ao final de toda funcionalidade, no frontend (Playwright) e no backend (HTTP ou a camada MCP, S23), e executa os AC dos fluxos principais dos UC dela. Não deixa suíte no repositório e não corrige; bug no formato do P15. Fala do humano: "Ele é um agente que roda sempre ao final de uma funcionalidade no frontend backend".
- **Q05 Adversarial:** roda depois do Q04 sem bug aberto, no frontend e no backend. Executa os AC dos FA e FE e a lista fixa de ataques do cartão no [[modelo-briefing-subagente]]: valores fora do ENT, perfil errado e URL direta, duplo clique, ação durante a atualização em tempo real, estado inicial pela URL, voltar ou recarregar e mensagem igual para erros diferentes. Não corrige; bug no formato do P15. Bug achado volta para um implementador novo, e os dois agentes rodam de novo.
- **Q06 Fluxos registrados e roteiro do humano:** funcionalidade que passou nos dois agentes tem os fluxos de teste registrados no cofre (`geral-plano-teste-humano`, do [[modelo-roteiro-teste-humano]]), prontos para o humano usar a qualquer momento. Só na etapa final o orquestrador entrega o roteiro, sucinto e didático: tarefas só com o objetivo (descoberta) e poucos fluxos que cobrem o máximo de AC. Vem antes da aceitação final (P07); achados viram opções (P06).

## 🔗 Conexões
- Mapa: [[MOC Programação]]
- Nota-mãe: [[Manual da Orquestra]]
- Relacionadas: [[Manual da Orquestra - Perfil estudo]], [[Manual da Orquestra - Núcleo comum]], [[Padrão de projeto de software]], [[Contrato funcional]]

## 🕓 Histórico
- v1 (2026-11-16): criação, com P01 a P16 e os trechos do Manual que presumiam software (princípio 7, §4, §5 passos 5, 6 e 8, §8, §9, A2, A5, acesso do modelo de CLAUDE, briefing).
- v2 (2026-11-16): A2 e A5 perguntam se o projeto será publicado ou só local (`--publicado` do `cofre.py criar`) e põem a proposta de arquitetura e stack no `geral-plano`.
- v3 (2026-11-17): §5 com Q01 a Q06 (contrato funcional em `docs/contrato/` do repositório, tela sem regra, contrato antes da tela, verificador de fluxo principal, adversarial, fluxos registrados e roteiro do humano no fim); P01 com o contrato e os M-xx no repositório; P14 e P07 com os dois agentes e o roteiro; §4 com os agentes, a cópia do contrato e os cartões.
