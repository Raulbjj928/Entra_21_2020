#--- Exercício 4  - Funções
#--- Escreva uma função para listar endereços cadastrados:
#---    a função deve retornar todos os endereços cadastrados na função do ex2
#--- Escreva uma função para exibir um endereço específico:
#        a função deve retornar um endereço cadastrado na função do ex2 filtrando por 
#           id da pessoa



LOCAL = [{'rua': 'alameda', 'numcasa': '23', 'comp': 'prox prefeitura', 'bairro': 'centro',
 'cidade': 'bnu', 'estado': 'sc', 'ID': 1},
 {'rua': 'repa', 'numcasa': '171', 'comp': 'prox hannes', 'bairro': 'ponta aguda',
  'cidade': 'bnu', 'estado': 'sc', 'ID': 2}]

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

LISTAR_END()