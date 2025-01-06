"""Exercice 8 : Trouver le maximum**

- Demandez trois nombres à l'utilisateur.
- Affichez le plus grand parmi ces nombres.

"""
def findMax():
    a,b,c = map(int, input("give three numbers").split())
    lsNum = []
    lsNum.extend((a,b,c))
    mx = max(lsNum)
    print(f'le maximum de {lsNum} est {mx}')
    return mx
findMax()