# 018 Faça um programa que leia um ângulo qualquer e mostre na tela o seno, cosseno e tangente desse ângulo.

# Usa os valores em radianos, então preciso converter o valor digitado para radiano.

# Objetivo: pedir uma angulo ao usuário e calcular sen, cos, e tan.

# 1°) Transforma o angulo digitado em radianos e depois calcula o sin, con e tan.

from math import radians, sin, cos, tan

angulo_0 = float(input("Digite um ângulo: "))
radianos = radians(angulo_0)
seno = sin(radianos)
cosseno = cos(radianos)
tangente = tan(radianos)

print(f"O seno de {angulo_0}° é {seno:.2f}.")
print(f"O cosseno de {angulo_0}° é {cosseno:.2f}.")
print(f"A tangente de {angulo_0}° é {tangente:.2f}.")

# 2°) Forma direta: 

from math import radians, sin, cos, tan

angulo = float(input("Digite um ângulo: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f"O seno de {angulo}° é {seno:.2f}.")
print(f"O cesseno de {angulo}° é {cosseno:.2f}.")
print(f"A tangente de {angulo}° é {tangente:.2f}.")