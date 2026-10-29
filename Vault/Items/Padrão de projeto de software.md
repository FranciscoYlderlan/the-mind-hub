---
aliases: [Padrão de software, Regras de projeto de software, Software project standard, Como conduzo um projeto com código]
tags: [estudos/programacao]
tipo: manual
status: em-uso
criado: 2026-11-16
origem: Regras S01 a S25 do pacote aprovado pelo humano em 2026-11-16 (diario-2026-11-16-regras-para-o-vault, no stonebid-vault); S26 e S27 do pacote "contrato funcional e validação" de 2026-11-17
---
# 💻 Padrão de projeto de software

> [!tldr] Em uma linha
> As regras de branch, deploy, código, dependências e testes que todo projeto prático com código segue, além do [[Manual da Orquestra - Perfil projeto prático|perfil projeto prático]].

É o **código de obras da cidade**: não diz que casa construir, mas fixa a fiação, o encanamento e quem assina a vistoria, para qualquer casa ficar de pé. O formato dos commits continua no [[Padrão de commit]]; a arquitetura de partida está na [[Referência de arquitetura e stack]].

---

## 1. 🌿 Branches e entrega

- **S01 ID do requisito em todo lugar:** na branch, no commit e no PR, mais uma tabela requisito → teste → etapa → PR.
- **S02 Branches:** `main` é produção, `staging` é teste, trabalho em `tipo/ID-descricao` (o `tipo` é o do [[Padrão de commit]]). `staging` → `main` só por fast-forward.
- **S03 Merge na `main` é do humano.** O implementador termina no push, com CI verde (forma geral em G5, [[Manual da Orquestra - Agentes em paralelo]]).
- **S09 Push recusado:** `git format-patch` de um lado e `git am` do outro, em vez de forçar.
- **S19 Comando destrutivo** (reset, reescrita de histórico, `--force`) só com confirmação do humano, avisando o que continua detectável depois.

## 2. 🚀 Só com deploy (S04 a S08)

> [!warning] Este bloco só vale para projeto publicado
> Projeto que roda só localmente, em WSL ou Docker, não leva S04 a S08, nem o S24, que só existe com hospedagem.

- **S04 Só o CD publica.** CI e CD em arquivos separados; o CD roda depois do CI verde.
- **S05 Segredos num módulo só**, validados na subida; CI sem chave guardada (autenticação federada no provedor).
- **S06 Staging fixo** com banco separado do de produção.
- **S07 Seed reexecutável**, sem rede externa, rodando no CD e com relógio injetado (data controlada pelo teste).
- **S08 Aplicação vazia no ar na etapa 1:** o pipeline inteiro é provado antes da primeira funcionalidade.
- **S24 Critério de hospedagem:** custo, região, instância mínima, alerta de gasto e plano de desligar no fim.

## 3. 🧱 Código

- **S10 Reuso:** inventário antes de criar; variar por props ou slot; extrair na 2ª repetição.
- **S11 Gerado ou de biblioteca só pela CLI oficial;** nunca editar à mão.
- **S12 Nomes:** arquivos em inglês e kebab-case; identificadores na convenção da linguagem. Exceção só em decisão, com motivo.
- **S13 Camadas com uma direção de dependência;** uma feature não importa outra.
- **S14 Regra de negócio no domínio;** autorização, validação e dinheiro sempre no servidor.
- **S15 Erro com código próprio** e `details` acionável; o teste confere o código, não a mensagem.
- **S23 Camada MCP para agentes testarem:** uma tool por rota, desligada em produção, chave obrigatória.
- **S26 Campo de entrada nasce do contrato:** todo campo de entrada do frontend tem schema zod tirado do ENT-xx do contrato (`Anexos/contrato/02-entidades.md` do cofre do projeto) (tipo, tamanho, formato, valores permitidos, teto), uma mensagem diferente para cada violação (a do ERR-xx) e impede o impossível (ex.: campo de valor só aceita número). O schema da entidade é a fonte; a tela não inventa regra (Q02 do [[Manual da Orquestra - Perfil projeto prático|perfil]], [[Contrato funcional]]). É o par de frontend do S14.
- **S27 Comentário curto e pontual:** só o porquê que o código não mostra, em poucas linhas, sem repetir o código. ID citado só se existir no contrato (`Anexos/contrato/` do cofre do projeto). Fala do humano (2026-11-17): "comentários devem ser menos extensos e mais pontuais".

## 4. 📦 Versões e dependências

- **S16 Versão "citada ou mais recente",** sem trava; o mesmo runtime em todo ambiente (imagem local e, se publica, CI e CD). Conferir se a versão não é rc.
- **S17 Dependência nova pede justificativa** (para quê, alternativa, custo de manutenção); trocar biblioteca de base pede decisão.
- **S18 Limite conhecido e contorno** numa seção própria do README.

## 5. 🧪 Testes

- **S20 Teste de correção falha sem a correção** (ver [[Teste de corrida com janela forçada]]).
- **S21 Opcional desligado não restringe o caso base;** regra arriscada fica atrás de flag, testada ligada e desligada.
- **S22 Estado inválido provado no CI**, nunca como dado de demonstração. A suíte do repositório é de unitário e de API do backend; o E2E de interface é dos agentes de validação (Q04 e Q05 do perfil), sem suíte no repositório.

## 6. 🏗️ Arquitetura proposta na criação

- **S25** Ao criar um cofre de projeto prático de software, o agente **propõe a arquitetura (frontend e backend) e as tecnologias** a partir da [[Referência de arquitetura e stack]], para o humano ajustar em vez de partir do zero. A proposta fica na seção "Proposta de arquitetura e stack" do `geral-plano` do cofre novo; o aval vira as decisões de estrutura e stack, que citam essa seção no campo Proposta. Lá dentro, esta nota e a Referência são citadas como texto "Nome (no Vault)", nunca como wikilink. Fala do humano (2026-11-16, 09:56): "essa arquitetura deve ser proposta e apresentada sempre que for criar um vault do tipo projeto ... e as tecnologias devem ser proposta também para que eu posso propor sugestões de mudança em cima delas e não precisar partir do absoluto 0". Passo em [[Criar um novo cofre]].

## 🔗 Conexões
- Mapa: [[MOC Programação]]
- Perfil: [[Manual da Orquestra - Perfil projeto prático]]
- Relacionadas: [[Referência de arquitetura e stack]], [[Padrão de commit]], [[Criar um novo cofre]], [[Contrato funcional]]

## 🕓 Histórico
- v1 (2026-11-16): criação, com S01 a S25.
- v2 (2026-11-16): S25 diz onde a proposta mora (`geral-plano` do cofre novo), que as decisões a citam e que nota do `Vault` é citada lá como texto "Nome (no Vault)".
- v3 (2026-11-17): S26 (campo de entrada com schema tirado do ENT do contrato e mensagem por violação) e S27 (comentário curto e pontual).
- v4 (2026-11-19): S26 e S27 apontam para o contrato em `Anexos/contrato/` do cofre do projeto.
