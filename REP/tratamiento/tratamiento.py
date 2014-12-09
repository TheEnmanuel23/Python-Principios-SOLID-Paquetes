import traceback
import datetime

from tratamiento.configurador import Configurador
from identificador.identificador import Identificador
from modelo.senial import Senial


class Tratamiento(object):

    @staticmethod
    def tecla():
        while True:
            if input('C para continuar> ') == "C":
                break
        return

    def ejecutar(self):
        try:
            print('Iniciando...')
            'Inicializar Objetos'
            p = Configurador.procesador
            v = Configurador.visualizador
            repo_adq = Configurador.repo_Adq
            repo_pro = Configurador.repo_Pro
            i = Identificador()
            print('Se inicializaron los componentes')

            print('Iniciar Adquisición')
            self.tecla()
            Configurador.adquisidor.leer_senial()
            sa = Configurador.adquisidor.obtener_senial_adquirida()
            sa.fecha_adquisicion = datetime.datetime.now().date()
            i.ingresar(sa, "Señal Adquirida")

            print('Fecha de lectura: {0}'.format(sa.fecha_adquisicion))
            print('Cantidad de valores obtenidos {0}'.format(sa.cantidad))
            v.mostrar_datos(sa)
            self.tecla()

            print('Se persiste la señal adquirida')
            repo_adq.guardar(sa)
            repo_adq.auditar(sa, "Señal Guardada:" + str(sa.id))
            print('Señal Guardada')

            print('Iniciar Procesamiento')
            self.tecla()
            p.procesar(sa)
            sp = p.obtener_senial_procesada()
            i.ingresar(sp, "Senial Procesada")
            v.mostrar_datos(sp)
            self.tecla()

            print('Se persiste la señal procesada')
            repo_pro.guardar(sp)
            repo_pro.auditar(sp, "Señal Guardada:" + str(sp.id))
            print('Señal Guardada')

            print('Se lee la senial persistida y guardada')
            sproc = repo_pro.obtener(sp.id, Senial())
            repo_pro.auditar(sproc, "Señal Rescatada" + sproc.id)
            print(sproc.comentario)

        except Exception as e:
            print(e)
            traceback.print_exc()
            exit()


if __name__ == '__main__':
    Tratamiento.ejecutar()