# Critérios de aceite (AC)

Um critério por fluxo (principal, alternativo e exceção), no formato dado / quando / então. Ao final de cada funcionalidade, o verificador de fluxo principal executa os AC dos fluxos principais e, depois, o adversarial executa os dos FA e FE: no backend pela API e, se a funcionalidade tem interface, também no frontend.

| ID | UC | Fluxo | Dado | Quando | Então |
|---|---|---|---|---|---|
| AC-01 | UC-01 | principal | um cliente que entrou e uma sala ativa livre amanhã às 10h | ele reserva essa sala para amanhã das 10h às 11h, com 4 pessoas | a reserva aparece em `pendente` na lista dele |
| AC-02 | UC-01 | FA-01 | o mesmo cliente e a mesma sala livre nas próximas 4 semanas | ele reserva com "repetir toda semana" por 4 semanas | 4 reservas em `pendente`, uma por semana |
| AC-03 | UC-01 | FE-01 | a sala já reservada amanhã às 10h | outro cliente tenta reservá-la às 10h30 | aparece a mensagem de ERR-01 e nada é gravado |
| AC-04 | UC-01 | FE-02 | o formulário de reserva aberto | o cliente digita "dez" em pessoas | o campo não aceita letras; pela API, a resposta é ERR-03 |
