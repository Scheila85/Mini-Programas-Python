# Faça um programa que leia o ano de nascimento e o sexo de um/uma jovem e informe, de acordo com a sua idade
# - Se ele/ela ainda vai se alistar ao serviço militar;
# - Se é hora de se alistar;
# - Se já passou do tempo de alistamento.
# - Seu programa deverá também mostrar o tempo que falta ou que passou do prazo.

from datetime import date

print("A seguir informe o ano do seu nascimento para saber se você já pode se alistar ao serviço militar.")
ano_nascimento = int(input("Em qual ano você nasceu? ").strip())
sexo = input("""Sexo:
[1] Feminino
[2] Masculino 
""")

ano_atual = date.today().year
idade = ano_atual - ano_nascimento
ano_alistamento = ano_nascimento + 18 

if sexo == "1":
    print("Mulheres não precisam se alistar ao serviço militar!")
elif sexo == "2":
    if idade > 18:
        saldo_alistamento = idade - 18
        print(f"Se você ainda não se alistou, está atrasado há {saldo_alistamento} ano(s).")
        print(f"Você deveria ter se alistado em {ano_alistamento}.")
    elif idade < 18: 
        saldo_alistamento = 18 - idade
        print(f"Você vai se alistar ao serviço militar em {saldo_alistamento} anos.")
        print(f"Ano de alistamento: {ano_alistamento}")
    else: 
        print(f"Você já tem {idade}. Está na hora de se alistar!")