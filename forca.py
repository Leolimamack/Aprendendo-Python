def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Forca")
    print("*********************************")

    
    secret_word = "banana".upper()
    guess_letters_list = ["_","_","_","_","_","_"]

    hanged = False
    got_right = False
    error = 0

    print("porfavor chute uma letra ")
    print(guess_letters_list)

    while(not hanged and not got_right):

        guess = input("qual letra quer chutar? ")
        guess = guess.strip().upper()

        if (guess in secret_word):
            position = 0
            for letter in secret_word:
                if (guess== letter):
                    guess_letters_list[position]  = letter
                position += 1 
        else:
            error += 1
        hanged = error == 6 
        got_right = "_" not in guess_letters_list
        print(guess_letters_list)



    if(got_right):
        print("Parabéns, voce ganhou")
    else:
        print("Triste, voce perdeu")
    print ("Fim do jogo")

if(__name__=="__main__"):
    jogar()