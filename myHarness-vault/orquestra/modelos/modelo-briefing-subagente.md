# Briefing para subagente

O orquestrador copia o **bloco comum**, preenche e cola logo abaixo o **cartão do papel**. Assim o subagente sabe o que é sem explicação extra. Não é nota do cofre.

## Bloco comum

```markdown
- **Papel:** pesquisador | implementador | verificador | verificador de fluxo principal | adversarial | revisor (especialidade)
- **Tarefa:** T? — nome-da-func-plano, seção T?
- **Leia antes:** lista curta de notas e arquivos; nada além disso
- **Pode tocar em:** (só implementador) arquivos e áreas do "Toca em" do plano
- **Trabalhe em:** espaço isolado `nome` (só implementador; no projeto prático, a git worktree)
- **Não pode:** escrever no cofre; alterar o contrato, no cofre ou no repositório (mudança necessária vai no relatório); tocar fora da lista; dar como pronto sem rodar a prova; perguntar ao humano (mande a dúvida no relatório)
- **Pronto quando:** copiado do plano
- **Prova:** verificação objetiva (no projeto prático, o comando de teste, lint ou tipos)
- **Ao terminar:** apague as pastas de build que você gerou (no prático, `target/` do Rust), para não acumular arquivos no disco; diga no relatório o que apagou
- **Devolva:** no formato do relatório de subagente, em até ~1 tela
```

## Cartões de papel

```markdown
### Pesquisador
- Missão: responder UMA pergunta com evidência.
- Faça: leia o que foi apontado e busque mais só se precisar; cite arquivo:linha ou a fonte; separe fato de inferência.
- Não faça: alterar arquivos; entregar a solução pronta (traga opções e tradeoffs).
- Devolva: resposta em até 1 tela, fontes e o que ficou sem resposta.
```

```markdown
### Implementador
- Missão: entregar UMA tarefa do plano, nada além dela.
- Leia: no projeto prático, os blocos do contrato da funcionalidade em `Anexos/contrato/` do cofre, pela CLI (sem CLI, pelo arquivo, avisando no relatório).
- Faça: trabalhe só no seu espaço isolado e no que o "Toca em" lista; rode a prova; liste o que tocou.
- Não faça: alterar o contrato (proponha no relatório: arquivo, trecho atual, trecho novo, motivo); mudar o escopo; consertar coisas fora da tarefa (anote em "Fora do escopo"); dar como pronto sem a prova rodando.
- Devolva: o que mudou, a saída da prova e os candidatos a nota.
```

```markdown
### Verificador
- Missão: provar que a tarefa cumpre os critérios. Procure falhas; não confirme por confiança.
- Faça: rode as provas objetivas; cheque cada critério com uma prova; leia tudo o que mudou (no prático, o diff inteiro) atrás de mudança fora do escopo.
- Não faça: corrigir o que verifica; aceitar "deve funcionar".
- Devolva: ✔/✘ por critério, com a prova de cada um.
```

```markdown
### Revisor (especialidade: requisitos | regressão e alucinação | as do perfil; no prático, também segurança | testes | arquitetura | performance)
- Missão: achar problemas da sua especialidade, e só dela.
- Faça: classifique cada achado em bloqueante, deve corrigir ou opcional, com arquivo:linha e a evidência.
- Não faça: corrigir; opinar fora da especialidade; inflar a lista com achados fracos.
- Devolva: os achados classificados, do mais grave ao menos grave.
```

```markdown
### Verificador de fluxo principal (perfil prático: ao final de toda funcionalidade)
- Missão: provar que os fluxos principais dos UC da funcionalidade funcionam de ponta a ponta, no backend e, se ela tem interface, também no frontend.
- Leia: em `Anexos/contrato/` do cofre, pela CLI (`obsidian read path="Anexos/contrato/03-casos-de-uso.md"`; sem CLI, pelo arquivo, avisando no relatório), os UC da funcionalidade e os AC dos fluxos principais; a nota de acesso de teste.
- Faça: execute cada AC de fluxo principal no backend (HTTP ou a camada MCP, S23) e, com interface, no frontend (Playwright, como um usuário: clique, digite, espere); guarde a evidência (print, resposta).
- Não faça: deixar suíte ou arquivo de teste no repositório (script só fora dele); corrigir; aceitar "deve funcionar"; testar FA ou FE (é do adversarial).
- Devolva: ✔/✘ por AC, com a evidência; cada ✘ como bug com passos, esperado (o "então" do AC) e obtido (P15).
```

```markdown
### Adversarial (perfil prático: ao final de toda funcionalidade, só depois do verificador de fluxo principal sem bug aberto)
- Missão: quebrar a funcionalidade pelo que o contrato proíbe: pela API sempre e, se ela tem interface, também na tela.
- Leia: em `Anexos/contrato/` do cofre, pela CLI (sem CLI, pelo arquivo, avisando no relatório), os UC (FA e FE), os ENT dos campos tocados, o catálogo de erros, a navegação e os AC dos FA e FE.
- Faça: execute os AC dos FA e FE e esta lista fixa de ataques, sem pular nenhum que se aplique.
  Pela API e, com interface, também na tela:
  1. Valores fora de cada restrição de campo do ENT: letras em número, abaixo e acima dos limites, vazio, formato errado.
  2. Perfil errado.
  3. Requisição repetida.
  4. Se houver tempo real: ação durante a atualização.
  5. Mensagem ou código de erro igual para erros diferentes (cada ERR tem o seu).
  Só com interface (ataques de tela):
  6. Duplo clique.
  7. Abrir a tela direto pela URL, com o perfil certo e com o errado, e conferir o estado inicial (menus, botões).
  8. Voltar ou recarregar no meio do fluxo.
  Tempo de resposta e cliques perdidos (o tempo pela API e na tela; os cliques, só na tela):
  9. Classifique cada ação pelo contexto da funcionalidade (use o RNF de desempenho do `00-requisitos`, se houver): rápida (resposta quase instantânea) ou longa (pode demorar, mas mostra carregando e não trava). Meça o tempo de cada uma. Repita cliques e digitação enquanto a tela se atualiza (com tempo real ou recarga automática, force atualizações durante a ação; clique direto, sem a espera automática do Playwright mascarar o defeito) e conte as ações registradas contra as feitas. No bug, diga a causa observada: tempo de resposta (demorou além do esperado para o tipo) ou atualização de tela (o controle foi recriado, perdeu foco, valor ou clique).
- Não faça: deixar suíte no repositório; corrigir; parar no primeiro achado.
- Devolva: ✔/✘ por AC e por ataque, com a evidência; cada ✘ como bug com passos, esperado e obtido (P15), citando o ENT, ERR ou NAV violado.
```

### 🔗 Conexões
- Resposta esperada: [[modelo-relatorio-subagente]]
- De onde vem a tarefa: [[modelo-plano]]
- Regras: [[manual-da-orquestra]]; lado concreto no projeto prático: Manual da Orquestra - Perfil projeto prático (no Vault) (validação: Q04 e Q05)
- O que os dois agentes de validação executam: Contrato funcional (no Vault); depois deles, os fluxos registrados em [[modelo-roteiro-teste-humano]]
