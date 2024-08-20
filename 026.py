"""
Faça um programa que pergunte o preço de três produtos e informe qual produto
você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""
a = float(input("Digite o preço do produto 1: "))
b = float(input("Digite o preço do produto 2: "))
c = float(input("Digite o preço do produto 3: "))

if a < b and a < c:
    print(f"O produto com o menor preco é o 1, custando R${a:.2f}")
elif b < a and b < c:
    print(f"O produto com o menor preco é o 2, custando R${b:.2f}")
elif c < a and c < b:
    print(f"O produto com o menor preco é o 3, custando R${c:.2f}")