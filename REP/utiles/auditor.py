
from modelo.senial import *


class BaseAuditor(metaclass=ABCMeta):

    @abstractmethod
    def auditar(self, entidad, auditoria):
        pass