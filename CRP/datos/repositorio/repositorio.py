
from utiles.auditor import *
from utiles.trazador import *
import datetime


class BaseRepositorio(metaclass=ABCMeta):
    def _init__(self, ctx):
        self._ctx = ctx
    """
    Define la interfaz para el acceso a la persistencia de datos
    """
    @abstractmethod
    def guardar(self, entidad):
        """
        Persiste lo señal
        """
        pass

    @abstractmethod
    def obtener(self, entidad, id_entidad):
        pass


class RepositorioSenial(BaseRepositorio, BaseAuditor, BaseTrazador):
    """
    TBD
    """
    def __init__(self, ctx):
        super()._init__(ctx)

    def guardar(self, senial):
        try:
            self._ctx.persistir(senial, senial.id)
        except Exception as ex:
            self.trazar(senial, ex.args)
            raise Exception
        return

    def obtener(self, id_entidad, senial):
        try:
            return self._ctx.recuperar(id_entidad, senial)
        except Exception:
            msj = 'Error al leer una senial persistada: '
            msj += ' - ID: ' + str(id_entidad)
            self.trazar(senial, msj)
            raise Exception

    def auditar(self, senial, auditoria):

        nombre = 'auditor.log'
        try:
            with open(nombre, 'a') as auditor:
                auditor.writelines('------->\n')
                auditor.writelines(str(senial) + '\n')
                auditor.writelines(str(datetime.datetime.now()) + '\n')
                auditor.writelines(str(auditoria) + '\n')
        except IOError as eIO:
            raise eIO

    def trazar(self, senial, mensaje):

        nombre = 'logger.log'
        try:
            with open(nombre, 'a') as logger:
                logger.writelines('------->\n')
                logger.writelines(str(senial) + '\n')
                logger.writelines(str(datetime.datetime.now()) + '\n')
                logger.writelines(str(mensaje) + '\n')
        except IOError as eIO:
            raise eIO
