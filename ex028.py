import random
comp = random.randint (0,5)
print ("""Jogo da advinhação!\nO computador ja escolheu um numero que vai do 0 ao 5.\nDigite qual número de 0 a 5 você acha que o computador escolheu.""")
user = int (input ())
if comp == user:
    print ("Parabéns, você Acertou!!!")
else:
    print ("Que pena, você Errou!!!")