# Elabore um programa que calcule o valor a ser pago por um produto, considerando o preço normal e condição
# de pagamento:
# - à vista dinheiro/cheque: 10% de desconto;
# - à vista no cartão: 5% de desconto;
# - em até 2x no cartão: preço normal;
# - 3x ou mais no cartão: 20% de juros.

print(f'{" RODRILAR ":=^40}')  
valor_compra = float(input("Valor da compra: R$"))
forma_pagamento = input("""
FORMAS DE PAGAMENTO:
[1] À vista dinheiro/cheque
[2] À vista no cartão
[3] Parcelado 2x no cartão
[4] Parcelado 3x ou mais no cartão 

Escolha a forma de pagamento: 
""")

if forma_pagamento == "1":
    valor_final = valor_compra - valor_compra * (10/100)
    print(f"\nParabéns! Você recebeu 10% de desconto.")
elif forma_pagamento == "2":
    valor_final = valor_compra - valor_compra * (5/100) 
    print(f"\nParabéns! Você recebeu 5% de desconto.")
elif forma_pagamento == "3":
    valor_final = valor_compra
    valor_parcela = valor_compra / 2
    print(f"\nCompra parcelada em 2x de R${valor_parcela:.2f}.")
elif forma_pagamento == "4":
    valor_final = valor_compra + valor_compra * (20/100)
    numero_parcelas = int(input("\nQuantas parcelas? "))
    valor_parcela = valor_final / numero_parcelas
    print(f"\nCompra parcelada em {numero_parcelas}x de R${valor_parcela:.2f} com acréscimo de 20% de juros.")
else:
    valor_compra = 0
    valor_final = 0
    print("\nOpção inválida, tente novamente!")

print(f"Valor inicial: R${valor_compra:.2f}.")
print(f"Valor final: R${valor_final:.2f}.")