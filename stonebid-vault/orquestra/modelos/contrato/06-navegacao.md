# Estados e navegação (NAV)

Só para funcionalidade com interface. Cada transição diz de onde, com que evento, sob que condição e para onde. Os estados são lógicos; o mapa para telas vem depois, na última coluna.

| ID | Origem | Evento | Condição | Destino | Tela (preencher depois) |
|---|---|---|---|---|---|
| NAV-01 | lista-de-reservas | escolheu "Nova reserva" | perfil ATR-02 ou ATR-03 | formulario-de-reserva | |
| NAV-02 | formulario-de-reserva | servidor confirmou (UC-01, passo 5) | — | reserva-criada | |
| NAV-03 | qualquer estado protegido | abriu pela URL sem ter entrado | — | entrar; depois, volta à URL pedida | |

## Estado inicial

Aberto direto pela URL, cada estado já mostra o que precisa, sem clique prévio.

| Estado | Mostra ao abrir |
|---|---|
| lista-de-reservas | menu principal, "Nova reserva" (se o perfil pode) e as reservas do cliente |
| formulario-de-reserva | menu principal e o formulário no estado `vazio` de CMP-01 |
