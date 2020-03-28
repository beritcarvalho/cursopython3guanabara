#Exercício Python #102 - Função para Fatorial
#Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num,show=False):
  """-> Calcula o Fatorial de um numero.
  : para num: O número a ser calculado
  : para show: (opcional) Mostrar ou não a conta.
  : return: O valor do Fatorial de num.
  """
  print(20*'-')
  total = 1
  escrita = ''
  for c in range(num, 1, -1):#contagem reversa
    total = total*c
    if show == True:
      print(c, end=' x ')
  if show == True:
    print('1',end=' = ')
  return total


print(fatorial(5,True))
print(fatorial(5))
