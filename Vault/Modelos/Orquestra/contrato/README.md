# Contrato funcional

Fonte de verdade do que o produto faz, para o frontend e para o backend. O backend implementa daqui as entidades (regra no domínio) e os erros (código próprio); o frontend implementa daqui os componentes, a navegação e a validação de cada campo. Tela nenhuma cria regra.

## Arquivos

| Arquivo | Bloco | IDs |
|---|---|---|
| `00-requisitos.md` | Requisitos do documento-fonte | RF-xx, RNF-xx, RN-xx |
| `01-atores.md` | Atores e perfis | ATR-xx |
| `02-entidades.md` | Modelo de dados e invariantes | ENT-xx |
| `03-casos-de-uso.md` | Casos de uso e fluxos | UC-xx, FA-xx, FE-xx |
| `04-componentes.md` | Componentes lógicos | CMP-xx |
| `05-erros.md` | Catálogo de erros | ERR-xx |
| `06-navegacao.md` | Estados e navegação | NAV-xx |
| `07-rastreabilidade.md` | Mapa de rastreabilidade | (cruza os IDs) |
| `08-criterios-de-aceite.md` | Critérios de aceite | AC-xx |
| `mudancas.md` | Mudanças aprovadas | M-xx |

## Ordem de preenchimento

1. Requisitos (00), atores (01) e entidades (02).
2. Casos de uso, com os três tipos de fluxo: principal, alternativo (FA) e exceção (FE) (03).
3. Erros (05), alimentados pelos fluxos de exceção.
4. Componentes (04).
5. Navegação (06).
6. Rastreabilidade (07) e critérios de aceite (08).
7. Só então as telas.

Cada funcionalidade com interface preenche os blocos dela antes da primeira tela.

## Regra da tela

- Cada tela lista os CMP, UC e NAV que realiza e não cria regra.
- Regra que falta entra primeiro aqui (ver "Como mudar") e só depois na tela.
- Validação de campo vem do ENT: o schema da entidade é a fonte. Mensagem de erro vem do ERR: uma por condição.

## Como mudar

1. Alguém aponta o conflito ou a necessidade.
2. A IA propõe o texto exato e o impacto em requisitos, critérios de aceite e plano.
3. O humano aprova ou recusa.
4. O bloco passa a dizer só o estado novo, e a mudança entra em `mudancas.md` (M-xx).
5. Só então o código muda.

## IDs

- Um ID nunca é reaproveitado. Item removido sai do bloco; o M-xx registra a remoção.
- O código cita um ID só se ele existir aqui.
- Os agentes de verificação executam os AC ao final de cada funcionalidade: os dos fluxos principais primeiro, depois os dos FA e FE.
