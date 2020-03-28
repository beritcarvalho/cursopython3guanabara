def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um numero: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()

print(f'F1={f1},F2={f2},F3={f3}')

#as funcoes tambem retornal valores logicos. ou strings

def par(numero=0):
    if numero % 2 == 0:
        return True
    else:
        return False

valor = int(input('Digite um numero: '))
if par(valor):
    print('É par!')
else:
    print('Não é par!')