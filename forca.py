import random

def print_message_opening():
    print("*********************************")
    print("Bem vindo ao jogo de Forca")
    print("*********************************")

def load_secret_word():
    arquivo = open("palavras.txt","r")
    words = []

    for linha in arquivo:
        linha = linha.strip()
        words.append(linha)

    arquivo.close()
    number = random.randrange(0, len(words))
    secret_word = words[number].upper()
    return secret_word

def start_guessed_letters(word):
    return ["_" for cha in word]

def ask_guess():
    guess = input("qual letra quer chutar? ")
    guess = guess.strip().upper()
    return guess

def mark_correct_guess(guess, guessed_letters_list, secret_word):
    position = 0
    for letter in secret_word:
        if (guess== letter):
            guessed_letters_list[position]  = letter
        position += 1 

def print_message_winner():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def print_message_loser(secret_word):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenha_forca(error):
    print("  _______     ")
    print(" |/      |    ")

    if(error == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(error == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(error == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(error == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(error == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(error == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (error == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def jogar():

    print_message_opening()

    secret_word = load_secret_word()

    guessed_letters_list =  start_guessed_letters(secret_word) #cha means character
    print("porfavor chute uma letra ")
    print(guessed_letters_list)


    hanged = False
    got_right = False
    error = 0

 

    while(not hanged and not got_right):

        guess = ask_guess()

        if (guess in secret_word):
            mark_correct_guess(guess, guessed_letters_list, secret_word)
        else:
            error += 1
            desenha_forca(error)
        

        hanged = error == 6 
        got_right = "_" not in guessed_letters_list
        print(guessed_letters_list)



    if(got_right):
        print_message_winner()
    else:
        print_message_loser(secret_word)

if(__name__=="__main__"):
    jogar()