# 049) Pedindo para o usuário digitar um número qualquer para saber a sua tabuada
#  Com laço for.

from time import sleep
numero = int(input("Digite um número para saber a sua tabuada: ").strip())

print(f"\nA tabuada de {numero} é: \n")
for contagem in range(1, 11):
    tabuada = numero * contagem
    sleep(0.5)
    print(f"{numero} x {contagem} = {tabuada}")