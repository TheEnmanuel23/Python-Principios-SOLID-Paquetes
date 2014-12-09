from acceso_datos.contexto_datos import *


class FactoryContextoDatos(object):
    """
    Responsable de crear la clase de contexto de datos
    """
    def __int__(self):
        pass

    @staticmethod
    def obtener_contexto(tipo_contexto, *param):

        contexto = None
        if tipo_contexto == 'archivo':
            contexto = CtxArchivo()
            contexto.crear(param[0])

        elif tipo_contexto == 'pickle':
            contexto = CtxPickle()
            contexto.crear(param[0])

        return contexto