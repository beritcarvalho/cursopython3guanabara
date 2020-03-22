val = float (input('Digite o valor do produto: '))
per = float (input ('Digite percentual de desconto: '))
des = ((val*per)/100)
tot = val-des
print ('Voce fez {}% de desconto'.format (per))
print ('total de desconto {:.2f}'.format(des))
print ('Valor do produto com desconto {:.2f}'.format (tot))
