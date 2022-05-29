print('=-=' * 10)
print('    PROGRESSÃO GEOMÉTRICA')
print('-=-' * 10)

a1 = int(input('Primeiro termo: '))
q = int(input('Razão: '))
termo = a1
n = 1

while n <= 10:
    print('{} ¬ '.format(termo), end='')
    termo *= q
    n += 1

print('Fim')
soma = str(input('\n Deseja somar os termos da P.G? [S/N]')).upper()

if soma == 'S':
    an = a1 * pow(q, 10 - 1)
    s = (a1 * (pow(q, 10) - 1)) / (q - 1)
    print('A soma dos termos da P.G. é igual a {:.0f}'.format(s))
else:
    print('Fim do programa!')
