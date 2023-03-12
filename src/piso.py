from numpy import array
import random

class Piso():
    """Clase piso.
    Representa la región para adoquinar.
    Contiene a  la matriz de m x m, donde m = 2^n.

    Atributos:
        M:matriz
        numeros:[]
    """

    def __init__(self, n):
        '''Constructor, inicializa el objeto Piso.
        Args:
            n:int, n es un número natural.
        '''
        self.numeros = self.creaLista()
        self.M = self.creaMatriz(n)
        self.adoquinamiento(self.M)

    def creaLista(self):
        '''creaLista: crea y devuelve un a lista en orden ascedente
        de numeros del 1 al 89.
        Returns:
            l:[]
        '''
        l = list(range(1,90))
        return list(reversed(l))

    def creaMatriz(self, n):
        '''creaMatriz: crea y dimensiona la matriz.
        Args:
            n:int, un número natural.
        Returns:
            M:matriz, matrix de m x m.
        '''
        M = []
        m = 2**n
        for i in range(m):
            M.append([0]*m)
        x = random.randint(0, m-1)
        y = random.randint(0, m-1)
        M[y][x] = self.numeros.pop()
        print(f"El cuadrado especial original está en: (c={x},r={y})")
        return array(M)

    def buscaEspecial(self, M):
        '''buscaEspecial: Recorre la matriz en busca del cuadro especial.
        Args:
            M:matriz, la matriz contiene uno y solo un cuadro especial.
        Returns:
            (i,j), i el renglon del cuadrado especial
                   j la columna del cuadrado especial
        '''
        m = len(M)
        for i in range(m):
            for j in range(m):
                if M[i][j] != 0:
                    return (i,j)

    def adoquinamiento(self, M):
        '''adoquinamiento: implementa el algoritmo recursivo para adoquinar
        el area representada por la matriz de area m x m.
        Args:
            M:matriz
        '''
        m = len(M)
        n = m // 2
        (y,x) = self.buscaEspecial(M)
        # Casos base:
        # Si m = 1
        # La matriz e de 1x1, es en sí misma el cuadro especial
        if m == 1:
            return
        # Si m = 2
        # La matriz es de 2x2, donde sea que esté el cuadro especial,
        # Siempre se puede poner un adoquin.
        if m == 2:
            e = self.numeros.pop()
            for i in range(m):
                for j in range(m):
                    if M[i,j] != M[y,x]:
                        M[i,j] = e
        # Caso recursivo
        # Dependiendo de dónde esté el cuadro especial se coloca el adoquin
        # central y se manda a llamar recursivamente la funcion con las
        # submatrices con sus propio cuadro especial.
        else:
            if y < n:
                # Subregion 1
                if x < n:
                    e = self.numeros.pop()
                    M[n,n] = e
                    M[n,n-1] = e
                    M[n-1,n] = e
                    self.adoquinamiento(M[0:n,0:n])
                    self.adoquinamiento(M[0:n,n:m])
                    self.adoquinamiento(M[n:m,0:n])
                    self.adoquinamiento(M[n:m,n:m])
                # Subregion 2
                else:
                    e = self.numeros.pop()
                    M[n,n] = e
                    M[n,n-1] = e
                    M[n-1,n-1] = e
                    self.adoquinamiento(M[0:n,0:n])
                    self.adoquinamiento(M[0:n,n:m])
                    self.adoquinamiento(M[n:m,0:n])
                    self.adoquinamiento(M[n:m,n:m])
            else:
                # Subregion 3
                if x < n:
                    e = self.numeros.pop()
                    M[n,n] = e
                    M[n-1,n] = e
                    M[n-1,n-1] = e
                    self.adoquinamiento(M[0:n,0:n])
                    self.adoquinamiento(M[0:n,n:m])
                    self.adoquinamiento(M[n:m,0:n])
                    self.adoquinamiento(M[n:m,n:m])
                # Subregion 4
                else:
                    e = self.numeros.pop()
                    M[n-1,n-1] = e
                    M[n,n-1] = e
                    M[n-1,n] = e
                    self.adoquinamiento(M[0:n,0:n])
                    self.adoquinamiento(M[0:n,n:m])
                    self.adoquinamiento(M[n:m,0:n])
                    self.adoquinamiento(M[n:m,n:m])
        print(M)
