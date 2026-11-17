---
aliases: [Esquema do banco, Mapa das tabelas, Database schema, Como a IA lê o banco]
tags: [estudos/programacao]
tipo: referencia
tema: treino
status: em-uso
criado: 2026-11-06
origem: Levantado pelo Claude em 2026-11-06 a partir da cópia (mysqldump) do banco `compliance` do humano
---
# 🗺️ Esquema do Banco Compliance

> [!tldr] Em uma linha
> As tabelas, colunas e ligações do banco `compliance` do `mysql-estudos`, e como a IA lê o banco quando não alcança o WSL.

O banco é como **um prédio com elevador só até o andar da conta**: para chegar da transação ao cliente, sempre se passa pela conta. Quem pula esse andar soma errado.

---

## Ligações
```
clientes (520) ──< contas (681) ──< transacoes (66.871)
   ├──< alertas (1.936) ──> regras_monitoramento (8)
   └──< socios_pj (230)   (cliente_pj_id e cliente_pf_id apontam para clientes)
lista_restritiva (65) · paises_risco (8) · stg_transacoes_bruto (2.719, tudo em texto)
gabarito.casos_plantados (62)
```

## Colunas principais
| Tabela | Colunas |
|---|---|
| `clientes` | `cliente_id`, `tipo_pessoa` (PF/PJ), `nome`, `documento`, `renda_mensal`, `faturamento_anual`, `patrimonio_declarado`, `segmento`, `risco_kyc` (BAIXO/MEDIO/ALTO), `pep`, `data_cadastro`, `data_ultima_revisao_kyc`, `status` |
| `contas` | `conta_id`, `cliente_id`, `tipo_conta`, `data_abertura`, `status` |
| `transacoes` | `transacao_id`, `conta_id`, `data_hora` (com hora), `tipo` (PIX, TED, BOLETO, DEPOSITO_ESPECIE…), `direcao` (C/D), `valor`, `contraparte_nome`, `contraparte_documento`, `pais_contraparte`, `canal` |
| `alertas` | `alerta_id`, `cliente_id`, `regra_codigo`, `data_geracao`, `score_risco`, `valor_envolvido`, `status`, `desfecho` (FALSO_POSITIVO/MONITORAR/COMUNICADO_COAF), `analista`, `data_encerramento`, `justificativa` |
| `regras_monitoramento` | `regra_codigo`, `nome`, `descricao`, `parametros`, `ativa` |
| `socios_pj` | `cliente_pj_id`, `nome_socio`, `documento_socio`, `participacao_pct`, `cliente_pf_id` |
| `lista_restritiva` | `fonte` (ONU_CSNU, OFAC_SDN, UE, LISTA_INTERNA, PEP_CGU), `nome`, `aliases`, `documento`, `data_nascimento`, `pais` |
| `stg_transacoes_bruto` | `sistema_origem`, `id_evento_origem`, `conta_texto`, `data_evento_texto`, `valor_texto`, `tipo_texto`, `direcao_texto`, `contraparte_texto`, `recebido_em` |

> [!warning] Três armadilhas
> - `transacoes` **não tem** `cliente_id`: o caminho é `transacoes → contas → clientes`.
> - 161 clientes têm mais de uma conta: a granularidade da soma precisa ser o cliente, não a conta.
> - Período de 2025-11-01 a 2026-10-31; `data_hora` tem hora, então filtre com `>= '2026-01-01' AND < '2027-01-01'`.

## Como a IA lê o banco
A sessão na nuvem **não alcança** o WSL (nem `localhost:3306`, nem o IP 172.25.227.200). O caminho é uma cópia:
1. No WSL, o humano exporta: `sudo docker exec mysql-compliance sh -c 'mysqldump -uroot -p"$MYSQL_ROOT_PASSWORD" --databases compliance gabarito' > /mnt/c/Users/Ylderlan/Documents/Projetos/mysql-estudos-dump/compliance.sql`
2. A IA pede acesso à pasta `C:\Users\Ylderlan\Documents\Projetos\mysql-estudos-dump`, traz o arquivo para a nuvem e carrega num MariaDB 10.11, trocando a collation `utf8mb4_0900_ai_ci` por `utf8mb4_unicode_ci` (o MariaDB não conhece a do MySQL 8).
3. Com isso a IA roda as consultas do humano e confere a correção. A cópia morre com a sessão: em chat novo, refazer o passo 2.

## Conectar pelo DBeaver
Erro "Public Key Retrieval is not allowed": em **Edit Connection → Driver properties**, `allowPublicKeyRetrieval = true` e `useSSL = false`. Host `localhost` (ou 172.25.227.200), porta 3306, banco `compliance`. Senha: `sudo docker exec mysql-compliance printenv MYSQL_ROOT_PASSWORD`.

> [!tip] Quando abrir esta nota
> Depois da checagem do M0 de [[trilha-sql-didatica]] (antes disso, o mapa é meu), antes de cada drill de [[questoes-sql-de-prova]] e no começo das sessões com banco.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** Transação chega ao cliente pela conta.
* **Ponto 2:** Diga a granularidade antes de somar: cliente com várias contas infla ou quebra o resultado.
* **Ponto 3:** A IA confere o SQL numa cópia do banco, não no banco do WSL.

### 🔗 Conexões
- Mapa: [[moc-orquestra]]
- Relacionadas: [[banco-mocado-contexto]], [[questoes-sql-de-prova]], [[questoes-por-cenario]], [[sql-window-functions-mysql]]
- Próxima: [[questoes-sql-de-prova]]
