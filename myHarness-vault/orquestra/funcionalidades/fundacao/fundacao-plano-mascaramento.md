---
tipo: plano
funcionalidade: fundacao
status: aprovado
criado: 2026-11-23
---
# 📋 Plano — fundação: verificação da T2 (mascaramento)

Histórico da verificação da T2 do [[fundacao-plano]], separado por tamanho.

- **Verificação:**
  - Data: 2026-11-19
  - Critérios ✔/✘ com a prova de cada um: ✘ texto livre (8 de 69 casos adversariais vazam: `Bearer` com valor entre aspas ou após quebra de linha, `token=` e `--token` com quebra de linha, `Bearer:`/`bearer=`, XML e `=>`, token como usuário de URL; prefixo em maiúsculas); ✔ `Segredo` sem valor no `Debug` e no `Display`; ✔ campos da T1 como `TextoMascarado`; ✔ testes dos formatos cobertos; ✔ só `crates/core/`, sem dependência nova, commit `45b204f`. Excesso de máscara em prosa (`token: expirado há pouco tempo`).
  - Devolvido para correção: sim, 2026-11-19, para um implementador novo (vazamentos e excesso de máscara); corrigido em `4be7722`.
  - Segunda volta (2026-11-19): ✘ 73 de 83 casos passam; vazam senha com `&` fora de aspas e token antigo como usuário de URL com senha; excesso de máscara depois de `--token` com espaço e depois do esquema do `Authorization`; `api key` com espaço sem máscara. ✔ `Segredo` e `TextoMascarado`, testes dos vazamentos da primeira volta, escopo e commit.
  - Terceira volta: aval do humano em 2026-11-19, sessão das 17h27, para um implementador novo, só nesses pontos.
  - Terceira volta (2026-11-20, commit `7c6f82e`): ✔ nenhum vazamento em 109 casos; ✔ testes, escopo e commit; ✘ excesso de máscara na mensagem padrão do clap (`--token <TOKEN>` lido como tag XML apaga o resto). Opcional: `Authorization: Digest` mascara `username=` e deixa o hash de `response` à vista.
  - Quarta volta: 2026-11-20, para um implementador novo, só nesses dois pontos.
  - Quarta volta (commit `c0e07eb`): ✔ dica do clap intacta; ✔ `Digest` mascarado até o fim da linha; ✘ regressão: tag XML sem fechamento na mesma linha deixou de mascarar (4 vazamentos que o `7c6f82e` cobria).
  - Quinta volta: interrompida em 2026-11-20 pela troca de abordagem ([[geral-decisao-2026-11-20-mascaramento-sem-adivinhar]]). A T2 é refeita na branch `feat/setup-mascaramento-por-prefixo`, a partir da T1 (`56437a5`); a branch `feat/setup-mascaramento-segredo` fica fora da PR.
  - Refeita (commit `055aa69`, 2026-11-20): ✔ valor guardado, sem heurística, prosa intacta, `Segredo` e `TextoMascarado`, escopo e commit; ✘ segredo guardado dentro de um token deixa o resto do token à vista. Lacuna: token depois de `%20` ou `%3D` não mascarado (fronteira). Opcional: prefixo nu (`ghs_`) mascarado.
  - Devolvido para um implementador novo: trechos unidos numa passada só; prefixo sem exigir fronteira; prefixo só vira token com pelo menos 1 caractere depois.
  - Segunda verificação da refeita (commit `8896227`, 2026-11-20): ✔ nos 6 critérios. 1932 casos de token sem vazamento; segredo guardado dentro, colado ou encavalado sem pedaço à vista; prefixo nu intacto; 35 frases de prosa e erro de CLI iguais; `Segredo` e `TextoMascarado` sem valor; só `crates/core/`; `pnpm check` passando. Efeito aceito: palavra com prefixo no meio é mascarada dali em diante (`desk-ant-abc` → `de••••`).
  - **T2 concluída** na branch `feat/setup-mascaramento-por-prefixo`.

### 🔗 Conexões
- Plano: [[fundacao-plano]]
- Funcionalidade: [[fundacao-contexto]]
- Mascaramento: [[geral-decisao-2026-11-20-mascaramento-sem-adivinhar]]
