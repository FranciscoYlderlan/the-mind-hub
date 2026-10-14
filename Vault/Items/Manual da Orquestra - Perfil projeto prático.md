---
aliases: [Perfil projeto prático, Regras de cofre de projeto prático, Hands-on project profile, Como a orquestra roda num projeto de entrega]
tags: [estudos/programacao, ferramentas/obsidian]
tipo: manual
status: em-uso
criado: 2026-11-16
origem: Regras P01 a P16 do pacote aprovado pelo humano em 2026-11-16 (diario-2026-11-16-regras-para-o-vault, no stonebid-vault) e trechos do Manual da Orquestra até a v9
---
# 🏗️ Manual da Orquestra: perfil projeto prático

> [!tldr] Em uma linha
> O que vale a mais num cofre de projeto que entrega algum produto: contrato, roteiro em fatias, verificação, aceitação final e o lado concreto (worktree, diff, testes) das regras neutras do Manual.

É a **obra com planta aprovada**: o regulamento do condomínio ([[Manual da Orquestra - Núcleo comum]]) vale para todo mundo, mas quem está construindo tem também alvará, vistoria e entrega das chaves. Este é um perfil do [[Manual da Orquestra]]; o outro é o [[Manual da Orquestra - Perfil estudo]]. Projeto de software soma o [[Padrão de projeto de software]] e, na criação, a proposta da [[Referência de arquitetura e stack]].

---

## 1. 📜 Contrato e roteiro

- **P01 Contrato versionado:** o que foi combinado com o humano mora num hub com uma nota por seção vigente e uma nota `-mudancas` com os itens M-xx. Mudança de escopo segue 5 passos: (1) alguém aponta o conflito ou a necessidade; (2) a IA propõe o texto exato e o impacto em requisitos, testes e plano; (3) o humano aprova ou recusa; (4) o contrato e o histórico de versões são atualizados; (5) só então o produto muda.
- **P02 Etapa = fatia de ponta a ponta:** cada etapa do roteiro atravessa o produto inteiro, liga-se aos IDs dos requisitos que atende e vai para o ar.
- **P13 Teste e requisito saem juntos:** um teste só sai do escopo junto com o requisito que ele prova.
- **P14 Definição de pronto global:** uma lista única, valendo para toda tarefa, além do "pronto quando" de cada uma.

## 2. 🔍 Verificação e aceitação

- **P04 Duas frentes:** a verificação olha o ambiente real e o código, em rodadas com nome.
- **P03 Seção "Desvios"** na Verificação: desvios aprovados (com link para a decisão) e desvios "sem aval".
- **P05 Recurso único:** atende um verificador por vez (forma geral em G7, [[Manual da Orquestra - Agentes em paralelo]]).
- **P06 Achados vão ao humano como opções:** corrigir, registrar como limite ou deixar como opcional.
- **P15 Bug com passos, esperado e obtido.** O verificador não corrige.
- **P16 Dados de teste** criados em ambiente compartilhado ficam listados na Verificação.
- **P07 Aceitação final** contra o documento-fonte: verificadores por área mais um avaliador independente (nota de 0 a 10). O encerramento registra o período no ar e o estado final.

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
| §4 e §5 passo 6 (verificador) | Lê o diff inteiro atrás de mudança fora do escopo; roda testes, lint e tipos |
| §4 (revisor) | Lê código e decisões; especialidades: segurança, requisitos, testes, arquitetura, regressão e alucinação, performance |
| §5 passo 8 (juntar) | Merge das branches só com aval do humano; depois, a suíte inteira |
| §8 Dial | `alto` para código legado; `baixo` para código bem estruturado |
| §9 Riscos | Worktree por implementador evita colisão; verificador sempre junto com testes, lint e tipos |
| A2 e A5 de [[Criar um novo cofre]] | Perguntar o repositório e se o projeto será publicado ou só local (`--publicado` do `cofre.py criar`); ligar o repositório com o [[modelo-claude-do-repositorio]]; em software, propor arquitetura e stack no `geral-plano` (S25) |
| "Acesso" do [[Modelo de CLAUDE do cofre]] | Onde ficam os repositórios vira decisão em `funcionalidades/geral/`; apagar arquivos, forçar push ou mexer na branch principal fora do CI/CD: sempre com confirmação |
| [[modelo-briefing-subagente]] | "Trabalhe em" = worktree; "Prova" = comando de teste, lint ou tipos |

## 🔗 Conexões
- Mapa: [[MOC Programação]]
- Nota-mãe: [[Manual da Orquestra]]
- Relacionadas: [[Manual da Orquestra - Perfil estudo]], [[Manual da Orquestra - Núcleo comum]], [[Padrão de projeto de software]]

## 🕓 Histórico
- v1 (2026-11-16): criação, com P01 a P16 e os trechos do Manual que presumiam software (princípio 7, §4, §5 passos 5, 6 e 8, §8, §9, A2, A5, acesso do modelo de CLAUDE, briefing).
- v2 (2026-11-16): A2 e A5 perguntam se o projeto será publicado ou só local (`--publicado` do `cofre.py criar`) e põem a proposta de arquitetura e stack no `geral-plano`.
