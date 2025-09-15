# Crie um programa que leia o ano de nascimento de sete pessoas (laço que leia). No final, mostre quantas
# pessoas ainda não atingiram a maioridade e quantas já são maiores.
# É para ficar assim no final:
# de tantas pessoas digitadas, tantas já atingiram a maioridade e tantas ainda não. (Considerar maioridade 21 anos)

from datetime import date

n_pessoas_maior_idade = 0
n_pessoas_menor_idade = 0

for c in range(7):
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    idade_atual = date.today().year - ano_nascimento
    if idade_atual > 21:
        n_pessoas_maior_idade += 1
    else: 
        n_pessoas_menor_idade += 1

print(f"De {c+1} pessoas avaliadas, {n_pessoas_menor_idade} ainda não atingiram a maioridade", end=" ")
print(f"e {n_pessoas_maior_idade} já atingiram a maioridade.")