import math
ang = float (input ("Digite um angulo: "))
seno = math.sin(math.radians(ang))
coss = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print ("O ângulo {:.2f} tem o seno de {:.2f}.".format (ang,seno))
print ("O ângulo {:.2f} tem o conseno de {:.2f}".format (ang,coss))
print ("O ângulo {:.2f} tem a tangente de {:.2f}".format (ang,tang))