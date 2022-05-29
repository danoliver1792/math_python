c = float(input('Qual o valor do capital? '))
i = float(input('Qual é a taxa de juros? '))
n = float(input('Qual é o período? '))

juros = c * (i / 100) * n
m = juros + c
print('O valor dos juros corresponde a uma aplicação de R$ {:.2f}, em um período de {:.0f} meses com taxa de {}% ao mês é igual a R$ {:.2f}'.format(c, n, i, juros))
print('O montante da aplicação será de R$ {:.2f}'.format(m))

