"""Exercice 9 : Palindrome**

- Demandez à l'utilisateur d'entrer un mot.
- Indiquez si ce mot est un palindrome (il se lit de la même manière dans les deux sens).

"""
def palindrome():
    mot = input("donne un mot et je te dis si cest un palindrome ")
    print(f'le fait que le mot {mot} soit un palindrom est {mot== mot[::-1]}')
    return mot == mot[::-1]
palindrome()