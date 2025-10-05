# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário, ou então o
# emprestimo será negado. 
# Sem considerar juros.

from time import sleep

PRAZO_MAXIMO_FINANCIAMENTO = 35 
cor = {"verde": "\033[32m",
    "vermelho":"\033[31m",
    "limpa": "\033[m"}

while True: 
    print("Olá, seja bem vindo! Está pronto para fazer a simulação do seu imóvel \ne realizar o sonho da casa própria?")
    valor_casa = float(input("Qual o valor da casa? R$").strip())
    salario = float(input("Qual o seu salário? R$").strip())
    tempo_pagamento = int(input("Em quantos anos você pretende quitar o financiamento? ").strip())

    salario_30_porcento = salario * (30/100)
    prestacao = valor_casa / (tempo_pagamento*12)

    print("Processando...")
    sleep(2)
    if tempo_pagamento > PRAZO_MAXIMO_FINANCIAMENTO or prestacao > salario_30_porcento:
        print(f"{cor['vermelho']}Empréstimo negado!{cor['limpa']}")
        if tempo_pagamento > PRAZO_MAXIMO_FINANCIAMENTO:
            print(f"Tempo de financiamento ({cor['vermelho']}{tempo_pagamento} anos{cor['limpa']}) excede o prazo máximo de financiamento {cor['vermelho']}(35 anos){cor['limpa']}.")
        if prestacao > salario_30_porcento: 
            print(f"O valor da prestação ({cor['vermelho']}R${prestacao:.2f}{cor['limpa']}) excede 30% ({cor['vermelho']}R${salario_30_porcento:.2f}{cor['limpa']}) do seu salário.")
    else: 
        print(f"{cor['verde']}Financiamento aceito!{cor['limpa']}")
        print("Parabéns! Você está prestes a realizar o sonho da casa própria!")
        print(f"Para pagar uma casa de {cor['verde']}R${valor_casa:.2f}{cor['limpa']} em {cor['verde']}{tempo_pagamento} anos{cor['limpa']}, o valor da parcela será {cor['verde']}R${prestacao:.2f}{cor['limpa']}.")
    continuacao = input("Deseja realizar outras simulaçoes? [S/N] ").strip().upper()
    while continuacao not in "SN":
        continuacao = input("Deseja realizar outras simulaçoes? [S/N] ").strip().upper()
    if continuacao == "N":
        break