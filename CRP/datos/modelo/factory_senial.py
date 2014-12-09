from datos.modelo.senial import *


class FactorySenial(object):

    def __int__(self):
        pass

    @staticmethod
    def obtener_senial(tipo_senial, tamanio):

        if tamanio is int:
            return None

        senial = None
        if tipo_senial == 'basica':
            senial = Senial(tamanio)

        elif tipo_senial == 'pila':
            senial = SenialPila(tamanio)

        elif tipo_senial == 'cola':
            senial = SenialCola(tamanio)

        return senial
