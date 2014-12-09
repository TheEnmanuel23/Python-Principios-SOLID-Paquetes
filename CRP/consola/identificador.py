class Identificador(object):

    def __init__(self):
        pass

    @staticmethod
    def ingresar(senial, titulo):

        opcion = 'N'
        while opcion != 'S':
            print('      > ' + titulo)
            senial.id = int(input('      > Identificación de la señal (numero): '))
            senial.comentario = input('      > Descripción: ')
            opcion = input('Acepta Ingreso (S/N): ')
