#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

#Primeiro nos criamos 4 variaveis que irá receber 4 vaores do tipo float
#Foi usado o split somente para treinar, mas n precisava
n1, n2, n3, n4 = input(f"Digite a nota: ").split(" ")
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)
media = ((n1+n2+n3+n4))/4
print(f"A média foi de {media}")