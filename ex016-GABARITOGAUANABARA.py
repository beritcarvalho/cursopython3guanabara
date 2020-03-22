#pelo fato que neste programa utilizamos apenas uma uma função da biblioteca math, para o o programa nao ficar muito grande, ao invez de utilizarmos import math, utilizaremos from math import trunc
from math import trunc
num = float (input ("Digite um numero: "))
trun = trunc (num)
print ("O numero {} tem a parte inteira: {}.".format (num,trun))
