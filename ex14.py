"""Exercice 14 : Calcul du factoriel**

- Demandez un nombre entier à l'utilisateur.
- Calculez et affichez le factoriel de ce nombre.

"""
def factorielle():
    x = int(input("donne un nombre et je te calcule le factoriel de ce nombre"))
    res=1
    for i in range(1,x+1):
        res *=i
    print(f'le factoriel de {x} est {res}')
    return res
factorielle()

