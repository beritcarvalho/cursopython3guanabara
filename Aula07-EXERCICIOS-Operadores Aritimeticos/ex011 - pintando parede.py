alt = float (input ('Digite a altura: '))
lar = float (input ('Digite a largura: '))
are = alt*lar
tin = 2
lit = int (((are*1)/tin)+0.5)
print ('Sua area é {}m², para pintar essa area, você irá precisar de {} litros'.format (are,lit))
