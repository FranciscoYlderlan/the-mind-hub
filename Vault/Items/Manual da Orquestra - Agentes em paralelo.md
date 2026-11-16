---
aliases: [Paralelismo da orquestra, Agentes ao mesmo tempo, Parallel agents, Como dividir trabalho entre agentes]
tags: [estudos/programacao, ferramentas/obsidian]
tipo: manual
status: em-uso
criado: 2026-11-16
origem: Regras G1 a G11 do pacote aprovado pelo humano em 2026-11-16 (diario-2026-11-16-regras-para-o-vault, no stonebid-vault)
---
# 🔀 Manual da Orquestra: agentes em paralelo

> [!tldr] Em uma linha
> Como dividir o trabalho entre vários agentes ao mesmo tempo sem colisão: combinar a interface, partir, integrar com aval e verificar o conjunto.

É uma **mudança com vários amigos**: antes de carregar, todo mundo combina onde vai cada caixa; cada um leva o seu cômodo; a escada estreita é um por vez; e no fim alguém confere a casa inteira. Detalhe do princípio 5 do [[Manual da Orquestra]]; as regras de conduta estão em [[Manual da Orquestra - Núcleo comum]].

Vale para cofre de projeto prático e de estudo. Cada regra traz um exemplo "em software" e um "em estudo" quando ajuda.

---

## 🧩 Antes de partir

- **G1 Interface antes do paralelo:** se duas tarefas paralelas dependem uma da outra, uma tarefa anterior define o combinado entre elas; só então as duas partem.
  - Em software: contrato da API, tipos ou esquema do banco antes de frontend e backend.
  - Em estudo: sumário e glossário comuns antes de dois agentes resumirem capítulos que se citam.
- **G2 Partir para paralelizar:** tarefa grande é dividida em partes que não tocam nas mesmas notas ou arquivos.
  - Em software: por módulo ou pasta.
  - Em estudo: por capítulo, tema ou lista de exercícios.
- **G3 Cadeia fica com um agente:** quando cada passo depende do anterior, a cadeia inteira fica com um agente só, em série.
  - Em software: migração → modelo → rota.
  - Em estudo: exercícios em que cada um usa o resultado do anterior.
- **G7 Recurso exclusivo:** o que só aceita um usuário por vez é listado no plano, e só um agente o usa de cada vez.
  - Em software: banco de teste, conta do ambiente de teste, navegador.
  - Em estudo: plataforma de simulado com uma sessão por conta.
- **G11 Teto:** no máximo **5 agentes que escrevem** ao mesmo tempo. Agentes que só leem (pesquisa, verificação) não têm teto.

## ⚙️ Durante

- **G4 Pesquisa adiantada:** enquanto uns constroem, pesquisadores já levantam o que a próxima tarefa vai precisar.
  - Em software: documentação da biblioteca da etapa seguinte.
  - Em estudo: fontes do próximo tema.
- **G9 Registrar e commitar durante:** o orquestrador registra cada relatório assim que chega e commita o cofre a cada registro concluído, sem esperar todos terminarem (N12 e N15 no [[Manual da Orquestra]]).
- **G10 Retomar do histórico:** agente interrompido não recomeça do zero; o próximo retoma do que ficou registrado (relatório, diário, commits).
  - Em software: log da branch e último relatório.
  - Em estudo: notas já escritas e "Onde parei" do diário.

## 🤝 Depois

- **G5 Entrega independente, integração com aval:** cada agente entrega a sua parte sozinho; juntar as partes só com o aval do humano.
  - Em software: o agente termina no push da própria branch; o merge é do humano.
  - Em estudo: cada resumo entra como nota própria; juntar no material final só com aval.
- **G6 Conflito na integração:** o humano decide a ordem; quem ficou para depois ajusta a sua parte sem apagar a do outro.
  - Em software: resolver o conflito mantendo as duas mudanças.
  - Em estudo: nota que repete a outra passa a linkar em vez de apagar.
- **G8 Verificar o conjunto** depois que tudo entrou, não só cada parte.
  - Em software: suíte inteira depois da última integração.
  - Em estudo: revisão do material inteiro (links, contradições entre resumos).

## 🔗 Conexões
- Mapa: [[MOC Programação]]
- Nota-mãe: [[Manual da Orquestra]]
- Relacionadas: [[Manual da Orquestra - Núcleo comum]], [[Atualizar a memória]]

## 🕓 Histórico
- v1 (2026-11-16): criação, com G1 a G11 em forma neutra.
