---
aliases: [Requisitos não funcionais, RNF do StoneBid, Non-functional requirements, Qualidades do sistema]
tags: [estudos/programacao]
tipo: referencia
tema: requisitos
status: rascunho
criado: 2026-10-29
origem: Contrato do Projeto Stonebid v0.2 (2026-10-27), seção 6
---
# 📜 Contrato: requisitos não funcionais (RNF)

> [!tldr] Em uma linha
> Como o StoneBid deve ser (no ar, consistente, resiliente, seguro, privado, testável), sempre com um jeito de medir.

É a **vistoria do carro**: não importa só que ele ande, mas que freie, não vaze óleo e passe na inspeção. Seção 6 do [[contrato-do-projeto|contrato]] v0.2, copiada sem reinterpretar.

> [!info] Por que isso importa
> Sommerville divide os requisitos não funcionais em três grupos: de **produto** (desempenho, confiabilidade, segurança, usabilidade), **organizacionais** (processo, entrega, operação) e **externos** (leis, regulamentos). Ele também insiste que sejam escritos de forma **mensurável**, com um número ou um teste, em vez de adjetivos como "rápido" ou "fácil". A coluna "Categoria" abaixo segue essa classificação. Os números marcados como `[PROPOSTO]` são metas minhas, para você aceitar ou ajustar.

| ID | Requisito | Categoria | Como verificar | Origem |
|---|---|---|---|---|
| RNF-01 | A aplicação está no ar em uma URL pública estável (HTTPS) durante a avaliação, e o README informa a URL. | Organizacional | Abrir a URL em janela anônima. | E1/E2 |
| RNF-02 | Um script **reexecutável** cria 1 leiloeiro, 2 licitantes e ao menos 1 lote ao vivo com lances (mais um agendado e um encerrado, para demonstração). As credenciais estão no README. O lote ao vivo DEVE cobrir o período de avaliação (Q-11). | Organizacional | Rodar o script do zero e percorrer o fluxo. | E4 |
| RNF-03 | O README explica passo a passo como configurar o banco e executar o sistema, lista os comportamentos inesperados e as limitações, e resume as decisões principais. | Organizacional | Uma pessoa de fora consegue rodar o projeto só com o README. | E4 |
| RNF-04 | **Consistência financeira:** em qualquer momento o disponível é maior ou igual a zero e o comprometido é igual à soma dos lances em que o usuário lidera. Lances paralelos não quebram isso. | Produto (confiabilidade) | T-02, T-03 | E3 |
| RNF-05 | **Resiliência:** com a API externa fora do ar, vitrine, sala, auditoria e comprovante funcionam normalmente. A busca do painel falha com mensagem clara, dentro de um tempo limite definido e documentado. | Produto (confiabilidade) | T-07 | E3 |
| RNF-06 | **Tempo real:** um lance novo aparece nas outras salas abertas em até 2 segundos, em condições normais. `[PROPOSTO]` | Produto (eficiência) | Duas janelas abertas e um cronômetro. | E2, Prop. |
| RNF-07 | **Segurança básica:** senha com hash adaptativo, validação de toda entrada no servidor, autorização no servidor, segredos fora do repositório e HTTPS. | Produto (segurança) | T-08 e revisão do repositório. | Prop. |
| RNF-08 | **Privacidade:** respostas públicas não contêm dados pessoais (minimização, no espírito da LGPD). | Externo (legislação) | T-09 | E3 |
| RNF-09 | **Manutenibilidade e testabilidade:** as regras RN-02 a RN-12 ficam numa camada de domínio sem dependência de framework nem de banco. | Produto | Os testes de domínio rodam sem subir servidor nem banco. | Prop. |
| RNF-10 | **Usabilidade:** toda ação recusada explica o motivo e o que fazer. O layout é usável em celular e em desktop. `[PROPOSTO]` | Produto | Revisão manual nos dois tamanhos de tela. | E2, Prop. |
| RNF-11 `[OPC-3]` | **Docker Compose:** um comando sobe aplicação, banco e dados de teste. | Organizacional | Rodar o comando em uma máquina limpa. | E5 |
| RNF-12 `[OPC-4]` | **Testes automatizados** cobrindo T-01 a T-11, executáveis com um comando. | Organizacional | Rodar o comando de testes. | E5 |
| RNF-13 `[OPC-5]` | **Tema claro e escuro:** segue a preferência do sistema, permite alternar e lembra a escolha. | Produto | Alternar o tema em todas as telas. | E5 |

> [!warning] v0.3 (M-11)
> O RNF-12 passa a ler: testes de todo requisito implementado, executáveis com um comando (`npm test`) e rodando no CI. Detalhe em [[geral-decisao-2026-10-29-testes-no-escopo]].

> [!tip] Quando abrir esta nota
> Ao preparar o deploy, o seed, o README ou uma revisão de segurança: cada RNF diz como verificar.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** no ar com HTTPS e seed reexecutável cobrindo o período de avaliação (RNF-01, RNF-02).
* **Ponto 2:** consistência financeira e resiliência à API externa são provadas por teste ([[contrato-testes]]).
* **Ponto 3:** os três últimos RNF são os opcionais OPC-3 a OPC-5 (Docker Compose, testes, tema).

### 🔗 Conexões
- Mapa: [[contrato-do-projeto]] · [[moc-orquestra]]
- Relacionadas: [[contrato-testes]], [[contrato-arquitetura]], [[contrato-regras-de-negocio]]
- Próxima: [[contrato-modelo-de-dados]]
