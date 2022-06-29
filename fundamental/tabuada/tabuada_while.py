while True:
    print('\033[35m-\033[m' * 30)
    print('\033[33m{:.^30}\033[m'.format('TABUADA'))
    print('\033[35m-\033[m' * 30)
    print('\033[31mApenas números naturais não nulos\033[m')
    number = int(input('Digite um número para saber sua tabuada: '))
    if number > 0:
        for cont in range(1, 11):
            print(f'{number} X {cont} = {number * cont}')
    if number <= 0:
        break
print('\033[31mFim do programa!\033[m')
