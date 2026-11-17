---
aliases: [Mapa de programação, Como eu trabalho com código, Programming map]
tags: [estudos/programacao]
tipo: moc
status: em-uso
criado: 2026-10-26
origem: Manual do Meu Cérebro no Obsidian
---
# 🗺️ MOC Programação

> [!tldr] Em uma linha
> O mapa de como eu trabalho com código e do que estudo em programação.

## 🌿 Git e commits
- [[Padrão de commit]]: o formato fixo das minhas mensagens. Comece por aqui.
- [[Tipos e emojis de commit]]: a tabela de qual emoji usar em cada tipo.
- [[Commit atômico]]: uma mudança por commit.
- [[Commitar no the-mind-hub]]: o `.git` fica na raiz; sem acesso a ela, peço a pasta antes de commitar.

## 🚦 Etapas vitais (não pular)
- [[Criar um novo cofre]]: etapas A, do pedido ao `cofre.py verificar` com zero ERRO.
- [[Atualizar a memória]]: etapas B, para toda escrita em qualquer cofre.
- [[Manual da Orquestra#🔄 Passagem de turno]]: etapas C, para trocar de chat sem perder o fio.
- [[Manual da Orquestra#🚦 Etapas vitais]]: a tabela-fonte, com a prova de cada etapa.

## 🧠 Cofres (memórias) por projeto
- [[Criar um novo cofre]]: como abrir uma memória nova para um projeto.
- [[Guia do cofre para IA]]: o `CLAUDE.md` que todo cofre tem para os agentes.
- [[Registrar cofre no README]]: como colocar o cofre no mapa do repositório.

## 🐞 Bugs de ambiente
- [[Obsidian CLI via MCP não carrega]]: ferramentas `obsidian_*` ausentes na sessão; a config MCP certa é a que o botão "Editar configuração" abre.

## 🧪 Lições de projeto (valem para todos)
- [[API simulada conferida contra a API real]]: mock segue o presenter da API; erro que não veio da API não vai cru para a tela.
- [[Imagem de terceiro com anti-robô passa pelo servidor]]: rota própria com id validado, cache e limite.
- [[Teste de corrida com janela forçada]]: a prova de uma trava é o teste falhar sem ela.
- [[Tarefa agendada idempotente com disparo na leitura]]: agendador e leitura disparam; idempotência garante uma vez só.
- [[Tempo real por SSE com recarga de reserva]]: evento depois do COMMIT, polling de reserva e limite de concorrência.
- [[Histórico à prova de adulteração com hash encadeado]]: hash do anterior, selo com etiqueta e cabeça selada.
- [[Auditoria confere os dados derivados]]: comprovante, extrato e colunas de cópia conferidos contra a cadeia.
- [[Regra de concorrência decidida dentro da trava]]: estado lido sob a trava, sequência global e fronteira exata.
- [[Dinheiro em centavos num livro de movimentos]]: fórmula do saldo, entrada ambígua recusada e chave de idempotência.
- [[Sessão entre domínios com JWT no cabeçalho]]: login opcional sem 401, cache pessoal e redirect só interno.
- [[Busca e cache em rota pública]]: filtro em rota nova, `LIKE` escapado e falha fora do cache.
- [[API externa escolhida por versão, licença e chave]]: versão estável, licença do uso real e API sem chave.

## 🎼 Agentes em paralelo
- [[Manual da Orquestra]]: orquestrador, subagentes, fluxo de uma sessão e a estrutura `orquestra/` dos cofres de projeto.
- [[Manual da Orquestra - Núcleo comum]]: fontes, conduta da IA, pedido, entrega, riscos e convenções de todo cofre (prático e estudo).
- [[Manual da Orquestra - Agentes em paralelo]]: G1 a G11, da interface antes do paralelo ao teto de 5 agentes que escrevem.
- [[Manual da Orquestra - Perfil projeto prático]]: P01 a P16 (contrato, fatias, verificação, aceitação) e o lado concreto das regras neutras (worktree, diff, testes).
- [[Manual da Orquestra - Perfil estudo]]: lugar reservado para as regras do futuro agente de estudo.
- [[Padrão de projeto de software]]: S01 a S25 (branches, deploy, código, versões, testes); S04 a S08 só com deploy.
- [[Contrato funcional]]: os 8 blocos em `docs/contrato/` do repositório, para a interface ter regra como o servidor; detalhe em [[Contrato funcional - Os 8 blocos]].
- [[Referência de arquitetura e stack]]: a arquitetura e as tecnologias de partida que o agente propõe ao criar um cofre de software.

## 📚 Conceitos por trás
- [[Conventional Commits]]: a especificação que inspira o meu padrão.
- [[Versionamento semântico]]: o que significa um número como `v1.0.6`.

## 🔗 Conexões
- Mapa: [[Home]]
- Perfil: [[Atenção em túnel]], porque um assunto por vez vale também no código.
