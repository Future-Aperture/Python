from functions.utilidadesCeV import header, showMenu, escolhas

# Abre o arquivo
try:
    arquivo = open("C:\\Future_Apperture\\Python\\exercícios_python\\exercíciosMiguel\\Curso_Em_Vídeo\\Exercícios_91-115\\Mundo_3_Ex_115\\dadospessoas.txt", "x")
except:
    print("Não foi possivel abrir o arquivo.")

# Menuzinho inicial
header()
showMenu()

while True:
    # Input do que o usuario quer fazer
    try:
        opcao = int(input("\nSua opção: "))
    
    except ValueError:
        print("\n\033[0;31mPor favor, digite um número inteiro válido.\033[0m\n")
        showMenu()
        continue

    # Usa a função dependendo do input anterior
    escolhas(opcao)

    # Caso o input seja '3', fecha o programa
    if opcao == 3:
        print("\n\033[7mSaindo do sistema, até logo.\033[0m")
        break