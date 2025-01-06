"""Exercice 7 : Compter les voyelles**

- Demandez à l'utilisateur d'entrer une phrase.
- Comptez et affichez le nombre de voyelles présentes dans la phrase.

"""

def countVowels():
    phrase = input("enter a phrase")
    vowels = ["a", "e", "o","u","i","y"]
    count=0
    lsPhrase = list(phrase.replace(" ", ""))
    for i in lsPhrase:
        if i in vowels:
            count +=1
    print(lsPhrase,count)
    return count
countVowels()