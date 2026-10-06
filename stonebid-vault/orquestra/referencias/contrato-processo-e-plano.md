---
aliases: [Plano de entrega, Linha de corte, Definição de pronto, Checklist de entrega, Incrementos I0 a I5]
tags: [estudos/programacao]
tipo: referencia
tema: gestao
status: rascunho
criado: 2026-10-29
origem: Contrato do Projeto Stonebid v0.2 (2026-10-27), seção 11
---
# 📜 Contrato: processo e plano

> [!tldr] Em uma linha
> Entrega incremental (I0 a I5) até a entrega (2026-10-30 16:00), com o que cortar primeiro se o tempo apertar, a definição de pronto e o checklist final.

É a **receita com a ordem dos passos**: cada etapa já sai pronta para comer, e se faltar tempo você sabe o que pular. Seção 11 do [[contrato-do-projeto|contrato]], no texto vigente (v0.3). O roteiro oficial do cofre continua em [[geral-plano]].

## 11.1 Modelo de processo `[PROPOSTO]`

**Entrega incremental, com práticas leves do desenvolvimento ágil.** Em vez de construir tudo e juntar no fim, cada incremento é uma fatia que funciona de ponta a ponta e já vai para produção.

> [!info] Por que isso importa
> Sommerville apresenta o desenvolvimento incremental como o mais indicado quando os requisitos não são totalmente estáveis e o feedback rápido ajuda. Ele também lista as práticas de programação extrema (XP): pequenas versões, projeto simples, testes dirigindo o desenvolvimento, refatoração e integração contínua. Pressman organiza qualquer processo em cinco atividades: **comunicação, planejamento, modelagem, construção e implantação**. Cada incremento abaixo percorre as cinco, em ponto pequeno. Os dois também defendem planejar sem fingir que o plano é imutável.

## 11.2 Os 7 princípios de Hooker (Pressman) aplicados aqui

| Princípio | No seu projeto |
|---|---|
| A razão de tudo existir | Todo requisito aponta para o enunciado ou para uma decisão sua. |
| KISS (mantenha simples) | Monólito, sem microsserviços e sem recursos fora do escopo. |
| Mantenha a visão | Este contrato é a visão. Mudanças só pelo protocolo da seção 13.4. |
| O que você produz, outros consumirão | README e código claros: o avaliador, a IA e o você do futuro vão ler. |
| Esteja aberto ao futuro | Decisões registradas, tokens de tema desde o I0 e adaptador para a API externa. |
| Planeje para o reuso | O domínio isolado funciona com qualquer tela ou banco. |
| Pense! | Pensar antes de pedir código à IA vale mais do que corrigir depois. |

## 11.3 Plano de entrega

Prazo de 2026-10-29 09:06 até a entrega, em **2026-10-30 16:00**, com trabalho contínuo. O plano com horários **ainda não foi feito**: sai destes incrementos, com a linha de corte (11.4) aplicada, e é o próximo passo do [[geral-plano]]. As últimas horas ficam **só** para revisão e deploy final, sem nada novo.

| Incremento | Entrega (fatia de ponta a ponta) | Requisitos | Pronto quando |
|---|---|---|---|
| I0 | **Esqueleto no ar:** repositório, banco, login com papéis, dados de teste, deploy, Docker Compose, tokens de tema, rotina de testes | RF-01 a RF-03, RNF-01, RNF-02, RNF-11, base de RNF-12 e RNF-13 | Aplicação "vazia" no ar com os 3 usuários de teste |
| I1 | **Carteira e lotes:** depósito, busca na API, criação do lote com cópia do item, vitrine básica | RF-40 a RF-42, RF-20 a RF-22, RF-25, RF-10, RN-13, RN-16 a RN-18 | O leiloeiro cria um lote a partir da API e ele aparece na vitrine. O licitante deposita. |
| I2 | **Lances:** validação, saldo comprometido, mensagens de recusa, registro com hash encadeado | RF-33, RF-70, RN-02 a RN-09, lado de escrita da RN-14 | T-01 a T-03 passando, incluindo concorrência |
| I3 | **Ao vivo e fechamento:** sala em tempo real, anti-sniping, liquidação, comprovante, resultados | RF-30 a RF-32, RF-24, RF-50 a RF-52, RN-10, RN-11 | Um leilão completo, do início ao comprovante |
| I4 | **Auditoria pública** | RF-60, RF-61, RN-14, RN-15 | T-06 detecta os 4 tipos de adulteração |
| I5 | **Opcionais restantes e fechamento:** busca e filtros, cancelamento com estorno, polimento do tema, README e revisão final | RF-11, RF-23, RNF-13, RNF-03 | Checklist final 100% (11.6) |

**Observação do plano:** a escrita do histórico com hash (I2) nasce junto com o primeiro lance. Deixar o hash para depois, sobre dados já gravados, custaria muito mais. I3 e I4 são os incrementos mais carregados e os primeiros a ajustar no plano até a entrega.

## 11.4 Linha de corte `[PROPOSTO]` (Q-12)

Se o tempo apertar, corte nesta ordem (o primeiro da lista sai primeiro):

| Ordem de corte | O que cortar | Por quê |
|---|---|---|
| 1º | Filtros avançados do OPC-1 (manter a busca simples por texto) | É o que menos mexe nas regras de negócio. |
| 2º | Polimento do tema escuro (os tokens de tema ficam) | Os tokens do I0 já deixam 80% pronto. |
| 3º | Cancelamento com estorno (OPC-2) | Depende de regras da carteira, mas pode ficar para o fim. |
| 4º | Docker Compose (OPC-3) | Ajuda o avaliador, mas o README pode cobrir a execução. |
| Nunca por conta própria | Testes (OPC-4) | O teste só sai junto com o requisito que prova: T-01 a T-09 e T-10a ficam sempre; T-10b sai com o OPC-2 e T-11 com a RN-18 ([[geral-decisao-2026-10-29-testes-no-escopo]]). |

## 11.5 Definição de pronto

Um requisito só está pronto quando:

1. O critério de aceite foi verificado.
2. As regras envolvidas têm teste passando (T-xx).
3. A mensagem de erro, se houver, é clara.
4. O README foi atualizado se houve comportamento novo ou inesperado.
5. Está **no ar** (deploy do incremento).
6. A tabela de rastreabilidade foi atualizada.

## 11.6 Checklist de entrega (derivado do enunciado)

- [ ] Deploy no ar, com a URL no README
- [ ] Dois papéis funcionando (leiloeiro e licitante)
- [ ] Vitrine: ao vivo, agendados e encerrados; cancelados ocultos
- [ ] Painel do leiloeiro: buscar itens, criar lote, cancelar lote sem lances, resultados e total recebido
- [ ] Sala ao vivo: lance atual, histórico, posição, contagem regressiva, "você está ganhando" ou "foi superado", sem recarregar
- [ ] Carteira: total, comprometido, disponível e depósito simulado
- [ ] Meus arremates, com comprovante e link de compartilhamento
- [ ] Auditoria pública, sem login, com veredito íntegro ou adulterado
- [ ] Mensagens de feedback para cada lance recusado
- [ ] Regras de lance (RN-02 a RN-05) e saldo comprometido (RN-07 e RN-08)
- [ ] Anti-sniping e liquidação funcionando
- [ ] Histórico à prova de adulteração, com a técnica explicada no README
- [ ] Privacidade: sem dados pessoais na auditoria e no comprovante
- [ ] API externa fora do ar não derruba vitrine, salas, auditoria nem comprovante
- [ ] Dados de teste: 1 leiloeiro, 2 clientes e 1 lote com lances abertos
- [ ] README completo, com configuração, execução e comportamentos inesperados
- [ ] Opcionais: busca e filtro, cancelamento com estorno, Docker Compose, testes e tema escuro

> [!tip] Quando abrir esta nota
> Ao propor as etapas do roteiro em [[geral-plano]] e ao fechar cada incremento (definição de pronto e checklist).

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** seis incrementos (I0 a I5); deploy já no I0, hash junto com o primeiro lance no I2.
* **Ponto 2:** se apertar, corta filtros, depois tema, estorno e Compose; teste só sai junto com o requisito: T-01 a T-09 e T-10a nunca (M-11, [[geral-decisao-2026-10-29-testes-no-escopo]]).
* **Ponto 3:** pronto = critério verificado, teste passando, README atualizado e **no ar**.

### 🔗 Conexões
- Mapa: [[contrato-do-projeto]] · [[moc-orquestra]]
- Relacionadas: [[geral-plano]], [[contrato-riscos]], [[contrato-testes]]
- Próxima: [[contrato-tecnologias]]
