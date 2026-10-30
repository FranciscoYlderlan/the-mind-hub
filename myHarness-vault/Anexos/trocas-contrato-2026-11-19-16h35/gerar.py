import json,os
E="ENT-05, ENT-06, ENT-09, ENT-10, ENT-18"
R="RN-31"
t=[]
def T(a,at,nv,m="M-21: gravação dupla"): t.append({"arquivo":a,"atual":at,"novo":nv,"motivo":m})
row30="| RN-30 | Toda nota devolvida por uma busca ou leitura pela Obsidian CLI vem com o nome do cofre de onde saiu. Violação: resultado sem origem não é entregue ao agente (ERR-40). Sem exceção. | ENT-11, ENT-02 | Seção 1 · Várias memórias; condição |"
T("00-requisitos.md",row30,row30+"\n| RN-31 | O que mora no SQLite e no cofre (plano, tarefa, relatório, achado e o aval da decisão) é gravado nos dois na mesma operação do núcleo, com o mesmo conteúdo, e uma conferência compara os dois lados [a confirmar: quando roda, além do teste]. Violação: se um lado falha, o outro é desfeito e nada é gravado; diferença achada na conferência vai ao Log (ERR-51). Sem exceção. | "+E+", ENT-12 | Decisão do Humano (M-21) · Memória; condição |")
T("README.md","RN-01 a RN-30 |","RN-01 a RN-31 |")
T("README.md","ERR-01 a ERR-50","ERR-01 a ERR-51")
T("README.md","AC-01 a AC-146","AC-01 a AC-148")
for at in ["Mora em: SQLite + decisão no cofre.","Mora em: SQLite + plano no cofre.","Mora em: SQLite + resumo no cofre.","Mora em: SQLite + bug no cofre.","no SQLite fica só o aval."]:
    T("02-entidades.md",at,at+" Gravação dupla, com o mesmo conteúdo nos dois lados (RN-31; falha: ERR-51).")
r50=None
T("07-rastreabilidade.md","| RN-30 | UC-11, UC-14 | principal | CMP-02 | ENT-02, ENT-11 | ERR-40 | TEL-01 (prevista) | AC-53, AC-87 |","| RN-30 | UC-11, UC-14 | principal | CMP-02 | ENT-02, ENT-11 | ERR-40 | TEL-01 (prevista) | AC-53, AC-87 |\n| RN-31 | — (decisão do Humano) | — | — (backend) | "+E+", ENT-12 | ERR-51 | — | AC-147, AC-148 |")
ac87="| AC-87 | UC-11, UC-14 | regra RN-30 | uma busca que acha notas em dois cofres | o resultado volta | cada nota traz o nome do cofre e a aba \"Obsidian usado\" agrupa por cofre |"
T("08-criterios-de-aceite.md",ac87,ac87+"\n| AC-147 | — (decisão do Humano) | regra RN-31 | o cofre de memória sem permissão de escrita | o núcleo grava uma tarefa | nada fica gravado no SQLite nem no cofre e aparece o ERR-51 |\n| AC-148 | — (decisão do Humano) | regra RN-31 | uma tarefa, um relatório e um achado gravados | a conferência compara o SQLite com as notas | todos os campos batem; uma diferença forçada vai ao Log com o ERR-51 |")
T("08-criterios-de-aceite.md","e AC-146, por requisito acrescentado depois","AC-146, por requisito acrescentado depois, e AC-147 e AC-148, por regra acrescentada depois")
json.dump(t,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"trocas.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print(len(t))
