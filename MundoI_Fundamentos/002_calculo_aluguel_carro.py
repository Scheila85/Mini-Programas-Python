# Faça um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de 
# dias pelos quais ele foi alugado. Calcule o preço a pagar:
# sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

#Objetivo: 
# ler quando km foram percorridos
# ler quantidade de dias que o carro ficou alugado 
# calcular o valor do aluguel

km_percorrido = float(input("Quantos km foram percorridos? "))

quantidade_dias_alugado = int(input("Por quantos dias o carro ficou alugado? "))
preco_por_km = 0.15 * km_percorrido
preco_por_dia = 60 * quantidade_dias_alugado

print(f"O valor a ser pago pelo aluguel do carro é de R${preco_por_km + preco_por_dia:.2f}.")