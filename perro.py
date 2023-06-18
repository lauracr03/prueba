"""
Clase Perro.

Autor: Jaime Rabasco Ronda.
"""
import sphinx

class Perro:
    def __init__(self):
        self.ladrar= 'guau'

    def ladrar(self):
        print(self.ladrar())

p = Perro();
