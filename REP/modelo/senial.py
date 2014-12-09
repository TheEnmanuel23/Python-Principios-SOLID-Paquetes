
from abc import ABCMeta, abstractmethod
from datetime import datetime
from collections import deque
"""
Modulo que define las entidades del domino.
"""


class BaseSenial(metaclass=ABCMeta):
    """
    Definición de la entidad tipo Senial.
    En este caso es una definicion de una clase concreta.
    Tiene las funciones:
    -> poner_valor(valor)
    -> obtener_valot(indice)
    -> obtener_tamanio()
    """
    def __init__(self, tamanio=10):
        """
        Constructor: Inicializa la lista de valores vacia
        :return:
        """
        self._valores = []
        self._fecha_adquisicion = datetime.now().date()
        self._tamanio = tamanio
        self._cantidad = 0
        self._id = ''
        self._comentario = ''
        return

    def __str__(self):
        return 'ID: ' + str(self._id) + '\n' + 'Comentario: ' + self._comentario

    #Propiedades
    #Fecha de Adquisicion
    @property
    def fecha_adquisicion(self):
        return self._fecha_adquisicion

    @fecha_adquisicion.setter
    def fecha_adquisicion(self, valor):
        self._fecha_adquisicion = valor

    @fecha_adquisicion.deleter
    def fecha_adquisicion(self):
        del self._fecha_adquisicion

    #Tamanio de la adquisicion
    @property
    def tamanio(self):
        return self._tamanio

    @tamanio.setter
    def tamanio(self, valor):
        self._tamanio = valor

    #Cantidad actual de valores
    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor):
        self._cantidad = valor

    #identificador
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, valor):
        self._id = valor

    @property
    def comentario(self):
        return self._comentario

    @comentario.setter
    def comentario(self, valor):
        self._comentario = valor

    @abstractmethod
    def poner_valor(self, valor):
        pass

    @abstractmethod
    def sacar_valor(self, *valor):
        pass

    def limpiar(self):
        """
        Deja a la senial sin valores
        """
        self._valores.clear()
        self._cantidad = 0

    def obtener_valor(self, indice):
        """
        Devuelve el valor contenido en la lista de acuerdo a al indice
        :param indice:
        :return: valor
        """
        try:
            valor = self._valores[indice]
            return valor
        except Exception as ex:
            print("Error:", ex.__str__())
            return None

    def obtener_valores(self):
        return self._valores


class Senial(BaseSenial):
    #Metodos
    def poner_valor(self, valor):
        """
        Agrega dato a la lista de la senial
        :param valor: dato de la senial obtenida
        """
        if self._cantidad < self._tamanio:
            self._valores.append(valor)
            self._cantidad += 1
        else:
            raise Exception('No se pueden poner mas datos')
        return

    def sacar_valor(self, *indice):
        if self._cantidad > 0:
            valor = self.obtener_valor(indice)
            self._valores.remove(valor)
            self._cantidad -= 1
            return valor
        else:
            print('No hay nada para sacar')
            return None


class SenialPila(BaseSenial):

    def poner_valor(self, valor):
        """
        Agrega dato a la lista de la senial
        :param valor: dato de la senial obtenida
        """
        if self._cantidad < self._tamanio:
            self._valores.append(valor)
            self._cantidad += 1
        else:
            raise Exception('No se pueden poner mas datos')
        return

    def sacar_valor(self):
        valor = 0
        try:
            valor = self._valores.pop()
            self._cantidad -= 1
            return valor
        except Exception('No se pueden sacar datos'):
            print('No hay nada para sacar')
            return valor


class SenialCola(Senial):
    def __init__(self, tamanio):
        super().__init__(tamanio)
        self._valores = deque([])
        return

    def poner_valor(self, valor):
        if self._cantidad < self._tamanio:
            self._valores.append(valor)
            self._cantidad += 1
        else:
            raise Exception('No se pueden poner mas datos')
        return

    def sacar_valor(self):
        valor = 0
        try:
            valor = self._valores.popleft()
            self._cantidad -= 1
            return valor
        except Exception('No se pueden sacar datos'):
            print('No hay nada para sacar')
            return valor