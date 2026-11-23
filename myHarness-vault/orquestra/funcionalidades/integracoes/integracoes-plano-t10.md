---
tipo: plano
funcionalidade: integracoes
status: aprovado
criado: 2026-11-26
---
# 📋 Integrações — plano da T10

## T10: carregando curto contra duplo clique nos cartões
- **Faz:** depois de qualquer clique numa ação do cartão da TEL-02 ("Conectar", "Testar", "Desconectar", "Repetir"), o cartão mostra o estado de carregando e deixa os botões dele inativos por um tempo mínimo curto, mesmo quando o núcleo responde antes. Assim o segundo clique de um duplo clique não cai num botão novo que nasce sob o ponteiro. O tempo mínimo fica numa constante só, com o nome do motivo. A lógica das operações e a guarda do núcleo não mudam.
- **Origem:** opcional B1 do adversarial da tela ([[integracoes-plano-verificacoes-t6-t7#Validação final]]); resposta do humano em 2026-11-26, 18h10: "tratar duplo clique com um delay de loading só para evitar duplos cliques".
- **Toca em:** `src/features/integracoes/` e os testes dela
- **Depende de:** nenhuma
- **Paralelo:** sim (só a tela)
- **Pronto quando:**
  - [x] duplo clique em "Desconectar" (também no canto do botão, como no B1) faz 1 `desconectar` e nenhum `conectar`, nos cartões do GitHub e do Claude CLI
  - [x] duplo clique em "Conectar", "Testar" e "Repetir" faz 1 chamada cada
  - [x] clique único segue igual: a ação começa na hora e o resultado aparece logo depois do tempo mínimo
  - [x] teste vitest do tempo mínimo com relógio falso; `pnpm check:web` passando; `pnpm check:rapido` antes do push
- **Prova:** `pnpm check:web`; Playwright no `dev:simulado` (`?cenario=todas-conectadas`) com duplo clique por `page.mouse` no canto do botão
- **Contrato:** proposta do CMP-11 aprovada pelo humano em 2026-11-27, às 7h30, e aplicada (M-51 em `Anexos/contrato/mudancas.md`).
- **Verificação:** histórico em [[integracoes-plano-verificacoes-t10-t11]].

### 🔗 Conexões
- Plano: [[integracoes-plano]]
- Verificações: [[integracoes-plano-verificacoes-t10-t11]]
- Funcionalidade: [[integracoes-contexto]]
- Projeto: [[geral-contexto]]
