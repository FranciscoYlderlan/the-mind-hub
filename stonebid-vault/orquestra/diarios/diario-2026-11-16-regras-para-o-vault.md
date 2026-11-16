---
tipo: diario
status: consolidada
criado: 2026-11-16
---
# 📓 Diário 2026-11-16: regras do Stonebid para o Vault

Pacote aprovado pelo humano (08:58 a 09:26) para escrever no `Vault`. Cada regra entra **no estado geral**, sem nomes do Stonebid; a fonte fica na nota como origem.

## Destino no Vault
- **Núcleo comum** (todo cofre, prático e estudo): Manual da Orquestra neutro.
- **Perfil projeto prático:** nota própria. **Perfil estudo:** só o lugar reservado, vazio, para o futuro agente.
- **Padrão de projeto de software:** nota própria; o bloco "com deploy" (S04–S08) só vale para projeto publicado (projeto local, em WSL ou Docker, não leva).
- **Lições técnicas:** notas de conceito em `Items/`, no MOC Programação.
- Trechos do `Vault` que presumem software (papéis, worktree, "código legado", etapas A2 e A5 de criar cofre, briefing com diff e lint, seção de repositórios do modelo de CLAUDE) vão para o perfil prático; o núcleo fica neutro.

## Núcleo comum
- **N01** Alteração da decisão: reescrito no estado atual; cronologia no diário.
- **N02** Decisão sem código muda na própria nota (+1 linha no diário); já aplicada vira nota nova com `substitui:`.
- **N03** Substituição parcial: nota nova só para o ponto; a antiga segue `aprovada`, linha reescrita + link.
- **N04** Diário com partes: o "Onde parei" vigente só na parte mais recente; o principal aponta para ela.
- **N05** Precedência das fontes (documento externo > contrato > decisões > artefato); conflito: parar e perguntar.
- **N06** Documento-fonte: transcrição fiel com numeração própria, original em `Anexos/`, mapa de cobertura (no estudo: ementa).
- **N07** Conduta da IA: propõe e não decide; ambiguidade = opções + recomendação + pergunta; não inventa números; não finge sucesso; conservador no risco; fatias pequenas.
- **N08** Entrega ao humano: resumo de quem aprende, o que atende, como testar, trade-offs, dúvidas, riscos; proposta técnica em linguagem leiga antes do aval.
- **N09** Modelo de pedido: Contexto, Tarefa, Fora do escopo, Pronto quando, Restrições.
- **N10** Interpretação marcada até confirmar; confirmada vira fato com citação.
- **N11** Fato e autorização do humano citados ao pé da letra, com data e hora.
- **N12** Registrar relatório e decisão aprovada assim que chegam (substitui "registrar no fim" do princípio 8).
- **N13** Verificação dispensada: "não verificado, presumido", com a frase do humano.
- **N14** Passagem de turno também com limite de uso ou crédito perto do fim; adiamento registrado.
- **N15** Commitar o cofre a cada ciclo, para poder desfazer com `git restore`.
- **N16** Plano com "Pontos para o aval" e perguntas abertas com proposta; cada resposta aprovada vira decisão.
- **N17** Critério sem prova: ✘ "sem prova" com motivo, nunca ✔ por dedução.
- **N18** Divergência aceita sem mudar nada: "exceção registrada" com escopo fechado.
- **N19** Riscos com probabilidade, impacto, mitigação, sinal; travou 1 h: escalar.
- **N20** Ordem de corte em degraus definida antes; últimas horas só para revisão.
- **N21** Convenções: DEVE/DEVERIA/PODE, IDs com prefixo, status `[DECIDIDO]`/`[PROPOSTO]`/`[PENDENTE]`.

## Perfil projeto prático
- **P01** Contrato versionado (hub, uma nota por seção vigente, `-mudancas` com M-xx) e mudança de escopo em 5 passos.
- **P02** Cada etapa do roteiro é fatia de ponta a ponta ligada a IDs e vai para o ar.
- **P03** Seção "Desvios" na Verificação: aprovados (com link para a decisão) e "sem aval".
- **P04** Verificação em duas frentes (ambiente real e código), com rodadas nomeadas.
- **P05** Recurso único atende um verificador por vez (coberto também por G7).
- **P06** Achados vão ao humano como opções: corrigir, registrar como limite ou opcional.
- **P07** Aceitação final contra o documento-fonte: verificadores por área + avaliador independente (0 a 10); encerramento registra período no ar e estado final.
- **P08** Manual de bordo do agente e nota de acesso de teste; segredo real nunca no cofre.
- **P09** Mapear o que cada ambiente do agente alcança; insistir em caminho bloqueado é proibido.
- **P10** Briefing do implementador cita as regras de forma do humano (commit).
- **P11** Cada implementador entrega assim que termina; o orquestrador registra enquanto trabalham.
- **P12** Tarefa-interface antes de tarefas paralelas que dependem uma da outra (forma geral em G1).
- **P13** Teste só sai do escopo junto com o requisito que prova.
- **P14** Definição de pronto global.
- **P15** Bug com passos, esperado e obtido; o verificador não corrige.
- **P16** Dados de teste criados em ambiente compartilhado listados na Verificação.

## Padrão de projeto de software
- **S01** ID do requisito na branch, no commit e no PR, mais tabela requisito → teste → etapa → PR.
- **S02** `main` produção, `staging` teste, trabalho em `tipo/ID-descricao`; `staging` → `main` só por fast-forward.
- **S03** Merge na `main` é do humano; o implementador termina no push com CI verde.
- **S04–S08 (só com deploy):** só o CD publica, CI e CD separados; segredos num módulo só e CI sem chave guardada; staging fixo com banco separado; seed reexecutável sem rede externa, no CD, com relógio injetado; publicar a aplicação vazia na etapa 1.
- **S09** Push recusado: `format-patch` e `git am`.
- **S10** Reuso: inventário antes de criar, variar por props ou slot, extrair na 2ª repetição.
- **S11** Gerado ou de biblioteca só pela CLI oficial; nunca editar à mão.
- **S12** Arquivos em inglês e kebab-case; identificadores na convenção da linguagem.
- **S13** Camadas com uma direção de dependência; feature não importa outra.
- **S14** Regra de negócio no domínio; autorização, validação e dinheiro no servidor.
- **S15** Erro com código próprio e `details` acionável; teste pelo código.
- **S16** Versão "citada ou mais recente", sem trava; mesmo runtime em todo ambiente (imagem, CI e CD só se publica); conferir se é rc.
- **S17** Dependência nova pede justificativa; trocar biblioteca de base pede decisão.
- **S18** Limite conhecido e contorno numa seção do README.
- **S19** Comando destrutivo (reset, reescrita de histórico, `--force`) só com confirmação, avisando o que segue detectável.
- **S20** Teste de correção falha sem a correção.
- **S21** Opcional desligado não restringe o caso base; regra arriscada atrás de flag, testada ligada e desligada.
- **S22** Estado inválido provado no CI, nunca como dado de demonstração.
- **S23** Camada MCP para agentes testarem (uma tool por rota, desligada em produção, chave obrigatória).
- **S24** Critério de hospedagem (custo, região, instância mínima, alerta, plano de desligar).
- **S25** Na criação de um cofre de projeto de software, o agente **propõe a arquitetura (frontend e backend) e as tecnologias** a partir de uma referência no `Vault`, extraída das decisões de estrutura, stack, componentes e testes deste projeto, para o humano ajustar em vez de partir do zero; o aval vira as decisões de estrutura e stack do projeto novo (humano, 09:56: "essa arquitetura deve ser proposta e apresentada sempre que for criar um vault do tipo projeto ... e as tecnologias devem ser proposta também para que eu posso propor sugestões de mudança em cima delas e não precisar partir do absoluto 0"). Entra no lote 4.

## Lições técnicas (notas de conceito)
L1 idempotência e servidor que dorme; L2 tempo real (evento após COMMIT, SSE + polling, concorrência); L3 integridade (hash encadeado, selo, auditoria de derivados, coluna derivada na mesma transação); L5 concorrência (estado dentro da trava, sequência global, fronteira exata); L6 dinheiro (fórmula do saldo, centavos, entrada ambígua recusada, chave de idempotência); L7 web (auth opcional sem 401, cache pessoal, JWT no cabeçalho, redirect interno, falha fora do cache, filtro em rota nova, LIKE escapado); L8 dados externos (versão estável, licença, API sem chave). **L4 fica de fora.**

## Commits
- O `Padrão de commit` vale em todo cofre (prático e estudo) e em todo repositório: os dois modelos de CLAUDE (cofre e repositório) levam a seção.
- **Escopo:** sem regra geral; escolhido na criação de cada cofre ou repositório (área, ID do requisito ou outro) e registrado num bloco `<!-- projeto: -->` com a lista fechada de escopos.
- **C2** Cofre: commit a cada registro concluído e na passagem de turno. **C3** Código: um commit por unidade lógica e PR ao fim da tarefa.

## Agentes em paralelo (núcleo, com linha "em software" e "em estudo")
G1 interface antes do paralelo; G2 partir para paralelizar; G3 cadeia fica com um agente; G4 pesquisa adiantada; G5 entrega independente, integração com aval do humano; G6 conflito na integração (humano decide a ordem, quem ficou para depois ajusta sem apagar o outro); G7 recurso exclusivo listado no plano, um agente por vez; G8 verificar o conjunto depois que tudo entrou; G9 registrar e commitar durante; G10 retomar do histórico; **G11 teto: 5 agentes que escrevem ao mesmo tempo**, leitores sem teto.

## Conflitos resolvidos
- K1 a K3: vale o Stonebid (N01, N12, S03/G5). K4: estudo ganha cofre, com plano.
- **K5:** humano, 09:28: não usar regra de projeto em bloco do CLAUDE.md, "justamente pelo crescimento desnecessário do arquivo"; vale o outro padrão do Guia do cofre para IA: regra só do projeto vira nota de decisão em `funcionalidades/geral/`. Humano, 09:30: "no claude.md fará referência ao funcionalidades/geral/ para ser pesquisado via cli do obsidian", para o consumo de tokens não escalar. O CLAUDE.md só aponta para `funcionalidades/geral/` e manda buscar lá pela CLI; o trecho dos blocos no Guia é reescrito. Humano, 09:30, "sim": o bloco `padroes` sai do CLAUDE.md para nota própria lida pelo `cofre.py` (ajuste no script), e o `verificar` ganha teto de palavras no CLAUDE.md (1000 no modelo, 1500 em cada cofre).
- **K6:** `limite-palavras` fixo em 2000 a partir de agora; o `stonebid-vault` fica com o dele (nasceu antes).

## Migração dos blocos do `CLAUDE.md` deste cofre
- 2026-11-16: implementador na worktree `$HOME/wt-migra`, branch `stonebid/migra-blocos` (a partir de `vault/lote-1-claude-enxuto`), levou os blocos `projeto:padronizacao`, `projeto:padroes` e `projeto:repositorios` do `CLAUDE.md` para notas, pela K5. Novas decisões: [[geral-decisao-2026-11-16-grafia-do-nome]], [[geral-decisao-2026-11-16-numeracao-do-enunciado]], [[geral-decisao-2026-11-16-forma-das-notas-de-decisao]], [[geral-decisao-2026-11-16-diario-com-partes]], [[geral-decisao-2026-11-16-limite-de-tamanho]], [[geral-decisao-2026-11-16-repositorios-e-acesso]]. Exceções de nome de arquivo (hooks e gerados) já estavam inteiras em [[geral-decisao-2026-10-28-estrutura-frontend]] e [[geral-decisao-2026-10-28-estrutura-backend]]; modo de implementação já em [[geral-decisao-2026-10-29-modo-de-implementacao]]. O bloco `padroes` foi inteiro para [[padroes]] (`limite-palavras: 2073`), com uma linha `antigo:` nova para o formato antigo. `CLAUDE.md` regenerado pelo `cofre.py sincronizar` do kit do lote 1 (índice, sem blocos): 3318 → 1293 palavras.
- Termos varridos: "projeto:padronizacao", "Regras deste projeto", "Repositórios e acesso", "bloco padroes", "Padronização do CLAUDE", "CLAUDE.md" (em `funcionalidades/` e `referencias/`), "2073", "texto vigente". Tocadas: [[geral-contexto]] (fato do acesso e mapa de decisões), [[moc-orquestra]], [[geral-decisao-2026-10-28-estrutura-frontend]] (linha da exceção de hook), [[passo-a-passo-do-agente]] (diário com partes e `--force`), `CLAUDE.md`, [[padroes]]; kit atualizado pelo `sincronizar` (`cofre.py`, [[manual-do-cerebro]]). Diários, bugs e "O que já foi feito" ficaram como histórico.

> [!tip] Onde parei
> - Seguiu na parte [[diario-2026-11-16-lote-2]], onde está o "Onde parei" vigente.

### 🔗 Conexões
- Diário do dia: [[diario-2026-11-16]]
- Parte seguinte: [[diario-2026-11-16-lote-2]]
- Mapa: [[moc-orquestra]]
- Projeto: [[geral-contexto]]
