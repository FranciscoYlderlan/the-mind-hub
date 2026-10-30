---
aliases: [Mock fiel à API, Teste de contrato do mock, Mock API contract check]
tags: [estudos/programacao]
tipo: conceito
status: em-uso
criado: 2026-10-30
origem: bugs do projeto Stonebid, 2026-10-29 e 2026-10-30
---
# 🧪 API simulada conferida contra a API real

> [!tldr] Em uma linha
> Mock que ninguém confere contra os controllers reais prova o mock, não o sistema.

Uma API simulada é como o ensaio com dublê: se o dublê não tem a altura do ator, a cena passa no ensaio e quebra na filmagem. No teste de tela (Playwright), o mock devolvia um campo que a API real não mandava, e o bug só apareceu no ar. Vale para todo projeto com [[Manual da Orquestra|agentes]] escrevendo front e back em paralelo.

> [!note] Como funciona
> 1. Cada rota simulada copia o formato do **presenter** da API real, campo a campo.
> 2. Um teste de contrato (ou o verificador) compara o mock com os controllers sempre que uma rota muda.
> 3. Schema do cliente sem campo opcional à toa: opcional com nome errado passa no `parse` e o dado some calado.
> 4. Erro que não veio da API nunca vai cru (`error.message`) para o usuário: mensagem genérica na tela, detalhe no console.

> [!tip] Quando abrir esta nota
> Ao criar ou mudar uma rota que o front consome, ou quando o teste passa local e a tela falha no ar.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** um presenter por recurso, usado por todas as rotas que devolvem esse recurso.
* **Ponto 2:** o mock segue o presenter; quem confere é outro agente, não quem escreveu.
* **Ponto 3:** erro comum: mock "mais bonito" que a API real esconde o defeito.

### 🔗 Conexões
- Mapa: [[MOC Programação]]
- Relacionadas: [[Manual da Orquestra]], [[Imagem de terceiro com anti-robô passa pelo servidor]]
- Próxima: [[Teste de corrida com janela forçada]]
