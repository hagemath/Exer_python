"""
Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.

Considere que a cobertura da tinta é de 1 litro para cada 3 metros
quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.

Informe ao usuário a quantidades de latas de tinta
a serem compradas e o preço total.
"""
metros_quadrados = float(input("Qual o tamanho [M²]? "))
litros_tinta = metros_quadrados / 3
if litros_tinta <= 18:
    preco = 80
else:
    preco = (litros_tinta/18) * 80
print(f"Voçe precisa de {litros_tinta :.2f}L de tinta e irá custar R${preco :.2f}")