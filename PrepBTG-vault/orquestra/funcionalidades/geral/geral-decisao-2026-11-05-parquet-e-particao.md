---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-05
substitui: 
aliases: [Decisão de Parquet e partição, Parquet com DuckDB]
---
# ✅ Treinar Parquet com DuckDB e partição de tabela e de arquivo

- **Proposta (plano):** P2 e P5, propostas pela IA a partir do [[relato-do-colega-do-time]].
- **Decisão:** as tabelas do `mysql-estudos` são exportadas para **Parquet particionado por mês** (`mes=AAAA-MM/`) e consultadas com **DuckDB** (SQL direto no arquivo) e com pandas. Partição de **tabela** no MySQL (por mês) entra como treino de reprocessamento. Viram as questões Q3.10 a Q3.12 de [[questoes-por-cenario]].
- **Alteração:** nenhuma.
- **Motivo:** o colega do time citou Parquet e partição como pontos que contam; Parquet particionado no S3 é o mesmo formato que o cenário 6 (AWS, Athena) usa, o que ajuda na lacuna de nuvem ([[pontos-delicados]]).
- **Consequências:** nova tarefa T0b no [[banco-mocado-plano]]; o `.venv` precisa de `duckdb` e `pyarrow`. No MySQL, a coluna da partição precisa estar em toda chave primária e única.

### 🔗 Conexões
- Funcionalidade: [[banco-mocado-contexto]]
- Plano: [[banco-mocado-plano]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
