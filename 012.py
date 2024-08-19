#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
altura = float(input("Qual é o sua altura? [EX:1.75] "))
calculo = (72.7*altura) - (58)
print(f"Seu peso ideial é de {calculo :.2f}Kg")
