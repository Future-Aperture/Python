palavra = input("Digite uma palavra: ")

print("\nQue tipo de variavel é?", type(palavra))
print("É apenas espaços?", palavra.isspace())
print("É um número?", palavra.isnumeric())
print("É alfabético?", palavra.isalpha())
print("É alfanumérico?", palavra.isalnum())
print("É em letras minuscúlas?", palavra.islower())
print("É em letras masiúsculas?", palavra.isupper())
print("É capitalizada?", palavra.istitle())


