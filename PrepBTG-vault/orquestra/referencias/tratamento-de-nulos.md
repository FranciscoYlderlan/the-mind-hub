---
aliases: [Tratamento de nulos, COALESCE, Null handling, Quando o dado não vem]
tags: [estudos/programacao]
tipo: referencia
tema: treino
status: rascunho
criado: 2026-11-05
origem: Dica do colega do time ([[relato-do-colega-do-time]]); regra em [[geral-decisao-2026-11-05-nulos-vao-para-quarentena]]
---
# 🕳️ Tratamento de Nulos (COALESCE e amigos)

> [!tldr] Em uma linha
> COALESCE pega o primeiro valor que existe; em Compliance ele serve para fallback rastreável, nunca para inventar valor ou data de transação.

É como **o contato de emergência da ficha da escola**: se o pai não atende, liga para a mãe, depois para a avó. Mas ninguém inventa um telefone que não está na ficha. Faz parte do cenário 3 em [[questoes-por-cenario]].

---

| Função | SQL (MySQL) | pandas | Uso |
|---|---|---|---|
| Primeiro não nulo | `COALESCE(a, b, c)` | `df['a'].fillna(df['b'])` | Fallback entre fontes |
| Nulo vira valor | `IFNULL(a, 0)` | `fillna(0)` | Só em contagem ou exibição |
| Valor vira nulo | `NULLIF(a, 0)` | `replace(0, np.nan)` | Evitar divisão por zero; "" vira nulo |
| Contar nulos | `SUM(a IS NULL)` | `df.isna().sum()` | Perfil da carga |

> [!example] Fallback rastreável
> ```sql
> SELECT id_origem,
>        COALESCE(data_sistema_a, data_sistema_b) AS data_evento,
>        CASE WHEN data_sistema_a IS NOT NULL THEN 'A'
>             WHEN data_sistema_b IS NOT NULL THEN 'B' END AS fonte_da_data
> FROM stg_transacoes_bruto;   -- linha sem nenhuma data: quarentena
> ```
> A coluna `fonte_da_data` é o que torna o COALESCE auditável.

> [!warning] Armadilha
> `COALESCE(valor, 0)` numa transação esconde um problema: a soma bate errado e ninguém sabe por quê. Valor, data e cliente ausentes vão para a **quarentena com o motivo** ([[roteiros-dos-cenarios-genericos]], cenário 3). `AVG` e `COUNT(coluna)` já ignoram nulos: preencher com 0 **muda** a média.

> [!tip] Quando abrir esta nota
> Na limpeza do cenário 3 e sempre que a head perguntar "e quando o dado não vem?".

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** `COALESCE` = primeiro valor que existe; `NULLIF` = transformar valor em nulo; `IFNULL` = atalho de dois argumentos.
* **Ponto 2:** Fallback só com a origem registrada ao lado.
* **Ponto 3:** Dado crítico ausente não se preenche: vai para quarentena.

### 🔗 Conexões
- Mapa: [[moc-orquestra]]
- Decisão: [[geral-decisao-2026-11-05-nulos-vao-para-quarentena]]
- Relacionadas: [[roteiros-dos-cenarios-genericos]], [[estatistica-basica-e-eda]], [[relato-do-colega-do-time]]
