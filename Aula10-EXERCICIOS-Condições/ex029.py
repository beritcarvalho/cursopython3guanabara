print ("RADAR DE VELOCIDADE\nLIMITE: 80km/h")
num = int (input ("Qual a velocidade do carro? "))
if num > 80:
    multa = (num-80)*7
    print ("Você foi muiltado. Sua multa custará o valor de R$ %.2f" % (multa))