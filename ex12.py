import random 

"""Exercice 12 : Générateur de mot de passe aléatoire**

- Écrivez un programme pour générer un mot de passe aléatoire composé de lettres, chiffres, et symboles.
- Demandez à l'utilisateur la longueur souhaitée du mot de passe.

"""

def generateMDP():
    # chat a fais les liste pour moi mais jai fais la logique
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    special_characters = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    numbers = [str(i) for i in range(10)]
    length = int(input("how long would you like your password to be ?"))
    a = random.randint(1, length-2)
    b = random.randint(1, length-a-1)  
    c = length - a - b 
    rand_lett= random.sample(letters,a)
    rand_sp=random.sample(special_characters,b)
    rand_numbers= random.sample(numbers,c)
    passw= rand_lett + rand_sp + rand_numbers
    pw = (",".join(passw)).replace(",", "")
    print(rand_lett,rand_sp,rand_numbers, passw,pw)
    return pw
generateMDP()





