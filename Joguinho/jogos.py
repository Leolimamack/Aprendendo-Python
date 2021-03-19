import forca
import adivinhacao

print("*********************************")
print("******Escolha o seu jogo!********")
print("*********************************")

print("Voce quer jogar (1) forca ou (2) adivinhação?")

jogo = int(input("Qual jogo voce quer jogae? "))

if (jogo == 1):
    print("jogando forca")
    forca.jogar()
elif(jogo == 2):
    print("jogando adivinhação")
    adivinhacao.jogar()