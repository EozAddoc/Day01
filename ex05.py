"""Exercice 5 : Liste inversée**

- Créez une liste contenant plusieurs éléments.
- Affichez cette liste dans l'ordre inversé.

"""
def revList(x):
    rev =x[::-1]
    print(rev)
    return f"{x} reversed is {rev}"
revList(["1","2","3","4","5","6","7","8"])