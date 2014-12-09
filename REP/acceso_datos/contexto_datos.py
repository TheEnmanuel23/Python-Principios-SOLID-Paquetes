
import pickle
from acceso_datos.mapeador import *
import os


class BaseContexto(metaclass=ABCMeta):
    """
    Clase abstract que define la interfaz de los contextos de datos
    """
    def __init__(self):
        self._recurso = None
        pass

    @property
    def recurso(self):
        return self._recurso

    @abstractmethod
    def crear(self, nombre):
        """
        Se crea el contexto, donde el nombre es el recurso fisico donde residen los datos
        junto con esto se crea el recurso fisico con el nombre
        :param nombre:
        :return:
        """
        if nombre is None or nombre == "":
            raise Exception("Nombre de recurso vacio")
        return

    @abstractmethod
    def persistir(self, entidad, nombre_entidad):
        """
        Se identifica a la instancia de la entidad con nombre_entidad y en entidad es el tipo a persistir
        """
        pass

    @abstractmethod
    def recuperar(self, id_entidad, entidad):
        """
        Se identifica a la instancia de la entidad con nombre_entidad y en entidad es devuelta por el metodo
        """
        pass


class CtxArchivo(BaseContexto):
    """
    Contexto del recurso de persistencia de tipo archivo
    """
    def crear(self, nombre):
        """
        Se crea el archivo con el path donde se guardarán los archivos
        de la entidades a persistir
        :param nombre: Path del repositorio de entidades
        :return:
        """
        try:
            super().crear(nombre)
            try:
                self._recurso = nombre
                os.mkdir(nombre)
                return True
            except IOError:
                print('Error en la creación del directorio: ', nombre)
                return False
        except Exception as eIO:
            raise eIO

    def persistir(self, entidad, nombre_entidad):
        """
        Agregar un objeto(entidad) para persistirlo.
        :param entidad: Tipo de entidad
        :param nombre_entidad: identificacion de la instancia de la entidad
        :return:
        """
        mapeador = MapeadorArchivo()
        archivo = str(nombre_entidad) + '.dat'
        contenido = mapeador.ir_a_persistidor(entidad)
        ubicacion = self._recurso + "/" + archivo

        try:
            with open(ubicacion, "w") as a:
                a.write(contenido)
        except IOError as eIO:
            raise eIO
        return

    def recuperar(self, id_entidad, entidad):
        """
        Obtiene la entidad guardada
        :param entidad:
        :param id_entidad:
        :return:
        """
        contenido = ''
        archivo = str(id_entidad) + '.dat'
        ubicacion = self._recurso + "/" + archivo
        try:
            with open(ubicacion) as persitidor:
                linea = persitidor.readline()
                while linea != '':
                    #contenido = contenido + linea
                    contenido += linea
                    linea = persitidor.readline()
            mapeador = MapeadorArchivo()
            return mapeador.venir_desde_persistidor(entidad, contenido)
        except IOError as eIO:
            raise eIO
        except ValueError:
            raise ValueError


class CtxPickle(BaseContexto):

    def crear(self, nombre):
        """
        Se crea el archivo con el path donde se guardarán los archivos
        de la entidades a persistir
        :param nombre: Path del repositorio de entidades
        :return:
        """
        try:
            super().crear(nombre)
            try:
                self._recurso = nombre
                os.mkdir(nombre)
                return True
            except IOError:
                print('Error en la creación del directorio: ', nombre)
                return False
        except Exception as eIO:
            raise eIO

    def persistir(self, entidad, nombre_entidad):
        """
        Agregar un el objeto(entidad) para persistirlo.
        :param entidad: Nombre de la entidad
        :param nombre_entidad: Lista de atributos de la entidad
        :return:
        """
        archivo = str(nombre_entidad) + '.pickle'
        ubicacion = self._recurso + "/" + archivo
        try:
            with open(ubicacion, "wb") as a:
                pickle.dump(entidad, a)
        except IOError as eIO:
            raise eIO
        return

    def recuperar(self, id_entidad, entidad):
        """
        :param entidad:
        :param id_entidad:
        :return:
        """
        archivo = str(id_entidad) + '.pickle'
        ubicacion = self._recurso + "/" + archivo
        e = None
        try:
            with open(ubicacion, "rb") as a:
                e = pickle.load(a)
        except IOError as eIO:
            print(eIO)
        except ValueError:
            print(ValueError)
        return e