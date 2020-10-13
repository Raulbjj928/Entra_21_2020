#--- Exercício 1  - Funções
#--- Escreva uma função para cadastro de pessoa:
#---       a função deve receber três parâmetros, nome, sobrenome e idade
#---       a função deve salvar os dados da pessoa em uma lista com escopo global
#---       a função deve permitir o cadastro apenas de pessoas com idade igual ou superior a 18 anos
#---       a função deve retornar uma mensagem caso a idade informada seja menor que 18
#---       caso a pessoa tenha sido cadastrada com sucesso deve ser retornado um id 
#--- A função deve ser salva em um arquivo diferente do arquivo principal onde será chamada
CAD = [{'nome': 'Raul', 'sobrenome': 'furtado', 'idade': 27, 'ID': 1}, 
{'nome': 'Milena', 'sobrenome': "Maria", "idade": 25, 'ID': 2}]

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
    

nome = input('Nome : ')
sobrenome = input('Sobrenome : ')
idade = int(input('Idade : '))

cadastro(nome, sobrenome, idade)
print(CAD)