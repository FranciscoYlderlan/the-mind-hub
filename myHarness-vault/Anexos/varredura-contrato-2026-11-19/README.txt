Varredura de impacto da regra "contrato em Anexos/contrato/ do cofre do projeto" no Vault — 2026-11-19
Feita por um pesquisador só de leitura, sobre uma cópia do Vault (sem a Obsidian CLI). Nada aplicado no Vault ainda.

A regra (dita pelo humano em 2026-11-19, vale para todo projeto prático):
1. O contrato funcional mora em Anexos/contrato/ do cofre do projeto, em Markdown puro; o cofre.py criar o põe lá e só ali ele é editado.
2. Durante o projeto o repositório não tem docs/contrato/; na etapa final, depois do aceite do humano, o orquestrador copia Anexos/contrato/ para docs/contrato/ num commit só.
3. Só o orquestrador altera o contrato; nenhum subagente o altera, nem no cofre nem na cópia do repositório; subagente propõe a mudança no relatório.
4. Subagentes leem o contrato no cofre pela Obsidian CLI (ou pelo arquivo, avisando).

Arquivos:
- proposta.diff: diff unificado de tudo (notas, modelos, cofre.py e as 2 linhas antigo: do CLAUDE.md). REVISAR ANTES DE APLICAR.
- edicoes.py: 50 trocas nas notas (texto atual exato, único, e texto novo).
- edicoes-cofre-py.py: 8 trocas no Modelos/Orquestra/cofre.py.
- aplicar.py: aplica e para se algum texto não for único.
  Uso, a partir de uma cópia: python3 -I aplicar.py <raiz do Vault> edicoes.py ; e o mesmo com edicoes-cofre-py.py
  Os textos foram tirados do Vault de 2026-11-19 12:45; se o Vault mudou depois, o aplicar.py acusa.

Provas na cópia: verificar Vault 0 ERRO (os mesmos 10 AVISO); as linhas antigo: dão 14 ERRO no Vault de hoje e 0 depois; cofre.py criar prático põe os 11 arquivos em Anexos/contrato/; estudo não cria; sincronizar não sobrescreve o contrato; verificar dá ERRO sem Anexos/contrato/00-requisitos.md e AVISO com orquestra/modelos/contrato/.

Depois de aplicar no Vault:
- myHarness-vault: mover docs/contrato/ do my-harness para Anexos/contrato/ (aprovado pelo humano: "Mover para o cofre"), git rm no repositório, cofre.py sincronizar, apagar orquestra/modelos/contrato/ só com confirmação, reescrever as notas do projeto que citam docs/contrato/ (geral-contexto, geral-plano, geral-plano-arquitetura-e-stack-integracoes-e-testes, geral-decisao-2026-11-19-estrutura, geral-decisao-2026-11-19-subagente-nao-altera-contrato, CLAUDE.md por sincronizar) e o relatorio-contrato-2026-11-19.txt (caminhos).
- O cofre.py novo faz o verificar do myHarness-vault dar ERRO até existir Anexos/contrato/.

Dúvidas do pesquisador para o humano:
1. Escopo de commit da cópia do contrato no repositório na aceitação final (setup ou um RF não servem bem).
2. Na nota "Contrato só do backend deixa a interface sem regra": o repositório fica sem o contrato durante o projeto, mas o S27 deixa citar IDs que existem no contrato do cofre. Está certo?
3. Mudança futura em Modelos/Orquestra/contrato/ não chega aos cofres existentes (o sincronizar não toca o contrato); levar à mão. Confirma?
4. Campo "Aprovação" do mudancas.md: virar wikilink agora que o contrato mora no cofre? (É Markdown puro; ficou texto.)

Observações: o parâmetro pratico de kit() ficou sem uso (limpeza); o verificar não lê Modelos/ nem orquestra/modelos/, então as linhas antigo: não pegam estado velho nos modelos: lá a garantia é a revisão do diff.
