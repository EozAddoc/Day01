"""Exercice 10 : Moyenne des notes**

- Demandez à l'utilisateur d'entrer plusieurs notes séparées par des virgules.
- Calculez et affichez la moyenne de ces notes.

"""
def moyenneDesNotes():
    a = map(int,input("entre des notes").split(","))
    notes =list(a)
    moyenne = sum(notes)/len(notes)
    print(f'ta note moyenne parmi tes notes de {notes} est {moyenne}')
    return moyenne
moyenneDesNotes()