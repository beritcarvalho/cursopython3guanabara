Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #5 - Crie um programa que solicite 3 notas do aluno (Av1, Av2, Av3), descarte a menor nota e exiba a média do aluno, informando se o mesmo foi aprovado ou não.
n1 = float (input('Digite a nota da AV1: '))
print('A nota da AV1 é {}'.format (n1))
n2 = float (input ('Digite a nota da AV2: '))
print ('A nota da AV2 é {}'.format (n2))
n3 = float (input('Digite a nota da AV3: '))
print ('A nota da AV3 é {}'.format (n3))
if (n1<n2) and (n1<n3):
    m = (n2+n3)/2
    print ('primeira condicao n1 menor nota', m)
else:
    if (n2 < n1) and (n2 < n3):
        m = (n1 + n3) / 2
        print('segunda condicao n2 menor nota', m)
    else:
        if (n3 < n1) and (n3 < n2):
            m = (n1 + n2) / 2
            print('terceira condicao n3 menor nota', m)
