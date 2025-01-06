"""Exercice 4 : Table de multiplication**

- Demandez un nombre à l'utilisateur.
- Affichez la table de multiplication de ce nombre (de 1 à 10).
"""

def multipleTable():
    num = int(input("give a number please"))
    headers = [int(i) for i in range(1,11)]
    rows =[]
    for i in range(1,11):
        rows.append(i*num)
    print(headers)
    print(rows)
#multipleTable()