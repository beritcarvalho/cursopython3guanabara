frase = input ("Escreva uma frase: ").strip()
frase = frase.upper ()
print ("A letra A aparece %s na frase" % (frase.count ("A")))
#em python, as casas de strings contam a partir do 0
#se digita-se amanda, apareceria na posicao 0
#para nao ficar estranho para o usuario, colocaremos +1, para facilitar o entendimento na hora que aparecer na tela
print ("Primeira vez em na posição %s" %(frase.find ("A")+1))
print ("E a ultima vez na posição %s" % (frase.rfind ("A")+1))

