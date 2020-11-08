#--- Exercício 3  - Funções
#--- Escreva uma função para listar pessoas cadastradas:
#---    a função deve retornar todas as pessoas cadastradas na função do ex1
#--- Escreva uma função para exibi uma pessoa específica:
#----    a função deve retornar uma pessoa cadastrada na função do ex1 filtrando por id

CAD = [{'nome': 'Raul', 'sobrenome': 'furtado', 'idade': 27, 'ID': 1}, 
{'nome': 'Milena', 'sobrenome': "Maria", "idade": 25, 'ID': 2}]


def LISTARNOME() :
        print(f'''
~~~~~~~~~~~~~~~~~~~ NOMES CADASTRADOS ~~~~~~~~~~~~~~~~~~~~
                ''')
        for i in CAD:
                print(f'''
                {i['nome']}''')
        print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')
        BUSCA = int(input('''DIGITE O NUMERO DO ID DA PESSOA QUE DESEJA COSULTAR : 
'''
))
        print(f'''
O NOME DA PESSOA REFERENTE AO ID QUE VOCÊ DIGITOU É :

>>>>>>> {CAD[(BUSCA)-1]['nome']}

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')


LISTARNOME()