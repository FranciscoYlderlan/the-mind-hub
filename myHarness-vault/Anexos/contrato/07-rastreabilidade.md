# Mapa de rastreabilidade

Uma linha por requisito. Célula vazia é lacuna: requisito sem UC, fluxo sem componente ou UC sem cenário de teste. A coluna Tela só é preenchida quando a tela existe (só com interface). O cenário de teste é o critério de aceite (AC-xx) que prova a linha.

Nenhuma tela existe ainda. A coluna Tela traz a tela prevista na fonte (TEL-xx), para fechar o RF ↔ TEL pedido; ela deve ser revista quando a tela existir. "—" é ausência confirmada na fonte (ex.: RF de necessidade do negócio, sem UC); `[lacuna]` é ausência a resolver. Fluxos citados são do UC da mesma linha.

## Requisitos funcionais

| Requisito | UC | Fluxos | CMP | ENT | ERR | Tela (preencher depois) | Cenário de teste (AC-xx) |
|---|---|---|---|---|---|---|---|
| RF-01 | UC-01 | principal, FA-01, FE-01 | CMP-03, CMP-11 | ENT-13 | ERR-01, ERR-04 | TEL-01, TEL-02 (previstas) | AC-01, AC-02, AC-03, AC-88 |
| RF-02 | UC-01 | principal, FE-03 | CMP-03, CMP-11 | ENT-13, ENT-02 | ERR-03 | TEL-01, TEL-02 (previstas) | AC-05, AC-89, AC-128 |
| RF-03 | UC-01 | principal, FE-02 | CMP-03, CMP-11 | ENT-13 | ERR-02 | TEL-01, TEL-02 (previstas) | AC-01, AC-04, AC-90, AC-127, AC-129 |
| RF-04 | UC-01 | principal | CMP-03 | ENT-13 | ERR-05, ERR-06, ERR-07 | TEL-01 (prevista) | AC-91 |
| RF-05 | UC-02 | principal, FE-01, FE-02 | CMP-04, CMP-06 | ENT-03, ENT-04 | ERR-05, ERR-08, ERR-42 | TEL-01 (prevista) | AC-06, AC-09, AC-10, AC-92, AC-122 |
| RF-06 | UC-04 | principal | CMP-04 | ENT-07 | ERR-17 | TEL-01 (prevista) | AC-93 |
| RF-07 | UC-02 | principal | CMP-07 | ENT-01, ENT-03 | — | TEL-01 (prevista) | AC-94 |
| RF-08 | UC-03 | principal, FE-01 | CMP-10, CMP-12 | ENT-05, ENT-06 | ERR-09, ERR-12 | TEL-01, TEL-03 (previstas) | AC-07, AC-14, AC-95 |
| RF-09 | UC-03 | principal, FA-01, FA-02, FE-02 | CMP-12, CMP-13 | ENT-05, ENT-06, ENT-18 | ERR-06, ERR-10, ERR-11 | TEL-03 (prevista) | AC-11, AC-12, AC-13, AC-15, AC-96, AC-130, AC-131, AC-132, AC-133 |
| RF-10 | UC-04 | principal, FA-01, FE-02 | CMP-04, CMP-05 | ENT-06, ENT-07, ENT-15 | ERR-09, ERR-11, ERR-12, ERR-13, ERR-16, ERR-44 | TEL-01 (prevista) | AC-16, AC-17, AC-97 |
| RF-11 | UC-04 | principal, FA-02, FE-01 | CMP-04, CMP-05, CMP-10 | ENT-09 | ERR-15, ERR-17 | TEL-01 (prevista) | AC-16, AC-18, AC-19, AC-98 |
| RF-12 | UC-04 | principal, FA-01 | CMP-05 | ENT-07 | ERR-44 | TEL-01 (prevista) | AC-99, AC-123, AC-126 |
| RF-13 | UC-09 | principal, FA-01, FE-01 | CMP-14 | ENT-15 | ERR-11, ERR-30 | TEL-04 (prevista) | AC-36, AC-37, AC-38, AC-100, AC-134, AC-135, AC-136 |
| RF-14 | UC-11 | principal | CMP-02 | ENT-11 | ERR-18 | TEL-01 (prevista) | AC-101 |
| RF-15 | UC-11 | principal | CMP-02 | ENT-11, ENT-02 | ERR-40 | TEL-01 (prevista) | AC-102 |
| RF-16 | UC-11 | principal, FA-01, FE-01 | CMP-02 | [lacuna: nenhuma entidade guarda as pastas em contexto] | ERR-32 | TEL-01 (prevista) | AC-42, AC-43, AC-44, AC-103 |
| RF-17 | UC-08 | principal | CMP-07 | ENT-03 | — | TEL-01 (prevista) | AC-104 |
| RF-18 | — (necessidade do negócio) | — | CMP-01 | ENT-14 | ERR-41 | TEL-01 (prevista) | AC-105 |
| RF-19 | — (necessidade do negócio) | — | CMP-01, CMP-07 | ENT-14, ENT-03 | ERR-41 | TEL-01 (prevista; visível em todas) | AC-106 |
| RF-20 | UC-08 | principal, FA-01, FE-01, FE-02 | CMP-04, CMP-07 | ENT-03, ENT-25 | ERR-07, ERR-29 | TEL-01 (prevista) | AC-32, AC-33, AC-34, AC-35, AC-107, AC-124 |
| RF-21 | — (necessidade do negócio) | — | CMP-08 | ENT-12 | — | TEL-01 (prevista) | AC-108 |
| RF-22 | — (necessidade do negócio) | — | CMP-08 | ENT-12 | — | TEL-01 (prevista) | AC-109 |
| RF-23 | UC-12 | principal, FA-01, FE-01 | CMP-09 | ENT-01, ENT-03 | ERR-33 | TEL-01 (prevista) | AC-45, AC-46, AC-47, AC-110 |
| RF-24 | UC-05 | principal, FA-01, FE-01, FE-02 | CMP-10, CMP-15 | ENT-06, ENT-10, ENT-21, ENT-24 | ERR-19, ERR-20, ERR-21, ERR-22 | TEL-01, TEL-05 (previstas) | AC-21, AC-22, AC-23, AC-24, AC-111 |
| RF-25 | UC-06 | principal, FA-01, FE-01, FE-02 | CMP-10, CMP-15 | ENT-10, ENT-16, ENT-19, ENT-20 | ERR-23, ERR-24, ERR-25, ERR-26, ERR-27 | TEL-01, TEL-05 (previstas) | AC-25, AC-26, AC-27, AC-28, AC-112 |
| RF-26 | UC-07 | principal, FA-01, FE-01 | CMP-15 | ENT-10 | ERR-28, ERR-43 | TEL-05 (prevista) | AC-29, AC-30, AC-31, AC-113, AC-137, AC-138, AC-139 |
| RF-27 | UC-10 | principal, FA-01, FE-01 | [lacuna: nenhum CMP lista os PRs nem a ordem sugerida] | ENT-07, ENT-23 | ERR-06, ERR-14, ERR-16, ERR-31 | TEL-01 (prevista) [a confirmar] | AC-39, AC-40, AC-41, AC-114 |
| RF-28 | UC-04 | principal | — (backend) | ENT-09, ENT-17, ENT-18 | ERR-13, ERR-15, ERR-39 | — | AC-16, AC-115 |
| RF-29 | — (necessidade do negócio) | — | — (backend) | ENT-15, ENT-19 | ERR-13, ERR-23 | — | AC-116 |
| RF-30 | UC-02 | principal, FE-01 | CMP-06 | ENT-04 | ERR-05, ERR-42 | TEL-01 (prevista) | AC-117, AC-125 |
| RF-31 | UC-13 | principal, FA-01, FA-02, FE-01, FE-02 | CMP-16 | ENT-08 | ERR-34, ERR-35 | TEL-06 (prevista) | AC-48, AC-49, AC-50, AC-51, AC-52, AC-118, AC-140, AC-141, AC-142 |
| RF-32 | — (necessidade do negócio) | — | CMP-08 (log "prompt de papel vN") | ENT-07, ENT-08 | ERR-36 | TEL-01 (prevista) | AC-119 |
| RF-33 | UC-14 | principal, FA-01, FA-02, FE-01, FE-02 | CMP-17 | ENT-02 | ERR-37, ERR-38 | TEL-06 (prevista) | AC-53, AC-54, AC-55, AC-56, AC-57, AC-120, AC-143 |
| RF-34 | UC-14 | principal, FA-02 | CMP-02, CMP-17 | ENT-02, ENT-11 | ERR-40 | TEL-01, TEL-06 (previstas) | AC-53, AC-55, AC-121 |

## Regras de negócio

| Requisito | UC | Fluxos | CMP | ENT | ERR | Tela (preencher depois) | Cenário de teste (AC-xx) |
|---|---|---|---|---|---|---|---|
| RN-01 | UC-04 | FE-02 | CMP-08 | ENT-07, ENT-17 | ERR-13 | TEL-01 (prevista) | AC-58, AC-116 |
| RN-02 | UC-02, UC-11, UC-12, UC-14 | UC-02 passo 2; UC-11 principal | CMP-02 | ENT-11, ENT-13 | ERR-18 | TEL-01 (prevista) | AC-59 |
| RN-03 | UC-04 | principal (passo 4) | CMP-08 | ENT-09, ENT-18 | ERR-15 | TEL-01 (prevista) | AC-60 |
| RN-04 | UC-01 | principal | CMP-08, CMP-11 | ENT-04, ENT-12, ENT-13 | — (mascarar) | TEL-01, TEL-02 (previstas) | AC-61 |
| RN-05 | UC-03 | principal | CMP-10, CMP-13 | ENT-05 | ERR-09 | TEL-03 (prevista) | AC-11, AC-62 |
| RN-06 | UC-03 | principal | CMP-13 | ENT-18 | ERR-10 | TEL-03 (prevista) | AC-63 |
| RN-07 | UC-02, UC-03, UC-09 | principal | CMP-06, CMP-12, CMP-14 | ENT-06, ENT-15 | ERR-11 | TEL-01, TEL-03, TEL-04 (previstas) | AC-64 |
| RN-08 | UC-01, UC-02, UC-03, UC-10, UC-14 | UC-02 FE-01; UC-03 FE-02; UC-08 FE-02 | CMP-03, CMP-06, CMP-11, CMP-13 | ENT-13 | ERR-05, ERR-06, ERR-07 | TEL-01, TEL-02, TEL-03 (previstas) | AC-09, AC-15, AC-65 |
| RN-09 | UC-05 | principal (passo 1) | CMP-04 | ENT-06, ENT-07 | ERR-19 | TEL-01 (prevista) | AC-66 |
| RN-10 | UC-06 | principal (passo 1) | CMP-04 | ENT-07, ENT-19 | ERR-23 | TEL-01 (prevista) | AC-67 |
| RN-11 | UC-06 | gatilho | [lacuna: nenhum CMP mostra a rodada nem o bloqueio] | ENT-20, ENT-21 | ERR-24 | — | AC-68 |
| RN-12 | UC-04 | FA-02 | CMP-04, CMP-10 | ENT-09 | — (converter em dúvida) | TEL-01 (prevista) | AC-18, AC-69 |
| RN-13 | UC-04 | FA-01 | CMP-05 | ENT-07, ENT-22 | ERR-44 | TEL-01 (prevista) | AC-17, AC-70 |
| RN-14 | UC-03, UC-04 | UC-03 FE-01 | CMP-12 | ENT-06 | ERR-12 | TEL-03 (prevista) | AC-14, AC-71 |
| RN-15 | UC-05, UC-06 | UC-06 FE-01 | [lacuna: espera de recurso sem CMP] | ENT-16 | ERR-25 | — | AC-27, AC-72 |
| RN-16 | UC-04 | principal (passo 1) | — (backend) | ENT-07 | ERR-16 | — | AC-73 |
| RN-17 | UC-04, UC-10 | UC-04 FE-02; UC-10 principal | CMP-08 | ENT-07, ENT-23 | ERR-14 | TEL-01 (prevista) | AC-20, AC-74 |
| RN-18 | UC-05 | FE-02 | CMP-15 [a confirmar] | ENT-24 | ERR-20 | TEL-05 (prevista) | AC-24, AC-75 |
| RN-19 | UC-05 | FE-01 | CMP-10 | ENT-06 | ERR-21 | TEL-01 (prevista) | AC-23, AC-76 |
| RN-20 | UC-05, UC-07 | UC-05 principal | CMP-15 | ENT-10, ENT-21 | ERR-22 | TEL-05 (prevista) | AC-21, AC-77 |
| RN-21 | UC-06, UC-07 | UC-06 principal (passo 3) | CMP-15 | ENT-10 | ERR-27 | TEL-05 (prevista) | AC-25, AC-78 |
| RN-22 | UC-07 | principal, FE-01 | CMP-10, CMP-15 | ENT-10 | ERR-28 | TEL-05 (prevista) | AC-31, AC-79 |
| RN-23 | UC-02, UC-08 | UC-02 FA-02; UC-08 principal, FA-01 | CMP-07 | ENT-03 | — (dispara a passagem) | TEL-01 (prevista) | AC-08, AC-33, AC-80 |
| RN-24 | UC-08 | FE-01 | CMP-04 | ENT-03, ENT-25 | ERR-29 | TEL-01 (prevista) | AC-34, AC-81 |
| RN-25 | UC-02, UC-04, UC-13 | principal | — (backend) | ENT-07, ENT-08 | ERR-36 | — | AC-82 |
| RN-26 | UC-13 | FE-01 | CMP-16 | ENT-08 | ERR-34 | TEL-06 (prevista) | AC-51, AC-83 |
| RN-27 | UC-13 | principal | — (backend) | ENT-08, ENT-15 | ERR-13 | — | AC-84 |
| RN-28 | UC-13 | FA-02 | CMP-16 | ENT-07, ENT-08 | — | TEL-06 (prevista) | AC-50, AC-85 |
| RN-29 | UC-14 | FA-01, FE-02 | CMP-17 | ENT-02 | ERR-38, ERR-39 | TEL-06 (prevista) | AC-54, AC-57, AC-86 |
| RN-30 | UC-11, UC-14 | principal | CMP-02 | ENT-02, ENT-11 | ERR-40 | TEL-01 (prevista) | AC-53, AC-87 |

## Requisitos não funcionais

O RNF é provado pela verificação descrita em `00-requisitos.md`, não por um AC [a confirmar: criar AC para RNF?].

| Requisito | UC | Fluxos | CMP | ENT | ERR | Tela (preencher depois) | Cenário de teste (AC-xx) |
|---|---|---|---|---|---|---|---|
| RNF-01 | UC-02 | principal | CMP-04 | — | — | TEL-01 (prevista) | [lacuna: verificação do RNF, sem AC] |
| RNF-02 | UC-02, UC-04 | principal | CMP-04, CMP-06, CMP-08 | — | — | TEL-01 (prevista) | [lacuna: verificação do RNF, sem AC] |
| RNF-03 | — | — | — | — | — | — | [lacuna: verificação do RNF, sem AC] |
| RNF-04 | UC-08 | principal | CMP-01, CMP-07 | ENT-03, ENT-14 | — | TEL-01 (prevista) | [lacuna: verificação do RNF, sem AC] |
| RNF-05 | UC-01 | principal | CMP-11 | ENT-13 | — | TEL-02 (prevista) | AC-61 (parcial) |
| RNF-06 | UC-04 | FE-02 | — (backend) | ENT-15 | ERR-13, ERR-14 | — | AC-20, AC-58, AC-74, AC-84 (parcial) |
| RNF-07 | UC-04 | FE-01 | CMP-04, CMP-05 | ENT-07 | ERR-17 | TEL-01 (prevista) | AC-19, AC-126 |
| RNF-08 | UC-12 | principal | CMP-09 | ENT-03, ENT-07 | — | TEL-01 (prevista) | [lacuna: verificação do RNF, sem AC] |
| RNF-09 | — | — | CMP-08 | ENT-12 | — | TEL-01 (prevista) | [lacuna: verificação do RNF, sem AC] |
| RNF-10 | UC-04 | principal | — | ENT-09, ENT-19 | — | — | [lacuna: verificação do RNF, sem AC] |
| RNF-11 | — | — | — | ENT-13 | — | — | [lacuna: verificação do RNF, sem AC] |
| RNF-12 | todos com tela | — | CMP-04, CMP-06, CMP-07, CMP-13 | — | — | TEL-01 a TEL-06 (previstas) | [lacuna: verificação do RNF, sem AC] |
| RNF-13 | UC-13 | principal | CMP-16 | ENT-08 | — | TEL-06 (prevista) | [lacuna: verificação do RNF, sem AC] |
| RNF-14 | UC-14 | principal | CMP-02 | ENT-02, ENT-11 | — | TEL-01 (prevista) | [lacuna: verificação do RNF, sem AC] |

## Cruzamento RF ↔ RN

União do que cada RF cita (campo "RN") com o que cada RN cita (campo "Usada por"). `*` = só o RF cita a RN; `†` = só a RN cita o RF. Sem marca, os dois lados concordam. As assimetrias são inconsistências da fonte [a confirmar].

| RF | RN |
|---|---|
| RF-01 | RN-04, RN-08 |
| RF-02 | RN-02, RN-08 |
| RF-03 | RN-04, RN-08 |
| RF-04 | RN-08 |
| RF-05 | RN-07 *, RN-08 * |
| RF-06 | RN-09 *, RN-10 * |
| RF-07 | RN-23 * |
| RF-08 | RN-05, RN-14 |
| RF-09 | RN-05, RN-06, RN-07 |
| RF-10 | RN-01, RN-05, RN-08, RN-13, RN-14, RN-16 * |
| RF-11 | RN-03, RN-12 |
| RF-12 | RN-13 * |
| RF-13 | RN-07 |
| RF-14 | RN-02 |
| RF-15 | RN-02 *, RN-30 † |
| RF-16 | — |
| RF-17 | RN-23 |
| RF-18 | — |
| RF-19 | RN-23 * |
| RF-20 | RN-23, RN-24 |
| RF-21 | RN-04 |
| RF-22 | RN-04 * |
| RF-23 | — |
| RF-24 | RN-09, RN-15, RN-18, RN-19, RN-20 |
| RF-25 | RN-10, RN-11, RN-15, RN-21 |
| RF-26 | RN-20, RN-21, RN-22 |
| RF-27 | RN-08 *, RN-16, RN-17 |
| RF-28 | RN-01, RN-03, RN-04 *, RN-06, RN-29 † |
| RF-29 | RN-01 *, RN-02 *, RN-10 *, RN-12 *, RN-27 † |
| RF-30 | RN-07 * |
| RF-31 | RN-26, RN-27 *, RN-28 |
| RF-32 | RN-25, RN-27, RN-28 |
| RF-33 | RN-08 *, RN-29 |
| RF-34 | RN-02 *, RN-30 |

## Cruzamento UC ↔ TEL

| UC | TEL | RF |
|---|---|---|
| UC-01 | TEL-02 (e CMP-03 da TEL-01) | RF-01, RF-02, RF-03, RF-04 |
| UC-02 | TEL-01 | RF-05, RF-07, RF-30 |
| UC-03 | TEL-03 | RF-08, RF-09 |
| UC-04 | TEL-01 | RF-06, RF-10, RF-11, RF-12, RF-28 |
| UC-05 | TEL-01, TEL-05 | RF-24 |
| UC-06 | TEL-01, TEL-05 | RF-25 |
| UC-07 | TEL-05 | RF-26 |
| UC-08 | TEL-01 | RF-17, RF-20 |
| UC-09 | TEL-04 | RF-13 |
| UC-10 | TEL-01 [a confirmar: sem CMP] | RF-27 |
| UC-11 | TEL-01 | RF-14, RF-15, RF-16 |
| UC-12 | TEL-01 | RF-23 |
| UC-13 | TEL-06 | RF-31 |
| UC-14 | TEL-06 | RF-33, RF-34 |
| — (necessidade do negócio) | TEL-01 | RF-18, RF-19, RF-21, RF-22, RF-32 |
| — (necessidade do negócio) | — (backend) | RF-29 |
