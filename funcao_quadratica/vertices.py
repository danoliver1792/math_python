a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))

delta = b * b - 4 * a * c

xv = -b / (2 * a)
yv = -delta / (4 * a)

print('Os vértices da parábola é o par ordenado ({:.0f}, {:.0f})'.format(xv, yv))



