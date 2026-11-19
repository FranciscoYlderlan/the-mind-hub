---
tipo: plano
funcionalidade: fundacao
status: aprovado
criado: 2026-11-19
---
# 📋 Plano — fundação (G1)

> [!warning] Proposta da IA
> Nada aqui é decisão. Decisões ficam nas notas `-decisao-` linkadas abaixo. Ordem e tarefas aprovadas pelo humano em 2026-11-19, sessão das 16h56.

## Objetivo desta rodada
Entregar, em série, as interfaces comuns do G1 da etapa 2 do [[geral-plano]].

## Decisões que este plano respeita
- [[geral-decisao-2026-11-19-stack]]
- [[geral-decisao-2026-11-19-agente-por-claude-p]]
- [[geral-decisao-2026-11-19-entidades-no-sqlite]]
- [[geral-decisao-2026-11-19-gravacao-dupla]]
- [[geral-decisao-2026-11-19-data-e-hora-em-utc]]

(O dial vem do [[geral-contexto]].)

## Tarefas

### T1: trait `Integracao`
- **Faz:** interface comum das integrações (RNF-11): status, conectar e versão, com fake só em teste.
- **Toca em:** `crates/core/`
- **Depende de:** nenhuma
- **Paralelo:** não
- **Pronto quando:**
  - [ ] trait e tipos de status e erro mapeados ao contrato (UC-01, CMP-03, CMP-11)
  - [ ] testes unitários cobrindo os estados
- **Prova:** `cargo fmt --check`, `cargo clippy -D warnings`, `cargo test`
- **Verificação:**
  - Data: 
  - Critérios ✔/✘ com a prova de cada um:
  - Devolvido para correção:

### T2: mascaramento de segredo
- **Faz:** módulo que mascara token e segredo em texto (RN-04, RNF-05).
- **Toca em:** `crates/core/`
- **Depende de:** T1
- **Paralelo:** não
- **Pronto quando:**
  - [ ] nenhum formato de segredo do contrato sai em texto puro nos testes
- **Prova:** `cargo test`
- **Verificação:**
  - Data: 
  - Critérios ✔/✘ com a prova de cada um:
  - Devolvido para correção:

### T3: montagem da chamada ao `claude -p`
- **Faz:** monta os argumentos (modelo, ferramentas, pastas, instruções, saída em fluxo JSON) conforme [[geral-decisao-2026-11-19-agente-por-claude-p]].
- **Toca em:** `crates/core/`
- **Depende de:** T2
- **Paralelo:** não
- **Pronto quando:**
  - [ ] chamada montada é testada contra o `tools/fake-claude`
- **Prova:** `cargo test`
- **Verificação:**
  - Data: 
  - Critérios ✔/✘ com a prova de cada um:
  - Devolvido para correção:

### T4: esquema SQLite das entidades
- **Faz:** migrações das entidades do `02-entidades`, com as trocas M-23 em diante (pontos 4 e 7).
- **Toca em:** `src-tauri/migrations/`, `src-tauri/src/infra/db/`
- **Depende de:** T3 e as trocas do contrato aplicadas
- **Paralelo:** não
- **Pronto quando:**
  - [ ] migração cria todas as entidades com as restrições do contrato
- **Prova:** `cargo test`
- **Verificação:**
  - Data: 
  - Critérios ✔/✘ com a prova de cada um:
  - Devolvido para correção:

### T5: contrato IPC do Tauri
- **Faz:** comandos e eventos entre a tela e o núcleo, com tipos gerados para o TypeScript.
- **Toca em:** `src-tauri/src/commands/`, `src/lib/`
- **Depende de:** T4
- **Paralelo:** não
- **Pronto quando:**
  - [ ] comandos e eventos tipados nos dois lados
- **Prova:** `pnpm check`
- **Verificação:**
  - Data: 
  - Critérios ✔/✘ com a prova de cada um:
  - Devolvido para correção:

## Próxima tarefa e a seguinte
T1 (em andamento) e T2.

## Prioridades
Série T1 → T5; cada tarefa passa por um verificador antes da seguinte. Cada tarefa na sua branch `feat/setup-...`; no fim, juntas na branch de integração `feat/setup-g1-interfaces`, com `pnpm check` local, numa PR única ([[geral-decisao-2026-11-19-branches-e-pr-unica]]).

## Candidatos a registro
- (nenhum)

### 🔗 Conexões
- Funcionalidade: [[fundacao-contexto]]
- Projeto: [[geral-contexto]]
- Branches: [[geral-decisao-2026-11-19-branches-e-pr-unica]]
- Roteiro: [[geral-plano]]
- Regras: [[manual-da-orquestra]]
