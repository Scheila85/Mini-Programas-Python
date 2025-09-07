# Crie um programa que faça o computador jogar jokenpô com você:
# pedra, papel, tesoura.

from random import choice
from time import sleep

print("Vamos jogar JO KEN PO? ")

opcao_jogador = input("""
Você tem 03 opções:

Pedra
Papel
Tesoura

Qual você escolhe? """)

opcao_jogador_formatada = opcao_jogador.strip().lower()
lista_opcoes_maquina = ["pedra", "papel", "tesoura"]
sorteio_lista_maquina = choice(lista_opcoes_maquina)

print("JO")
sleep(0.5)
print("KEN")
sleep(0.5)
print("PO")

sleep(0.5)
print("=+="*10)
print(f"Computador jogou: {sorteio_lista_maquina.title()}")
print(f"Jogador jogou: {opcao_jogador_formatada.upper()}")
print("=+="*10)

sleep(1)
if opcao_jogador_formatada != sorteio_lista_maquina:
    if opcao_jogador_formatada == "pedra" and sorteio_lista_maquina == "papel":
        print("COMPUTADOR VENCE")
    elif opcao_jogador_formatada == "papel" and sorteio_lista_maquina == "tesoura":
        print("COMPUTADOR VENCE")
    elif opcao_jogador_formatada == "tesoura" and sorteio_lista_maquina == "pedra":
        print("COMPUTADOR VENCE")
    elif opcao_jogador_formatada == "papel" and sorteio_lista_maquina == "pedra":
        print("JOGADOR VENCE")
    elif opcao_jogador_formatada == "pedra" and sorteio_lista_maquina == "tesoura":
        print("JOGADOR VENCE")
    elif opcao_jogador_formatada == "tesoura" and sorteio_lista_maquina == "papel":
        print("JOGADOR VENCE")
    else:
        print("Opção inválida! Você deve escolher entre: pedra, papel, tesoura.")
else:
    
    print("Empate! Quer tentar um desempate?")