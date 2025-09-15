# 055) Faça um programa que leia o peso de 5 pessoas e no final mostre qual foi 
# o maior e o menor peso lido.

maior_peso = 0
menor_peso = 0

for pessoas in range(1,6):
    peso = float(input("Qual é o seu peso (kg)? "))
    if pessoas == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print(f"O maior peso digitado é {maior_peso}kg.")
print(f"O menor peso digitado é {menor_peso}kg.")