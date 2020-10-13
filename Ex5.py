#--- Exercício 5  - Funções
#--- Escreva um programa para cadastro de pessoas e endereços:
#---       o programa deve solicitar os dados de pessoa utilizados na função do ex1
#---       o programa deve solicitar os dados de endereços utilizados na função do ex2
#---       o programa deve passar o id obtido na função do ex1 para a função do ex2
#---       o programa deve mostrar ao final os dados de todos as pessoas cadastradas 
#---              com seus respectivos endereços utilizando as funções do ex3 e ex4


import info
info.CAD
info.LOCAL

CAD = [{'nome': 'Raul', 'sobrenome': 'furtado', 'idade': 27, 'ID': 1}, 
{'nome': 'Milena', 'sobrenome': "Maria", "idade": 25, 'ID': 2}]

LOCAL = [{'rua': 'alameda', 'numcasa': '23', 'comp': 'prox prefeitura', 'bairro': 'centro',
 'cidade': 'bnu', 'estado': 'sc', 'ID': 1},
 {'rua': 'repa', 'numcasa': '171', 'comp': 'prox hannes', 'bairro': 'ponta aguda',
  'cidade': 'bnu', 'estado': 'sc', 'ID': 2}]



nome = input('Nome : ')
sobrenome = input('Sobrenome : ')
idade = int(input('Idade : '))

info.cadastro(nome, sobrenome, idade)


rua=input('RUA : ')
numcasa=input('Nº DA CASA : ')
comp=input('COMPLEMENTO : ')
bairro=input('BAIRRO : ')
cidade=input('CIDADE : ')
estado=input('ESTADO : ')
numeroid='ID'

info.endereco(rua,numcasa,comp,bairro,cidade,estado,numeroid)

info.LISTARNOME()
info.LISTAR_END()

