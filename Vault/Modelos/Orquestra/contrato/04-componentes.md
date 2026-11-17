# Componentes lógicos (CMP)

Só para funcionalidade com interface. Descreve o papel do componente, não a aparência. A tela escolhe o visual; o comportamento vem daqui.

## CMP-01 Formulário de reserva

- **Papel:** coletar os dados de uma reserva nova e enviá-los ao servidor.
- **Entradas:** salas ativas; reserva em edição (opcional).
- **Saídas:** reserva criada (ENT-01) ou erro (ERR-xx).
- **Eventos:** `alterou-campo`, `confirmou`, `cancelou`.
- **Atende:** UC-01 (passos 1 a 5, FA-01, FE-01, FE-02).
- **Valida:** `sala`, `inicio`, `pessoas` e `observacao` de ENT-01.

### Estados obrigatórios

| Estado | O que o usuário vê | Ações possíveis |
|---|---|---|
| vazio | formulário sem dados; confirmar desabilitado | preencher |
| carregando | indicação de envio; campos travados | nenhuma (duplo clique não reenvia) |
| preenchido | dados válidos; confirmar habilitado | confirmar, cancelar |
| erro | a mensagem do ERR junto ao campo ou no topo | corrigir, repetir |
| sucesso | confirmação com o resumo da reserva | ir para a lista |
| desabilitado | o motivo (perfil sem permissão, nenhuma sala ativa) | nenhuma |
