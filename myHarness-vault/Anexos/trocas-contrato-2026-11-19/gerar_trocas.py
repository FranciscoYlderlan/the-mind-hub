"""Gera trocas.json (lista ordenada de trocas do contrato). Rodar: python3 gerar_trocas.py"""
import json, pathlib

AQUI = pathlib.Path(__file__).parent
T = []

def t(id_, arq, atual, novo, motivo):
    T.append({"id": id_, "arquivo": arq, "atual": atual, "novo": novo, "motivo": motivo})

R = "00-requisitos.md"; A = "01-atores.md"; E = "02-entidades.md"; U = "03-casos-de-uso.md"
C = "04-componentes.md"; ER = "05-erros.md"; RA = "07-rastreabilidade.md"; AC = "08-criterios-de-aceite.md"
RM = "README.md"; MU = "mudancas.md"
L1 = "Lista 1 do relatório do contrato de 2026-11-19"
def LA(n): return f"Lista 2, grupo A, dúvida {n}"

# ---------------- LISTA 1 ----------------
t("L1-01", R,
  "| S1 | [a confirmar] O humano citou reinício a cada 4 h; os limites de uso do plano Claude funcionam em janelas de 5 h | RF-18, CMP-01 | Conferir no /usage do Claude CLI |\n"
  "| S2 | [a confirmar] A fonte do consumo semanal e da janela é o próprio Claude CLI; sem saída legível por máquina, o plano B é estimar pelos registros locais de sessão da CLI | RF-18, RNF-04 | Protótipo de leitura antes da tela |\n"
  "| S3 | [a confirmar] Cada agente é um processo `claude -p` com saída em fluxo JSON, modelo, ferramentas permitidas, pastas extras e instruções de sistema passados por parâmetro | RF-05, RF-10, RF-29, RF-32, RNF-06 | Conferir os parâmetros em `claude --help` da versão instalada |\n"
  "| S4 | [a confirmar] Alternativa ao S3: o Claude Agent SDK num processo Node ao lado do Rust | Arquitetura do backend | Decisão de arquitetura antes do RF-10 |\n"
  "| S5 | [a confirmar] Só o GitHub usa OAuth; o Claude CLI usa o login da própria CLI e a Obsidian CLI é local e exige o Obsidian aberto | RF-01 a RF-03, TEL-02 | Teste de conexão das três |\n"
  "| S6 | [a confirmar] O adversarial usa a integração do Claude CLI com o Chrome (Claude in Chrome); plano B, um servidor MCP de navegador | RF-25 | Protótipo de um agente abrindo a aplicação |\n",
  "", L1 + ", A(1): S1 a S6 viram D7 a D14")

t("L1-02", R,
  "| D6 | Mais de uma memória | O projeto pode ligar mais de um cofre do Obsidian como contexto de pesquisa (RN-29, RN-30, UC-14) | 2026-11-19 |\n",
  "| D6 | Mais de uma memória | O projeto pode ligar mais de um cofre do Obsidian como contexto de pesquisa (RN-29, RN-30, UC-14) | 2026-11-19 |\n"
  "| D7 | Fonte do consumo do plano | A janela de uso tem 5 h e a semana, 7 dias, lidos do evento `rate_limit_event` do Claude CLI; o SQLite guarda só a última leitura; sem o evento, o plano B estima pelos registros locais de sessão da CLI e marca o valor \"estimado\" (RF-18, RNF-04, ENT-14, CMP-01) | 2026-11-19 |\n"
  "| D8 | Como cada agente roda | Cada agente é um processo `claude -p` direto, com quatro camadas de permissão e `--setting-sources \"\"`; o Claude Agent SDK fica fora (RF-10, RF-29, RNF-06) | 2026-11-19 |\n"
  "| D9 | Configuração pessoal | Nenhum agente herda a configuração pessoal do Claude CLI do Humano (RNF-06, ENT-15) | 2026-11-19 |\n"
  "| D10 | Como cada integração conecta | Claude CLI pelo `/login` da própria CLI; GitHub por um app OAuth próprio do MyHarness, com device flow, e o token no cofre de credenciais do SO; Obsidian pelo servidor MCP da Obsidian CLI (RF-01 a RF-03, ATR-06 a ATR-08) | 2026-11-19 |\n"
  "| D11 | Navegador do adversarial | O adversarial roda em `claude -p --chrome`, disponível com `--strict-mcp-config` (RF-25, ATR-09) | 2026-11-19 |\n"
  "| D12 | Plataforma | App nativo para Windows; os RNF são medidos no Windows 11; o cofre de credenciais do SO é o Gerenciador de Credenciais do Windows (RNF-05, ENT-13) | 2026-11-19 |\n"
  "| D13 | Nome e identificador | Grafia MyHarness; identificador `dev.myharness.app`, com os dados do app em `%APPDATA%\\dev.myharness.app` (RNF-05) | 2026-11-19 |\n"
  "| D14 | Quem altera o contrato | Só o orquestrador altera `Anexos/contrato/` e as notas dos cofres; subagente propõe a mudança no relatório (RN-01, ATR-02 a ATR-05) | 2026-11-19 |\n",
  L1 + ", A(2): D7 a D14")

t("L1-03", RM, "decisões D1 a D6 e suposições S1 a S15", "decisões D1 a D14 e suposições S7 a S15", L1 + ", A(3): README:14")

t("L1-04", R,
  "| RF-01 | Detectar o Claude CLI instalado, verificar a autenticação e iniciar o login quando faltar.",
  "| RF-01 | Detectar o Claude CLI instalado, verificar a autenticação e, quando faltar, iniciar o login pelo `/login` da própria CLI (D10).",
  L1 + ", B: RF-01 (/login)")
t("L1-05", R,
  "| RF-02 | Verificar se o Obsidian está aberto, se a CLI responde e se o cofre do projeto está acessível.",
  "| RF-02 | Verificar se o Obsidian está aberto, se o servidor MCP da Obsidian CLI responde e se o cofre do projeto está acessível (D10).",
  L1 + ", B: RF-02 (MCP)")
t("L1-06", R,
  "| RF-03 | Autenticar no GitHub por OAuth e guardar o token no cofre de credenciais do sistema operacional. Entrada: consentimento no navegador.",
  "| RF-03 | Autenticar no GitHub pelo app OAuth próprio do MyHarness, com device flow (o Humano digita o código em github.com/login/device), e guardar o token no Gerenciador de Credenciais do Windows (D10, D12). Entrada: código do device flow confirmado pelo Humano no navegador.",
  L1 + ", B: RF-03 (device flow)")
t("L1-07", R,
  "| RF-10 | Iniciar um processo do Claude CLI por tarefa aprovada,",
  "| RF-10 | Iniciar um processo `claude -p` por tarefa aprovada (D8),",
  L1 + ", B: RF-10 (claude -p)")
t("L1-08", R,
  "| RF-18 | Obter o consumo semanal e o da janela de uso com reinício periódico, com a hora do próximo reinício. Entrada: dados de uso do Claude CLI [a confirmar: fonte, S2]. Saída: % semanal, % da janela, hora do reinício.",
  "| RF-18 | Obter o consumo da semana de 7 dias e o da janela de 5 h, com a hora do próximo reinício de cada um, pelo evento `rate_limit_event` do Claude CLI (D7). Entrada: `rate_limit_event`; sem ele, os registros locais de sessão da CLI, com o valor marcado \"estimado\". Saída: % semanal, % da janela, hora de cada reinício, origem e hora da leitura.",
  L1 + ", B: RF-18")
t("L1-09", R,
  "| RNF-04 | Desempenho (ambos): consumo do chat atualizado em até 2 s após cada resposta; consumo do plano em até 60 s [a confirmar]. | Uso normal; comparar o painel com os dados da CLI em 20 amostras |",
  "| RNF-04 | Desempenho (ambos): consumo do chat atualizado em até 2 s após cada resposta; consumo do plano em até 60 s [a confirmar], igual ao do `/usage` do Claude CLI dentro da tolerância [a preencher]. | Uso normal; comparar o painel com o `/usage` do Claude CLI em 20 amostras |",
  L1 + ", B: RNF-04 (comparar com /usage)")
t("L1-10", R,
  "| RNF-05 | Segurança (backend): tokens de OAuth ficam no cofre de credenciais do SO, nunca em arquivo; 0 tokens em texto puro no disco, nos logs, no SQLite e no cofre Obsidian. | Após conectar as três integrações e rodar um ciclo completo; busca automatizada pelos tokens nas pastas do app e do projeto |",
  "| RNF-05 | Segurança (backend): tokens de OAuth ficam no Gerenciador de Credenciais do Windows (D12), nunca em arquivo; 0 tokens em texto puro no disco, nos logs, no SQLite e no cofre Obsidian. | Após conectar as três integrações e rodar um ciclo completo; busca automatizada pelos tokens na pasta do app (`%APPDATA%\\dev.myharness.app`, D13) e na do projeto |",
  L1 + ", B: RNF-05")
t("L1-11", R,
  "| RNF-06 | Segurança (backend): cada processo de agente recebe só as ferramentas e pastas do seu papel; 100% das tentativas fora do papel negadas (escrita no cofre por subagente, merge, push --force).",
  "| RNF-06 | Segurança (backend): cada processo de agente recebe só as ferramentas e pastas do seu papel e não herda a configuração pessoal do Claude CLI do Humano (D8, D9); 100% das tentativas fora do papel negadas (escrita de subagente em cofre, em `Anexos/contrato/` ou em `docs/contrato/`, merge, push --force).",
  L1 + ", B: RNF-06; decisão subagente-nao-altera-contrato")
t("L1-12", R,
  "| RN-01 | Só o orquestrador grava, altera ou move notas no cofre do projeto, em qualquer chat. Violação: a escrita de subagente é recusada e vira log de violação (ERR-13). Exceção: o Humano escreve direto no Obsidian, fora do harness. |",
  "| RN-01 | Só o orquestrador grava, altera ou move notas no cofre do projeto e altera o contrato (`Anexos/contrato/`), em qualquer chat; nenhum subagente escreve em cofre algum nem no contrato, nem na cópia em `docs/contrato/` do repositório (D14). Violação: a escrita de subagente é recusada e vira log de violação (ERR-13). Exceção: o Humano escreve direto no Obsidian, fora do MyHarness. |",
  L1 + ", B: RN-01 (contrato incluído); grafia")
t("L1-13.1", R, "a partir das regras do harness,", "a partir das regras do MyHarness,", L1 + ", B: grafia 00:44")
t("L1-13.2", R, "(governança no harness, não no cofre)", "(governança no MyHarness, não no cofre)", L1 + ", B: grafia 00:44")
t("L1-13.3", R, "passam a viver no núcleo do harness. Em todas, a origem é decisão do negócio e quem altera ou valida é o Humano, dono do harness.",
  "passam a viver no núcleo do MyHarness. Em todas, a origem é decisão do negócio e quem altera ou valida é o Humano, dono do MyHarness.", L1 + ", B: grafia 00:72")
t("L1-13.4", R, "O que sai do cofre e vira núcleo do harness:", "O que sai do cofre e vira núcleo do MyHarness:", L1 + ", B: grafia 00:118")
t("L1-13.5", A, "Validador final e dono do harness;", "Validador final e dono do MyHarness;", L1 + ", B: grafia 01:9")
t("L1-13.6", A, "escrever direto no Obsidian, fora do harness (RN-01)", "escrever direto no Obsidian, fora do MyHarness (RN-01)", L1 + ", B: grafia 01:9")
t("L1-13.7", A, "| Ler .md do cofre direto | sim (fora do harness) |", "| Ler .md do cofre direto | sim (fora do MyHarness) |", L1 + ", B: grafia 01:26")
t("L1-13.8", A, "| Gravar no cofre de memória | sim (fora do harness) |", "| Gravar no cofre de memória | sim (fora do MyHarness) |", L1 + ", B: grafia 01:27")
t("L1-13.9", A, "| Gravar em cofre de consulta | sim (fora do harness) |", "| Gravar em cofre de consulta | sim (fora do MyHarness) |", L1 + ", B: grafia 01:28")
t("L1-13.10", RM, "- **Produto:** MyHarness (Harness), aplicação", "- **Produto:** MyHarness, aplicação", L1 + ", B: grafia README:5")

t("L1-14", A,
  "| ATR-06 | Claude CLI | Sistema externo: executa orquestrador e subagentes | Fornecer processos, eventos de resposta e uso de tokens; login próprio (S5) | — |",
  "| ATR-06 | Claude CLI | Sistema externo: executa orquestrador e subagentes, cada um num processo `claude -p` (D8) | Fornecer processos, eventos de resposta e uso de tokens; login próprio pelo `/login` (D10), com falha de autenticação devolvida como `authentication_failed` (ERR-04) | — |",
  L1 + ", C: ATR-06")
t("L1-15", A,
  "| ATR-07 | Obsidian CLI | Sistema externo local; exige o Obsidian aberto (S5) |",
  "| ATR-07 | Obsidian CLI | Sistema externo local, acessado pelo servidor MCP da Obsidian CLI; exige o Obsidian aberto (D10) |",
  L1 + ", C: ATR-07")
t("L1-16", A,
  "| ATR-08 | GitHub | Sistema externo, autenticado por OAuth (RF-03) |",
  "| ATR-08 | GitHub | Sistema externo, autenticado pelo app OAuth próprio do MyHarness, com device flow (RF-03, D10) |",
  L1 + ", C: ATR-08")
t("L1-17", A,
  "| ATR-09 | Claude in Chrome | Sistema externo: navegador usado pelo adversarial (S6) |",
  "| ATR-09 | Claude in Chrome | Sistema externo: navegador usado pelo adversarial, que roda em `claude -p --chrome`, disponível com `--strict-mcp-config` (D11) |",
  L1 + ", C: ATR-09")
t("L1-18.1", A, "escrever direto no Obsidian, fora do MyHarness (RN-01) | — |",
  "escrever direto no Obsidian e alterar o contrato, fora do MyHarness (RN-01, D14) | — |", L1 + ", C: ATR-01")
t("L1-18.2", A, "gravar no cofre de memória (relatórios, decisões aprovadas, \"Onde parei\"); falar com o Humano |",
  "gravar no cofre de memória (relatórios, decisões aprovadas, \"Onde parei\"); alterar o contrato em `Anexos/contrato/` (RN-01, D14); falar com o Humano |", L1 + ", C: ATR-02")
t("L1-18.3", A, "| Escrever no cofre (RN-01); perguntar ao Humano (RN-12); merge,",
  "| Escrever em cofre algum ou no contrato (RN-01, D14); perguntar ao Humano (RN-12); merge,", L1 + ", C: ATR-03")
t("L1-18.4", A, "corrigir código (prompt de fábrica); escrever no cofre (RN-01);",
  "corrigir código (prompt de fábrica); escrever em cofre algum ou no contrato (RN-01, D14);", L1 + ", C: ATR-04")
t("L1-18.5", A, "usar o navegador ao mesmo tempo que outro agente (RN-15); escrever no cofre (RN-01) |",
  "usar o navegador ao mesmo tempo que outro agente (RN-15); escrever em cofre algum ou no contrato (RN-01, D14) |", L1 + ", C: ATR-05")
t("L1-19", A,
  "| Gravar em cofre de consulta | sim (fora do MyHarness) | não | não | não | não |\n",
  "| Gravar em cofre de consulta | sim (fora do MyHarness) | não | não | não | não |\n"
  "| Alterar `Anexos/contrato/` | sim (fora do MyHarness) | sim | não | não | não |\n",
  L1 + ", C: matriz, linha \"Alterar Anexos/contrato/\"")

t("L1-20.1", E, "Mora em: SQLite (status) + cofre de credenciais do SO.",
  "Mora em: SQLite (status) + Gerenciador de Credenciais do Windows (D12).", L1 + ", D: ENT-13")
t("L1-20.2", E, "| credencial (RN-04) | segredo | — | só GitHub (S5) | — | só no cofre de credenciais do SO | — |",
  "| credencial (RN-04) | segredo | — | só GitHub: token do device flow (D10) | — | só no Gerenciador de Credenciais do Windows | — |", L1 + ", D: ENT-13")
t("L1-21", E,
  "| proximo_reinicio | data e hora | — | sim | — | janela de 4 h ou 5 h [a confirmar, S1] | — |\n",
  "| proximo_reinicio | data e hora | — | sim | ISO 8601 UTC | reinício da janela de 5 h (D7) | — |\n"
  "| semanal_reinicio | data e hora | — | sim | ISO 8601 UTC | reinício da semana de 7 dias (D7) | — |\n"
  "| lida_em | data e hora | — | sim | ISO 8601 UTC | hora da leitura | — |\n"
  "| origem | enumeração | — | sim | — | evento, estimado | — |\n"
  "| janela_status | enumeração | — | sim | — | [a confirmar: valores do `rate_limit_event`] | — |\n"
  "| semanal_status | enumeração | — | sim | — | [a confirmar: valores do `rate_limit_event`] | — |\n"
  "| excedente | [a confirmar: tipo] | — | não | — | [a confirmar] | — |\n"
  "\n### Invariantes (nunca violadas, em nenhum fluxo)\n\n"
  "- Guarda só a última leitura: cada leitura nova substitui a anterior (D7).\n"
  "- `origem = evento` quando vem do `rate_limit_event`; `origem = estimado` quando vem dos registros locais de sessão da CLI (D7).\n",
  L1 + ", D: ENT-14; " + LA(4))
t("L1-22", E, "- Subagente não tem ferramenta de escrita no cofre (RN-01, RF-29).",
  "- Subagente não tem ferramenta de escrita em cofre algum nem no contrato (RN-01, RF-29).\n"
  "- Nenhum papel herda a configuração pessoal do Claude CLI do Humano; o processo roda com `--setting-sources \"\"` (D8, D9).",
  L1 + ", D: ENT-15")

t("L1-23", U, "2. Humano clica em \"Conectar\" numa integração → sistema abre o login ou o OAuth.",
  "2. Humano clica em \"Conectar\" numa integração → sistema inicia o `/login` do Claude CLI, o device flow do GitHub (mostra o código a digitar em github.com/login/device) ou o teste do servidor MCP da Obsidian CLI (D10).",
  L1 + ", E: UC-01 passo 2")
t("L1-24", U, "| FE-02 | 3 | ERR-13 (escrita no cofre) ou ERR-14 (merge) |",
  "| FE-02 | 3 | ERR-13 (escrita em cofre ou no contrato) ou ERR-14 (merge) |", L1 + ", E: UC-04 FE-02")
t("L1-25", ER, "processo que não é o orquestrador tenta escrever no cofre (RN-01, RN-27; UC-04 FE-02) (agente)",
  "processo que não é o orquestrador tenta escrever em cofre ou no contrato (`Anexos/contrato/`, `docs/contrato/`) (RN-01, RN-27; UC-04 FE-02) (agente)",
  L1 + ", E: ERR-13")
t("L1-26.1", C, "- **Papel:** mostrar o consumo semanal e o da janela de uso com reinício.",
  "- **Papel:** mostrar o consumo da janela de 5 h e o da semana de 7 dias (D7).", L1 + ", E: CMP-01")
t("L1-26.2", C, "- **Eventos:** `passou-o-mouse` (mostra a hora do próximo reinício).",
  "- **Eventos:** `passou-o-mouse` (mostra a hora do próximo reinício de cada um e a hora da última leitura).", L1 + ", E: CMP-01")
t("L1-26.3", C, "- **Regras:** fica visível em todas as telas. Janela de 4 h ou 5 h [a confirmar, S1].",
  "- **Regras:** fica visível em todas as telas. Mostra a última leitura, com a hora dela; valor estimado pelos registros locais aparece marcado \"estimado\" (D7).", L1 + ", E: CMP-01")
t("L1-26.4", C, "| preenchido | dois percentuais (semanal e janela) | passar o mouse para ver o reinício |",
  "| preenchido | dois percentuais (janela e semanal), com a hora da última leitura e, se for o caso, \"estimado\" | passar o mouse para ver os reinícios |", L1 + ", E: CMP-01")
t("L1-27", ER, "| o OAuth do GitHub é cancelado ou recusado (UC-01 FE-02) |",
  "| o device flow do GitHub é cancelado, recusado (`access_denied`) ou expira (`expired_token`) (UC-01 FE-02) |", L1 + ", E: ERR-02")

t("L1-28", AC, "| AC-04 | UC-01 | FE-02 | o OAuth cancelado | o navegador fecha | o status continua desconectado (ERR-02) |",
  "| AC-04 | UC-01 | FE-02 | o device flow do GitHub iniciado | o Humano recusa no GitHub (`access_denied`) ou o código expira (`expired_token`) | o status continua desconectado (ERR-02) |",
  L1 + ", F: AC-04")
t("L1-29", AC, "| AC-129 | UC-01 | TEL-02 FE-01 | o OAuth recusado | o navegador fecha | o cartão mostra o motivo (ERR-02) |",
  "| AC-129 | UC-01 | TEL-02 FE-01 | o device flow recusado ou expirado | o núcleo recebe `access_denied` ou `expired_token` | o cartão mostra o motivo (ERR-02) |",
  L1 + ", F: AC-129")
t("L1-30", AC, "| ele tenta escrever em orquestra/ |", "| ele tenta escrever em orquestra/ ou em Anexos/contrato/ |", L1 + ", F: AC-58")
t("L1-31", AC, "| a regra RN-01 ativa | um subagente é despachado | a ferramenta de escrita no cofre não está entre as dele |",
  "| a regra RN-01 ativa | um subagente é despachado | nenhuma ferramenta de escrita em cofre ou no contrato está entre as dele, e ele não herda a configuração pessoal do Claude CLI |",
  L1 + ", F: AC-116")
t("L1-32", AC, "No MyHarness, \"API\" é a camada de comandos do núcleo Rust (Tauri) [a confirmar: como o verificador chama o backend sem a tela].",
  "No MyHarness, \"API\" é a camada de comandos do núcleo Rust (Tauri), que o verificador chama sem a tela; a tela é verificada no navegador com o núcleo simulado e pelo tauri-driver.",
  L1 + ", F: 08:5")
t("L1-33", RM, "o frontend é a interface React, no mesmo repositório [a confirmar].",
  "o frontend é a interface React, no mesmo repositório `my-harness`.", L1 + ", F: README:8")

# mudancas.md M-01 (estado do contrato)
t("L1-M01.1", RM, "- **Estado:** rascunho de 2026-11-19, ainda sem aval do humano. Pontos sem fonte estão marcados `[a confirmar]`.",
  "- **Estado:** aprovado pelo Humano em 2026-11-19; as mudanças estão em `mudancas.md`. Pontos sem fonte seguem marcados `[a confirmar]`.",
  L1 + ", mudancas.md: M-01 rascunho aprovado")
t("L1-M01.2", R, "- **Preenchido em:** 2026-11-19 (rascunho do pesquisador, aguardando aval do humano)",
  "- **Preenchido em:** 2026-11-19 (aprovado pelo Humano em 2026-11-19)", L1 + ", mudancas.md: M-01 rascunho aprovado")
linhas_m = (AQUI / "mudancas-novas.md").read_text(encoding="utf-8").strip("\n") + "\n"
t("L1-M01.3", MU,
  "Nenhuma mudança aprovada ainda: este contrato é o rascunho inicial, transcrito de \"Harness — especificação funcional\" (18 de nov. de 2026, com D5 e D6 de 2026-11-19). A primeira linha entra quando o humano aprovar o rascunho ou a primeira alteração dele.",
  "Contrato transcrito de \"Harness — especificação funcional\" (18 de nov. de 2026, com D5 e D6 de 2026-11-19) e aprovado pelo Humano em 2026-11-19 (M-01).",
  L1 + ", mudancas.md: M-01")
t("L1-M01.4", MU, "| ID | Data | O que mudou | Blocos e IDs afetados | Motivo | Aprovação |\n|---|---|---|---|---|---|\n",
  "| ID | Data | O que mudou | Blocos e IDs afetados | Motivo | Aprovação |\n|---|---|---|---|---|---|\n" + linhas_m,
  "mudancas.md: M-01 a M-14 (linhas de mudancas-novas.md)")

# ---------------- LISTA 2, GRUPO A ----------------
# A-01 entidades no SQLite + ENT-26
t("A-01.1", E,
  "Fonte: tabela \"Entidades e onde moram\" do documento-fonte (ENT-01 a ENT-16). As ENT-17 a ENT-25 não estão nessa tabela: aparecem só no campo \"Dados\" das RN e estão aqui para que toda RN tenha entidade [a confirmar].",
  "Fonte: tabela \"Entidades e onde moram\" do documento-fonte (ENT-01 a ENT-16). As ENT-17 a ENT-26 não estão nessa tabela: as ENT-17 a ENT-25 aparecem no campo \"Dados\" das RN, e a ENT-26 guarda as pastas em contexto do RF-16; cada uma diz onde mora.",
  LA(1) + "; decisão entidades-no-sqlite")
for n, nome, antigo, novo in [
    (17, "Escrita", "Citada em RN-01 (Escrita.caminho) e RF-28 (nota, motivo, hora). Mora em: [a confirmar].",
                    "Citada em RN-01 (Escrita.caminho) e RF-28 (nota, motivo, hora). Mora em: SQLite."),
    (18, "Decisão", "Citada em RN-03 (registrada_em) e RN-06 (aval_id). Mora no cofre e [a confirmar] no SQLite.",
                    "Citada em RN-03 (registrada_em) e RN-06 (aval_id). Mora no cofre, como nota; no SQLite fica só o aval."),
    (19, "Briefing", "Citado em RN-10 (Briefing.conteudo).", "Citado em RN-10 (Briefing.conteudo). Mora em: SQLite."),
    (20, "Rodada", "Citada em RN-11 (Rodada.status).", "Citada em RN-11 (Rodada.status). Mora em: SQLite."),
    (21, "Funcionalidade", "Citada em RN-11 e RN-20 (Funcionalidade.status).", "Citada em RN-11 e RN-20 (Funcionalidade.status). Mora em: SQLite."),
    (22, "Configuração", "Citada em RN-13.\n", "Citada em RN-13. Mora em: SQLite.\n"),
    (23, "PR", "Citado em RN-17 (PR.status).", "Citado em RN-17 (PR.status). Mora em: SQLite."),
    (24, "Critério", "Citado em RN-18 (Critério.status, Critério.prova).", "Citado em RN-18 (Critério.status, Critério.prova). Mora em: SQLite."),
]:
    t(f"A-01.{n}", E, f"## ENT-{n} {nome} [a confirmar: fora da tabela da fonte]\n\n{antigo}",
      f"## ENT-{n} {nome}\n\n{novo}", LA(1) + "; decisão entidades-no-sqlite")
t("A-01.25", E, "## ENT-25 Diário [a confirmar: fora da tabela da fonte; mora no cofre]\n\nCitado em RN-24 (Diário.onde_parei).",
  "## ENT-25 Diário\n\nCitado em RN-24 (Diário.onde_parei). Mora só no cofre.", LA(1) + "; decisão entidades-no-sqlite")
t("A-01.26", E, "| adiamento | texto | — | não | — | um por chat (RN-23) | — |",
  "| adiamento | texto | — | não | — | um por chat (RN-23) | — |\n\n"
  "## ENT-26 PastaContexto\n\n"
  "Citada em RF-16 (pastas que o orquestrador e os subagentes podem acessar). Mora em: SQLite.\n\n"
  "| Campo | Tipo | Tamanho ou faixa | Obrigatório | Formato | Valores permitidos | Erro por violação |\n"
  "|---|---|---|---|---|---|---|\n"
  "| projeto | referência | — | sim | id de ENT-01 | — | — |\n"
  "| caminho | caminho | — | sim | caminho de pasta no disco [a confirmar: absoluto?] | pasta existente e com permissão | inacessível: ERR-32 |\n\n"
  "### Invariantes (nunca violadas, em nenhum fluxo)\n\n"
  "- A lista vale para as próximas execuções: pasta adicionada passa a ser acessível, pasta removida deixa de ser (UC-11 passo 3, FA-01).",
  LA(1) + "; decisão entidades-no-sqlite (ENT-26 nova)")
t("A-01.27", C, "- **Entradas:** RF-14 (ENT-11), RF-16; resultados de RF-34.",
  "- **Entradas:** RF-14 (ENT-11), RF-16 (ENT-26); resultados de RF-34.", LA(1) + "; ENT-26 no CMP-02")
t("A-01.28", RA, "| ENT-11, ENT-02 | ERR-40 | TEL-01 (prevista) | AC-102 |",
  "| ENT-11, ENT-02, ENT-26 | ERR-40 | TEL-01 (prevista) | AC-102 |", LA(1) + "; RF-15 mostra as pastas em contexto")
t("A-01.29", RA, "| [lacuna: nenhuma entidade guarda as pastas em contexto] |", "| ENT-26 |", LA(1) + "; lacuna do RF-16 fechada")
t("A-01.30", RM, "| Modelo de dados e invariantes | ENT-01 a ENT-25 |", "| Modelo de dados e invariantes | ENT-01 a ENT-26 |", LA(1))

# A-02 push e PR pelo núcleo
t("A-02.1", R, "| D3 | Até onde o subagente vai no GitHub | Worktree e branch próprias, push e PR aberto; o merge é do Humano | 2026-11-18 |",
  "| D3 | Até onde o subagente vai no GitHub | Worktree e branch próprias, até o commit; o núcleo faz o push e abre o PR (RF-27), e o merge é do Humano | 2026-11-19 |",
  LA(2) + "; decisão push-e-pr-pelo-nucleo (D3 dizia o contrário)")
t("A-02.2", R, "| RN-17 | O subagente termina no push e no PR aberto; o merge é sempre do Humano. Violação: bloqueia merge, push --force e push na branch principal (ERR-14). Sem exceção. |",
  "| RN-17 | O subagente de funcionalidade termina no commit na própria worktree; o push e o PR são do núcleo (RF-27), e o merge é sempre do Humano. Nenhum agente recebe token do GitHub. Violação: o núcleo nega a agente push, merge e push --force (ERR-14). Sem exceção. |",
  LA(2) + "; decisão push-e-pr-pelo-nucleo")
t("A-02.3", R, "em `docs/contrato/`, merge, push --force).", "em `docs/contrato/`, push, merge, push --force).", LA(2) + "; RNF-06 nega push de agente")
t("A-02.4", A, "Trabalhar na própria worktree e branch (RN-16); tocar os arquivos da tarefa; fazer push e abrir PR;",
  "Trabalhar na própria worktree e branch (RN-16); tocar os arquivos da tarefa; commitar na worktree (o push e o PR são do núcleo, RF-27);",
  LA(2) + "; ATR-03")
t("A-02.5", A, "perguntar ao Humano (RN-12); merge, push --force, push na branch principal (RN-17);",
  "perguntar ao Humano (RN-12); push, merge, push --force (RN-17);", LA(2) + "; ATR-03")
t("A-02.6", A, "| Push e abrir PR | sim | não | sim | não | não |",
  "| Push e abrir PR | sim (no GitHub) | não | não (o núcleo faz, RF-27) | não | não |", LA(2) + "; matriz")
t("A-02.7", E, "| comandos (RN-17) | lista | — | — | — | sem merge, push --force, push na principal | ERR-14 |",
  "| comandos (RN-17) | lista | — | — | — | sem push, merge nem push --force | ERR-14 |", LA(2) + "; ENT-07")
t("A-02.8", E, "Rode a prova antes de dizer que terminou e termine com push e PR. Devolva o relatório no formato pedido, com dúvidas e o que notou fora do escopo. | 45 |",
  "Rode a prova antes de dizer que terminou e termine com o commit. Devolva o relatório no formato pedido, com dúvidas e o que notou fora do escopo. | 44 [a confirmar: texto de 2026-11-19, contado pela regra da fonte] |",
  LA(2) + "; prompt de fábrica de Funcionalidade")
t("A-02.9", E, "uma contagem por espaços dá 52, 43, 33, 43 e 23.", "uma contagem por espaços dá 52, 42, 33, 43 e 23.", LA(2) + "; contagem do prompt novo")
t("A-02.10", U, "3. Subagente termina, faz push e devolve o relatório.",
  "3. Subagente termina com o commit na worktree e devolve o relatório; o núcleo faz o push e abre o PR (RF-27).", LA(2) + "; UC-04 passo 3")
t("A-02.11", U, "ou ERR-14 (merge) |", "ou ERR-14 (push ou merge) |", LA(2) + "; UC-04 FE-02")
t("A-02.12", ER, "| agente tenta merge, push --force ou push na branch principal (RN-17; UC-04 FE-02) (agente) |",
  "| agente tenta push, merge ou push --force (RN-17; UC-04 FE-02) (agente) |", LA(2) + "; ERR-14")
t("A-02.13", AC, "| AC-114 | UC-10 | requisito RF-27 | uma tarefa concluída | o subagente termina | existe um PR aberto da branch dela |",
  "| AC-114 | UC-10 | requisito RF-27 | uma tarefa concluída com commit na worktree | o subagente termina | o núcleo faz o push e existe um PR aberto da branch dela, sem token do GitHub na execução do subagente |",
  LA(2) + "; AC-114")

# A-03 papel pesquisa
t("A-03.1", R, "Exceção: subagente só de leitura (pesquisa) [a confirmar, S10].",
  "Exceção: tarefa do papel pesquisa, que só lê (nada escreve, nem no repositório nem nos cofres), é despachada sem aval.", LA(3) + "; decisão papel-pesquisa")
t("A-03.2", R, "Exceção: subagentes só de leitura e de teste não contam.",
  "Exceção: subagentes do papel pesquisa e de teste não contam.", LA(3) + "; decisão papel-pesquisa (fora do teto)")
t("A-03.3", R, "| S10 | [a confirmar] Subagente só de leitura (pesquisa) pode rodar sem aval do plano | RN-05 | Decisão do humano |\n", "", LA(3) + "; S10 sai das suposições")
t("A-03.4", RM, "suposições S7 a S15", "suposições S7 a S9 e S11 a S15", LA(3) + "; S10 removida")
t("A-03.5", A, "Papel de pesquisa (subagente só de leitura) aparece em RN-05 e RN-13, mas não está na lista de papéis da fonte (RF-13: orquestrador, funcionalidade, teste, adversarial) [a confirmar, S10].",
  "Papel pesquisa (subagente só de leitura): nada escreve, nem no repositório nem nos cofres; é despachado sem aval do Humano (RN-05) e não conta no teto (RN-13). O modelo padrão e o prompt de papel dele [a confirmar].",
  LA(3) + "; decisão papel-pesquisa")
t("A-03.6", E, "salvo pesquisa só de leitura [a confirmar, S10].", "salvo tarefa do papel pesquisa, que só lê (RN-05).", LA(3))
t("A-03.7", E, "| id de ENT-15 | funcionalidade, teste, adversarial (pesquisa [a confirmar]) | — |",
  "| id de ENT-15 | funcionalidade, teste, adversarial, pesquisa | — |", LA(3) + "; ENT-06")
t("A-03.8", E, "| id de ENT-15 | orquestrador, funcionalidade, teste, adversarial | ação fora do papel: ERR-13, ERR-14 |",
  "| id de ENT-15 | orquestrador, funcionalidade, teste, adversarial, pesquisa | ação fora do papel: ERR-13, ERR-14 |", LA(3) + "; ENT-07")
t("A-03.9", E, "| nome | enumeração | — | sim | — | orquestrador, funcionalidade, teste, adversarial (pesquisa [a confirmar]) | — |",
  "| nome | enumeração | — | sim | — | orquestrador, funcionalidade, teste, adversarial, pesquisa | — |", LA(3) + "; ENT-15")

# A-04 data e hora em UTC
t("A-04.1", E, "Campo marcado \"(RN-xx)\" é citado só pela regra e não está na tabela da fonte.\n",
  "Campo marcado \"(RN-xx)\" é citado só pela regra e não está na tabela da fonte.\n\n"
  "Data e hora: todo campo do tipo \"data e hora\" é guardado no SQLite como texto ISO 8601 em UTC, com `Z` (ex.: `2026-11-19T18:20:00Z`), e mostrado na tela na hora local do Windows.\n",
  LA(4) + "; decisão data-e-hora-em-utc")
t("A-04.2", E, "| aprovado_em | data e hora | — | só se aprovado | [a confirmar] | — | — |",
  "| aprovado_em | data e hora | — | só se aprovado | ISO 8601 UTC | — | — |", LA(4))
t("A-04.3", E, "| registrado_em (RN-03) | data e hora | — | sim antes da próxima delegação | — |",
  "| registrado_em (RN-03) | data e hora | — | sim antes da próxima delegação | ISO 8601 UTC |", LA(4))
t("A-04.4", E, "leitura direta de nota sem autorização: ERR-18 |\n| hora | data e hora | — | sim | — |",
  "leitura direta de nota sem autorização: ERR-18 |\n| hora | data e hora | — | sim | ISO 8601 UTC |", LA(4) + "; ENT-11")
t("A-04.5", E, "| inicio | data e hora | — | sim | — |", "| inicio | data e hora | — | sim | ISO 8601 UTC |", LA(4) + "; ENT-12")
t("A-04.6", E, "| fim | data e hora | — | não (rodando) | — |", "| fim | data e hora | — | não (rodando) | ISO 8601 UTC |", LA(4) + "; ENT-12")
t("A-04.7", E, "| motivo | texto | — | sim | — | — | — |\n| hora | data e hora | — | sim | — |",
  "| motivo | texto | — | sim | — | — | — |\n| hora | data e hora | — | sim | ISO 8601 UTC |", LA(4) + "; ENT-17")
t("A-04.8", E, "| registrada_em | data e hora | — | sim antes da próxima delegação | — |",
  "| registrada_em | data e hora | — | sim antes da próxima delegação | ISO 8601 UTC |", LA(4) + "; ENT-18")

# A-05 ENT-01 Projeto
t("A-05.1", E, "| nome | texto | [a confirmar] | sim [a confirmar] | livre | — | [a confirmar] |",
  "| nome | texto | 1 a 80 caracteres | sim | livre | único entre os projetos | vazio, longo ou repetido: ERR-45 |", LA(5))
t("A-05.2", E, "| repositorio | texto (caminho ou URL) [a confirmar] | — | [a confirmar] | [a confirmar] | — | [a confirmar] |",
  "| repositorio | caminho | — | [a confirmar] | caminho absoluto | pasta com `.git` | inválido: ERR-46 |", LA(5))
t("A-05.3", E, "| limite_contexto_padrao | inteiro (tokens) | > 0 [a confirmar] | sim | só algarismos | padrão 100 mil (S7) | [a confirmar] |",
  "| limite_contexto_padrao | inteiro (tokens) | 10 mil a 1 milhão | sim | só algarismos | padrão 100 mil (S7) | fora da faixa: ERR-47 |", LA(5))
NOVOS_ERR = [
  "| ERR-45 | `PROJETO_NOME_INVALIDO` | nome do projeto vazio, com mais de 80 caracteres ou igual ao de outro projeto (ENT-01) | voltar | [a confirmar] | projeto não salvo |",
  "| ERR-46 | `REPOSITORIO_INVALIDO` | repositório do projeto que não é caminho absoluto de uma pasta com `.git` (ENT-01) | voltar | [a confirmar] | projeto não salvo |",
  "| ERR-47 | `LIMITE_DE_CONTEXTO_FORA_DA_FAIXA` | limite de contexto do projeto ou do chat fora de 10 mil a 1 milhão de tokens (ENT-01, ENT-03; CMP-07) | voltar | [a confirmar] | limite anterior mantido |",
]
ERR44 = "| ERR-44 | `TETO_DE_ESCRITA_ATINGIDO` | 6º subagente que escreve código com 5 rodando (RN-13; UC-04 FA-01) | aguardar | contador \"x de 5 que escrevem\" e a tarefa na fila (CMP-05) | execução `na fila` |\n"
t("A-05.4", ER, ERR44, ERR44 + "\n".join(NOVOS_ERR) + "\n", LA(5) + "; ERR-45 a ERR-47 novos")
t("A-05.5", RA, "| CMP-07 | ENT-01, ENT-03 | — | TEL-01 (prevista) | AC-94 |",
  "| CMP-07 | ENT-01, ENT-03 | ERR-47 | TEL-01 (prevista) | AC-94 |", LA(5) + "; RF-07")
t("A-05.6", RA, "| CMP-09 | ENT-01, ENT-03 | ERR-33 |", "| CMP-09 | ENT-01, ENT-03 | ERR-33, ERR-45, ERR-46, ERR-47 |", LA(5) + "; RF-23")
t("A-05.7", RM, "| Catálogo de erros | ERR-01 a ERR-44 |", "| Catálogo de erros | ERR-01 a ERR-49 |", LA(5) + ", 7, 9: ERR-45 a ERR-49")

# A-06 ENT-02 Cofre e S13
t("A-06.1", E, "| status | enumeração | — | sim | — | conectado, desconectado [a confirmar] | — |",
  "| status | enumeração | — | sim | — | conectado, desconectado | — |", LA(6))
t("A-06.2", R, "| S13 | [a confirmar] Os cofres extras são só de consulta; continua havendo um único cofre onde o orquestrador grava | RN-29, CMP-17 | Confirmação do humano |\n",
  "", LA(6) + "; S13 confirmada (já é RN-29)")
t("A-06.3", RM, "suposições S7 a S9 e S11 a S15", "suposições S7 a S9, S11, S12, S14 e S15", LA(6) + "; S13 removida")

# A-07 ENT-03 Chat
t("A-07.1", E, "| limite_tokens | inteiro | > 0 [a confirmar] | sim | só algarismos | padrão: o do projeto (100 mil, S7) | [a confirmar] |",
  "| limite_tokens | inteiro | 10 mil a 1 milhão | sim | só algarismos | padrão: o do projeto (100 mil, S7) | fora da faixa: ERR-47 |", LA(7))
t("A-07.2", E, "| status | enumeração | — | sim | — | ativo, pausado, encerrado, só leitura [a confirmar] | — |",
  "| status | enumeração | — | sim | — | ativo, pausado, encerrado, só leitura | — |", LA(7))
t("A-07.3", E, "| adiamento_usado | booleano (RN-23) [a confirmar] | — | sim | — | — | segundo adiamento: [a confirmar] |",
  "| adiamento_usado | booleano (RN-23) | — | sim | — | sim, não | segundo adiamento: ERR-48 |", LA(7))
t("A-07.4", E, "| pausado | limite de uso do plano atingido (UC-02 FE-02) | ativo [a confirmar: ao reinício da janela] |",
  "| pausado | limite de uso do plano atingido (UC-02 FE-02) | ativo, no reinício da janela (`resetsAt` do `rate_limit_event`) |", LA(7))
t("A-07.5", E, "| encerrado | passagem de turno concluída (UC-08) | (final; reabre só para leitura [a confirmar]) |",
  "| encerrado | passagem de turno concluída (UC-08) | (final; reabre só para leitura) |", LA(7))
t("A-07.6", E, "| só leitura | cofre do projeto não encontrado ao reabrir (UC-12 FE-01) | ativo [a confirmar] |",
  "| só leitura | cofre do projeto não encontrado ao reabrir (UC-12 FE-01) | ativo, quando o cofre do projeto reaparece |", LA(7))
t("A-07.7", R, "Exceção: o Humano pode adiar uma vez por chat; o adiamento vai ao diário.",
  "Exceção: o Humano pode adiar uma vez por chat; o adiamento vai ao diário, e um segundo adiamento é recusado (ERR-48).", LA(7) + "; RN-23")
t("A-07.8", C, "- **Valida:** `limite_tokens` de ENT-03 [a confirmar: faixa].",
  "- **Valida:** `limite_tokens` de ENT-03 (10 mil a 1 milhão; violação: ERR-47).", LA(7) + "; CMP-07")
t("A-07.9", ER, NOVOS_ERR[2] + "\n", NOVOS_ERR[2] + "\n"
  "| ERR-48 | `ADIAMENTO_JA_USADO` | segundo pedido de adiamento da passagem de turno no mesmo chat (RN-23; ENT-03) | bloquear | [a confirmar] | a passagem de turno segue |\n",
  LA(7) + "; ERR-48 novo")
t("A-07.10", RA, "| CMP-04, CMP-07 | ENT-03, ENT-25 | ERR-07, ERR-29 |", "| CMP-04, CMP-07 | ENT-03, ENT-25 | ERR-07, ERR-29, ERR-48 |", LA(7) + "; RF-20")
t("A-07.11", RA, "| ENT-03 | — (dispara a passagem) |", "| ENT-03 | ERR-48 (segundo adiamento); dispara a passagem |", LA(7) + "; RN-23")

# A-08 ENT-04 Mensagem
t("A-08.1", E, "| autor | enumeração [a confirmar] | — | sim | — | Humano, orquestrador [a confirmar] | — |",
  "| autor | enumeração | — | sim | — | Humano, orquestrador, sistema | — |", LA(8))
t("A-08.2", E, "| texto | texto | [a confirmar] | sim | livre | segredos mascarados (RN-04) | — |",
  "| texto | texto | sem limite próprio | sim | livre | segredos mascarados (RN-04) | vazio: o envio fica bloqueado |", LA(8))
t("A-08.3", E, "| uso_tokens | inteiro | ≥ 0 | [a confirmar] | — | — | — |",
  "| uso_tokens | inteiro | ≥ 0 | sim quando autor = orquestrador | — | — | — |", LA(8))
t("A-08.4", C, "- **Valida:** texto do prompt [a confirmar: tamanho máximo, vazio]; modelo (RN-07).",
  "- **Valida:** texto do prompt (`texto` de ENT-04: sem limite próprio; vazio bloqueia o envio); modelo (RN-07).", LA(8) + "; CMP-06")

# A-09 ENT-06 Tarefa
t("A-09.1", E, "| faz | texto | [a confirmar] | sim | livre | — | [a confirmar] |",
  "| faz | texto | 1 a 500 caracteres | sim | livre | — | vazio ou longo: ERR-49 |", LA(9))
t("A-09.2", E, "| toca_em | lista de caminhos | — | sim [a confirmar] |", "| toca_em | lista de caminhos | — | sim no papel funcionalidade |", LA(9))
t("A-09.3", E, "| pronto_quando | texto | — | sim | livre | — | — |", "| pronto_quando | texto | — | sim | livre | — | vazio: ERR-49 |", LA(9))
t("A-09.4", E, "| prova | texto | — | sim | comando ou evidência | — | — |", "| prova | texto | — | sim | comando ou evidência | — | vazio: ERR-49 |", LA(9))
t("A-09.5", E, "| implementada_por (RN-09) | referência | — | [a confirmar] |", "| implementada_por (RN-09) | referência | — | sim, preenchido no despacho da implementação |", LA(9))
t("A-09.6", E, "| testada_por (RN-09) | referência | — | [a confirmar] |", "| testada_por (RN-09) | referência | — | sim, preenchido no despacho do teste |", LA(9))
t("A-09.7", ER, "| a passagem de turno segue |\n", "| a passagem de turno segue |\n"
  "| ERR-49 | `TAREFA_INCOMPLETA` | tarefa do plano com `faz` vazio ou acima de 500 caracteres, ou com `pronto_quando` ou `prova` vazios (ENT-06) (agente) | bloquear | [a confirmar] | [a confirmar] |\n",
  LA(9) + "; ERR-49 novo")
t("A-09.8", RA, "| ENT-05, ENT-06 | ERR-09, ERR-12 |", "| ENT-05, ENT-06 | ERR-09, ERR-12, ERR-49 |", LA(9) + "; RF-08")

# A-10 ENT-07 Execução
t("A-10.1", E, "| tarefa | referência | — | sim (salvo orquestrador [a confirmar]) | id de ENT-06 | — | — |",
  "| chat | referência | — | sim | id de ENT-03 | — | — |\n"
  "| tarefa | referência | — | sim (não para o orquestrador) | id de ENT-06 | — | — |", LA(10))
t("A-10.2", E, "| status | enumeração | — | sim | — | na fila, rodando, concluido, falhou, interrompida | — |",
  "| status | enumeração | — | sim | — | na fila, rodando, concluido, falhou, interrompida | — |\n"
  "| motivo_fila | enumeração | — | sim quando status = na fila | — | teto, toca_em, recurso | — |", LA(10))
t("A-10.3", E, "| na fila | teto atingido (RN-13), espera de \"toca em\" (RN-14) ou de recurso (RN-15) [a confirmar: \"aguardando recurso\" é estado próprio?] | rodando |",
  "| na fila | teto atingido (RN-13), espera de \"toca em\" (RN-14) ou de recurso (RN-15), com o motivo em `motivo_fila` | rodando |", LA(10))
t("A-10.4", E, "| interrompida | o app fecha durante a execução (RNF-08) | [a confirmar] |",
  "| interrompida | o app fecha durante a execução (RNF-08) | (final) |", LA(10))
t("A-10.5", E, "- Toda ação relevante tem quem, o quê, quando e de qual chat (RNF-09) [a confirmar: o Log tem \"chat\"?].",
  "- Toda ação relevante tem quem, o quê, quando e de qual chat (RNF-09); o chat vem de `execucao.chat` (ENT-07).", LA(10) + "; inferência: Execução.chat responde à dúvida do Log")

# A-11 ENT-09 e ENT-10
t("A-11.1", E, "| resultado | enumeração [a confirmar] | — | sim | — | concluído, falhou, bloqueado [a confirmar] | — |",
  "| resultado | enumeração | — | sim | — | concluído, falhou, bloqueado | — |", LA(11))
t("A-11.2", E, "| criterios | lista de ENT-24 | — | [a confirmar] |", "| criterios | lista de ENT-24 | — | sim no papel teste |", LA(11))
t("A-11.3", E, "| passos | texto | — | sim | lista numerada [a confirmar] | — | [a confirmar] |",
  "| passos | lista de texto | 1 passo ou mais | sim | lista numerada | — | [a confirmar] |", LA(11))
t("A-11.4", E, "| captura | arquivo | — | sim para adversarial [a confirmar] |", "| captura | arquivo | — | sim para adversarial |", LA(11))
t("A-11.5", E, "| status (RN-20) | enumeração [a confirmar] | — | sim | — | aberto, fechado [a confirmar] | — |",
  "| status (RN-20) | enumeração | — | sim | — | aberto, fechado | — |", LA(11))

# A-12 códigos e "aguardar"
t("A-12.1", ER, "Os códigos são proposta deste rascunho, derivados das RN e dos FE [a confirmar].",
  "Os códigos, derivados das RN, dos FE e dos campos das entidades, estão aprovados pelo Humano.", LA(12))
t("A-12.2", ER, "- **aguardar** [a confirmar: tratamento novo, não está no modelo]:", "- **aguardar:**", LA(12))

(AQUI / "trocas.json").write_text(json.dumps(T, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(len(T), "trocas gravadas")
