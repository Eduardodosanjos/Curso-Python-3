import random

def jogar():
    print("*********************************")
    print("Bem Vindo ao Jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("\nQual nível de dificuldade?")
    print("(1) Fácil\n(2) Médio\n(3) Difícil")

    nivel = int(input("Defina o nível: "))
    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5
    print("")

    for rodada in range(1, total_de_tentativas + 1):
        print(f'Tentativa {rodada} de {total_de_tentativas}')

        chute = int(input("Digite um número entre 1 e 100: "))
        print(f'Você digitou: {chute}')

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print(f'Você Acertou e fez {pontos} pontos!')
            break
        else:
            if maior:
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif menor:
                print("Você errou! O seu chute foi menor do que o número secreto.")
            pontos -= (abs(numero_secreto - chute))

    print("Fim do Jogo")

if __name__ == "__main__":
    jogar()