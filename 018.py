"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""
tamanho = float(input("Qual o tamanho do arquivo [Mb]? "))
velocidade = float(input("Qual a velocidade da internet [Mbps]? "))
tempo = tamanho / velocidade
horas = tempo // 60
minutos = tempo % 60
segundos = minutos % 60
print(f"O programa irá demorar {horas :.0f}:{minutos :.0f}")