---
aliases: [Lista de componentes, Componentes criados, Component registry, Que componentes já existem]
tags: [estudos/programacao]
tipo: referencia
tema: frontend
status: em-uso
criado: 2026-10-28
origem: geral-decisao-2026-10-28-criacao-de-componentes
---
# 📚 Registro de componentes do stonebid-web

> [!tldr] Em uma linha
> A lista resumida de todo componente que já existe no frontend, para consultar antes de criar outro.

Funciona como o **inventário da despensa** antes da feira: olho o que já tem na prateleira antes de comprar de novo. Antes de criar um componente, confiro aqui; o roteiro completo está em [[geral-decisao-2026-10-28-criacao-de-componentes]].

> [!note] Como funciona
> 1. Antes de criar: buscar aqui pelo nome e pelo que o componente faz, e também por algo **parecido** que possa receber a variação por props, `children` ou slot.
> 2. Não achou: checar o shadcn/ui e instalar pela CLI antes de criar do zero.
> 3. Criou ou instalou: o orquestrador acrescenta **uma linha** na tabela da camada certa.

> [!tip] Quando abrir esta nota
> Toda vez que uma tela pedir um botão, tabela, modal ou formulário novo.

## shadcn/ui (`components/ui/`)
| Componente | Comando | Onde é usado |
|---|---|---|
| (nenhum ainda) | | |

## Layout (`components/layout/`)
| Componente | Para quê | Arquivo |
|---|---|---|
| (nenhum ainda) | | |

## Comuns (`components/common/`)
| Componente | Para quê | Arquivo |
|---|---|---|
| (nenhum ainda) | | |

## Por feature (`features/<feature>/components/`)
| Feature | Componente | Para quê |
|---|---|---|
| (nenhum ainda) | | |

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** consultar antes de criar, sempre; reuso vem antes de código novo ([[geral-decisao-2026-10-28-estrutura-frontend]]).
* **Ponto 2:** shadcn/ui primeiro; componente próprio só quando ele não resolve.
* **Ponto 3:** passou de ~350 palavras, dividir por camada em submemórias.

### 🔗 Conexões
- Mapa: [[moc-orquestra]]
- Relacionadas: [[geral-decisao-2026-10-28-criacao-de-componentes]], [[geral-decisao-2026-10-28-stack-frontend]]
- Projeto: [[geral-contexto]]
