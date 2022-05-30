print('\033[4;31mVamos ver se o número digitado é par ou ímpar? \033[m')

numero = int(input('Digite um número: '))
resultado = numero % 2
pc = randint(0, 5)

if resultado == 0:
    print('O número {} é par'.format(numero))
else:
    print('O número {} é ímpar'.format(numero))