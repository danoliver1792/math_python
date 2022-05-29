from math import radians, sin, cos
from time import sleep

print('-' * 36)
print('RELAÇÃO FUNDAMENTAL DA TRIGONOMETRIA')
print('-' * 36)
angulo = int(input('Digite o ângulo: '))

print('''Escolha a opção:
[ 1 ] Seno
[ 2 ] Cosseno
''')

opcao = int(input('Qual opção? '))

if opcao == 1:
    cosseno = 1 - (sin(radians(angulo)))**2
    print('temos sen²{}º + cos²x = 1'.format(angulo))
    print('Calculando...')
    sleep(0.5)
    print('{:.2f}'.format(cosseno))
elif opcao == 2:
    seno = 1 - (cos(radians(angulo)))**2
    print('temos sen²x + cos²{} = 1'.format(angulo))
    print('Calculando...')
    sleep(0.5)
    print('{:.2f}'.format(seno))
else:
    print('Opção inválida!')
