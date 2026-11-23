---
tipo: plano
funcionalidade: integracoes
status: aprovado
criado: 2026-11-27
---
# 📋 Integrações — plano da T11

## T11: links externos da TEL-02 abrem fora da janela do Tauri
- **Faz:** na janela do Tauri, os três links externos da TEL-02 abrem pelo opener do sistema: device do GitHub (AC-01), instalação do Claude CLI (ERR-01, AC-03) e `obsidian://open` (ERR-03). No navegador (`dev:simulado`), os links seguem abrindo como hoje. A permissão nas `capabilities` cobre só esses destinos.
- **Origem:** teste manual do humano em 2026-11-26, 18h32 ([[bug-link-do-device-nao-abre-na-janela-real-2026-11-26]]); aval do humano em 2026-11-27, às 7h30.
- **Toca em:** `src/features/integracoes/` e os testes dela, um utilitário de link externo em `src/lib/`, `src-tauri/` (plugin e `capabilities`), `package.json` e `pnpm-lock.yaml`
- **Depende de:** nenhuma
- **Paralelo:** sim (com a T10; os dois tocam em `src/features/integracoes/`, então a segunda PR pode precisar de rebase)
- **Branch:** `fix/integracoes-links-externos`
- **Pronto quando:**
  - [ ] na janela do Tauri, os três links chamam o opener do sistema; no navegador seguem iguais
  - [ ] a permissão nas `capabilities` é a mínima
  - [ ] teste vitest prova que cada link chama a função de abrir com a URL certa; `pnpm check:web` passando
  - [ ] `pnpm check:rapido` antes do push e `pnpm check` completo uma vez
- **Prova:** `pnpm check:web`, `pnpm check:rapido` e `pnpm check`; Playwright rápido no `dev:simulado`. A prova na janela real é o teste manual do humano.
- **Verificação:** histórico em [[integracoes-plano-verificacoes-t10-t11]].

### 🔗 Conexões
- Plano: [[integracoes-plano]]
- Bug: [[bug-link-do-device-nao-abre-na-janela-real-2026-11-26]]
- Verificações: [[integracoes-plano-verificacoes-t10-t11]]
- Funcionalidade: [[integracoes-contexto]]
- Projeto: [[geral-contexto]]
