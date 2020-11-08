class CELULAR:
    MODELO = 'REDMI'

    def __init__(self, nome, capacidade):
        self.nome = nome
        self.capacidade = capacidade
    
    def __str__(self):
        return f'O celular {self.nome} tem {self.capacidade}GB de memória '

if __name__ == '__main__' :
    c = CELULAR('REDMI_NOTE8',68)
    print(c)
    

class RELOGIO:
    TIPO = 'Pulso'

    def __init__(self, marca, valor):
        self.marca = marca
        self.valor = valor

    def __str__(self):
        return f'O relógio de {self.TIPO},{self.marca} custa {self.valor:.2f} Reais '

if __name__ == '__main__':
    r = RELOGIO('Rolex', 1150.50)
    print(r)

class LIVRO:
    FORMATO = 'E-BOOK'

    def __init__(self, nome, quantpg):
        self.nome = nome
        self.quantpg = quantpg

    def __str__(self):
        return f'O {self.FORMATO} {self.nome}, tem {self.quantpg} páginas .'

if __name__ == '__main__':
    L = LIVRO('BIBLIA', 1000)
    print(L)

class CARRO:
    SEGMENTO = 'PASSEIO'

    def __init__(self, nome, ano, lugares):
        self.nome = nome
        self.ano = ano
        self.lugares = lugares

    def __str__(self):
        return f'''
        Carro : {self.nome}
        Segmento : {self.SEGMENTO}
        Ano : {self.ano}
        Lugares : {self.lugares} 
        '''
if __name__ == '__main__':
    S = CARRO('Up', 2016, 5)
    print(S)

class GARRAFA:
    BEBIBA = 'VINHO'

    def __init__(self, tipo, conteudo, ano, marca):
        self.tipo = tipo
        self.conteudo = conteudo
        self.ano = ano
        self.marca = marca

    def __str__(self):
        return f'''
    GARRAFA DE {self.BEBIBA}

TIPO : {self.tipo}
CONTEÚDO : {self.conteudo}L
ANO : {self.ano}
MARCA : {self.marca}
'''
if __name__ == '__main__':
    V = GARRAFA('TINTO', 1.5, 1990,'ARGENTO')
    print(V)

