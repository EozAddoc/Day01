import random as rd
"""Exercice 6 : Jeu de devinettes**

- Le programme génère un nombre aléatoire entre 1 et 100.
-L'utilisateur doit deviner ce nombre, avec des indications si le nombre est trop haut ou trop bas.

"""

def guessingGame():
    x =rd.randrange(100)
    tries =0
    guess = 0
    while guess != x:
        tries +=1
        guess = int(input("guess a number between 1 and 100 "))
        while guess > 100 or guess < 1:
            guess = int(input(" wrong guess a number between 1 and 100 "))
        if guess > x:
            print("lower")
        else :
            print("higher")

    
    print(f'you won after {tries} tries you guessed {x} correctly')
    return x
guessingGame()