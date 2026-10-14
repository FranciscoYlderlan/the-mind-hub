---
aliases: [Dados externos, Versão estável, Licença de imagem, External API selection]
tags: [estudos/programacao]
tipo: conceito
status: rascunho
criado: 2026-11-16
origem: projeto Stonebid (stonebid-vault, decisões api-de-itens, busca-so-em-dominio-publico, prisma-7, typescript-6-no-web e node-26), 2026-10-29
---
# 📦 API externa escolhida por versão, licença e chave

> [!tldr] Em uma linha
> Dependência ou fonte de dados externa: versão estável, licença conferida para o uso real e, se der, API sem chave.

É escolher o fornecedor da festa: o bolo tem de existir de verdade (não a "versão de teste"), você pode servir para os convidados (licença) e não depende de pegar uma senha na portaria todo dia (chave).

> [!note] A regra e como aplicar
> 1. **Versão estável:** "a citada ou a mais recente da linha"; confira se a mais nova é `rc` ou outro produto com o mesmo nome (ex.: sem o comando de migração).
> 2. Linha travada quando uma ferramenta vizinha ainda não suporta a próxima (ex.: o linter atrás do compilador); subir pede decisão nova.
> 3. Mesma versão do runtime na imagem, no CI, no CD e na máquina local.
> 4. **Licença:** leia a regra da fonte para o seu uso (ex.: dados livres, mas imagem só reusável em obra de domínio público) e filtre na busca.
> 5. **API sem chave** quando houver opção equivalente; compare também chamadas por item e itens sem imagem.
> 6. Acesso por um adaptador só, com timeout e erro claro; nenhuma outra tela chama a fonte.

> [!warning] Armadilha
> Copiar para o seu banco e servir em público uma imagem protegida porque "os dados da API são abertos": dado e imagem podem ter licenças diferentes.

> [!tip] Quando abrir esta nota
> Ao escolher biblioteca, ORM, runtime ou API pública de dados para um projeto novo.

### 🛠️ Resumo direto para o cérebro
* **Ponto 1:** número de versão maior não é versão melhor; olhe o canal (`rc`, estável).
* **Ponto 2:** licença vale para o uso que você faz, não para a API em geral.
* **Ponto 3:** o formato da fonte muda; o [[API simulada conferida contra a API real|mock conferido contra a real]] pega antes da tela.

### 🔗 Conexões
- Mapa: [[MOC Programação]]
- Relacionadas: [[Busca e cache em rota pública]], [[Imagem de terceiro com anti-robô passa pelo servidor]]
