import datetime
from utiles.trazador import *
from utiles.auditor import *
import math


class BaseAdquisidor(BaseAuditor, metaclass=ABCMeta):
    """ Clase Abstracta adquisidor
    """
    def __init__(self, senial):
        """
        Inicializa el adquisidor con una lista vacia de valores de la senial
        :valor: Tamanio de la coleccion de valores de la senial
        """
        self._senial = senial

    def obtener_senial_adquirida(self):
        """
        Devuelve la lista de valores de la senial adquirida
        :return: senial
        """
        return self._senial

    def auditar(self, entidad, auditoria):
        nombre = 'auditor.log'
        try:
            with open(nombre, 'a') as auditor:
                auditor.writelines('------->\n')
                auditor.writelines(str(entidad) + '\n')
                auditor.writelines(str(datetime.now()) + '\n')
                auditor.writelines(str(auditoria) + '\n')
        except IOError as eIO:
            raise eIO

    @abstractmethod
    def leer_senial(self):
        """
        Metodo abstracto. Cada adquisidor tiene su propia implementacion
        de la lectura de la senial
        """
        pass

    @abstractmethod
    def _leer_dato_entrada(self):
        pass


class AdquisidorSimple(BaseAdquisidor):
    """
    adquisidor de datos desde el teclado
    """
    def _leer_dato_entrada(self):
        """
        Lee un dato por teclaso
        :return: dato leido
        """
        dato = 0
        while True:
            try:
                dato = float(input('Valor:'))
                break
            except ValueError:
                print('Dato mal ingresado, <enter>')
        return dato

    def leer_senial(self):
        """
        llena la coleccion de valores de la senial desde el teclado
        :return:
        """
        print("Lectura de la senial")
        for i in range(0, self._senial.tamanio):
            self._senial.poner_valor(self._leer_dato_entrada())
            print("Dato nro:", self._senial.cantidad)
        self.auditar('Lectura desde teclado', 'Realizada')
        return


class AdquisidorArchivo(BaseAdquisidor):
    """
    adquisidor de datos desde Archivo
    """
    def __init__(self, senial, ubicacion):
        """
        Inicializa la instancia con la ubicacion del archivo a leer
        :param ubicacion:
        """
        BaseAdquisidor.__init__(self, senial)
        if isinstance(ubicacion, str):
            self._ubicacion = ubicacion
        else:
            raise Exception('El dato no es de una ubicacion valida, (No es un nombre de archivo)')

        try:
            with open(self._ubicacion, 'r'):
                print('El archivo', self._ubicacion, 'existe.')
        except IOError as e:
            raise Exception('I/O Error: ', e)
        return

    @property
    def ubicacion(self):
        return self._ubicacion

    def _leer_dato_entrada(self):
        pass

    def leer_senial(self):
        print('Lectura de la senial')
        try:
            with open(self._ubicacion, 'r') as a:
                for linea in a:
                    dato = float(linea)
                    self._senial.poner_valor(dato)
                    print("Dato nro:", self._senial.cantidad, "Valor Leido:", dato)
                self.auditar('Lectura desde archivo', 'Realizada')
        except IOError:
            print('I/O Error')
        except ValueError:
            print('Dato de senial no detectado')
        except Exception as e:
            print("Error:", e)


class AdquisidorSenoidal(BaseAdquisidor):
    """
    Simulador de una entrada de senial senoidal
    """
    def __init__(self, senial):
        BaseAdquisidor.__init__(self, senial)
        self._valor = 0
        self._i = 0

    def _leer_dato_entrada(self):
        self._valor = math.sin((float(self._i) / (float(self._senial.tamanio))) * 2 * 3.14) * 10
        self._i += 1
        return self._valor

    def leer_senial(self):
        print('Lectura de la senial')
        i = 0
        try:
            while i < self._senial.tamanio:
                self._senial.poner_valor(self._leer_dato_entrada())
                i += 1
            self.auditar('Lectura desde archivo', 'Realizada')
        except Exception as e:
            print("Error:", e)
