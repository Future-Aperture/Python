from functions.utilidadesCeV import *

try:
    arquivo = open("C:\\Future_Aperture\\Python\\exercícios_python\\exercíciosMiguel\\Curso_Em_Vídeo\\Exercícios_91-115\\Mundo_3_Ex_115\\dadospessoas.txt", "x")
except:
    None

header()
showMenu()

while True:
    try:
        opcao = int(input("\nSua opção: "))
    
    except ValueError:
        print("\n\033[0;31mPor favor, digite um número inteiro válido.\033[0m\n")
        showMenu()
        continue

    escolhas(opcao)

    if opcao == 3:
        print("\nSaindo do sistema, até logo.")
        break