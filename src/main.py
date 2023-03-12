from tkinter import Tk, Frame
from adoquin import *
from piso import *
import sys

class App():
    """Clase App
    Interfaz grafica del problema de adoquinamiento
    Atributos:
        window:Tk
        piso:Piso
        frame:Frame
    """

    def __init__(self, parent):
        '''Constructor, inicializa el objeto App
        Args:
            parent:Tk
        '''
        self.window = parent
        self.frame = self.asignaFrame()
        self.piso = Piso(int(sys.argv[1]))
        self.imprime(self.piso.M)

    def asignaFrame(self):
        '''asignaFrame: crea un "plano" en la Interfaz Grafica
        en el que pondremos los adoquines.
        Returns:
            frame:Frame
        '''
        frame = Frame(self.window, pady=4, padx=4)
        frame.grid(column=0, row=0)
        return frame

    def imprime(self, M):
        '''imprime: despliega en nuestro plano la representacion
        de la matriz.
        Args:
            M:matriz, M ya esta resuelta por el algoritmo de adoquinamiento.
        '''
        m = len(M)
        area = []
        for i in range(m):
            area.append(list(M[i]))
        for i in range(m):
            for j in range(m):
                area[i][j] = Adoquin(parent=self.frame, color=area[i][j])
        for i in range(m):
            for j in range(m):
                area[i][j].cuadro.grid(row=i, column=j)

if __name__ == "__main__":
    root = Tk()
    root.geometry( "600x600" )
    root.title('Adoquinamiento')
    if int(sys.argv[1]) > 4:
        print('No hay colores suficientes para ese tamaño')
        print('Por favor intentalo con un número mas pequeño')
        exit(1)
    app = App(root)
    root.mainloop()
