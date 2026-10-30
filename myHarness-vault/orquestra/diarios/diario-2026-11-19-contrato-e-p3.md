---
tipo: diario
status: consolidada
criado: 2026-11-19
---
# 📓 Diário 2026-11-19 — contrato e P3 tela

## O que foi feito
- Sessão das 15h35 (chat novo): relatório do pesquisador das trocas do contrato registrado (lido sem a Obsidian CLI, cópias no container) e aplicado pelo orquestrador em `Anexos/contrato/`: 144 trocas em 10 arquivos cobrindo a Lista 1 (33 itens) e o grupo A (dúvidas 1 a 12); novos ERR-45 a ERR-49 e ENT-26 PastaContexto; linhas M-01 a M-14 no `mudancas.md`. Prova: 144/144 trocas, nenhuma citação a S1..S6, S10 e S13 fora do histórico, 365 IDs citados sem órfão. Retoque do orquestrador: D1 reescrita no estado de [[geral-decisao-2026-11-19-entidades-no-sqlite]]. Íntegra, scripts e 11 pontos `[a confirmar]` em `Anexos/trocas-contrato-2026-11-19/`.
- P3 tela rodado pelo humano no Windows: (a) navegador com núcleo simulado **passou** (14 de 14); (b) janela real **passou** (9 de 9) depois que o orquestrador baixou pelo Chrome do humano o `msedgedriver` 157.0.4341.60 e o pôs na pasta; tela em `http://tauri.localhost/` no Windows (registro em [[geral-plano-arquitetura-e-stack-integracoes-e-testes-prototipos]]).

## Decisões tomadas
- (nenhuma nova; aplicado o aval já registrado em [[diario-2026-11-19]])

## Bugs registrados
- (nenhum)

## Candidatos que não viraram nota
- Lição de processo: encadear o commit depois do `verificar` com `| tail` esconde o código de saída; o commit `32c3365` entrou com 1 ERRO (diário acima do limite), corrigido no commit seguinte.

> [!tip] Onde parei
> - **Próximo passo:** etapa 2 do [[geral-plano]], em construção. Contrato já com a Lista 1 e o grupo A aplicados (M-01 a M-14). Falta: (1) P3 tela passou nas duas partes no Windows; o humano responde se o modo `simulado` entra na etapa 2; (2) tarefas-interface (G1) em série: trait `Integracao`, esquema SQLite, contrato IPC, mascaramento de segredo e montagem da chamada ao `claude -p`; o grupo B (dúvidas 13 a 30) espera cada funcionalidade.
> - **Ambiente:** a máquina virtual da nuvem é nova a cada chat: para trabalhar, copiar `Projetos\my-harness` para ela (tar por `device_stage_files`) e devolver por `device_commit_files`; `node_modules/` e `target/` não vão. Pastas a pedir no início: `Projetos\my-harness` e `Projetos\the-mind-hub`, com permissão de apagar (git).
> - **Threads abertas:** 11 dúvidas da especificação levantadas no rascunho do contrato (RF-30 fora de ordem, ligações RF↔RN assimétricas, entidades e campos que faltam, mensagens divergentes, contagem de palavras do RN-26); GitHub ainda inexistente.
> - **Dúvidas para o humano:** as 18 do grupo B do relatório do contrato (não bloqueiam o G1); os 11 pontos `[a confirmar]` de `Anexos/trocas-contrato-2026-11-19/relatorio.txt` (os 5, 6, 7 e 8 tocam o esquema SQLite do G1); modo `simulado` na etapa 2.
> - **Tempo do humano hoje:** até as 18h. Passagem de turno às 15h16 (145 mil tokens) e de novo às 15h33, com 91,5 mil tokens na linha Messages (orçamento: 100 mil); o limite de 5 h do plano já estourou uma vez hoje (reinício às 15h).

### 🔗 Conexões
- Mapa: [[moc-orquestra]]
- Parte anterior do dia: [[diario-2026-11-19]]
- Funcionalidades tocadas: [[geral-contexto]], [[geral-plano-arquitetura-e-stack-integracoes-e-testes-prototipos]]
