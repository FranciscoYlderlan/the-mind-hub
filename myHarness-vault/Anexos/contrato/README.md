# Contrato funcional

Fonte de verdade do que o produto faz, para o frontend e para o backend. O backend implementa daqui as entidades (regra no domínio) e os erros (código próprio); o frontend implementa daqui os componentes, a navegação e a validação de cada campo. Tela nenhuma cria regra.

- **Produto:** MyHarness (Harness), aplicação desktop Tauri + Rust + React que governa agentes do Claude CLI, usa o cofre Obsidian só como memória e deixa o humano como validador final.
- **Documento-fonte:** "Harness — especificação funcional", 18 de nov. de 2026 (D5 e D6 de 2026-11-19).
- **Estado:** rascunho de 2026-11-19, ainda sem aval do humano. Pontos sem fonte estão marcados `[a confirmar]`.
- **Backend e frontend:** "servidor" e "API" nestes blocos são o núcleo Rust (Tauri) e a camada de comandos dele; o frontend é a interface React, no mesmo repositório [a confirmar].

## Arquivos

| Arquivo | Bloco | IDs |
|---|---|---|
| `00-requisitos.md` | Requisitos do documento-fonte, decisões D1 a D6 e suposições S1 a S15 | RF-01 a RF-34, RNF-01 a RNF-14, RN-01 a RN-30 |
| `01-atores.md` | Atores e perfis | ATR-01 a ATR-09 |
| `02-entidades.md` | Modelo de dados e invariantes | ENT-01 a ENT-25 |
| `03-casos-de-uso.md` | Casos de uso e fluxos | UC-01 a UC-14, FA-xx, FE-xx |
| `04-componentes.md` | Telas previstas e componentes lógicos | TEL-01 a TEL-06, CMP-01 a CMP-17 |
| `05-erros.md` | Catálogo de erros | ERR-01 a ERR-44 |
| `06-navegacao.md` | Estados e navegação | NAV-01 a NAV-23 |
| `07-rastreabilidade.md` | Mapa de rastreabilidade | (cruza os IDs) |
| `08-criterios-de-aceite.md` | Critérios de aceite | AC-01 a AC-143 |
| `mudancas.md` | Mudanças aprovadas | M-xx |

## Ordem de preenchimento

1. Requisitos (00), atores (01) e entidades (02).
2. Casos de uso, com os três tipos de fluxo: principal, alternativo (FA) e exceção (FE) (03).
3. Erros (05), alimentados pelos fluxos de exceção.
4. Componentes (04), só com interface.
5. Navegação (06), só com interface.
6. Rastreabilidade (07) e critérios de aceite (08).
7. Só então o código (e as telas, se houver).

Toda funcionalidade preenche os blocos dela antes do código: ENT, UC com FA e FE, ERR e AC. Com interface, também CMP, NAV e a coluna Tela da rastreabilidade, antes da primeira tela.

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
- Os agentes de verificação executam os AC ao final de cada funcionalidade, pela API e, com interface, na tela: os dos fluxos principais primeiro, depois os dos FA e FE.
- FA e FE têm numeração local a cada UC (cite como "UC-03 FE-01").
