#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = int(input("Qual a dimensão do lado do quadrado? "))
area = (lado**2)
print(f"A área do quadrado é de {area}m² e o quadrado da sua área é de {(area)**2}m²")