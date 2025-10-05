# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar desconsidere-o.

print("A seguir, digite 6 números inteiros para saber a soma dos números pares: ")

soma = 0
contador = 0
impares_desconsiderados = []
numeros = ["primeiro número","segundo número","terceiro número","quarto número","quinto número","sexto número" ]

for numero in numeros:
    entrada = int(input(f"Digite o {numero}: "))
    if entrada % 2 == 0:
        soma += entrada
        contador += 1  
    else:
        impares_desconsiderados.append(entrada)  

print(f"Os números ímpares {impares_desconsiderados} digitados foram desconsiderados.")
print(f"Você digitou {contador} números par (es) e a soma é: {soma}.")
