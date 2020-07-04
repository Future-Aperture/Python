def notas(*notasLista, sit = False):
    """
    Função para calcular a quantidade de notas, média, maior e menor e a situação dá media da turma.
    :param *nota: Notas do aluno.
    :param sit: Situação da turma, dependendo da média. Default = False
    :return: Dicionario com todas as informações.
    """

    # Calcula a média
    media = round(sum(notasLista) / len(notasLista), 1)

    # Dicionario com as informações
    ficha = {"quantidade": len(notasLista), "maior": max(notasLista), "menor": min(notasLista), "media": media}

    # Altera a situação dependendo da média
    if sit:
        if media < 6:
            situaVar = "RUIM"
        elif media > 7:
            situaVar = "BOA"
        else:
            situaVar = "RAZOÁVEL"
        ficha["situacao"] = situaVar

    return ficha


resp = notas(9.6, 10, 5.3, 2.3, 4, sit = True)
print(resp)