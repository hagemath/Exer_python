"""
Faça um Programa para uma loja de tintas.

O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.

Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00
ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas
e os respectivos preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o preço seja o menor.
        Acrescente 10% de folga e sempre arredonde os valores para cima,
        isto é, considere latas cheias.
"""
metros_quadrados = float(input("Qual o tamanho [M²]? "))
litros_tinta = (metros_quadrados / 6) * 1.1
opcao = int(input(f"Qual opção seria a melhor? Voçe usará {litros_tinta}L de tinta\n"
                "Comprar apenas latas de 18 litros [1]\n"
                "Comprar apenas galões de 3,6 litros [2]\n"
                "Misturar latas e galões, de forma que o preço seja o menor[3]\n"
                ""
))
if opcao == 1:
    if litros_tinta <= 18:
        preco = 80
    else:
        preco = (litros_tinta/18) * 80
        preco * 1.1
elif opcao == 2:
    if litros_tinta <= 3.6:
        preco = 25*1.1
    else:
        preco = (litros_tinta/3.6) * 25
        preco *= 1.1
elif opcao == 3:
        r1 = int(litros_tinta)/int(18)
        r2 = (int(litros_tinta) - (int(r1 * 18)))/3.6
        preco = r1*80 + r2*25
        preco *= 1.1
print(f"O valor é de R${int(preco) :.2f}")