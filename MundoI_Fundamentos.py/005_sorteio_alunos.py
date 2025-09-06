# 019 Um professor quer sortear um dos seus alunos para apagar o quadro. Faça um programa que leia 
# o nome dos quatro alunos e escreva o nome do escolhido.

# Objetivo: 
# perguntar o nome dos 4 alunos
# sortear o escolhido 

from random import choice

nome_1 = input("Digite o nome do 1° aluno: ").strip().title()
nome_2 = input("Digite o nome do 2° aluno: ").strip().title()
nome_3 = input("Digite o nome do 3° aluno: ").strip().title()
nome_4 = input("Digite o nome do 4° aluno: ").strip().title()
sorteado = choice([nome_1, nome_2, nome_3, nome_4])
print(f"O aluno sorteado será: {sorteado}")