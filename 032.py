"Desenvolva um jogo de acerte o número, onde o computador escolhe um número inteiro aleatório de 0 a 10, e o usuário tem 5 tentativas para adivinhar o número"
import random #importamos a biblioteca
numero_pc = random.randint(0, 10) #pedmos para ela escolher um número aleatório entr 0 e 10 e armazenar

def jogar ():
    numero_pc = random.randint(0, 10) #pedmos para ela escolher um número aleatório entr 0 e 10 e armazenar
    i = 0 #numero tentativas
    pc = 0 #pontos pc
    jogador = 0 #pontos jogador
    nome = str(input("Digite seu nome: "))
    print(f"Olá {nome}, eu sou a Ariza e irei te ensinar a jogar esse jogo... Eu irei escolher um numero entre 0 e 10, aleatório e você tem 5 tentativas de acertar o número que eue escolhi.")
    
    while i < 5:
        numero_jogador = int(input("Digite o seu número [0 - 10]: "))
        while numero_jogador < 0 or numero_jogador > 10:
            print('O número tem que ser entre 0 e 10, tente novamente')
            numero_jogador = int(input("Digite o seu número [0 - 10]: "))
        if numero_jogador == numero_pc:
            print(f"Você acertou o número que o computador escolheu {numero_pc}, parabéns")
            jogador += 1
            break
        else:
            i += 1
            pc += 1
            print(f"O número não esta correto tente novamente, você tem mais {5-i} tentativa(s) restante(s)")
        print(f"O placar esta {nome}: {jogador} x Azira: {pc}")
while True:
    jogar()
    resposta = input("Você quer jogar novamente? (S/N): ").upper()
    if resposta == 'N' or resposta == "NÃO":
        print("Obrigado por jogar! Até a próxima.")
    while resposta != "SIM" or resposta != "NÃO" or resposta != "S" or resposta != "N":
        print("A resposta deve ser sim ou não [S/N]")
        resposta = input("Você quer jogar novamente? (S/N): ").upper()
        break

        