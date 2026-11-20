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
  - [x] trait e tipos de status e erro mapeados ao contrato (UC-01, CMP-03, CMP-11)
  - [x] testes unitários cobrindo os estados
- **Prova:** `cargo fmt --check`, `cargo clippy -D warnings`, `cargo test`
- **Verificação:**
  - Data: 2026-11-19
  - Critérios ✔/✘ com a prova de cada um: ✔ mapeamento a ENT-13 e ERR-01 a ERR-07 (testes `nomes_seguem_ent_13`, `ids_e_codigos_seguem_o_catalogo`, `estado_final_de_cada_erro`); ✔ 13 testes por estado, por `dyn` e genérico; ✔ só `crates/core/`, `Cargo.toml` e `Cargo.lock`; ✔ nenhuma credencial em tipo público (RN-04); ✔ commit `feafd97` na branch `feat/setup-integracao-trait`; `fmt`, `clippy`, `cargo test` e `pnpm check` passando.
  - Devolvido para correção: não

### T2: mascaramento de segredo
- **Faz:** módulo que mascara token e segredo em texto (RN-04, RNF-05) e aplicação dele no texto livre da CLI que a T1 leva ao `Display` e ao `Debug` (`ObsidianFechado.mensagem_da_cli`, `LoginClaudeCliFalhou.motivo`).
- **Toca em:** `crates/core/`
- **Depende de:** T1
- **Paralelo:** não
- **Pronto quando:**
  - [ ] nenhum formato de segredo do contrato sai em texto puro nos testes
- **Prova:** `cargo test`
- **Verificação:**
  - Data: 2026-11-19
  - Critérios ✔/✘ com a prova de cada um: ✘ texto livre (8 de 69 casos adversariais vazam: `Bearer` com valor entre aspas ou após quebra de linha, `token=` e `--token` com quebra de linha, `Bearer:`/`bearer=`, XML e `=>`, token como usuário de URL; prefixo em maiúsculas); ✔ `Segredo` sem valor no `Debug` e no `Display`; ✔ campos da T1 como `TextoMascarado`; ✔ testes dos formatos cobertos; ✔ só `crates/core/`, sem dependência nova, commit `45b204f`. Excesso de máscara em prosa (`token: expirado há pouco tempo`).
  - Devolvido para correção: sim, 2026-11-19, para um implementador novo (vazamentos e excesso de máscara); corrigido em `4be7722`.
  - Segunda volta (2026-11-19): ✘ 73 de 83 casos passam; vazam senha com `&` fora de aspas e token antigo como usuário de URL com senha; excesso de máscara depois de `--token` com espaço e depois do esquema do `Authorization`; `api key` com espaço sem máscara. ✔ `Segredo` e `TextoMascarado`, testes dos vazamentos da primeira volta, escopo e commit.
  - Terceira volta: aval do humano em 2026-11-19, sessão das 17h27, para um implementador novo, só nesses pontos.
  - Terceira volta (2026-11-20, commit `7c6f82e`): ✔ nenhum vazamento em 109 casos; ✔ testes, escopo e commit; ✘ excesso de máscara na mensagem padrão do clap (`--token <TOKEN>` lido como tag XML apaga o resto). Opcional: `Authorization: Digest` mascara `username=` e deixa o hash de `response` à vista.
  - Quarta volta: 2026-11-20, para um implementador novo, só nesses dois pontos.

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
T2 (em andamento) e T3.

## Prioridades
Série T1 → T5; cada tarefa passa por um verificador antes da seguinte. Cada tarefa na sua branch `feat/setup-...`; no fim, juntas na branch de integração `feat/setup-g1-interfaces`, com `pnpm check` local, numa PR única ([[geral-decisao-2026-11-19-branches-e-pr-unica]]).

## Candidatos a registro
- Teste `mensagens_seguem_o_catalogo` não cobre ERR-04 a ERR-06 (observação do verificador da T1).
- `a_partir_do_erro` leva ERR-05 a ERR-07 a desconectado mesmo vindo de sem login ou não instalado; sem efeito na T1, revisar na etapa 3.
- Link de instalação do ERR-01: tela ou núcleo, decidir na etapa 3.
- Ambiente: `cargo clippy --workspace` exige GTK e WebKitGTK (`libwebkit2gtk-4.1-dev`, `libgtk-3-dev`, `libayatana-appindicator3-dev`, `librsvg2-dev`).

### 🔗 Conexões
- Funcionalidade: [[fundacao-contexto]]
- Projeto: [[geral-contexto]]
- Branches: [[geral-decisao-2026-11-19-branches-e-pr-unica]]
- Roteiro: [[geral-plano]]
- Regras: [[manual-da-orquestra]]
