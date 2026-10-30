---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-20
substitui: 
---
# ✅ Mascaramento sem adivinhar

- **Proposta (plano):** T2 do [[fundacao-plano]]: depois de quatro voltas de verificação em que cada correção do mascaramento por formato abria outra brecha, o orquestrador ofereceu trocar a abordagem.
- **Decisão:** o núcleo mascara (••••) só tokens com prefixo conhecido (`ghp_`, `gho_`, `ghu_`, `ghs_`, `ghr_`, `github_pat_`, `sk-ant-`), que somem inteiros, e o valor exato de todo segredo que o próprio núcleo guarda. Nada de reconhecer segredo pelo formato do texto (cabeçalho `Authorization`, `chave=valor`, senha em URL, PEM).
- **Alteração:** RN-04 reescrita no contrato (M-36).
- **Motivo:** resposta do humano em 2026-11-20, sessão das 08h37: "nada de tentar adivinhar vamos parar com isso; mascarar só os prefixos conhecidos e os segredos que o próprio núcleo guarda, sem tentar adivinhar".
- **Consequências:** a T2 é refeita numa branch nova a partir da T1, mais simples; as voltas por formato ficam como histórico no [[fundacao-plano]]. Segredo que o núcleo não guarda e que não tem prefixo conhecido não é mascarado. Todo segredo que o núcleo recebe (token do OAuth, chaves) precisa ser registrado como segredo para entrar na máscara.

### 🔗 Conexões
- Funcionalidade: [[geral-contexto]]
- Plano: [[fundacao-plano]]
- Regras: [[manual-da-orquestra]], [[padroes]]
