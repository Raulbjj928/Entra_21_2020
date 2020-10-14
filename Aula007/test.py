
CAD = [{'nome': 'Raul', 'sobrenome': 'furtado', 'idade': 27, 'ID': 1}, 
{'nome': 'Milena', 'sobrenome': "Maria", "idade": 25, 'ID': 2}]

LOCAL = [{'rua': 'alameda', 'numcasa': '23', 'comp': 'prox prefeitura', 'bairro': 'centro',
 'cidade': 'bnu', 'estado': 'sc', 'ID': 1},
 {'rua': 'repa', 'numcasa': '171', 'comp': 'prox hannes', 'bairro': 'ponta aguda',
  'cidade': 'bnu', 'estado': 'sc', 'ID': 2}]

INFOS = []
INFOS.append(CAD)
INFOS.append(LOCAL)

def LISTAGEM() :
    for i in INFOS:
        print(f'''{i[0]['ID']}
        ''')

LISTAGEM()