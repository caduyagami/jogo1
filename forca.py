def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palabra_secreta = 'eu'.upper()
    lista_palavra = ['_' for letra in palabra_secreta]
    enforcou = False
    acertou = False
    erros = 0

    print(lista_palavra)

    # enquanto verdadeiro continua do laço.
    while(not enforcou and not acertou):
        print ('Jogando....')
        chute = input('Qual a letra? ')
        chute = chute.strip().upper() # Tiro o espaço e transformo em maiuscula

        if chute in palabra_secreta:
            index = 0
            for letra in palabra_secreta:
                if(chute == letra):
                    lista_palavra[index] = chute
                    print('Voce acertou a letra {}'.format(chute))
                    print(lista_palavra)
                index = index + 1
        else:
            erros += 1 # += tipo de incremento
            print('Voce erro a letra e esta na tentativa {} de 6'.format(erros))
        enforcou = erros == 6
        acertou = '_' not in lista_palavra
    if acertou:
        print('Voce acertou!!! parabens!!!')
    else:
        print('Voce errou, mais sorte na proxima')

    print("Fim do jogo")
if(__name__ == '__main__'):
    jogar()