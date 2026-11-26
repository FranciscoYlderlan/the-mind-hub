---
tipo: bug
funcionalidade: integracoes
status: aberto
criado: 2026-11-26
aliases: [Link do device não abre, github.com/login/device não abre, External link does not open in the Tauri window]
---
# 🐞 Link do device flow não abre na janela real

## Contexto
Teste manual do humano em 2026-11-26, 18h32, no app real (`pnpm tauri dev` no Windows), pelos fluxos de [[geral-plano-teste-humano]] (seção integracoes, passo 4, AC-01).

## Sintoma
- Esperado: clicar no link `github.com/login/device` do cartão do GitHub abre a página no navegador do sistema.
- Observado: o clique não abre nada. O resto dos 11 passos funcionou.

## Impacto
O humano precisa digitar o endereço à mão para concluir o "Conectar" do GitHub. Não bloqueia, mas quebra o fluxo principal do AC-01 na janela real.

## Hipóteses
- **A janela do Tauri não abre link externo sozinha** `[a confirmar]`: precisa do plugin `opener` (ou equivalente) e da permissão nas `capabilities`; no navegador (`dev:simulado`), o link abre, por isso os agentes não viram.
- Pode valer para os outros links externos da TEL-02: instalação do Claude CLI (ERR-01) e `obsidian://open` (ERR-03), que já estavam `[a confirmar]` na janela real.

## Linha do tempo técnica
- 2026-11-26 18h32: o humano relatou o sintoma; demais passos ✔.

## Pseudocódigo do problema
`<a href="https://github.com/login/device">` na janela do Tauri → clique → nada.

## Testes feitos
- Verificador e adversariais só no navegador (`dev:simulado`), onde o link abre.

## Evidências encontradas
- Relato do humano.

## Correção aplicada
Nenhuma ainda.

## Solução
`[a preencher]`: tarefa nova na `integracoes`, decidida no chat seguinte.

## Como validar que não voltou
No app real, os três links da TEL-02 (device, instalação do Claude CLI, `obsidian://open`) abrem fora da janela.

## Logs que deveriam existir
Erro de permissão do Tauri no console da janela, se houver.

## O que aprendi
Teste de tela no navegador não prova link externo da janela do Tauri.

### 🔗 Conexões
- Funcionalidade: [[integracoes-contexto]]
- Fluxos: [[geral-plano-teste-humano]]
- Outros bugs: [[bug-conectar-repetido-abre-segundo-fluxo-2026-11-26]]
- Diário: [[diario-2026-11-26-testes-leves-e-prazo]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
