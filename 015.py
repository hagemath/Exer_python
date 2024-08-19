"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês.

Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:

    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido.
"""
ganha_hora = float(input("Quanto você recebe por hora? "))
hora_trabalhada = int(input("Quantas horas voçe trabalha no mês? "))
salario_bruto = ganha_hora * hora_trabalhada
imposto_de_renda = 0.11 * salario_bruto
inss = 0.08 * salario_bruto
sindicato = 0.05 * salario_bruto
salario_liquido = salario_bruto - (imposto_de_renda + inss + sindicato)
print(
    f"+ Salário Brunto: R${salario_bruto :.2f}\n"
    f"- IR (11%): R${imposto_de_renda :.2f}\n"
    f"- INSS (8%): R${inss :.2f}\n"
    f"- Sindicato (5%): R${sindicato :.2f}\n"
    f"= Salário Liquido: R${salario_liquido :.2f}"
)