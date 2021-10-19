print("*********************************")
print("Bem Vindo ao Jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while rodada <= total_de_tentativas:
    print(f'Tentativa {rodada} de {total_de_tentativas}')
    chute = int(input("Digite o seu número: "))
    print(f'Você digitou: {chute}')

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Você Acertou!")
    else:
        if maior:
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif menor:
            print("Você errou! O seu chute foi menor do que o número secreto.")

    rodada += 1

print("Fim do Jogo")