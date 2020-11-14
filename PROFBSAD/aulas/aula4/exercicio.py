'''Construa uma classe chamada veículo com no minímo 5 atributos e 3 metódos
Faça outras 3 classes que herdem da classe veículo;
 por exemplo Carro; e ajuste as funções onde necessário (polimorfismo)'''
from pessoa import Pessoa

listapessoas = []

class Veiculo:
    

    def __init__(self, marca, nome,cor, peso, combustivel):
        self.marca = marca
        self.nome = nome
        self.cor = cor
        self.peso = peso
        self.combustivel = combustivel
    
    def direcao(self):
        return '???'
    
    def capacidade(self):
        return '???'

    def Addpessoa(self, p):
        listapessoas.append(p)
    
    def Removepessoa(self, p):
        listapessoas.remove(p)



class Moto(Veiculo):
    def __init__(self, marca, nome, cor, peso, combustivel):
        super().__init__(marca, nome, cor, peso, combustivel)

    def direcao(self):
        return 'Guidão'

    def capacidade(self):
        return '1 piloto e 1 passageiro'


class Carro(Veiculo):
    def __init__(self, marca, nome, cor, peso, combustivel):
        super().__init__(marca, nome, cor, peso, combustivel)

    def direcao(self):
        return 'Volante'

    def capacidade(self):
        return '1 motorista e 4 passageiros'


class Carroca(Veiculo):
    def __init__(self, marca, nome, cor, peso, combustivel):
        super().__init__(marca, nome, cor, peso, combustivel)

    def direcao(self):
        return 'Cavalo'

    def capacidade(self):
        return 'Quantos couber'
        
moto = Moto('Honda', 'Cg', 'Vermelha', '150 kg','Gasolina')
carro = Carro('VW','UP', 'Branco', '300 kg', 'Flex')
carroca = Carroca('Sei lá','Tbm ñ sei', 'azul', 'depende', 'pasto')

listaveiculo = [moto, carro, carroca]
print(moto.nome)
for veiculo in listaveiculo:
    print(f'''
O Veiculo {type(veiculo).__name__}: 
é direcionado por um {veiculo.direcao()}
e tem a capacidade de {veiculo.capacidade()}
''')

if __name__ == '__main__':
    p1 = Pessoa('Raul', 30, 2332332)
    p2 = Pessoa('Henrque',40, 1210201)
    v = Veiculo('', '','','','')
    v.Addpessoa(p1)
    v.Addpessoa(p2)

    print(*listapessoas)
    v.Removepessoa(p1)  
    print(*listapessoas)
