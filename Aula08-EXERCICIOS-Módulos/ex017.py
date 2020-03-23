#Faça um programa que leia o comprimento de cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.
import math
opo = float (input ("Digite o cateto oposto: "))
adj = float (input ("Digite o cateto adjacente: "))
print ("a² = b² + c²")
print ("a² = {}² + {}²".format (opo,adj))
b = pow (opo,2)
c = pow (adj,2)
a = b+c
print ("a² = {} + {}".format (b,c))
print ("a² = {}".format (a))
print ("a = √{}".format (a))
a = math.hypot (opo,adj)
print ("a = {}".format (a))