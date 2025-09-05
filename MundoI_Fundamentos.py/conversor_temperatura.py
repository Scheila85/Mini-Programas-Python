# 014) Faça um programa que leia a temperatura em °C e tranforme em °F.

#Objetivo: ler temperatura em °C digitada pelo usuário e converter em °F.

temperatura_graus = float(input("Qual a temperatura em °C atual (apenas números)? "))
print(f"{temperatura_graus}°C correspondem a {(temperatura_graus * (9/5)) + 32}°F.")