def header(txt = "MENU PRINCIPAL"):
    print(f"""
{"-=" * 20}
{txt:^40}
{"-=" * 20}""")


def showMenu():
    lista = "Listar Cadastros", "Cadastrar Pessoa", "Sair do Sistema"

    print("-=" * 20)
    for i , j in enumerate(lista):
        print(f"{i + 1} - {j}")
    print("-=" * 20)


def escolhas(num):
    if num == 1:
        header("LISTA DOS CADASTROS")

        arquivo = open("C:\\Future_Aperture\\Python\\exercícios_python\\exercíciosMiguel\\Curso_Em_Vídeo\\Exercícios_91-115\\Mundo_3_Ex_115\\dadospessoas.txt", "r")
        lista = arquivo.read().split("\n")

        print(f"Nomes{'Idade':>30}\n")

        for i in lista:
            j = i.split(";")

            print(f"{j[0]:<30}{j[1]}")
        
        print("-=" * 20)


    elif num == 2:
        header("CADASTRO DE PESSOA")



    elif num != 3:
        print("\n\033[0;31mDigite uma opção valida.\033[0m\n")
        showMenu()