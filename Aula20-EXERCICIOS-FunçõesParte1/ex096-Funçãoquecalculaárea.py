larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))

def calc_area():
    area = larg*comp
    print(f'A área de um terreno {larg:.1f}m x {comp:.1f}m é de {area:.1f}m².')

calc_area()