#Faça um Programa que peça 2 números inteiros e um número real.
#Calcule e mostre:
#    o produto do dobro do primeiro com metade do segundo.
#    a soma do triplo do primeiro com o terceiro.
#    o terceiro elevado ao cubo.
n1 = int(input("Qual o primeiro número? "))
n2 = int(input("Qual o segundo número? "))
n3 = float(input("Qual o terceiro número? "))

eq1 = (2*n1)*(n2/2)
eq2 = (3*n1) + (n3)
eq3 = (n2**3)
print(f"{eq1}\n{eq2}\n{eq3}")