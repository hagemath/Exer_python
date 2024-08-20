"""
Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""
a = float(input("Digite um numero: "))
b = float(input("Digite outro numero: "))
c = float(input("Digite mais um numero: "))

if  (a > b > c):
    print(f"{a} > {b} > {c}")
elif (a > c > b):
    print(f"{a} > {c} > {b}")
elif (b > a > c):
    print(f"{b} > {a} > {c}")
elif (b > c > a):
    print(f"{a} > {a} > {a}")
elif (c > a > b):
    print(f"{c} > {a} > {b}")
elif (c > b > a):
    print(f"{c} > {b} > {a}")