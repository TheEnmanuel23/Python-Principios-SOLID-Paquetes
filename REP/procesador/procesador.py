
from modelo.senial import *


class BaseProcesador(metaclass=ABCMeta):
    """
    TBD
    """
    def __init__(self, senial):
        """
        TBD
        """
        self._senial_procesada = senial
        return

    @abstractmethod
    def procesar(self, senial):
        pass

    def obtener_senial_procesada(self):
        return self._senial_procesada


class Procesador(BaseProcesador):

    def procesar(self, senial):
        print("Procesando...")
        for i in range(0, senial.tamanio):
            self._senial_procesada.poner_valor(senial.obtener_valor(i) * 2)
        return


class ProcesadorConUmbral(BaseProcesador):
    def __init__(self, senial, umbral):
        super().__init__(senial)
        self._umbral = umbral

    def procesar(self, senial):
        print("Procesando con umbral")
        for i in range(0, senial.tamanio):
            if senial.obtener_valor(i) < self._umbral:
                self._senial_procesada.poner_valor(senial.obtener_valor(i))
            else:
                self._senial_procesada.poner_valor(0)
        return


class ProcesadorDiferencial(BaseProcesador):
    def procesar(self, senial):
        print("Procesar con diferencial.")
        valor_anterior = 0
        for i in range(0, senial.tamanio):
            self._senial_procesada.poner_valor(senial.obtener_valor(i) - valor_anterior)
            valor_anterior = senial.obtener_valor(i)
        return
