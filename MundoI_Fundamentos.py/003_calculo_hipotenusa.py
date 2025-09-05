# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo 
# retangulo. Calcule e mostre o comprimento da hipotenusa.

#Cálculo sem uso da biblioteca math 

cateto_oposto = float(input("Qual o comprimento do cateto oposto? "))
cateto_adjacente = float(input("Qual o comprimento do cateto adjacente? "))

hipotenusa = (cateto_oposto**2 + cateto_adjacente**2)**(1/2)

print(f"Sendo o comprimento do cateto oposto {cateto_oposto} e do cateto adjacente {cateto_adjacente} o comprimento da hipotenusa é {hipotenusa:.2f}.")

#Cálculo usando a biblioteca math

from math import hypot

cateto_oposto_1 = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente_1 = float(input("Digite o comprimento do cateto adjacente: "))

print(f"A hipotenusa é {hypot(cateto_oposto_1, cateto_adjacente_1):.2f}.")

