print("Bem vindo ao jogo de adivinhação")
print("********************************")

import random

chute = int(random.random() * 100)
tentativa = 3

for rodada in range (1, tentativa + 1):
    # print("Voce esta na rodada ",rodada, "de ", tentativa)

    print("Voce esta na rodada {} de {}".format(rodada,tentativa))
    print("")
    numero = input("Digite um numero de 1 á 100: ")
    numero_int = int(numero)

    maior = numero_int > chute
    menor = numero_int < chute
    acertou = numero_int == chute
    dentro_intervalo = numero_int < 101 and numero_int != 0

    if dentro_intervalo:
        if acertou:
            print("")
            print("Voce acertou parabens")
            # Se acertar eu paro o laço do while
            break
        else:
            if maior:
                print("Voce digitou um numero maior, mais sorte na proxima")
            elif menor:
                print("Voce digitou um numero menor, mais sorte na proxima")
    else:
        print("Voce digitou um numero fora do intervalo...")
        print("")
        print("Na proxima digite um numero de 1 á 100")

print("")
print("Fim de jogo")
print("")
print("O numero era: ", chute)