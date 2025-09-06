# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

#Objetivo: 
# ler nome dos alunos
# embaralhar ordem 
# mostrar a ordem sorteada

from random import shuffle
aluno_1 = input("Escreva o nome do primeiro aluno: ").strip().title()
aluno_2 = input("Escreva o nome do segundo aluno: ").strip().title()
aluno_3 = input("Escreva o nome do terceiro aluno: ").strip().title()
aluno_4 = input("Escreva o nome do quarto aluno: ").strip().title()

lista = [aluno_1, aluno_2, aluno_3, aluno_4]
shuffle(lista)

print(f"A ordem de apresentação será: {lista}")

