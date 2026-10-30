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
- **Alteração:** nenhuma
- **Motivo:** o P3(a) passou com ele (14 de 14); testar a tela não deve custar cota. Aval do humano em 2026-11-19, sessão das 16h23.
- **Consequências:** toda mudança no contrato IPC (G1) atualiza também o núcleo simulado, para a tela não testar contra um contrato velho.

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[geral-plano]]
- Regras: [[manual-da-orquestra]]
