class Visualizador(object):

    def __init__(self):
        pass
        
    def mostrar_datos(self, senial):
        print("Mostrar la senial")
        for i in range(0, senial.cantidad):
            print('Dato nro:', i, "Valor:", senial.obtener_valor(i))
        return