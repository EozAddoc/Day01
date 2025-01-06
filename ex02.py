"""Exercice 2 : Calculatrice simple**

- Écrivez un programme qui effectue des additions, soustractions, multiplications et divisions selon l'opération choisie par l'utilisateur.

"""
def calcSimple():
    operation = input("choisie une operation a effectuer(+,-,*,/) ")
    x =input("donne deux chiffre sur lequel effecteuer cette operations").split()
    y= map(int,x)
    y = list(y)
    res = 0
    while operation not in ["+","-","*","/"] :
        operation = input("erreur choisie une operation a effectuer(+,-,*,/) ")
    if operation == "+":
        for i in y:
                res +=i
    elif operation == "-":
        for i in y:
                res -=i
    elif operation == "*":
        res=1
        for i in y:
            res *=i
    elif operation == "/":
        res=1
        for i in y:
            if i == 0:
                return "Erreur: division par zéro."
            res /=i
    else:
        "erreur"
    print(f'resultat de {operation} des {y} est {res} ')

    return res


#calcSimple()