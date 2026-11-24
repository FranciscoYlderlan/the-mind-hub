---
tipo: decisao
funcionalidade: geral
status: aprovada
criado: 2026-11-24
substitui: 
---
# ✅ Versão do Rust só é fixada no fim do projeto

- **Proposta (plano):** Tci do [[integracoes-plano]]: o `CI` usa sempre o Rust estável mais novo (`dtolnay/rust-toolchain@stable`) e quebrou sozinho com o clippy 1.100; o implementador sugeriu fixar a versão no repositório.
- **Decisão:** o `CI` segue no Rust estável mais novo durante o desenvolvimento; a versão é fixada só no fim do projeto (etapa 10 do [[geral-plano]]).
- **Alteração:** nenhuma.
- **Motivo:** resposta do humano em 2026-11-24, às 08h34: "deixar como está e fixar só ao final do projeto".
- **Consequências:** lint novo do Rust estável pode quebrar o `CI` sem mudança no código; a correção entra numa tarefa `ci(setup)` própria, como a Tci. O ambiente do agente fica no Rust 1.97 (o proxy bloqueia `static.rust-lang.org`), então o `CI` da PR é a prova final.

### 🔗 Conexões
- Funcionalidade: [[integracoes-contexto]]
- Plano: [[integracoes-plano]], [[geral-plano]]
- Bugs: [[bug-ci-sem-execucao-actions-desligado-2026-11-24]]
- Projeto: [[geral-contexto]]
