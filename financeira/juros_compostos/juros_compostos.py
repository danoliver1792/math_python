import math

print('=' * 30)
print('{:^30}'.format('Juros Compostos'))
print('=' * 30)

print('\033[31mEscolha uma opção abaixo:\033[m')

opcao = int(input('''O que deseja calcular? 
[1] Montante (m)
[2] Capital (c)
[3] Taxa (i)
[4] Período (n)
Escolha uma opção: '''))

if opcao == 1:
    c = float(input('Qual o valor do capital? R$ '))
    i = float(input('Qual a taxa de juros? (%) '))
    t = float(input('Quantos meses? (t) '))
    m = c * pow((1 + (i / 100)), t)
    print(f'''Aplicando um capital de R$ {c:.2f} no período de {t:.0f} meses com taxa de juros de {i:.2f}% ao mês
     resulta num montante de R$ {m:.2f}''')
    juros = str(input('Deseja calcular os juros? [S/N]')).strip().upper()[0]
    if juros == 'S':
        j = m - c
        print(f'O valor dos juros é igual a R$ {j:.2f}')
    else:
        print('Fim do programa!')
if opcao == 2:
    m = float(input('Qual o valor do montante? R$ '))
    i = float(input('Qual a taxa de juros? (%) '))
    t = float(input('Quantos meses? (t)'))
    c = m / pow((1 + (i / 100)), t)
    print(f'''Para resultar um montante de R$ {m:.2f} no período de {t:.0f} meses com taxa de juros de {i:.2f}% ao mês
deve-se aplicar um capital de R$ {c:.2f}''')
    juros = str(input('Deseja calcular os juros? [S/N}')).strip().upper()[0]
    if juros == 'S':
        j = m - c
        print(f'O valor dos juros é igual a R$ {j:.2f}')
    else:
        print('Fim do programa!')
if opcao == 3:
    c = float(input('Qual o valor do capital? R$ '))
    m = float(input('Qual o valor do montante? R$ '))
    t = float(input('Quantos meses? (t) '))
    i = (pow((m / c), 1 / t) - 1) * 100
    print(f'''Com um capital de R$ {c:.2f}, montante de R$ {m:.2f} e um período de {t:.0f} meses
temos uma taxa de juros de {i:.2f}% ao mês''')
if opcao == 4:
    c = float(input('Qual o valor do capital? R$ '))
    m = float(input('Qual o valor do montante? R$ '))
    i = float(input('Qual a taxa de juros? (%) '))
    t = math.log((m / c)) / math.log(1 + (i / 100))
    print(f'''Com um capital de R$ {c:.2f}, montante de R$ {m:.2f} e uma taxa de {i:.2f}% ao mês
temos um período de {t:.0f} meses''')
