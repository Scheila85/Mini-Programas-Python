# Faça um programa que leia um número e diga se ele é ou não um número primo.
# Um número é primo se ele é divisil por 1 e por ele mesmo.
# por exemplo: número 5, se entre 1 e 5 ele foi divisível apenas por 1 e ele mesmo
# então é primo, caso contrário não.

print("\033[mA seguir digite um número aleatório para saber se ele é um número primo ou não.")
numero = int(input("\033[mDigite o número desejado: "))
vezes_que_foi_divisil = 0

for c in range(1, numero + 1):
    if numero % c == 0:
        vezes_que_foi_divisil += 1

if vezes_que_foi_divisil == 2:
    print(f"\n\033[mO número {numero} digitado foi divisível {vezes_que_foi_divisil} vezes por isso é um número primo.")
else: 
    print(f"\n\033[mO número {numero} digitado foi divisível {vezes_que_foi_divisil} vezes por isso não é um número primo.")
    