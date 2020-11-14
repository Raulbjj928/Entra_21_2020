from random import randrange

arqPessoa = "cadastroPessoa.txt"
arqConta = "cadastroConta.txt"


class Banco():
    def __init__(self):
        pass
    
    def geraNumConta(self):
        num = randrange(100, 999)
        return num
    
    def procurarPessoa(self):
        pessoas = []
        cpf = input("⮚ Digite o CPF para ver os dados: ")
        with open("cadastroPessoasBanco.txt", "r") as pesquisa:
            for pessoa in pesquisa:
                pessoas.append(pessoa.strip().split(';'))

        for i in pessoas:
            if cpf == i[2]:
                print(f'''

▛                   
        CLIENTE  
    ⨑ {i[0]} ⨑ 
                   
Endereço: {i[1]}
Cpf: {i[2]}
Telefone: {i[3]}

                    ▟

''')
            else:
                continue
    
    def mostraSaldo(self):
        saldos = []
        numeroConta = input("⮚ Digite o número da conta para consultar o saldo : ")
        banco = (input('''
⮛ Escolha o banco referente a conta ⮛

        1 ⬗ NuConta
        2 ⬗ ViaCred

⮚ Digite a opção desejada: '''))
        if banco == '1' or banco == '2':
            with open("cadastroConta.txt", "r") as consulta:
                for conta in consulta:
                    saldos.append(conta.strip().split(';'))

            for i in saldos:
                if i[1] == '1' :
                    nomebanco ='NuConta'
                else:
                    nomebanco = 'ViaCred'

                if numeroConta == i[2] and banco == i[1]:
                    print(f'''
▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩

  Demonstrativo {nomebanco}
    CONTA Nº {i[2]} 

   SALDO ⟫ R$ {float(i[3]):.2f}

▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩
''')
                    break
                else:
                    continue
        
        else:
            print('''

⫸⫸⫸⫸⫸⫸⫸⫸⫸ BANCO INVÁLIDO ⫷⫷⫷⫷⫷⫷⫷⫷⫷

            ''')
    

    def deposito(self):
        saldo = []
        numeroConta = input("⮚ Digite o número da conta para depósito : ")
        banco = input('''
⮛ Banco referente a conta de depósito ⮛

        1 ⬗ NuConta
        2 ⬗ Viacredi

⮚ Digite a opção desejada: ''')
        if banco == 2 or banco == 1:
            valor = float(input("⮚ Digite o valor do deposito : "))
            with open("cadastroConta.txt", "r+") as novoSaldo:
                for conta in novoSaldo:
                    saldo.append(conta.strip().split(';'))
        
            arqApaga = open("cadastroConta.txt", "w")
            for i in saldo:
                if numeroConta == i[2] and banco == i[1]:
                    valorNovo = i[3]
                    i[3] = str(float(valorNovo) + valor)
                    arqApaga.write(f"{i[0]};{i[1]};{i[2]};{i[3]}\n")
                    continue
                else:
                    arqApaga = open("cadastroConta.txt", "w")
                    arqApaga.write(f"{i[0]};{i[1]};{i[2]};{i[3]}\n")
            arqApaga.close()
        else:
            print('''

⫸⫸⫸⫸⫸⫸⫸⫸⫸ BANCO INVÁLIDO ⫷⫷⫷⫷⫷⫷⫷⫷⫷

            ''')
class DataSaver():
    global arqPessoa
    global arqConta

    def __init__(self):
        pass

    def cadastroPessoa(self):
        nome = input("⮚ Digite seu nome: ").strip().title()
        endereco = input("⮚ Digite seu endereço: ").strip().title()
        cpf = input("⮚ Digite seu número de CPF: ")
        telefone = input("⮚ Digite seu número de telefone: ")
        dadosPessoa = f"{nome};{endereco};{cpf};{telefone}"
        return self.gravaDados(arqPessoa, dadosPessoa)
    
    def cadastroConta(self):
        listaPessoasCadastradas = []
        listaCpfBanco = []
        continuaCadastro = False
        possuiConta = False
        saldo = 0
        with open("cadastroPessoasBanco.txt") as arqAberto:
            for linha in arqAberto:
                listaPessoasCadastradas.append(linha.strip().split(';'))
        
        with open("cadastroConta.txt") as verificacao:
            for linha in verificacao:
                listaCpfBanco.append(linha.strip().split(';'))

        cpf = input("⮚ Digite seu CPF para abrir a conta: ")
        for index in listaCpfBanco:
            cpfArquivo = str(index[0])
            if cpf == cpfArquivo:
                possuiConta = True
                break
            else:
                continue

        for index in listaPessoasCadastradas:
            cpfArquivo = str(index[2])
            if cpf == cpfArquivo:
                continuaCadastro = True
                break
            else:
                continuaCadastro = False

        if (continuaCadastro and possuiConta == False):
            banco = Banco()
            escolhaBanco = int(input("""
    ⮛ Opções banco ⮛

    1 ⬗ NuConta
    2 ⬗ ViaCred

⮚ Escolha seu banco: """))
            if escolhaBanco == 1:
                numeroConta = banco.geraNumConta()
                print(f'''
⬒ Seu banco é o NuConta e sua conta é {numeroConta} ⬓
            ⬓ Seu saldo é R$0,00 ⬒ 
                 ''')
            elif escolhaBanco == 2:
                numeroConta = banco.geraNumConta()
                print(f'''
⬒ Seu banco é a ViaCred e sua conta é {numeroConta} ⬓
            ⬓ Seu saldo é R$0,00 ⬒ 
                 ''')
            else:
                print("⫸⫸⫸ BANCO INVÁLIDO ⫷⫷⫷")

            dadosConta = f"{cpf};{escolhaBanco};{numeroConta};{saldo}"
            return self.gravaDados(arqConta, dadosConta)
        elif (continuaCadastro and possuiConta == True):
            print("⫸⫸⫸ VOCÈ JÁ POSSUI UMA CONTA ⫷⫷⫷")
        else:
            print("⫸⫸⫸ CLIENTE INEXISTENTE ! ⫷⫷⫷")

    def gravaDados(self, nomeArquivo, conteudo):
        if (nomeArquivo == arqPessoa):
            pessoas = open("cadastroPessoasBanco.txt", "a")
            pessoas.write(f"{conteudo}\n")
            pessoas.close()
        elif (nomeArquivo == arqConta):
            conta = open("cadastroConta.txt", "a")
            conta.write(f"{conteudo}\n")
            conta.close()

if __name__ == "__main__":
    print('''
    ▛                        ▜
      ▚  BEM VINDO CLIENTE  ▞ 
    ▙                        ▟
     ''')
    while True:
        dataSaver = DataSaver()
        banco = Banco()
        valor = int(input(
            """
▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚ 

        ᄽ MENU  BANCO ᄿ

    1 ⬗  Cadastrar Pessoa
    2 ⬗  Cadastrar Conta
    3 ⬗  Visualizar Saldo
    4 ⬗  Fazer um depósito
    5 ⬗  Procurar pessoas
    0 ⬗  Sair

▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚

⬔ Digite a operação desejada ⬕ : """))

        if (valor == 1):
            dataSaver.cadastroPessoa()
        elif (valor == 2):
            dataSaver.cadastroConta()
        elif (valor == 3):
            banco.mostraSaldo()
        elif (valor == 4):
            banco.deposito()
        elif (valor == 5):
            banco.procurarPessoa()
        elif(valor == 0):
            print('''
▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚ 

    Agradecemos a sua visita!

▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚ ▚ ''')
            break
        else:
            print("⫸⫸⫸ OPÇÃO INVÁLIDA ⫷⫷⫷")
  