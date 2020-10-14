#--- Exercício 5 - Funções
#--- Crie uma função para calculo de raiz
#--- A função deve ter uma variável que deternine qual é o indice da raiz(raiz quadrada, raiz cubica...)
#--- Leia um número do console, armazene em uma variável e passe para a função
#--- Realize o calculo da raiz e armazene em uma segunda variável e retorne 
#--- Imprima o resultado e uma mensagem usando f-string, fora da função
def RAIZ(A,B):
    C = A ** (1/B)
    print(f'O  radicando {A} elevado ao índice {B} tem por resultado a raiz {C:.1f}')
    return C
N1=int(input('DIGITE O RADICANDO : '))
N2=int(input('DIGITE O ÍNDICE DO RADICAL QUE DESEJA SABER A RAÍZ : '))
RAIZ(N1,N2)



