# Crie um programa que leia uma frase pelo teclado e mostre: 
# Quantas vezes aparece a letra "A";
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

frase = input("Digite uma frase: ").strip().lower()
separando_string = frase.split()
joined_lista = "".join(separando_string)

print(f"A letra 'A' aparece {joined_lista.count("a")} vezes.")
print(f"A letra 'A' aparece pela PRIMEIRA vez no caractere {joined_lista.find("a")+1}")
# COLOCO + 1 porque eu sei que o Python começa a contar a posição a partir de 0, mas queM estará usando
# o programa não sabe, então o ideal é que apareça de acordo com a quantidade de caracteres que a frase tem.

print(f"A letra 'A' aparece pela ÚLTIMA vez no caractere {joined_lista.rfind("a")+1}.")

#### Agora deixando o usuário escolher a letra que quer analisar:

frase = input("Digite uma frase: ").strip().upper()
escolhendo_letra = input("Digite a letra que você quer analisar: ").strip().upper()
lista = frase.split()
joined = "".join(lista)

print(f"A letra '{escolhendo_letra}' aparece {joined.count(escolhendo_letra)} vezes.") 
print(f"A letra '{escolhendo_letra}' aparece pela PRIMEIRA vez no caractere {joined.find(escolhendo_letra)+1}")
print(f"A letra '{escolhendo_letra}' aparece pela ÚLTIMA vez no caractere {joined.rfind(escolhendo_letra)+1}.")