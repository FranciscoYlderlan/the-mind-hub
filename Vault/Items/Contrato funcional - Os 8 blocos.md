---
aliases: [Blocos do contrato funcional, IDs do contrato, Functional contract blocks, O que vai em cada arquivo do contrato]
tags: [estudos/programacao]
tipo: manual
status: em-uso
criado: 2026-11-17
origem: Pacote "contrato funcional e validação" aprovado pelo humano em 2026-11-17
---
# 🧱 Contrato funcional: os 8 blocos

> [!tldr] Em uma linha
> O que cada bloco do [[Contrato funcional]] guarda, com o ID dele e o arquivo de `Anexos/contrato/` onde mora.

É a **ficha técnica de uma receita**: ingredientes com medida, modo de preparo em passos, o que fazer se a massa desandar e como saber que ficou pronto. Os modelos prontos, com um exemplo curto por bloco, estão no `Vault` em `Modelos/Orquestra/contrato/` (no cofre de projeto prático, o contrato em uso fica em `Anexos/contrato/`); a regra que os usa é a Q01 do [[Manual da Orquestra - Perfil projeto prático|perfil projeto prático]].

---

| # | Bloco e ID | Arquivo | O que guarda |
|---|---|---|---|
| 1 | Atores e perfis (ATR-xx) | `01-atores.md` | Quem interage e as permissões de cada perfil |
| 2 | Modelo de dados e invariantes (ENT-xx) | `02-entidades.md` | Por entidade: campos (tipo, tamanho, obrigatoriedade, formato, valores permitidos), invariantes nunca violadas em nenhum fluxo e estados do ciclo de vida |
| 3 | Casos de uso (UC-xx) | `03-casos-de-uso.md` | Ator, objetivo, pré e pós-condições; fluxo principal em passos (ator → sistema); FA-xx e FE-xx |
| 4 | Componentes lógicos (CMP-xx) | `04-componentes.md` | Papel (não aparência), entradas e saídas, eventos, estados obrigatórios e regras |
| 5 | Catálogo de erros (ERR-xx) | `05-erros.md` | Código, condição de disparo, tratamento, mensagem ao usuário e estado final |
| 6 | Estados e navegação (NAV-xx) | `06-navegacao.md` | Origem + evento + condição → destino, com estados lógicos |
| 7 | Mapa de rastreabilidade | `07-rastreabilidade.md` | Requisito, UC, fluxos, CMP, ENT, ERR, tela (depois) e cenário de teste (o AC-xx que prova a linha) |
| 8 | Critérios de aceite (AC-xx) | `08-criterios-de-aceite.md` | Um dado/quando/então por fluxo |

Toda funcionalidade preenche ENT, UC (com FA e FE), ERR e AC; CMP, NAV e a coluna Tela só entram quando ela tem interface. Mais dois arquivos: `00-requisitos.md` (RF, RNF e RN do documento-fonte) e `mudancas.md` (itens M-xx). O `README.md` é o índice.

---

> [!note] Regras de cada bloco
> 1. **ENT:** a validação pertence à entidade, não à tela; toda tela herda. Cada violação aponta o seu ERR, para a mensagem dizer o que está errado (S26).
> 2. **UC:** o FA diz o passo de origem, a variação e se volta ao principal ou termina; o FE diz o passo de origem, o ERR e o estado final.
> 3. **CMP:** estados obrigatórios vazio, carregando, preenchido, erro, sucesso e desabilitado; as regras dizem que campos de ENT ele valida e que UC atende.
> 4. **ERR:** o FE só referencia um ERR; o código é o código de erro do servidor (S15); tratamento padrão é repetir, voltar ou bloquear.
> 5. **NAV:** cada estado lógico é mapeado para tela depois; aberto pela URL, já mostra menus e botões sem clique prévio.
> 6. **AC:** um por fluxo (principal, FA e FE); são eles que o verificador de fluxo principal e o adversarial executam.

> [!example] Um fio do contrato
> RF-01 → UC-01 (fluxo principal) → CMP-01 valida `pessoas` de ENT-01 → digitar letras dispara ERR-03 → AC-04 prova que o campo não aceita letras.

> [!tip] Quando abrir esta nota
> Ao preencher um bloco do contrato ou ao revisar se uma tela cobre tudo o que o bloco pede.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** Oito blocos, um arquivo cada, IDs que se cruzam no mapa de rastreabilidade.
* **Ponto 2:** Célula vazia no mapa é lacuna: requisito sem UC ou UC sem AC aparece antes da tela.
* **Ponto 3:** Limite: a coluna Tela só é preenchida quando a tela existe, nunca antes do contrato.

### 🔗 Conexões
- Mapa: [[MOC Programação]]
- Nota-mãe: [[Contrato funcional]]
- Relacionadas: [[Padrão de projeto de software]], [[Manual da Orquestra - Perfil projeto prático]]

## 🕓 Histórico
- v1 (2026-11-17): criação, separada do [[Contrato funcional]] pelo tamanho.
- v2 (2026-11-19): os arquivos moram em `Anexos/contrato/` do cofre do projeto.
