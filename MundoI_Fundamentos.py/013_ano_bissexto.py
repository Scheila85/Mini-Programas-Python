# Faça um programa que leia um ano qualquer e mostre se ele é bissexto ou não. 

from datetime import date
from time import sleep

ano = int(input("Digite um ano qualquer para saber se ele é bissexto. \nOu digite 0 se quiser saber o ano atual: ").strip())

sleep(2)

if ano == 0:
    ano = date.today().year

if ano % 4 == 0:
    if ano % 100 != 0:
        print(f"O ano {ano} é bissexto.")
    elif ano % 100 == 0 and ano % 400 == 0:
        print(f"O ano {ano} é bissexto.")
    else:
        print(f"O ano {ano} não é bissexto.")
else: 
    print(f"O ano {ano} não é bissexto.")