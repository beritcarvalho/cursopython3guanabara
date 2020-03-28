#INTERACTIVE HELP
#serve para termos uma especie de ajuda ou especificaçoes de como funciona determinada funçao.\
#como funciona ou para que serve


#outra maneira de saber especificaçoes de funçao
#podemos usar o doc da funçao
#para usar, deve se utilizar __doc__
#exemplo:
#print(__doc__)

def contador (i,f,p):
    c = i
    while c<= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')

contador(2,10,2)

help(contador)
#--------------------------------------------------------------
#DOCSTRINGS
#como programadores, temos que nao so programar de forma que nos entendemos e sim de forma com que todos programadores entendam.
#muitas vezes em nosso programa, teremos de criar funcoes, mas nem todos que utiliziarem nosso programa saberao para que serve a funcao que criamos ou como utiliza-las.
#assim podemos criar uma especie de tutorial embutida em nossas funcoes.
#essa especie de manual, chamamos de docstrings.
#elas ficam uma linha apos a definicao de funcao.
#para cria-las fazemo desta forma:
#apos a linha de funcao colocamos 3 aspas duplas (") escrevemos o que precisamos e as fechamos.
def contador1 (i,f,p):
    """FUNCAO CRIADA PARA EXEMPLIFICAR COMO FUNCIONA AS DOCSTRINGS.
    i = valor inicial
    f = valor final
    p = valor de quanto em quanto a contagem sera realizada
    return: sem retorno

    FUNCAO CRIADA POR BERIT CARVALHO
    OBRIGADO POR UTILIZA-LA"""
    c = i
    while c<= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')


help(contador1)

#-------------------------------------------------------------------------------------
#PARAMETROS OPCIONAIS:

#quandop criamos uma funcao parametral, definimos a quantidade de parametros a serem utilizadas
#quando chamamos a funcao e colocamos uma quantidade parametros maior ou inferior a quantiidade que defimos, isso causa um problema.
#é possivel, deixarmos os parametros com valores pre definifos, que alteram quando o usuario informa valor, caso o usuario nao informe, o parametro permanece com o valor que pre-definimos, evitando problemas no codigo.

#EXEMPLO

def somar(a=0,b=0,c=0):
    s = a + b + c
    print(f'A soma vale {s}')

somar(2,5)
#note que informamos so dois valores e mesmo assim ele realizou a conta sem dar erro na compilaçao

print('\n')
print('\n')
print('\n')
#------------------------------------------------------------------------------------
#ESCOPO VARIAVEIS

#na programacao escopo é como se fosse o lugar onde a variavel existe.
#EXEMPLO

def teste():
    print(f'Na função, n vale {n}')

#PROGRAMA PRINCIPAL
n= 2
print(f'No programa principal, n vale {n}')

teste()


a = 5

def teste1(b):
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


teste1(a)
print(f'A fora vale {a}')


def teste3(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


teste3(a)
print(f'A fora vale {a}')
print('\n')
print('\n')
print('\n')

#---------------------------------------------------------------
#RETORNO DE VALORES

#quando usamos funcoes, todo calculo e variavel acontece dentro da funcao.
#ou seja a variavel existe apenas dentro da funcao
#quando quizermos o valor da variavel de dentro da funcao nao e possivel obtela desta forma:

def soma(a=0,b=0,c=0):
    s = a + b + c
    print(f'A soma vale {s}')

soma(1,2)

#assim nao funcionaria:
# valor_da_soma = soma(1,2) <- desta forma daria um erro no codigo.
# se quissemos obter o valor da soma teriamos de usar o retorno de resultado.

#assim teriamos que mudar a definicao da funcao e acrescentar o return.

def soma_retorno(a=0,b=0,c=0):
    s = a + b + c
    return s
    print(f'A soma vale {s}')


resultado = soma_retorno(1,2)
print(resultado)