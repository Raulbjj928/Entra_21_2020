from os import system, name 

palavra = ""
chances = 0

def carregar_config():
    global palavra
    global chances
    linhas_arquivo = []
    with open('C:\\Users\\Master\\Documents\\GitHub\\entra21\\aula1\\forca.cfg') as f:
        for linha in f:
            linhas_arquivo.append(linha.strip())
    palavra = str(linhas_arquivo[0])
    chances = int(linhas_arquivo[1])

def limpar_tela():
    if name == 'nt': 
        system('cls') 
        # for mac and linux(here, os.name is 'posix') 
    else: 
        system('clear')  
    
def jogar():
    global palavra
    global chances
    carregar_config()
    letras_usadas = []

    while True:
        tentativa_palavra = ""

        limpar_tela()      
  
        print(f"Número de chances: {chances} - tentativas:") # interpolação de string
        print(*letras_usadas) # imprime item por item do array
        print("\n")
        for x in palavra:
            tentativa_palavra += x if x in letras_usadas else "_"
        print(tentativa_palavra + "\n\n")

        if chances == 0:
            print("Você perdeu!")
            break   
        
        if tentativa_palavra == palavra:
            print(f"Você ganhou sobrando {chances} chance(s) !")
            break

        

        chute = ""
        chute = input("Digite uma letra:").lower().strip()
        letras_usadas.append(chute)
        if not chute in palavra:
            chances -= 1

             
        
if __name__ == "__main__":
    # implementar a função carregar_config
    # implementar a função verifica_fim_jogo
    # implementar a função limpar_tela

    # previnir que o usuário digite números
    # previnir que o usuário repita letras

    # implementar menu de usuário com as seguintes opções:
    # 1 - Jogar
    # 2 - Modificar as configurações
    # 3 - sair
    
    # https://realpython.com/quizzes/python-dicts/viewer/

    jogar()
