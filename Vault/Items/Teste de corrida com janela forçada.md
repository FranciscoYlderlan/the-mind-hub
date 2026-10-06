---
aliases: [Provar trava de concorrência, Race condition test, Teste de pedidos simultâneos]
tags: [estudos/programacao]
tipo: conceito
status: em-uso
criado: 2026-10-30
origem: regra RN-19 do projeto Stonebid, 2026-10-30
---
# 🏁 Teste de corrida com janela forçada

> [!tldr] Em uma linha
> Disparar pedidos simultâneos pelo HTTP pode passar sem a trava; a prova é forçar a janela no repositório e ver o teste falhar sem ela.

Dois carros só batem no cruzamento se chegarem no mesmo instante; testar "mandando vários carros" depende da sorte do semáforo. O jeito certo é segurar o primeiro carro no meio do cruzamento e soltar o segundo. Vale para todo código com trava, inclusive o que [[Manual da Orquestra|subagentes]] entregam.

> [!note] Como funciona
> 1. No teste do repositório, injete uma pausa entre o "ler" e o "gravar" (a janela da corrida).
> 2. Rode dois pedidos dentro da janela e espere só um sucesso.
> 3. Desligue a trava (ex.: `pg_advisory_xact_lock`) e confirme que o teste **falha**. Se não falha, ele não prova nada.

> [!tip] Quando abrir esta nota
> Ao escrever regra do tipo "um só por vez": obra única por lote, saldo, estoque, lance.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** teste de corrida que passa com e sem a trava é teste falso.
* **Ponto 2:** índice único não serve quando o estado é calculado pelo relógio; aí entra trava por chave.
* **Ponto 3:** worktrees em paralelo dividem a porta do Playwright (`reuseExistingServer`): use uma porta por worktree, senão o teste roda o código da outra.

### 🔗 Conexões
- Mapa: [[MOC Programação]]
- Relacionadas: [[API simulada conferida contra a API real]], [[Imagem de terceiro com anti-robô passa pelo servidor]]
