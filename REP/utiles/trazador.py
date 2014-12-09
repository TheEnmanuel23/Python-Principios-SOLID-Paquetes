
from modelo.senial import *


class BaseTrazador(metaclass=ABCMeta):

    @abstractmethod
    def trazar(self, entidad, auditoria):
        pass