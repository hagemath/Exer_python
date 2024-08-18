#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
recebe_mes = float(input("Quando você recebe por hora? "))
horas_trabalhadas = int(input("Quantas horas são trabalhadas no mês? "))
print(f"O valor recebido por mês é de R${recebe_mes*horas_trabalhadas :.2f}")