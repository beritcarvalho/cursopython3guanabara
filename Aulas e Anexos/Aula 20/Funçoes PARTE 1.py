def linha():
    print('------------------------------')

linha()
print(' SISTEMAS DE ALUNOS  ')
linha()
linha()
print('  CURSOS    ')
linha()
print('\n\n\n')

#funcoes é como criar uma especie de comando.
#uma rotina para ser exato, para quando precisar-mos repetir algo ou linhas de codigo, e com um comando realinhar varios comandos.
#toda função tem parentese depois.


#cria comandos personalizados.

#PARAMETROS

#com parametros podemos personalizar ainda mais, para se adequar melhor a nossa necessidade.

#exemplo:

print('------------------------------')
print('BERIT ARA SHALON DE CARVALHJO')
print('------------------------------')

print('------------------------------')
print('JOAO PAULO DE SOUSA')
print('------------------------------')

print('------------------------------')
print('JOAQUIM NABUCO DE OLIVEIRA')
print('------------------------------')

#nesse exemplo, percebemos que o que muda é apenas a mensagem de dentro, e as linhas personalizadas são iguais.
#dessa forma podemos criar um comando que mantenha as linhas, e altere apenas a mensagem. para assim não termos que ficar printando as linhas toda vez.

def mensagem(textodousuario):
    print('\n')
    print('------------------------------')
    print(textodousuario)
    print('------------------------------')
    print('\n')

#programa principal
mensagem('BERI ARA SHALON DE CARVALHO')

print('\n')
print('\n')
print('\n')
print('\n')
print('\n')


a = 4
b = 5
soma = a+b
print(soma)
print('\n')

a = 8
b = 9
soma = a+b
print(soma)
print('\n')

a = 3
b = 1
soma = a+b
print(soma)
print('\n')

print('\nagora com funçoes\n')

def soma(a, b):
    s = a+b
    print(f'{a} somado com {b} é igual a {s}')
    print('\n')


soma(4, 5)
soma(8, 9)
soma(2, 1)

def pulalinha():
    print('\n')
    print('\n')
    print('\n')
    print('\n')
    print('\n')


pulalinha()

#EMPACOTANDO PARAMENTOS

def contador(*num):
    tam = len(num)
    print(f'Voce digitou {num} ao todo são {tam} números')

contador(1,2,3)
contador(2,8,9,5)

pulalinha()

#trabalhando com lista

valores = [7,2,5,0,4]
print(valores)

#se quissemos dobrar cada valor de lista digitado

def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] = lista[pos]*2
        pos = pos+1
    print(lista)

dobra(valores)

pulalinha()


def soma_desempacotada(*valores):
    soma = 0
    for num in valores:
        soma = soma+num
    print(f'Somando os valores {valores} temos {soma}')


soma_desempacotada(0,2,3,8)
soma_desempacotada(1,8,9)
soma_desempacotada(7,23,6,9,2,1,4)