#5 - Crie um programa que solicite 3 notas do aluno (Av1, Av2, Av3), descarte a menor nota e exiba a média do aluno, informando se o mesmo foi aprovado ou não.
n1 = float (input('Digite a nota da AV1: '))
print('A nota da AV1 é {:.2f}'.format (n1))
n2 = float (input ('Digite a nota da AV2: '))
print ('A nota da AV2 é {:.2f}'.format (n2))
n3 = float (input('Digite a nota da AV3: '))
print ('A nota da AV3 é {:.2f}'.format (n3))
if (n1 == n2 == n3):
    m = (n1+n2+n3)/3
    print ('A sua média é {:.2f}'.format (m))
else:
        if (n1 < n2) and (n1 < n3):
            m = (n2 + n3)/2
            print ('A sua média é {:.2f}'.format (m))
        else:
                if (n2 < n1) and (n2 < n3):
                    m = (n1 + n3)/2
                    print ('A sua média é {:.2f}'.format (m))
                else:
                        if (n3 < n1) and (n3 < n2):
                            m = (n2 + n1)/2
                            print ('A sua média é {}'.format (m))
if (m >=6):
    print ('Com media {:.2f}, você está Aprovado'.format (m))
else:
    print ('Com media {:.2f}, você está Reprovado'.format (m))
