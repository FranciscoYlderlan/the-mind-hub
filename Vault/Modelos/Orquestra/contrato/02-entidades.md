# Modelo de dados e invariantes (ENT)

As validações pertencem à entidade, não à tela: toda tela que mostra ou edita o campo herda as regras daqui. No backend, a entidade é o domínio; no frontend, o schema do campo sai desta tabela. Cada violação tem o seu erro, para a mensagem dizer o que está errado.

## ENT-01 Reserva

### Campos

| Campo | Tipo | Tamanho ou faixa | Obrigatório | Formato | Valores permitidos | Erro por violação |
|---|---|---|---|---|---|---|
| sala | referência | — | sim | id de sala | só sala ativa | inativa: ERR-05 |
| inicio | data e hora | a partir de agora | sim | AAAA-MM-DD HH:mm | — | no passado: ERR-02 |
| pessoas | inteiro | 1 a 20 | sim | só algarismos | — | não numérico: ERR-03; fora da faixa: ERR-04 |
| observacao | texto | até 200 caracteres | não | livre | — | — |

### Invariantes (nunca violadas, em nenhum fluxo)

- O fim é depois do início.
- A mesma sala não tem duas reservas que se sobrepõem (RN-01; violação: ERR-01).

### Estados do ciclo de vida

| Estado | Entra quando | Pode ir para |
|---|---|---|
| pendente | a reserva é criada | confirmada, cancelada |
| confirmada | o pagamento é aprovado | cancelada, concluida |
| cancelada | o cliente ou o sistema cancela | (final) |
| concluida | o horário termina | (final) |
