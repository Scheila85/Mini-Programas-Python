# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status,
# de acordo com a tabela abaixo:
# - Abaixo de 18.5: ABAIXO DO PESO;
# - Entre 18.5 e 25: PESO IDEAL;
# - 25 até 30: SOBREPESO;
# - 30 até 40: OBESIDADE;
# - Acima de 40: OBESIDADE MÓRBIDA.

peso = float(input("Qual é seu peso? (kg) ").strip())
altura = float(input("Qual é a sua altura? (m) ").strip())
IMC = peso/(altura**2)

print(f"Seu IMC é {IMC:.1f},", end= " ")
if IMC < 18.5:
    print("você está abaixo do peso NORMAL.")
elif IMC >= 18.5 and IMC <= 25:
    print("seu peso é IDEAL.")
elif IMC > 25 and IMC <= 30:
    print("você está com SOBREPESO.")
elif IMC > 30 and IMC <= 40:      
    print("você está com OBESIDADE.")
else:
    print("você está com OBESIDADE MÓRBIDA.")