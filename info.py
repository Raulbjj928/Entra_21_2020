CAD = [{'nome': 'Raul', 'sobrenome': 'furtado', 'idade': 27, 'ID': 1}, 
{'nome': 'Milena', 'sobrenome': "Maria", "idade": 25, 'ID': 2}]

LOCAL = [{'rua': 'alameda', 'numcasa': '23', 'comp': 'prox prefeitura', 'bairro': 'centro',
 'cidade': 'bnu', 'estado': 'sc', 'ID': 1},
 {'rua': 'repa', 'numcasa': '171', 'comp': 'prox hannes', 'bairro': 'ponta aguda',
  'cidade': 'bnu', 'estado': 'sc', 'ID': 2}]


def cadastro (nome, sobrenome, idade):

    PESSOA = {}
    
    if idade >= 18:

        PESSOA['nome'] = nome
        PESSOA['sobrenome'] = sobrenome
        PESSOA['idade'] = idade        
        ID = len(CAD) + 1
        PESSOA['ID'] = ID
        CAD.append(PESSOA)

    else:
        return print('''
~~~~~~~~~~~~~~~~~~§ IDADE INVALÍDA §~~~~~~~~~~~~~~~~~~~~~~
   ^^^^^^ POR FAVOR EXECUTE NOVAMENTE O PROGRAMA ^^^^^
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')
            
    print(f'~~º ID {ID} º~~')


def endereco(rua, numcasa, comp, bairro, cidade, estado, numeroid ):

    END = {}          

    if  (
        rua == '' or numcasa == '' or 
        comp == '' or bairro == '' or 
        cidade == '' or estado == ''
        ) :
        return print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
§§§§§§§§§§§§§§§§§!!! DADO EM BRANCO !!!§§§§§§§§§§§§§§§§§§§
§§§§§§§§§!!! ENDEREÇO NÃO PODE SER ATUALIZADO !!!§§§§§§§§§
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')

    else:

        END['rua'] = rua
        END['numcasa'] = numcasa
        END['comp'] = comp
        END['bairro'] = bairro
        END['cidade'] = cidade
        END['estado'] = estado
        ID = len(LOCAL) + 1
        END['ID'] = ID
        LOCAL.append(END)

        return print('''
                ENDEREÇO ATUALIZADO !

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')


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

def LISTAR_END() :
        print(f'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                * ENDEREÇOS CADASTRADOS *
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')
        for i in LOCAL:
                
                print(f'''
                RUA : {i['rua']}
                Nº CASA :{i['numcasa']}
                COMPLEMENTO : {i['comp']}
                BAIRRO : {i['bairro']}
                CIDADE : {i['cidade']}
                ESTADO : {i['estado']}
                ID DA PESSOA : {i['ID']}

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                ''')
        BUSCA = int(input('''DIGITE O NUMERO DO ID DA PESSOA QUE DESEJA COSULTAR O ENDEREÇO :
 '''))
        
        print(f'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                RUA : {LOCAL[(BUSCA)-1]['rua']}
                Nº CASA : {LOCAL[(BUSCA)-1]['numcasa']}
                COMPLEMENTO : {LOCAL[(BUSCA)-1]['comp']}
                BAIRRO : {LOCAL[(BUSCA)-1]['bairro']}
                CIDADE : {LOCAL[(BUSCA)-1]['cidade']}
                ESTADO : {LOCAL[(BUSCA)-1]['estado']}

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

           ~º[| OBRIGADO POR USAR O PROGRAMA |]º~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
)

