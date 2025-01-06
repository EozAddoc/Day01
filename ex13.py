"""Exercice 13 : Tri d’une liste**

- Demandez à l'utilisateur d'entrer une liste de nombres séparés par des virgules.
- Affichez ces nombres triés dans l'ordre croissant.

"""
def triLs():
    a = map(int,input("entre des numero").split(","))
    num =list(a)
    num.sort()
    print(f'la liste triée devient {num}')
    return num
triLs()
