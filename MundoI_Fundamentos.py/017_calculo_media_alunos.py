# 040 Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando
# uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média entre 7.0 ou superior: APROVADO

from time import sleep
print("Digite as notas do aluno para saber se o mesmo foi aprovado ou reprovado.")
primeira_nota = float(input("Digite a primeira nota: ").strip())
segunda_nota = float(input("Digite a segunda nota: ").strip())

media_das_notas = (primeira_nota+segunda_nota)/2

print("Calculando média...")
sleep(1)

print(f"A média do aluno é {media_das_notas:.1f}")
if media_das_notas >= 7.0:
    print("Aluno APROVADO!")
elif media_das_notas > 5.0 and media_das_notas <= 6.9:
    print("O aluno está em RECUPERAÇÃO!")
else:
    print("O alundo está REPROVADO!")
