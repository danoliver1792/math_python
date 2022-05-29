from math import hypot

catetooposto = float(input('Comprimento do cateto oposto: '))
catetoadjascente = float(input('Comprimento do cateto adjascente: '))
hipotenusa = hypot(catetooposto, catetoadjascente)

print('A hipotenusa vale {:.2f}'.format(hipotenusa))

