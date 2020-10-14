#--- Exercício 3  - Funções
#--- Crie uma função que leia três números float
#--- Armazene cada valor lido em uma variável
#--- Calcule a média entre os três números e armazene em uma quarta variável
#--- Imprima a média e uma mensagem usando f-string 
def media():

    A = float(input('1º VALOR : '))
    B = float(input('2º VALOR : '))
    C = float(input('3º VALOR : '))
    MED = (A+B+C)/3
    print(f' A média entre os valores {A}, {B} e {C} é {MED:.2f}')

media()
