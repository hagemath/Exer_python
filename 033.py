notas = []
quantas_notas = int(input('Quantas notas você quer adicionar? '))
def adicionar_notas(quantas_notas):
    i = 0
    for i in range (0, quantas_notas):
        notas.append(float(input("Digite a nota: ")))
    print(notas)
def calcular_media():
    adicionar_notas(quantas_notas)
    print(f"A média das notas é {sum(notas)/len(notas)}")

calcular_media()