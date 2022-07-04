from random import randint

print('\033[4;31mVamos ver se o número digitado é par ou ímpar? \033[m')

numero = int(input('Digite um número: '))
resultado = numero % 2
vitoria = 0

if resultado == 0:
    print('O número {} é par'.format(numero))
else:
    print('O número {} é ímpar'.format(numero))

jogo = str(input('Gostaria de jogar PAR ou ÍMPAR? [S/N]')).upper()[0]

if jogo == 'S':
    while True:
        jogador = int(input('Diga um valor: '))
        pc = randint(0, 11)
        total = jogador + pc
        tipo = ' '
        while tipo not in 'PI':
            tipo = str(input('Par ou Ímpar? {P/I]')).strip().upper()[0]
        print(f'Você jogou {jogador} e o computador jogou {pc}. Total de {total} = ', end='')
        print('\033[33mDEU PAR\033[m' if total % 2 == 0 else '\033[33mDEU ÍMPAR\033[m')
        if tipo == 'P':
            if total % 2 == 0:
                print('\033[32mVocê venceu!\033[m')
                vitoria += 1
            else:
                print('\033[31mVocê perdeu!\033[m')
                break
        elif tipo == 'I':
            if total % 2 == 1:
                print('\033[32mVocê venceu!\033[m')
                vitoria += 1
            else:
                print('\033[31mVocê perdeu!\033[m')
                break
        print(f'Você venceu {vitoria} vezes')
else:
    print('Fim do programa!')
