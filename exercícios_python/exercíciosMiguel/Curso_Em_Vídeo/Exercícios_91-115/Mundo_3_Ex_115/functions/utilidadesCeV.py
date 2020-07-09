# Cria uma linha verde
def linha():
    print(f'\033[0;32m{"-=" * 20}\033[0m')


# Cria um header de título
def header(txt = "MENU PRINCIPAL"):
    
    print()
    linha()
    print(f"\033[0;36m{txt:^40}\033[0m")
    linha()


# Mostra o menu inteiro
def showMenu():
    lista = "Listar Cadastros", "Cadastrar Pessoa", "Sair do Sistema"

    linha()
    for i , j in enumerate(lista):
        print(f"\033[0;33m{i + 1} - {j}\033[0m")
    linha()


# Dependendo da escolha, iniciará uma função diferente
def escolhas(num):
    if num == 1:
        mostrarCadastros()

    elif num == 2:
        cadastrar()


# Caso não sejá nenhuma das opções, dá "erro"
    elif num != 3:
        print("\n\033[0;31mDigite uma opção valida.\033[0m\n")
        showMenu()


# Mostra toda a lista de pessoas cadastradas
def mostrarCadastros():
        header("LISTA DOS CADASTROS")

        # Abre o txt
        arquivo = open("C:\\Future_Aperture\\Python\\exercícios_python\\exercíciosMiguel\\Curso_Em_Vídeo\\Exercícios_91-115\\Mundo_3_Ex_115\\dadospessoas.txt", "r")
        lista = arquivo.read().split("\n")

        print(f"\033[4;34mNomes{'Idade':>30}\033[0m\n")

        #Pega cada linha do txt, e pega o nome e idade
        for i in lista:
            j = i.split(";")

            try:
                print(f"{j[0]:<30}{j[1]} anos")

            # Se estiver vazia, avisa q n tem nada
            except IndexError:
                print("Não há nenhuma pessoa cadastrada.\n")

        linha()

        arquivo.close()


# Cadastra uma pessoa nova no txt
def cadastrar():
        header("CADASTRO DE PESSOA")

        #Abre o arquivo txt
        arquivo = open("C:\\Future_Apperture\\Python\\exercícios_python\\exercíciosMiguel\\Curso_Em_Vídeo\\Exercícios_91-115\\Mundo_3_Ex_115\\dadospessoas.txt", "a+")

        #Inputs de nome e idade
        while True:
            nome = input("\nDigite o nome da pessoa:\n> ")

            try:
                idade = int(input("\nDigite a idade da pessoa:\n> "))

            #Caso n seja digitado um numero inteiro
            except ValueError:
                print("\n\033[0;31mDigite apenas números inteiros, tente novamente.\033[0m")
                continue

            break

        arquivo.seek(0)

        # Caso o txt não esteja vazia, pula uma linha
        if len(arquivo.read(100)) > 0:
            arquivo.write("\n")

        # Adiciona o nome no final do txt
        arquivo.write(f"{nome};{idade}")

        print()
        showMenu()