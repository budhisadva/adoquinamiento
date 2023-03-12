from tkinter import Canvas, Frame
from colores import lista

class Adoquin():
    """Clase Adoquin.
    Es la representacion grafica para cada etiqueta en la matriz
    ya adoquinada.
    Atributos:
        conf:{}, diccionario que contiene los atributos necesarios para
                 inicializar el objeto Canvas.
        cuadro:Canvas
    """

    def __init__(self, parent, color):
        '''Constructor, inicializa el objeto Adoquin
        Args:
            parent:Frame, es el "plano" al que anclaremos el adoquin.
            color:int, es la llave para el diccionario de colores.
        '''
        self.conf = {
        "bg": lista[color],
        "width": "30",
        "height": "30",
        }
        self.cuadro = Canvas(parent, self.conf)
