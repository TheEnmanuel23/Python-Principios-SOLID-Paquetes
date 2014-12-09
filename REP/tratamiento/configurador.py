# Se importan los modulos del principio anterior SRP
import os
from visualizador.visualizador import Visualizador
from acceso_datos.repositorio import RepositorioSenial
from modelo.factory_senial import FactorySenial
from adquisidor.factory_adquisidor import FactoryAdquisidor
from procesador.factory_procesador import FactoryProcesador
from acceso_datos.factory_contexto import FactoryContextoDatos

adq_archivo = '/Users/voval/PycharmProjects/Python-Principios-SOLID/datos.txt'


#Se instancian las clases que participan del procesamiento
class Configurador():
    #Define el tipo de la estructura de la señal de la adquisición
    senial_adquirida = FactorySenial.obtener_senial('pila', 100)
    #Define el tipo de la estructura de la señal procesada
    senial_procesada = FactorySenial.obtener_senial('basica', 100)

    #Define desde donde se toman los datos a adquirir (adquisidor)
    adquisidor = FactoryAdquisidor.obtener_adquisidor('senoidal', senial_adquirida, "")
    #Define el tipo de procesador de la señal
    procesador = FactoryProcesador.obtener_procesador('umbral', senial_procesada, 5)
    #Define el manera de visualizar la señal
    visualizador = Visualizador()

    #Define el persitidor de los datos adquiridos mediante el contexto y el repositorio
    #ctx_Adq = CtxArchivo()
    #ctx_Adq.crear('/Users/voval/PycharmProjects/Python-Principios-SOLID/Seniales/Adq')
    ctx_Adq = FactoryContextoDatos.obtener_contexto('archivo', os.getcwd() + '/Seniales/Adq')
    repo_Adq = RepositorioSenial(ctx_Adq)

    #Define el persitidor de los datos procesados mediante el contexto y el repositorio
    #ctx_Pro = CtxPickle()
    #ctx_Pro.crear('/Users/voval/PycharmProjects/Python-Principios-SOLID/Seniales/Pro')
    ctx_Pro = FactoryContextoDatos.obtener_contexto('archivo', os.getcwd()+ '/Seniales/Pro')
    repo_Pro = RepositorioSenial(ctx_Pro)

    def __init__(self):
        pass