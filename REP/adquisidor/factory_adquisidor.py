from adquisidor.adquisidor import *


class FactoryAdquisidor(object):

    def __int__(self):
        pass

    @staticmethod
    def obtener_adquisidor(tipo_adquisidor, senial, ubicacion):

        adquisidor = None
        if tipo_adquisidor == 'simple':
            adquisidor = AdquisidorSimple(senial)

        elif tipo_adquisidor == 'archivo':
            adquisidor = AdquisidorArchivo(senial, ubicacion)

        elif tipo_adquisidor == 'senoidal':
            adquisidor = AdquisidorSenoidal(senial)

        return adquisidor