"""Exercice 3 : Conversion de température**

- Convertissez une température saisie en Celsius vers Fahrenheit.
- Formule : `Fahrenheit = (Celsius * 9/5) + 32`.

"""
def covertTemp(celsius:float):
    farenheit = (celsius * (9/5))+32
    return f" {celsius} °C  is {farenheit} °F"

#print(covertTemp(30))