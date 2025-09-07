# 036 Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário, ou então
# emprestimo será negado.

from time import sleep
print("Olá, seja bem vindo! Está pronto para fazer a simulação do seu imóvel \ne realizar o sonho da casa própria?")
valor_casa = float(input("Qual o valor da casa? R$").strip())
salario = float(input("Qual o seu salário? R$").strip())
tempo_pagamento = int(input("Em quantos anos você pretende pagar o seu financiamento? ").strip())

salario_30_porcento = salario * (30/100)
PRAZO_MAXIMO_FINANCIAMENTO = 35
prestacao = valor_casa / (tempo_pagamento*12)

print("Processando...")
sleep(3)
if tempo_pagamento > PRAZO_MAXIMO_FINANCIAMENTO or prestacao > salario_30_porcento:
    print("Empréstimo negado!")
    if tempo_pagamento > PRAZO_MAXIMO_FINANCIAMENTO:
        print(f"Tempo de financiamento ({tempo_pagamento} anos) escolhido excede o prazo maximo de financiamento (35 anos).")
    if prestacao > salario_30_porcento: 
        print(f"O valor da prestação (R${prestacao:.2f}) excede 30% (R${salario_30_porcento:.2f}) do seu salário.")
else: 
    print("Financiamento aceito!")
    print("Parabéns! Você está prestes a realizar o sonho da casa própria!")
    print(f"Para pagar uma casa de R${valor_casa:.2f} em {tempo_pagamento} anos, o valor da parcela será R${prestacao:.2f}.")