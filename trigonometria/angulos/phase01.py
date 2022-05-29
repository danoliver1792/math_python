from math import radians, sin, cos, tan

angulo = float(input('Digite o ângulo: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('''Para o ângulo de {:.0f}°, temos:
seno igual a {:.2f}
cosseno igual a {:.2f}
tangente igual a {:.2f}.'''.format(angulo, seno, cosseno, tangente))
