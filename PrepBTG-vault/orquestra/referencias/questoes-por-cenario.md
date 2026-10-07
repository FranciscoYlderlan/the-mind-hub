---
aliases: [Questões do banco mocado, Exercícios por cenário, Lista de questões do treino, Case study questions]
tags: [carreira/entrevistas, estudos/programacao]
tipo: referencia
tema: treino
status: rascunho
criado: 2026-11-05
origem: Criadas pelo Claude a partir dos [[cenarios-de-pratica]] e do banco simulado `mysql-estudos` (2026-11-05)
---
# 🧩 Questões por Cenário (banco mocado)

> [!tldr] Em uma linha
> As perguntas concretas que preciso resolver em cada um dos 6 cenários, já apontando para as tabelas do banco simulado.

Os [[cenarios-de-pratica]] são o **título da prova**; esta nota é a **folha de questões**. Cada cenário abre com o enunciado como a head falaria, e depois vêm as questões em ordem. Elas não trazem resposta: o gabarito dos dados fica no banco `gabarito`, e a resposta oral se monta no treino ([[instrucoes-do-coach-de-entrevista]]).

> [!warning] Não é o teste real
> Questões criadas pelo Claude. Os dados são 100% simulados.

> [!note] Legenda
> **SQL** = consulta pura · **PY** = Python/pandas · **ORAL** = só raciocínio, sem código.
> Tabelas do banco `compliance`: `clientes`, `socios_pj`, `contas`, `transacoes`, `paises_risco`, `regras_monitoramento`, `alertas`, `lista_restritiva`, `stg_transacoes_bruto`.

---

## 1. Faturamento incompatível de PJ (e outros sinais de PLD)

> *"Recebemos a informação de que empresas recém-abertas estão sendo usadas para movimentar dinheiro de terceiros. Como você encontraria e priorizaria esses clientes?"*

- **Q1.1 (SQL)** Para cada PJ, compare os créditos de cada mês com o faturamento mensal declarado. Quantas passam de 3x? E de 10x?
- **Q1.2 (SQL + PY)** Para as PJs encontradas, junte sinais extras: idade da empresa, risco KYC atual, número de contrapartes por mês e concentração das saídas. Monte um score simples e justifique os pesos.
- **Q1.3 (SQL)** Olhe os sócios dessas PJs em `socios_pj`. Algum sócio aparece em mais de uma? O perfil dele combina com isso?
- **Q1.4 (SQL + ORAL)** Existe PJ com volume muito alto que **não** é suspeita? Por que a sua regra não deveria pegá-la?
- **Q1.5 (SQL ou PY)** Em PF, encontre fracionamento: 3 ou mais depósitos em espécie entre R$ 8 mil e R$ 10 mil numa janela de 7 dias.
- **Q1.6 (PY)** Encontre contas de passagem: muitos remetentes entrando e 90% ou mais saindo em até 48h.
- **Q1.7 (SQL)** Liste as remessas para países de `paises_risco`: quem, quanto, quando e para onde.
- **Q1.8 (SQL)** Qualidade do KYC: clientes de risco ALTO com revisão há mais de 24 meses, e PF sem renda cadastrada.
- **Q1.9 (ORAL)** Que informação você pediria ao cliente e a outras áreas antes de concluir? Em que ponto o caso vira comunicação ao COAF?

## 2. Alertas demais, pouco valor

> *"O time fecha quase todo alerta como falso positivo e a fila só cresce. O que você faria?"*

- **Q2.1 (SQL)** Volume de alertas por regra e por mês. Taxa de falso positivo e taxa de comunicação ao COAF por regra.
- **Q2.2 (SQL + PY)** Tempo de encerramento (média, mediana e p90) por analista e por regra. Quantos passam de 30 dias? [a confirmar: SLA real da área]
- **Q2.3 (SQL)** Qualidade do encerramento: alertas fechados sem justificativa. Algum analista tem padrão fora da curva?
- **Q2.4 (SQL)** Backlog de hoje: quantos ABERTO e EM_ANALISE, idade em dias e score.
- **Q2.5 (PY)** O `score_risco` separa bem verdadeiros de falsos positivos? Compare as distribuições por desfecho.
- **Q2.6 (SQL)** Cobertura: dos casos que você achou no cenário 1, quais nunca geraram alerta? O que isso diz sobre as regras?
- **Q2.7 (ORAL + PY)** Proposta: quais regras recalibrar ou desligar, quanto o volume cai e como provar, com teste retroativo, que nenhum caso real se perde.
- **Q2.8 (ORAL)** Quais 3 a 5 métricas você colocaria no painel da área, e para quem?

## 3. Pipeline confiável (dados atrasados, duplicados e em formatos diferentes)

> *"As transações chegam de três sistemas, com atraso, repetidas e cada uma num formato. As regras rodam em cima disso. Como você garante que o dado é confiável?"*

- **Q3.1 (SQL)** Perfil da `stg_transacoes_bruto`: linhas por sistema, nulos e exemplos de cada formato.
- **Q3.2 (PY)** Converta `data_evento_texto` para data e hora, tratando cada formato e o fuso.
- **Q3.3 (PY)** Converta `valor_texto` para decimal: vírgula, "R$" e valores em centavos.
- **Q3.4 (PY)** Padronize conta, tipo e direção para os mesmos domínios da tabela `transacoes`.
- **Q3.5 (SQL ou PY)** Duplicados: qual é a chave? Quando o reenvio muda o valor, qual versão vale e por quê?
- **Q3.6 (PY)** Atraso: distribuição de `recebido_em` menos a data do evento. Que janela de reprocessamento você adotaria, e o que acontece com uma regra que roda em D+1?
- **Q3.7 (SQL)** Reconcilie a staging limpa com `transacoes`: contagem, soma e divergências.
- **Q3.8 (SQL + PY)** Grave uma tabela limpa e uma de quarentena. Que checagens rodam a cada carga? Como a carga continua segura se rodar duas vezes?
- **Q3.9 (ORAL)** Como você monitora o pipeline: volume, atraso, mudança de formato, linhagem do dado?

## 4. Assistente de GenAI com RAG para Compliance

> *"Queremos um assistente que responda dúvidas dos analistas sobre as regras e os procedimentos. Como você desenharia?"*

- **Q4.1 (ORAL)** Que fontes alimentam o assistente (políticas, `regras_monitoramento`, procedimentos)? O que **não** pode entrar, como dados de cliente?
- **Q4.2 (ORAL)** Desenhe o fluxo: ingestão, divisão dos documentos, busca, geração da resposta e citação da fonte.
- **Q4.3 (ORAL)** Governança: quem acessa o quê, registro das perguntas, dados pessoais, alucinação e revisão humana.
- **Q4.4 (ORAL)** Como medir se ele responde bem: conjunto de perguntas com resposta conhecida, taxa de citação correta, recusa quando não sabe.
- **Q4.5 (SQL + ORAL)** Olhe as justificativas em `alertas`. Se o assistente aprendesse com elas, o que daria errado? (liga com a Q2.3)

## 5. Screening de nomes contra listas restritivas e PEP

> *"Precisamos checar clientes e contrapartes contra listas de sanções e PEP. Como você faz isso sem afogar o time em homônimos?"*

- **Q5.1 (PY)** Normalize nomes: acentos, caixa, pontuação e ordem das palavras.
- **Q5.2 (PY)** Compare dois métodos de similaridade (texto inteiro e por palavras). Escolha um limiar olhando falsos positivos e falsos negativos.
- **Q5.3 (SQL + PY)** Use documento e data de nascimento para classificar cada achado em confirmado, provável ou descartado, com justificativa.
- **Q5.4 (PY)** Faça o screening também das contrapartes em `transacoes` e dos sócios em `socios_pj`.
- **Q5.5 (SQL)** Cruze a fonte PEP com a coluna `clientes.pep`. Há cadastro desatualizado? O que muda no risco?
- **Q5.6 (ORAL)** Explicabilidade: que evidência fica guardada por match para o auditor? Como refazer o screening quando a lista muda (`data_inclusao`)?
- **Q5.7 (ORAL)** Aqui são 520 clientes contra 65 nomes. E com 5 milhões de clientes e 1 milhão de nomes?

## 6. Arquitetura na AWS para processar transações e entregar alertas

> *"Como ficaria isso tudo na nuvem, da transação chegando até o alerta na tela do analista?"*

- **Q6.1 (ORAL)** Mapeie as camadas usando o banco como exemplo: bruto (`stg_`), limpo (a tabela da Q3.8) e pronto para regras e alertas.
- **Q6.2 (ORAL)** Que regras precisam rodar quase em tempo real e quais podem rodar em lote? Use R01 a R08 como exemplo.
- **Q6.3 (ORAL)** Como o alerta chega ao analista e como fica a trilha de auditoria do que ele decidiu?
- **Q6.4 (ORAL)** Segurança: criptografia, acesso mínimo, separação de ambientes e dados sensíveis.
- **Q6.5 (ORAL)** Custo, observabilidade e o que acontece quando uma parte cai.
- **Q6.6 (ORAL)** Como falar com honestidade da minha lacuna em AWS ([[pontos-delicados]]).

---

> [!info] Fechamento de cada cenário
> Resposta nos 5 blocos de [[cenarios-de-pratica]] e a versão de cerca de 90 segundos em voz alta.

> [!tip] Quando abrir esta nota
> No começo de cada sessão de treino, para escolher a próxima questão do [[banco-mocado-plano]].

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** 6 cenários, 44 questões; 1, 2, 3 e 5 usam dados, 4 e 6 são quase só raciocínio.
* **Ponto 2:** O cenário 3 gera a tabela limpa que o 6 usa; o 1 gera os casos que o 2 usa para medir cobertura.
* **Ponto 3:** Gabarito só depois de tentar: `SELECT * FROM gabarito.casos_plantados`.

### 🔗 Conexões
- Mapa: [[moc-orquestra]]
- Relacionadas: [[cenarios-de-pratica]], [[banco-mocado-contexto]], [[instrucoes-do-coach-de-entrevista]], [[pontos-delicados]]
- Próxima: [[banco-mocado-plano]]
