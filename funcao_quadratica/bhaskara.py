Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import math

print('Este programa vai calcular as raízer de uma equação do segundo grau na forma ax²+bx+c=0')
a = ('Digite o valor de A: ')
b = ('Digite o valor de B: ')
c = ('Digite o valor de C: ')

delta = b*b - 4*a*c

if (delta < 0):
    print('Não tem raízes reais')
elif (delta == 0):
    x = -b / (2*a)
    print('Temos duas raízes iguais com solução {}'.format(x))
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print('Temos duas soluções para a equação: x1 = {:.0f} e x2 = {:.0f}'.format(x1, x2))