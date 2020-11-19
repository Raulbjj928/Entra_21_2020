  
import sqlite3

class Pessoa():
    def __init__(self, id_veiculo_pessoa:int, nome:str, data_nascimento:str, cpf:str, 
                 endereco:str, salario:float, profissao:str,
                 email:str, telefone:str, nome_de_responsavel:str,
                 sexo:str, naturalidade:str, nacionalidade:str):

        self.id_veiculo_pessoa = id_veiculo_pessoa
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
        self.salario = salario
        self.profissao = profissao
        self.email = email
        self.telefone = telefone
        self.nome_de_responsavel = nome_de_responsavel
        self.sexo = sexo
        self.naturalidade = naturalidade
        self.nacionalidade = nacionalidade
        
    def salvar_pessoa_na_tabela(self):
        
        conn = sqlite3.connect('cadastro_de_veiculos_concessionaria_do_vale.db')
        cursor = conn.cursor()
        
        tupla_dados_pessoa = (self.id_veiculo_pessoa, self.nome, self.data_nascimento, 
                               self.cpf, self.endereco, self.salario,
                               self.profissao, self.email,self.telefone,
                               self.nome_de_responsavel, self.sexo,
                               self.naturalidade, self.nacionalidade)
        
        cursor.execute("""
                        INSERT INTO cadastro_de_pessoas (id_veiculo_pessoa, nome, data_nascimento, 
                                                        cpf, endereco, salario, profissao, email,
                                                        telefone, nome_de_responsavel, sexo, 
                                                        naturalidade, nacionalidade) 
                        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""", tupla_dados_pessoa)
                    
        conn.commit()
        conn.close()
        
        
class Carro():
    def __init__(self, nome_veiculo:str, marca:str, modelo_categoria:str,
                       cor:str, tipo_motor:str, combustivel:str, ano:int,
                       num_portas:int, qtd_passageiros:int, placa:str,
                       nome_proprietario:object, criado_em:str):
        
        self.nome_veiculo = nome_veiculo
        self.marca = marca
        self.modelo_categoria = modelo_categoria
        self.cor = cor
        self.tipo_motor = tipo_motor
        self.combustivel = combustivel
        self.ano = ano
        self.num_portas = num_portas
        self.qtd_passageiros = qtd_passageiros
        self.placa = placa
        self.nome_proprietario = nome_proprietario
        self.criado_em = criado_em
    
    def salvar_veiculo_na_tabela(self):
        conn = sqlite3.connect('cadastro_de_veiculos_concessionaria_do_vale.db')
        cursor = conn.cursor()

        tupla_dados_veiculo = (self.nome_veiculo, self.marca, self.modelo_categoria,
                                 self.cor, self.tipo_motor,
                                self.combustivel, self.ano, self.num_portas,
                                 self.qtd_passageiros, self.placa,
                                self.nome_proprietario, self.criado_em)
        
        cursor.execute("""
                        INSERT INTO cadastro_de_veiculos(nome_veiculo, marca, 
                        modelo_categoria, cor, tipo_motor, combustivel, ano,
                        num_portas, qtd_passageiros, placa, nome_proprietario, criado_em
                         )
                        VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""", tupla_dados_veiculo)

        conn.commit()
        conn.close()


p = Pessoa(1,'Raul',12131993, 2222202002, 'lalala', 30.000, 'dev', 'arrarara@hha', 3232323, 'lsokaoska', 'm','cvel','br')
p.salvar_pessoa_na_tabela()
