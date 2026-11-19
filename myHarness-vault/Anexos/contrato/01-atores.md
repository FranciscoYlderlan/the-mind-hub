# Atores e perfis (ATR)

Quem interage com o sistema e o que cada perfil pode fazer. A permissão é checada no servidor; a tela só esconde o que o perfil não pode.

No MyHarness não há login no app (D4: uma pessoa, no próprio computador). "Servidor" aqui é o núcleo Rust: as permissões são entre papéis de agente e quem as impõe é o núcleo, nunca o texto do prompt (RN-27, RNF-06).

| ID | Ator | Quem é | Pode | Não pode |
|---|---|---|---|---|
| ATR-01 | Humano | Validador final e dono do MyHarness; usuário único, com permissão total nas telas (D4) | Conversar com o orquestrador; aprovar, alterar ou recusar o plano; trocar modelos; decidir achados; fazer o merge no GitHub; editar prompts de papel; ligar cofres; adiar a passagem de turno uma vez por chat; dispensar prova (RN-18); registrar exceção de conclusão (RN-20); autorizar leitura sem CLI (RN-02); escrever direto no Obsidian e alterar o contrato, fora do MyHarness (RN-01, D14) | — |
| ATR-02 | Orquestrador | Sessão principal do Claude CLI | Buscar e ler no cofre pela Obsidian CLI; propor plano de delegação; despachar subagentes após o aval; gravar no cofre de memória (relatórios, decisões aprovadas, "Onde parei"); alterar o contrato em `Anexos/contrato/` (RN-01, D14); falar com o Humano | Despachar sem aval (RN-05); registrar decisão sem aval (RN-06); delegar com relatório não registrado (RN-03); gravar em cofre de consulta (RN-29); ler .md direto (RN-02); implementar (prompt de papel de fábrica) |
| ATR-03 | Subagente de funcionalidade | Processo do Claude CLI que implementa uma tarefa | Trabalhar na própria worktree e branch (RN-16); tocar os arquivos da tarefa; commitar na worktree (o push e o PR são do núcleo, RF-27); ler o cofre pela CLI; devolver relatório com dúvidas | Escrever em cofre algum ou no contrato (RN-01, D14); perguntar ao Humano (RN-12); push, merge, push --force (RN-17); testar a própria funcionalidade (RN-09) |
| ATR-04 | Subagente de teste | Processo do Claude CLI que testa uma funcionalidade que não construiu | Rodar as provas; marcar ✔/✘ por critério com prova; registrar bugs com passos, esperado e obtido | Testar o que implementou (RN-09); marcar ✔ sem prova (RN-18); corrigir código (prompt de fábrica); escrever em cofre algum ou no contrato (RN-01, D14); perguntar ao Humano (RN-12) |
| ATR-05 | Agente adversarial | Processo do Claude CLI sem contexto, que usa a aplicação pela tela | Usar a aplicação pelo Claude in Chrome com objetivo, endereço e acesso de teste; relatar achados tipados (bug ou sugestão) com passos e captura | Receber conversa, plano, código ou notas (RN-10); rodar antes do fim da rodada (RN-11); usar o navegador ao mesmo tempo que outro agente (RN-15); escrever em cofre algum ou no contrato (RN-01, D14) |
| ATR-06 | Claude CLI | Sistema externo: executa orquestrador e subagentes, cada um num processo `claude -p` (D8) | Fornecer processos, eventos de resposta e uso de tokens; login próprio pelo `/login` (D10), com falha de autenticação devolvida como `authentication_failed` (ERR-04) | — |
| ATR-07 | Obsidian CLI | Sistema externo local, acessado pelo servidor MCP da Obsidian CLI; exige o Obsidian aberto (D10) | Buscar e ler notas; listar cofres | — |
| ATR-08 | GitHub | Sistema externo, autenticado pelo app OAuth próprio do MyHarness, com device flow (RF-03, D10) | Receber push, abrir PR, registrar merge feito pelo Humano | — |
| ATR-09 | Claude in Chrome | Sistema externo: navegador usado pelo adversarial, que roda em `claude -p --chrome`, disponível com `--strict-mcp-config` (D11) | Abrir a aplicação no endereço de teste; recurso exclusivo (RN-15) | — |

Papel pesquisa (subagente só de leitura): nada escreve, nem no repositório nem nos cofres; é despachado sem aval do Humano (RN-05) e não conta no teto (RN-13). O modelo padrão e o prompt de papel dele [a confirmar].

## Matriz de permissões

| Ação | ATR-01 | ATR-02 | ATR-03 | ATR-04 | ATR-05 |
|---|---|---|---|---|---|
| Ler nota do cofre pela Obsidian CLI | sim (no Obsidian) | sim | sim | sim [a confirmar] | não (RN-10) |
| Ler .md do cofre direto | sim (fora do MyHarness) | só com RN-02, exceção autorizada | só com RN-02, exceção autorizada | só com RN-02, exceção autorizada | não |
| Gravar no cofre de memória | sim (fora do MyHarness) | sim | não | não | não |
| Gravar em cofre de consulta | sim (fora do MyHarness) | não | não | não | não |
| Alterar `Anexos/contrato/` | sim (fora do MyHarness) | sim | não | não | não |
| Aprovar plano de delegação | sim | não | não | não | não |
| Despachar subagente | não (aprova) | sim, após aval | não | não | não |
| Escrever código na worktree | não | não | sim | não | não |
| Push e abrir PR | sim (no GitHub) | não | não (o núcleo faz, RF-27) | não | não |
| Merge, push --force, push na principal | sim (no GitHub) | não | não | não | não |
| Marcar critério ✔/✘ | dispensa prova (RN-18) | não | não | sim | não |
| Relatar achado tipado | não | não | não | sim (bug) | sim |
| Decidir sugestão (corrigir, limite, opcional) | sim | não | não | não | não |
| Falar com o Humano | — | sim | não (RN-12) | não (RN-12) | não (RN-12) |
| Editar prompt de papel, modelos, cofres | sim | não | não | não | não |
| Usar o navegador do Claude in Chrome | — | não [a confirmar] | não [a confirmar] | sim, um por vez (RN-15) | sim, um por vez (RN-15) |
