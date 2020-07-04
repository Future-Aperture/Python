#dentro do string -> \033[style];[text];[back]

def titulo():
    print('\033[32m', "~" * 30)
    print(f'{"Sistema de Ajuda PyHELP":<8}')
    print("~" * 30, '\033[0m')

def ajuda(comando):
    print(f"\n\033[0;31mAs informações de ajuda do comando {comando} são:\033[0m\n")
    help(comando)


titulo()

while True:
    cmd = input("\nDigite o comando que deseja pesquisar [Digite 'FIM' para sair]:\n> ").lower()

    if cmd != "fim":
        ajuda(cmd)
    else:
        break