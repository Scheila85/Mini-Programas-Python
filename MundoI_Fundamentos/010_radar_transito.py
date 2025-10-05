# Escreva um programa de leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma mensagem que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

tipo_carro = input("Qual o modelo do carro? ").strip().upper()
placa = input("Digite a placa do carro: ").strip().upper()
velocidade_carro = float(input("Qual a velocidade do carro na via? (km/h) ").strip())
valor_da_multa = (velocidade_carro - 80) * 7

if velocidade_carro > 80:
    print("Você ultrapassou o limite da pista (80 km/h), e por isso foi multado.")
    print(f"O carro {tipo_carro} de placa {placa} foi multado em R${valor_da_multa:.2f}.")
    print("Favor se dirigir ao órgão de transito mais próximo para realizar o pagamento da sua pendência.")
else: 
    print(f"O carro {tipo_carro} de placa {placa}, não ultrapassou o limite de velocidade da pista.")

# Radar de transito:

from time import sleep
from random import randint
print("Você está passando em um radar. Velocidade máxima permitida: 80 km/h.")
sleep(3)
velocidade = randint(20,200)
print(f"Velocidade: {velocidade}km/h.")

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f"Velocidade acima do permitido, você foi multado em R${multa:.2f}") 
else: 
    print("Continue dirigindo com segurança!")
