"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus
colaboradores e lhe contrataram para desenvolver o programa que calculará os
reajustes.

Faça um programa que recebe o salário de um colaborador e o reajuste segundo o
seguinte critério, baseado no salário atual:

    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante :
        aumento de 5% Após o aumento ser realizado,
    informe na tela:
        o salário antes do reajuste;
        o percentual de aumento aplicado;
        o valor do aumento;
        o novo salário, após o aumento.
"""
salario = float(input("Digite o seu salário para podermos fazer o calculo: "))
aumento = 0
if salario <= 280:
    aumento = 20
elif salario < 700:
    aumento = 15
elif salario < 1500:
    aumento = 10
elif salario >= 1500:
    aumento = 5
diferenca_salarios = salario * (aumento / 100)
salario_novo = salario + diferenca_salarios
print(f"Seu salário antes do reajuste era de R${salario:.2f}")
print(f"Seu salário foi aumentado em {aumento}%")
print(f"Seu salário foi aumentado em R${diferenca_salarios:.2f}")
print(f"Seu salário atual é de R${salario_novo:.2f}")