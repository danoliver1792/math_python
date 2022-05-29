from math import factorial
from time import sleep

m = int(input('Digite o primeiro elemento: '))
p = int(input('Digite o segundo elemento: '))
c = factorial(m) / ((factorial((m - p))) * factorial(p))

print('Calculando...')
sleep(1)
print('A combinação de {} elementos {} a {} é igual a {:.0f}'.format(m, p, p, c))




