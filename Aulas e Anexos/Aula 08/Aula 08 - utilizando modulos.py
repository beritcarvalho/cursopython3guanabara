#usando import usando todas funcionalidades
import math
num = int (input ('Digite um numero: '))
raiz = math.sqrt (num)
print ('A raiz de {} é igual {}'.format (num, raiz))
#Arredondar para cima é ceil
print ('A raia de {} arrendodado para cima é {}'.format (num, math.ceil (raiz)))
#Arredondar para cima é floor
print ('A raia de {} arrendodado para baixo é {}'.format (num, math.floor (raiz)))
#mostrando apenas com 2 casas decimais
print ('A raiz de {} é igual {:.2f}'.format (num, raiz))
