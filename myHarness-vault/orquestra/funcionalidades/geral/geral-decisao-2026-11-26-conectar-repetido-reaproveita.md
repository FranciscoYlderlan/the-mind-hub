---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-26
substitui: 
---
# ✅ Conectar repetido reaproveita a conexão em andamento

- **Proposta (plano):** adversarial da `integracoes` em 2026-11-26 ([[bug-conectar-repetido-abre-segundo-fluxo-2026-11-26]]) e as opções do orquestrador às 13h05.
- **Decisão:** o núcleo guarda a operação em andamento por integração. "Conectar" pedido de novo com a conexão em andamento devolve a mesma instrução (código do device flow ou `/login`) e não abre outro fluxo; o status final é o do fluxo em andamento (UC-01 FA-02, AC-157). "Desconectar" durante o login cancela o login, e o estado devolvido é o mesmo que o núcleo guarda (B2).
- **Alteração:** nenhuma
- **Motivo:** aval do humano em 2026-11-26, 13h10: reaproveitar (recomendado), corrigir o B2 junto e incluir os dois opcionais da tela.
- **Consequências:** contrato M-49 (texto do AC-03) e M-50 (FA-02 e AC-157), já aplicados. Tarefa T7 do [[integracoes-plano]]: guarda no núcleo (GitHub e Claude CLI), B2, zod nas respostas de comando da tela e duplo clique em "Repetir". Depois, verificador de fluxo principal e os dois adversariais de novo ([[geral-decisao-2026-11-26-adversarial-em-dois]]).

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[integracoes-plano]]
- Bug: [[bug-conectar-repetido-abre-segundo-fluxo-2026-11-26]]
- Projeto: [[geral-contexto]]
- Regras: [[manual-da-orquestra]]
