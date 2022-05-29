import math

print('    Bem-vindos ao programa')
print('=-=' * 10)
print(('       GEOMETRIA PLANA'))
print('=-=' * 10)

cor = 'Todas as medidas devem estar em metro (m)'

print('''O que deseja calcular? 
[ 0 ]Conversor
[ 1 ]Área
\033[31m{}\033[m'''.format(cor))

print('=-=' * 10)
opcao = int(input('Digite uma opção: '))

if opcao == 1:
    print(''' 
    [ 1 ]Quadrado
    [ 2 ]Retângulo
    [ 3 ]Paralelogramo
    [ 4 ]triângulo
    [ 5 ]Trapézio
    [ 6 ]Losango
    [ 7 ]Círculo''')

    escolha = int(input('Escolha um polígono: '))
    if escolha == 1:
        quad_a = float(input('Qual é a medida? (a) '))
        areaquad = pow(quad_a, 2)
        print('A área do quadrado é igual a {:.2f}m²'.format(areaquad))
    if escolha == 2:
        retan_b = float(input('Qual a medida da base? (b) '))
        retan_h = float(input('Qual a medida da altura? (h) '))
        area_retan = retan_b * retan_h
        print('A área do retângulo é igual a {:.2f}m²'.format(area_retan))
    if escolha == 3:
        paralel_b = float(input('Qual a medida da base? (b) '))
        paralel_h = float(input('Qual a medida da altura? (h) '))
        area_paralel = paralel_h * paralel_b
        print('A área do paralelogramo é igual a {:.2f}m²'.format(area_paralel))
    if escolha == 4:
        tri_b = float(input('Qual a medida da base? (b) '))
        tri_h = float(input('Qual a medida da altura? (h) '))
        area_tri = (tri_b * tri_h) / 2
        print('A área do triângulo é igual a {:.2f}m²'.format(area_tri))
    if escolha == 5:
        trap_bb = float(input('Qual a medida da base maior? (B) '))
        trap_b = float(input('Qual a medida da base menor? (b) '))
        trap_h = float(input('Qual a medida da altura? (h) '))
        area_trap = (trap_bb + trap_b) * trap_h / 2
        print('A área do trapézio é igual a {:.2f}m²'.format(area_trap))
    if escolha == 6:
        los_dd = float(input('Qual a medida da diagonal maior? (D) '))
        los_d = float(input('Qual a medida da diagonal menor? (d) '))
        area_los = (los_dd * los_d) / 2
        print('A área do losango é igual a {:.2f}m²'.format(area_los))
    if escolha == 7:
        circ_diametro = float(input('Qual é o diâmetro da circunferência? '))
        circ_r = circ_diametro / 2
        area_circ = math.pi * pow(circ_r, 2)
        print('A área do círculo é igual a {:.2f}m²'.format(area_circ))
    else:
        print('\033[31mEscolha uma opção válida!')
else:
    print('\033[31mOpção inválida!')
