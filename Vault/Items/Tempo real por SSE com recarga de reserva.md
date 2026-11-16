---
aliases: [Server-Sent Events, SSE com polling, Realtime with fallback, Evento depois do COMMIT]
tags: [estudos/programacao]
tipo: conceito
status: rascunho
criado: 2026-11-16
origem: projeto Stonebid (stonebid-vault, decisões tempo-real-por-sse, concorrencia-do-cloud-run e recarga-de-15s-ate-o-i3; sala-ao-vivo-plano), 2026-10-30
---
# 📡 Tempo real por SSE com recarga de reserva

> [!tldr] Em uma linha
> Quando só o servidor empurra dados, SSE basta; publique o evento depois do COMMIT e mantenha a recarga periódica como reserva.

É o rádio com a TV ligada no mudo: o rádio avisa na hora, e se a estação cair você ainda olha a tela de vez em quando. O cliente manda ações por requisição comum; o servidor só avisa mudanças. SSE (Server-Sent Events) cobre isso, e o `EventSource` reconecta sozinho.

> [!note] A regra e como aplicar
> 1. **Evento só depois do COMMIT:** publicar antes anuncia uma mudança que ainda pode ser desfeita.
> 2. Cada evento leva o objeto inteiro e a hora do servidor, não um "algo mudou".
> 3. **Recarga de reserva:** polling lento (ex.: 15 s) que acelera (ex.: 3 s) enquanto o stream estiver fora.
> 4. Stream público não leva dado pessoal: o `EventSource` não manda cabeçalho de autenticação.
> 5. Barramento em memória exige **uma instância só**; mais instâncias pedem pub/sub (ex.: `LISTEN/NOTIFY`).

> [!warning] Armadilha
> Cada stream aberto ocupa uma vaga de **concorrência** da instância. Com o padrão de 80 conexões no Cloud Run, o 81º visitante fica na fila: suba o limite (ex.: 1000) e o timeout da requisição.

> [!tip] Quando abrir esta nota
> Ao escolher entre WebSocket, SSE e polling para placar, leilão, fila ou painel ao vivo.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** fluxo de mão única pede SSE, não WebSocket.
* **Ponto 2:** evento depois do COMMIT e recarga de reserva: o cliente nunca fica preso num estado falso.
* **Ponto 3:** conexão longa conta como requisição em andamento; confira o limite de concorrência do host.

### 🔗 Conexões
- Mapa: [[MOC Programação]]
- Relacionadas: [[Tarefa agendada idempotente com disparo na leitura]], [[Sessão entre domínios com JWT no cabeçalho]]
- Próxima: [[Regra de concorrência decidida dentro da trava]]
