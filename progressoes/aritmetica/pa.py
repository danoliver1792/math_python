print('=-=' * 10)
print('    PROGRESSÃO ARITMÉTICA')
print('-=-' * 10)

a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = a1
n = 1

while n <= 10:
    print('{} ¬ '.format(termo), end='')
    termo += r
    n += 1

print('Fim')
soma = str(input(' \n Deseja somar os termos da P.A.? [S/N]')).upper()

if soma == 'S':
    an = a1 + (10 - 1) * r
    s = (a1 + an) * 10 / 2
    print('A soma dos termos da P.A. é igual a {:.0f}'.format(s))
else:
    print('Fim do programa!')

