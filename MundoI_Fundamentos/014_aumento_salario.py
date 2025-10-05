# 034 Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250,00 calcule um aumento de 10%.
# Para salários inferiores ou iguais, o aumento é de 15%.

salario = float(input("Qual o valor do seu salário atual: R$ ").strip())

if salario > 1250:
    aumento = salario + (salario*(10/100))
    print(f"Considerando um aumento de 10%, seu novo salário será de R${aumento:.1f}.")
else:
    aumento = salario + (salario*(15/100))
    print(f"Considerando um aumento de 15%, seu novo salário será de R${aumento:.1f}.")
