#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.
from random import shuffle
n1 = input ("Digite o nome do primeiro aluno: ")
n2 = input ("Digite o nome do segundo aluno: ")
n3 = input ("Digite o nome do terceiro aluno: ")
n4 = input ("Digite o nome do quarto aluno: ")
ordem = [n1,n2,n3,n4]
shuffle(ordem)
print ("")
print ("Quem irá apagar a lousa é o aluno (a)")
print (ordem)