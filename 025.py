"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""
a = float(input("Digite o numero a: "))
b = float(input("Digite o numero b: "))
c = float(input("Digite o numero c: "))

if a > b and a > c:
    maior = a
elif b > a and b > c:
    maior = b
elif c > a and c > b:
    maior = c
elif a < b and a < c:
    menor = a
elif b < a and b < c:
    menor = b
elif c < a and c < b:
    menor = c



