cidade = input("\nDigite o nome da cidade: ").lower()

if "santo" in cidade:
    print(f"\nA cidade {cidade.title()} possui a palavra 'Santo'")
else:
    print(f"\nA cidade {cidade.title()} NÃO possui a palavra 'Santo'")