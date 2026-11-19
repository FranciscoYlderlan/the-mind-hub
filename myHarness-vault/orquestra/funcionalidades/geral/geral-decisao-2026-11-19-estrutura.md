---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-19
substitui: 
---
# ✅ Estrutura do repositório e da arquitetura

- **Proposta (plano):** [[geral-plano]], seção "Proposta de arquitetura e stack", com detalhe em [[geral-plano-arquitetura-e-stack]] (seções 1 e 2) e [[geral-plano-arquitetura-e-stack-integracoes-e-testes]] (seção 8).
- **Decisão:** a tela React só mostra e pede, e o núcleo Rust decide tudo. O núcleo tem dois pacotes: `crates/core` (regras e casos de uso, sem Tauri) e `src-tauri` (ponte com a tela e integrações), em camadas `domain` → `application` → `infra`, com uma interface (`trait`) por integração. O repositório `my-harness` segue a árvore da seção 8, com `tools/fake-claude/`, `compose.yaml` e `docker/`; o `docs/contrato/` só entra na aceitação final, copiado de `Anexos/contrato/` do cofre. Nomes de arquivo em inglês e kebab-case; em Rust, `snake_case` (exceção da linguagem).
- **Alteração:** nenhuma
- **Motivo:** aval do humano em 2026-11-19.
- **Consequências:** regra nova mora no `core`, nunca na tela. Integração nova não toca em regra nem em tela (RNF-11). Só o núcleo acessa o SQLite.

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[geral-plano-arquitetura-e-stack]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
