# Lectura del tablero se encarga de la leer el tablero del archivo
# Recibe el tamaño de las columnas y los renglones


class LecturaDelTablero:
    def __init__(self, archivo="Tablero.txt"):
        self.tablero = leerTablero(archivo)
        self.fil = len(self.tablero)
        self.col = len(self.tablero[0])

    def __str__(self):
        salida = ""
        for f in range(self.fil):
            for c in range(self.col):
                if self.tablero[f][c] == 0:
                    salida += "  "
                if self.tablero[f][c] == 1:
                    salida += "x "
                if self.tablero[f][c] == 2:
                    salida += "I "
                if self.tablero[f][c] == 3:
                    salida += "F "
                if self.tablero[f][c] == 4:
                    salida += "- "
            salida += "\n"
        return salida

    def camino(self, lista):
        del lista[-1]
        for i in range(len(lista)):
            self.tablero[lista[i][0]][lista[i][1]] = 4


class Nodo:
    def __init__(self, pos=[0, 0], padre=None):
        self.pos = pos
        self.padre = padre
        self.h = distancia(self.pos, pos_f)

        if self.padre == None:
            self.g = 0
        else:
            self.g = self.padre.g + 1
        self.f = self.g + self.h


class AEstrella:
    def __init__(self, tablero):
        self.tablero = tablero

        # Nodos de inicio y fin.
        self.inicio = Nodo(buscarPos(2, tablero))
        self.fin = Nodo(buscarPos(3, tablero))

        # Crea las listas abierta y cerrada.
        self.abierta = []
        self.cerrada = []

        # Añade el nodo inicial a la lista cerrada.
        self.cerrada.append(self.inicio)

        # Añade vecinos a la lista abierta
        self.abierta += self.vecinos(self.inicio)

        # Buscar mientras objetivo no este en la lista cerrada.
        while self.objetivo():
            self.buscar()

        self.camino = self.camino()

    # Devuelve una lista con los nodos vecinos transitables.
    def vecinos(self, nodo):
        vecinos = []
        # basicamente: si los nodos (casillas) alrededor no son pared u
        # obstaculo entonces agregar como posibles vecinos

        # abajo
        if self.tablero.tablero[nodo.pos[0] + 1][nodo.pos[1]] != 1:
            vecinos.append(Nodo([nodo.pos[0] + 1, nodo.pos[1]], nodo))

        # arriba
        if self.tablero.tablero[nodo.pos[0] - 1][nodo.pos[1]] != 1:
            vecinos.append(Nodo([nodo.pos[0] - 1, nodo.pos[1]], nodo))

        # izquierda
        if self.tablero.tablero[nodo.pos[0]][nodo.pos[1] - 1] != 1:
            vecinos.append(Nodo([nodo.pos[0], nodo.pos[1] - 1], nodo))

        # derecha
        if self.tablero.tablero[nodo.pos[0]][nodo.pos[1] + 1] != 1:
            vecinos.append(Nodo([nodo.pos[0], nodo.pos[1] + 1], nodo))

        return vecinos

    # Pasa el elemento de f menor de la lista abierta a la cerrada.
    def f_menor(self):
        a = self.abierta[0]
        n = 0
        for i in range(1, len(self.abierta)):
            if self.abierta[i].f < a.f:
                a = self.abierta[i]
                n = i
        self.cerrada.append(self.abierta[n])
        del self.abierta[n]

    # Comprueba si un nodo está en una lista.
    def en_lista(self, nodo, lista):
        for i in range(len(lista)):
            if nodo.pos == lista[i].pos:
                return 1
        return 0

    # Gestiona los vecinos del nodo seleccionado.
    def ruta(self):
        for i in range(len(self.nodos)):
            if self.en_lista(self.nodos[i], self.cerrada):
                continue
            elif not self.en_lista(self.nodos[i], self.abierta):
                self.abierta.append(self.nodos[i])
            else:
                if self.select.g + 1 < self.nodos[i].g:
                    for j in range(len(self.abierta)):
                        if self.nodos[i].pos == self.abierta[j].pos:
                            del self.abierta[j]
                            self.abierta.append(self.nodos[i])
                            break

    # Analiza el último elemento de la lista cerrada.
    def buscar(self):
        self.f_menor()
        self.select = self.cerrada[-1]
        self.nodos = self.vecinos(self.select)
        self.ruta()

    # Comprueba si el objetivo objetivo está en la lista abierta.
    def objetivo(self):
        for i in range(len(self.abierta)):
            if self.fin.pos == self.abierta[i].pos:
                return 0
        return 1

    # Retorna una lista con las posiciones del camino a seguir.
    def camino(self):
        for i in range(len(self.abierta)):
            if self.fin.pos == self.abierta[i].pos:
                objetivo = self.abierta[i]

        camino = []
        while objetivo.padre != None:
            camino.append(objetivo.pos)
            objetivo = objetivo.padre
        camino.reverse()
        return camino


# ---------------------------------------------------------------------


# Funciones
# ---------------------------------------------------------------------

# Devuelve la posición de "x" en una lista.
# El simbolo para el nodo inicial es "I"
# El simbolo para el nodo final es "F"

def buscarPos(x, tablero):
    for f in range(tablero.fil):
        for c in range(tablero.col):
            if tablero.tablero[f][c] == x:
                return [f, c]
    return 0


# Distancia entre dos puntos.
def distancia(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Valor absoluto.


# Quita el ultimo caracter de una lista.
def quitarUltimo(lista):
    for i in range(len(lista)):
        lista[i] = lista[i][:-1]
    return lista


# Covierte una cadena en una lista.
def listarCadena(cadena):
    lista = []
    for i in range(len(cadena)):
        if cadena[i] == "-":
            lista.append(0)
        if cadena[i] == "x":
            lista.append(1)
        if cadena[i] == "I":
            lista.append(2)
        if cadena[i] == "F":
            lista.append(3)
    return lista


# Lee un archivo de texto y lo convierte en una lista.
def leerTablero(archivo):
    mapa = open(archivo, "r")
    mapa = mapa.readlines()
    mapa = quitarUltimo(mapa)
    for i in range(len(mapa)):
        mapa[i] = listarCadena(mapa[i])
    return mapa


# ---------------------------------------------------------------------

def main():
    tablero = LecturaDelTablero()
    globals()["pos_f"] = buscarPos(3, tablero)
    A = AEstrella(tablero)
    tablero.camino(A.camino)
    print(tablero)
    return 0


if __name__ == '__main__':
    main()
