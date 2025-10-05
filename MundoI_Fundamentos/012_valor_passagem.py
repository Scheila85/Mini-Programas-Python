# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, 
# cobrando 0,50 centavos por Km para viagens até 200 Km e 0,45 centavos para viagens mais longas.

distancia = float(input("Qual é a distância da sua viagem (Km)? ").strip())

if distancia <= 200:
    preco_passagem = 0.50 * distancia
else:
    preco_passagem = 0.45 * distancia

print(f"O valor da passagem é R${preco_passagem:.2f} para {distancia} km.")