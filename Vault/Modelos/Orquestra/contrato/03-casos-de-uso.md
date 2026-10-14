# Casos de uso (UC)

Um caso de uso por objetivo do ator. O fluxo principal vem em passos numerados (ator → sistema). Fluxo alternativo (FA) é outro caminho válido; fluxo de exceção (FE) termina num erro do catálogo (`05-erros.md`).

## UC-01 Criar reserva

- **Ator:** ATR-02
- **Objetivo:** reservar uma sala para um horário.
- **Requisitos:** RF-01, RN-01
- **Pré-condições:** o cliente entrou; existe ao menos uma sala ativa.
- **Pós-condições:** reserva em `pendente`, visível na lista do cliente.

### Fluxo principal

1. Ator escolhe "Nova reserva".
2. Sistema mostra o formulário com as salas ativas.
3. Ator escolhe sala, início e número de pessoas e confirma.
4. Sistema valida os campos (ENT-01) e a sobreposição (RN-01).
5. Sistema grava a reserva em `pendente` e mostra a confirmação.

### Fluxos alternativos (FA)

| ID | Passo de origem | Variação | Volta ou termina |
|---|---|---|---|
| FA-01 | 3 | Ator marca "repetir toda semana" por 4 semanas | Volta ao passo 4, uma vez por data |

### Fluxos de exceção (FE)

| ID | Passo de origem | Erro | Estado final |
|---|---|---|---|
| FE-01 | 4 | ERR-01 | Nada gravado; o formulário mantém os dados |
| FE-02 | 4 | ERR-03 | Nada gravado; o campo `pessoas` fica destacado |
