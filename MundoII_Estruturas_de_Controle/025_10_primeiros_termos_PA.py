# 051) Desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritmética.
# No final, mostre os 10 primeiros termos dessa progressão.
# Exemplo de progressão artimética: o número inicia em 0 e vai até 100, pulando de 6 em 6.
# Sendo assim, o primeiro elemento é 0 e a razão é 6, no caso do exemplo acima.

print("A seguir digite o primeiro termo e a razão de uma progressão aritmética para saber" \
" os 10 primeiros termos da progressão aritmética.")

primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Qual a razão da progressão aritmética? "))

print(f"\nOs 10 primeiros termo da PA são:", end="") 
soma_2 = primeiro_termo - razao

for contagem in range(10):
    soma_2 += razao
    print(f"{soma_2} ->", end=" ")
print("Acabou!")