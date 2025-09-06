# 022 Crie um programa que leia o nome completo de uma pessoa e mostre:
# Nome com todas as letras maiusculas;
# Nome com todas as letras minusculas;
# Quantas letras ao todo sem considerar espaços;
# Quantas letras tem o primeiro nome.

nome_completo = input("Digite seu nome completo: ")

print("Seu nome completo em maiusculo é:" , nome_completo.upper()) #Nome com todas as letras maiusculas
print("Seu nome completo em minusculo é:", nome_completo.lower()) #Nome com todas as letras minusculas

# Quantas letras ao todo sem considerar espaço: 
nome_completo_separado = nome_completo.split()
nome_completo_joined = "".join(nome_completo_separado)

print(f"Seu nome completo tem ao todo {len(nome_completo_joined)} letras.") 

# Quantas letras tem o primeiro nome:
print(f"Seu primeiro nome é {nome_completo_separado[0]} e ele tem {len(nome_completo_separado[0])} letras.")