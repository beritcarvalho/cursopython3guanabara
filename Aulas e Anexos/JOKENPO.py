from random import randint
from time import sleep
print ("="*21)
print ("=== J O K E N P O ===")
print ("="*21)

comp = ("PEDRA","PAPEL","TESOURA")
escolha = comp[randint(0,2)]
print ("O computador escolheu!\n") 
user = str(input("Sua vez, escolha: PEDRA, PAPEL ou TESOURA: \n").upper()).strip()


while escolha == user or user != str("PEDRA") and user != str ("PAPEL") and user != str("TESOURA"):
    if escolha == user:
        print ('\n')
        print ('JO')
        sleep(0.5)        
        print ('KEN')
        sleep(0.5)
        print ('PO')
        sleep(1)
        print ("\nEmpate! Escolha novamente: \nO computador trocou a mão!\n")
    else:
        print ("\nINVALIDO, Escolha: PEDRA, PAPEL ou TESOURA: \nO computador trocou a mão!\n")
    user = str(input("Sua vez, escolha: PEDRA, PAPEL ou TESOURA: \n").upper()).strip()
    comp = ("PEDRA","PAPEL","TESOURA")
    escolha = comp[randint(0,2)]
    
print ('\n')
print ('JO')
sleep(0.5)        
print ('KEN')
sleep(0.5)
print ('PO')
sleep(1)

print ('\n')

if user == str("PEDRA") and escolha == str("TESOURA"):
    print ("O computador escolheu {}, Você Ganhou".format (escolha))
elif user == str("PAPEL") and escolha == str("TESOURA"):
    print ("O computador escolheu {}, Você Perdeu".format (escolha))
elif user == str("TESOURA") and escolha == str("PEDRA"):
    print ("O computador escolheu {}, Você Perdeu".format (escolha))
elif user == str("PAPEL") and escolha == str("PEDRA"):
    print ("O computador escolheu {}, Você Ganhou".format (escolha))
elif user == str("TESOURA") and escolha == str("PAPEL"):
    print ("O computador escolheu {}, Você Ganhou".format (escolha))
elif user == str("PEDRA") and escolha == str("PAPEL"):
    print ("O computador escolheu {}, Você Perdeu".format (escolha))
