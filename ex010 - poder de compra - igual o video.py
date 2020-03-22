print ('Crie um programa que diga quantos dolares voce pode comprar, com o seu dinheiro')
car = float (input ('Digite quantos R$ você tem: '))
dolar = float (input ('Digite o valor do dolar autalmente: '))
pod = (car*1)/dolar
print ('Com R${:.2f} reais, você pode comprar U${:.2f} dolar(s)'.format(car,pod))
