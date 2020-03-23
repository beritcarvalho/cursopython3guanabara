lista = []
for c in range(0,5):
    lista.append(int(input(f'Digite um numero para posição {c}: ')))
  
print(f'O maior valor digitado foi {max(lista)} nas posições ',end='')
for c in range(0,(len(lista))):
    if lista[c] == max(lista):
        print(c,end='...')
print(end='\n')
print(f'O menor valor digitado foi {min(lista)} nas posições ',end='')
for c in range(0,(len(lista))):
    if lista[c] == min(lista):
        print(c,end='...')
