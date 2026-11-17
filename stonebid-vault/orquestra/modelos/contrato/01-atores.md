# Atores e perfis (ATR)

Quem interage com o sistema e o que cada perfil pode fazer. A permissão é checada no servidor; a tela só esconde o que o perfil não pode.

| ID | Ator | Quem é | Pode | Não pode |
|---|---|---|---|---|
| ATR-01 | Visitante | Ainda não entrou | Ver as salas | Reservar |
| ATR-02 | Cliente | Entrou com conta própria | Criar e cancelar as próprias reservas | Ver reservas de outros |
| ATR-03 | Administrador | Gerencia o sistema | Tudo do cliente; cadastrar salas | — |

## Matriz de permissões

| Ação | ATR-01 | ATR-02 | ATR-03 |
|---|---|---|---|
| Ver salas | sim | sim | sim |
| Criar reserva | não | sim | sim |
| Cadastrar sala | não | não | sim |
