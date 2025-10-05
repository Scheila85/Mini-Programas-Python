# A confederação nacional de natação precisa de um programa que leia o ano de nascimento
# de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM;
# - Até 14 anos: INFANTIL;
# - Até 19 anos: JUNIOR;
# - Até 25 anos: SÊNIOR;
# - Acima: master

from datetime import date
from time import sleep
print("A seguir digite o ano de nascimento do atleta para saber a categoria em que o mesmo se encontra.")

ano_nascimento = int(input("Qual a data de nascimento do atleta? ").strip())

idade = (date.today().year) - ano_nascimento

print("Calculando...")
sleep(2)

print(f"O atleta tem {idade} anos.")
if idade <= 9:
    print("Atletas com até 9 anos de idade são classificados como MIRIM.")
elif idade <= 14:
    print("Atletas entre 9 e 14 anos de idade são classificados como INFANTIL.")
elif idade <= 19:
    print("Atletas entre 14 e 19 anos de idade são classificados como JÚNIOR.")
elif idade <= 25:
    print("Atletas com 25 anos de idade são classificados como SÊNIOR.")
else: 
    print("Atletas acima de 25 anos de idade são classificados como MASTER.")