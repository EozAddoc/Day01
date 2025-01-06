"""Exercice 11 : FizzBuzz**

- Affichez les nombres de 1 à 100.
- Pour les multiples de 3, affichez "Fizz".
- Pour les multiples de 5, affichez "Buzz".
- Pour les multiples des deux, affichez "FizzBuzz".
- Sinon, affichez juste le nombre.

"""
def fizzbuzz():
    ls = [int(i) for i in range(1,101)]
    for i in range(len(ls)):
        if (ls[i] % 3 == 0 and ls[i] % 5 == 0):
            ls[i] = "FizzBuzz"
        elif ls[i] % 3 == 0:
            ls[i] = "Fizz"
        elif ls[i] % 5 == 0:
            ls[i] = "Buzz"
    print(ls)
    return ls



fizzbuzz()