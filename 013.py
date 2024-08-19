"""
Tendo como dado de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7
"""
altura = float(input('Qual a sua altura? [EX:1.75] '))
sexo = str(input("Qual o seu sexo? [M/F]"))
while len(sexo) > 1:
    print("Coloque apenas F para feminino e M para masculino")
    sexo = str(input("Qual o seu sexo? [M/F] "))
if sexo == "F" or sexo == "f":
    calculo_mulher = (62.1*altura) - 44.7
    print(f"Seu peso ideal é de {calculo_mulher :.2f}Kg")
else:
    calculo_homem = (72.7*altura) - 58
    print(f"Seu peso ideal é de {calculo_homem :.2f}Kg")
