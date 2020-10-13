#--- Exercício 2  - Funções
#--- Escreva uma função para cadastro de endereço:
#---       a função deve receber sete parâmetros, id da pessoa, rua, numero, complemento, bairro, cidade e estado
#---       a função deve salvar os dados de endereço em uma lista com escopo global
#---       a função deve permitir o cadastro apenas de endereços com todos os dados preenchidos
#---       a função deve retornar uma mensagem ao final de acordo com a situação
#--- A função deve ser salva em um arquivo diferente do arquivo principal onde será chamada

LOCAL = []

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

rua=input('')
numcasa=input('')
comp=input('')
bairro=input('')
cidade=input('')
estado=input('')
numeroid='ID'


endereco(rua,numcasa,comp,bairro,cidade,estado,numeroid)
print(LOCAL)