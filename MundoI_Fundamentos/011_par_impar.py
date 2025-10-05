# Crie um programa que leia um número inteiro e mostre se ele é PAR ou ÍMPAR

numero = int(input("Digite um número inteiro para saber se é par ou ímpar: ").strip())

if numero % 2 == 0: 
    print(f"O número {numero} digitado é par.")
else: 
    print(f"O numero {numero} digitado é ímpar.")

