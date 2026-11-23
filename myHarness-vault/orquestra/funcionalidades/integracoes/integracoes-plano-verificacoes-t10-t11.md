---
tipo: plano
funcionalidade: integracoes
status: aprovado
criado: 2026-11-27
---
# 📋 Integrações — verificações da T10 e da T11

## T10
- 2026-11-26 18h25 (implementador da T10, `fix/integracoes-duplo-clique`, cerca de 15 min): `e278aa3` (carregando mínimo de 500 ms, o tempo padrão de duplo clique do Windows, em `provedor-de-integracoes.tsx`; botões e linha da conta ficam no lugar, inativos, em `cartao-integracao.tsx`) e `ee18b05` (2 testes com relógio falso; 3 testes ajustados), com push e hook ativo. `pnpm check:web` com 67 testes; `check:rapido` de 45 s a 102 s; Playwright 9/9 no duplo clique (Desconectar, Conectar, Testar e Repetir fazem 1 chamada cada); com o código da `main`, o B1 volta. Proposta de contrato: CMP-11, estado "carregando", com os botões no lugar, inativos, por pelo menos 500 ms. Falta o verificador e a decisão sobre a proposta.
- 2026-11-27 07h45 (verificador leve da T10, cerca de 12 min, sem compilar Rust): ✔ nos 4 critérios. Playwright no `dev:simulado` com duplo clique por `page.mouse` a 5 px do canto: "Desconectar" faz 1 `desconectar` e 0 `conectar` no GitHub e no Claude CLI; "Conectar", "Testar" e "Repetir" fazem 1 chamada cada; clique único chama o núcleo na hora e mostra o resultado em cerca de 515 ms, sem o botão se mexer. `pnpm check:web` com 67 testes; os 2 testes novos falham com o provedor da `main`. Constante única, diff só em 3 arquivos de `src/features/integracoes/`, bate com o M-51. Sem bloqueante e sem "deve corrigir". Opcionais: os 500 ms valem também na checagem automática ao abrir a TEL-02; a linha da conta fica visível no carregando; botão inativo do shadcn deixa o clique passar ao `div` de baixo; `asyncUtilTimeout: 3000` vale no arquivo de teste inteiro. **T10 concluída**, PR #19.

## T11
- Em andamento.

### 🔗 Conexões
- Parte anterior: [[integracoes-plano-verificacoes-t6-t7]]
- Tarefas: [[integracoes-plano-t10]], [[integracoes-plano-t11]]
- Plano: [[integracoes-plano]]
- Funcionalidade: [[integracoes-contexto]]
- Projeto: [[geral-contexto]]
