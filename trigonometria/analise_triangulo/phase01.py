a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))

if a < b + c and b < a + c and c < b + c:
    print('Os segmentos {:.0f}, {:.0f} e {:.0f} podem formar um triângulo'.format(a, b, c))
    if a == b == c:
        print('Triângulo equilátero')
    elif a != b != c != a:
        print('Triângulo escaleno')
    else:
        print('Triângulo isósceles')
else:
    print('Os segmentos não podem formar um triângulo')
