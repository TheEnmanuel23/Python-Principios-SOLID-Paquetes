from procesador.procesador import *


class FactoryProcesador(object):

    def __int__(self):
        pass

    @staticmethod
    def obtener_procesador(tipo_procesador, senial, *param):

        procesador = None
        if tipo_procesador == 'basico':
            procesador = Procesador(senial)

        elif tipo_procesador == 'diferencial':
            procesador = ProcesadorDiferencial(senial)

        elif tipo_procesador == 'umbral':
            procesador = ProcesadorConUmbral(senial, param[0])

        return procesador