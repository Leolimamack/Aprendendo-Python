import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    secret_number = random.randrange(1,101)
    number_of_tries = 0
    pontuation = 1000

    print("qual dificuldade voce quer jogar?")
    print(" (1) fácil (2) médio ou (3) dificil")

    chose_dificulty = int(input( "escolha sua dificuldade"))

    if (chose_dificulty ==1):
        number_of_tries = 10
    elif (chose_dificulty == 2):
         number_of_tries = 5 
    else:
         number_of_tries = 3

    for Round in range(1, number_of_tries+1) :
        print("Tentativa {} de {}".format(Round,  number_of_tries))

        guess_str = input("Digite o seu número que esteja entre 1 e 100: ")
        print("Você digitou " , guess_str)
        guess_str = int(guess_str)

        if(guess_str<1 or guess_str>100):
            print("vice deve digitar um numero entre 1 e 100")
            continue

        got_right = guess_str == secret_number
        bigger = guess_str > secret_number
        smaller = guess_str < secret_number

        if(got_right):
            print("Parabéns! Você acertou e terminou com {} pontos!".format(pontuation))
            break
        else:
            if(bigger):
                print("O seu chute foi maior do que o número secreto!")
            elif(smaller):
                print("O seu chute foi menor do que o número secreto!")

            lost_points = abs(secret_number - guess_str)
            pontuation = pontuation - lost_points

    print("Fim do jogo")

if(__name__=="__main__"):
    jogar()