# Catálogo de erros (ERR)

Um erro por condição. O código do ERR é o código de erro que o servidor devolve; o frontend mostra a mensagem daqui. Fluxo de exceção (FE) só referencia um ERR. Duas condições diferentes nunca dividem a mesma mensagem.

| ID | Código no servidor | Condição de disparo | Tratamento | Mensagem ao usuário | Estado final |
|---|---|---|---|---|---|
| ERR-01 | `RESERVA_SOBREPOSTA` | a sala já tem reserva que se sobrepõe ao horário | voltar | Essa sala já está reservada nesse horário. Escolha outro. | nada gravado; dados mantidos |
| ERR-02 | `INICIO_NO_PASSADO` | o início é anterior a agora | bloquear | Escolha um início a partir de agora. | campo destacado |
| ERR-03 | `PESSOAS_NAO_NUMERICO` | `pessoas` não é um número inteiro | bloquear | Informe o número de pessoas só com algarismos. | campo destacado |
| ERR-04 | `PESSOAS_FORA_DA_FAIXA` | `pessoas` fora de 1 a 20 | bloquear | A sala comporta de 1 a 20 pessoas. | campo destacado |
| ERR-05 | `SALA_INATIVA` | a sala escolhida não está ativa | voltar | Essa sala não está disponível. Escolha outra. | nada gravado; lista de salas recarregada |

## Tratamentos

- **repetir:** falha passageira (rede, servidor ocupado); o usuário pode tentar de novo.
- **voltar:** o usuário corrige e reenvia.
- **bloquear:** não segue até corrigir; quando der, o próprio campo impede o valor (ex.: só aceita algarismos).
