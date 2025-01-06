import random as rd
"""Exercice 15 : Nombre mystère**

- Le programme choisit un nombre entre 1 et 1000.
- L'utilisateur a 10 essais pour deviner ce nombre.
- Après chaque essai, indiquez si le nombre est trop haut ou trop bas."""

def mysteryNum():
    x =rd.randrange(1000)
    guess = 0
    win = False
    for i in range(1,11):
        guess = int(input("guess a number between 1 and 1000 "))
        while guess > 1000 or guess < 1:
            guess = int(input(" wrong guess a number between 1 and 1000 "))
        if guess > x:
            print(f"lower you are at your {i} tries out of 10")
        elif guess < x :
            print(f"higher you are at your {i} tries out of 10")
        else:
            print(f'you won after {i} tries you guessed {x} correctly')
            win = True
    if win:
        print("congrats you won !!!")
    else:
        print(f"oh no you coudnt guess within the ten tries the correct guess was {x}")


    
    return x
mysteryNum()