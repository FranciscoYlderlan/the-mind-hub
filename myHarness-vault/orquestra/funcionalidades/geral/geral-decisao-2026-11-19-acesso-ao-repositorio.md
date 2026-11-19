---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-19
substitui: 
---
# ✅ Agente com acesso à pasta do repositório

- **Proposta (plano):** ponto de acesso da [[geral-decisao-2026-11-19-repositorio-e-ambiente]], que previa entrega por arquivo.
- **Decisão:** o agente **sempre tem acesso** à pasta `C:\Users\Ylderlan\Documents\Projetos\my-harness` e escreve direto nela. Implementa e testa na própria máquina virtual; o WSL fica só para quando o humano rodar o projeto por conta própria.
- **Alteração:** nenhuma
- **Motivo:** resposta do humano em 2026-11-19: "Sempre é você tendo acesso a pasta".
- **Consequências:** a sessão pede a pasta pelo `device_request_folder_access` quando ela não estiver conectada; não há mais entrega por arquivo. Ações irreversíveis na pasta (apagar, sobrescrever o que não se recupera, `--force`, branch principal) seguem pedindo confirmação.

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Decisão de origem: [[geral-decisao-2026-11-19-repositorio-e-ambiente]]
- Regras: [[manual-da-orquestra]]
