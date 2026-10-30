---
aliases: [Proxy de imagem, Imagem barrada pela Cloudflare, Image proxy for bot-protected sites]
tags: [estudos/programacao]
tipo: conceito
status: em-uso
criado: 2026-10-30
origem: bug do projeto Stonebid, 2026-10-29
---
# 🖼️ Imagem de terceiro com anti-robô passa pelo servidor

> [!tldr] Em uma linha
> Se o site de origem desafia o navegador (Cloudflare), a imagem vem por uma rota do meu servidor, com id validado, cache e limite.

É como um prédio com portaria rígida: o morador (servidor) entra direto, o visitante (navegador do usuário) para no interfone. O teste feito pelo servidor passa e engana; o usuário vê a imagem quebrada. Por isso a prova é sempre no navegador real, como diz o [[Manual da Orquestra]].

> [!note] Como funciona
> 1. Rota própria, ex.: `GET /items/images/:id/thumbnail`, que busca a imagem no servidor.
> 2. Valide o id (ex.: só UUID) para não virar SSRF: o cliente nunca manda URL.
> 3. Timeout, corte de tamanho, `Cache-Control` longo e cache em memória.
> 4. Limite de pedidos por IP; atrás de proxy (Cloud Run), confie só na faixa do proxy para ler o IP real.

> [!tip] Quando abrir esta nota
> Imagem externa quebrada só no navegador, ou ao integrar API pública de acervo, loja ou mapa.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** curl no servidor não prova o que o navegador recebe.
* **Ponto 2:** a rota vira alvo público: cache e limite nascem junto.
* **Ponto 3:** `trustProxy` numérico no Fastify 5.12.1+ não teria efeito (CVE-2026-16732) [a confirmar]; use faixa de IP ou função.

### 🔗 Conexões
- Mapa: [[MOC Programação]]
- Relacionadas: [[API simulada conferida contra a API real]]
- Próxima: [[Teste de corrida com janela forçada]]
