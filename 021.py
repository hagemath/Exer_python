"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""
letra = str(input("Digite F para feminino e M para masculino: "))
while len(letra) > 1:
    print("Queremos apenas a primeira letra [F/M]")
    letra = str(input("Digite F para feminino e M para masculino: "))
if letra == "F" or letra == "f":
    print("Feminino")
elif letra == "M" or letra == "m":
    print("Masculino")
else:
    print("Sexo inválido")
    