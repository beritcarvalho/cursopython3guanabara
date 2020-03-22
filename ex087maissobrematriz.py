linha = list()
coluna = list()
matriz = list()
pares = 0
soma = 0

#lina
for poslin in range(0, 3):
  for poscol in range(0, 3):
    valor = int(input(f'Digite um valor para [{poslin}, {poscol}]: '))
    coluna.insert(poscol, valor)
  
  
  linha.insert(poslin, coluna[:])
  coluna.clear()
  
matriz = linha[:]

print('=-'*30)
for linmat in matriz:
  for colmat in linmat:
    print(f'[{colmat:^5}]',end='')

    #soma dos valores pares
    if colmat % 2 == 0:
      pares += colmat
      
  print('')
print('=-'*30)



print(f'A soma dos valores pares é {pares}')

for c in range(0,3):
  soma += matriz[c][2]
print(f'A soma dos valores da terceira coluna é {soma}')


print(f'O maior valor da segunda linha é {max(matriz[1])}')
