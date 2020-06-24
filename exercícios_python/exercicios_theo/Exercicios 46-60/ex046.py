from time import sleep

start = int(input('''\nDigite 0 para começar a contagem regressiva:
> '''))

print('')


if start == 0:
    for contagem in range(10, -1, -1):
        print(contagem)
        sleep(0.5)
    print('\nPOW POW PIW FELIZ ANO NOVO KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK')

else:
    print('Pra começar é 0, doente. ')