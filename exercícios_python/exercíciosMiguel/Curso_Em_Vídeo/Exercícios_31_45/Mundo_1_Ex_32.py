from datetime import date

ano = int(input("Digite o ano que deseja verificar ('0' caso queira verificar o ano atual): "))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0:
    print(f"\nO ano {ano} é bissexto.")

else:
    if ano % 400 == 0:
        print(f"\nO ano {ano} é bissexto.")
    else:
        print(f"\nO ano {ano} não é bissexto.")