expressao = input("Digite uma operação matemática que possua parenteses:\n> ")

print("Sua expressão está correta!" if expressao.count('(') == expressao.count(')') else "Sua expressão está errada!")