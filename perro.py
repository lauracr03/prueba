"""
Clase Perro.
:date: 2023-05-22

:autor: Jaime Rabasco
"""
class Perro:

    def __init__(self) :
        """ Creamos el constructor con el atributo/campo self.ladrar que inicializara con guau"""
        self.ladrar = 'Guau'

    def ladrar(self):
        """Esta función hace que nuestro 'perro' ladre, tiene que salir por pantalla guau"""
        print(self.ladrar)

"""Creamos el objeto perro y hacemos que ladre."""
p = Perro()
