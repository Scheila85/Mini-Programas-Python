# Desenvolva um programa que leia o nome, idade e sexo de 04 pessoas. No final do programa, mostre:
# - A média de idade dessas 04 pessoas;
# - Qual é o nome do homem mais velho;
# - Quantas mulheres tem menos de 21 anos.


soma_idade = 0
sexo_feminino = 0
sexo_masculino = 0
mulheres_menos_21 = 0
nome_homem_mais_velho = ""
idade_homem_mais_velho = 0

for c in range(1,5): 
    print(f"Digite os seguintes dados da {c+1}° pessoa:")
    nome = input("Nome: ").strip().title()
    idade = int(input("Idade: "))
    sexo = input("""Sexo [F/M]: """).strip().upper()
    soma_idade += idade
    
    if sexo == "F" and idade < 21:
        sexo_feminino += 1
        mulheres_menos_21 += 1
    elif sexo == "M":
        sexo_masculino += 1
        if idade > idade_homem_mais_velho:
            idade_homem_mais_velho = idade
            nome_homem_mais_velho = nome
        
print(f"A média de idade das {c} pessoas avaliadas é: {soma_idade/c:.0f} anos.")

if idade_homem_mais_velho > 0:
    print(f"O homem mais velho tem {idade_homem_mais_velho} anos e seu nome é {nome_homem_mais_velho}.")
else:
    print("Nenhuma pessoa do sexo masculino foi inserida.")

if mulheres_menos_21 > 0:
    print(f"{mulheres_menos_21} mulher(es) tem menos de 21 anos.")
else:
    print("Nenhuma mulher com menos de 21 anos foi inserida.")