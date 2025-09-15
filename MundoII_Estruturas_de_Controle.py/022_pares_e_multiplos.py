# Faça um programa que calcule a soma entre todos os números ímpares que são multiplos 
# de três e que se encontram no intervalo de 1 até 500. 


soma = 0  
contador = 0  
for numero in range(1, 501, 2):
    if numero % 2 != 0:
        if numero % 3 == 0:
            soma += numero
            contador += 1
print(f"\n\nO resultado da soma entre todos os números ímpares e multiplos de 3 no intervalo entre (1, 501) é: {soma}.")
print(f"No intervalo de 1 e 500 há {contador} números ímpares multiplos de 3.")

#Coloquei quantos números ímpares multiplos de 3 aparecem no intervalo entre 1 e 500.

