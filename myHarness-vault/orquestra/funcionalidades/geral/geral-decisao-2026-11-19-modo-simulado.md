---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-19
substitui: 
---
# ✅ Modo simulado fica como ferramenta de desenvolvimento

- **Proposta (plano):** [[geral-plano-arquitetura-e-stack-integracoes-e-testes-prototipos]] (P3, parte a).
- **Decisão:** o núcleo falso `src/dev/nucleo-simulado.ts` e o script `dev:simulado` ficam no projeto a partir da etapa 2: a tela roda no navegador com respostas prontas, sem Claude CLI e sem gastar a cota do plano. Só no modo de desenvolvimento; não entra no app instalado.
- **Alteração:** em 2026-11-26 (12h39) o verificador de fluxo principal da `integracoes` achou a `main` sem o `src/dev/nucleo-simulado.ts` e sem o `dev:simulado`; o núcleo simulado estava só em `src/lib/ipc/nucleo-simulado-integracoes.ts`, usado pelos testes. O humano decidiu trazer os dois de volta ao repositório, para a tela rodar no navegador sem harness externo. Aplicação: tarefa T6 do [[integracoes-plano]], num chat novo, depois do adversarial.
- **Motivo:** o P3(a) passou com ele (14 de 14); testar a tela não deve custar cota. Aval do humano em 2026-11-19, sessão das 16h23.
- **Consequências:** toda mudança no contrato IPC (G1) atualiza também o núcleo simulado, para a tela não testar contra um contrato velho. O cenário vem pela URL ([[geral-decisao-2026-11-26-cenarios-do-modo-simulado]]).

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[geral-plano]], [[integracoes-plano]] (T6, T9)
- Ponto acrescentado: [[geral-decisao-2026-11-26-cenarios-do-modo-simulado]]
- Regras: [[manual-da-orquestra]]
