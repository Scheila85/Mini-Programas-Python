# Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.


from random import randint 
from time import sleep  
import pyttsx3 #adiciona voz

print("-=-++"*10)
voz = pyttsx3.init() 
texto = ("Tente adivinhar em qual número estou pensando...")
print(texto)
voz.say(texto)  # defino o que será falado
voz.setProperty("rate", 50)  #ajuste de velocidade
voz.runAndWait() # dou o comando para start e stop na frase.
print("-=-++"*10)

# POSSO FAZER ASSIM TAMBÉM, MAS A MENSAGEM NÃO SERÁ PRINTADA, APENAS FALADA.
# engine = pyttsx3.init()
# engine.say("Olá, jogador! Tente adivinhar o número que estou pensando.")
# engine.runAndWait()

numero_pensado = int(input("Entre 0 e 5, qual número estou pensando? ").strip())

print("Processando...")
sleep(3) 

numero_a_ser_sorteado = randint(0,5)
print(f"O número que eu estou pensando é: {numero_a_ser_sorteado}.")

if numero_pensado == numero_a_ser_sorteado:
    print("Parabéns, você venceu, sortudo!")
else:
    print("Ish, você perdeu! Sou mais esperto que você.")
print("Obrigada por se desafiar jogando comigo!")