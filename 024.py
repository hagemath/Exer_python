"""
Faça um Programa que leia três números e mostre o maior deles.
"""
a = float(input("Digite o numero a: "))
b = float(input("Digite o numero b: "))
c = float(input("Digite o numero c: "))
if a > b and a > c:
    print(f"O {a} é maior")
elif b>a and b>c:
    print(f"O {b} é o maior")
elif c>a and c>b:
    print(f"O {c} é o maior")
elif a == b == c:
    print("Eles são iguais")