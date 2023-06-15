"""
Clase Coche base para el Examen de la UD4
Refactorización
Extrae una superclase Vehículo con los campos
    num_serie
    fabricante
    color
:autor: Jaime Rabasco
"""
import sphinx

class Vehiculo :
    """Esta es la superclase Vehiculo con sus atributos"""
    """:param color: Definimos color como rojo
        :param fabricante: Definimos nuestro fabricante como Seat
        :param num_serie: definimos nuestro numero de serie como 1"""
    color = 'rojo';
    fabricante = 'seat';
    num_serie = 1;


class Coche(Vehiculo) :

    cilindrada = 1000;

    def __init__(self):
        pass;

    def __init__(self, num_serie, cilindrada, fabricante, color):
        """Nuestro constructor le pasaremos:
        :param num_serie: introducimos el numero de serie
        :param cilindrada: introducimos nuestra cilindrada
        :param fabricante: introducimos nuestro fabricante
        :param color: introducimos nuestro color"""
        self.num_serie = num_serie;
        self.cilindrada = cilindrada;
        self.fabricante = fabricante;
        self.color = color;

    @property
    def num_serie(self):
        """Propiedad getter
        :return self.__num_serie:"""
        return self.__num_serie

    @num_serie.setter
    def num_serie(self, value):
        """Propiedad setterrrrr  """
        self.__num_serie = value

    @property
    def color(self):
        """Propiedad getter
        :return self.__color:"""
        return self.__color

    @color.setter
    def color(self, value: int):
        """Propiedad setter"""
        self.__color = value

    @property
    def cilindrada(self):
        """Propiedad getter
        :return self.__cilindrada:"""
        return self.__cilindrada

    @cilindrada.setter
    def cilindrada(self, value):
        """Propiedad setter"""
        self.__cilindrada = value

    @property
    def fabricante(self):
        """Propiedad getter
        :return self.__fabricante:"""
        return self.__fabricante

    @fabricante.setter
    def fabricante(self, value):
        """Propiedad setter"""
        self.__fabricante = value
